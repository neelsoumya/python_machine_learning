# app.R
# -------------------------------------------------------------
# Shiny app to teach Feature Selection with LASSO & Tree-based
# importance (Random Forest via ranger). Designed for teaching.
# -------------------------------------------------------------

# ---- Packages ----
library(shiny)
library(shinythemes)
library(DT)
library(ggplot2)
library(glmnet)
library(ranger)
library(MASS)         # for Boston dataset

# ---- Helpers ----
# Safe model metrics for regression vs classification
metric_summary <- function(truth, pred, task){
  if(task == "regression"){
    rmse <- sqrt(mean((truth - pred)^2, na.rm = TRUE))
    mae  <- mean(abs(truth - pred), na.rm = TRUE)
    r2   <- 1 - sum((truth - pred)^2)/sum((truth - mean(truth))^2)
    data.frame(Metric = c("RMSE","MAE","R^2"), Value = c(rmse, mae, r2))
  } else {
    # classification
    acc  <- mean(truth == pred, na.rm = TRUE)
    data.frame(Metric = c("Accuracy"), Value = c(acc))
  }
}

# Extract nonzero coefficients at a given lambda
nonzero_coefs <- function(fit, s){
  cf <- coef(fit, s = s)
  if(is.list(cf)){
    # multinomial returns a list (one matrix per class); aggregate non-zeros by union
    nz <- unique(unlist(lapply(cf, function(mat){
      rownames(mat)[as.vector(mat != 0)]
    })))
    nz <- setdiff(nz, c("(Intercept)"))
    data.frame(Feature = nz)
  } else {
    idx <- which(as.vector(cf) != 0)
    feats <- rownames(cf)[idx]
    feats <- setdiff(feats, c("(Intercept)"))
    vals  <- as.numeric(cf[idx])
    data.frame(Feature = feats, Coefficient = vals)
  }
}

# Build model matrix X and response y from a data.frame and chosen outcome
build_xy <- function(df, outcome){
  y <- df[[outcome]]
  X <- df[setdiff(names(df), outcome)]
  # remove non-numeric predictors for glmnet; create model.matrix to one-hot factors
  mm <- model.matrix(~ . , data = X)
  mm <- mm[, colnames(mm) != "(Intercept)", drop = FALSE]
  list(x = as.matrix(mm), y = y)
}

# Determine task type
infer_task <- function(y){
  if(is.numeric(y)) return("regression")
  if(is.factor(y)) return("classification")
  if(is.character(y)) return("classification")
  if(is.logical(y)) return("classification")
  return("regression")
}

# Family for glmnet given y
family_for <- function(y){
  if(is.numeric(y)) return("gaussian")
  y <- as.factor(y)
  if(nlevels(y) == 2) return("binomial")
  return("multinomial")
}

# ---- UI ----
ui <- fluidPage(
  theme = shinytheme("flatly"),
  tags$head(tags$style(HTML(".small-note{font-size: 0.9em; color:#555;} .pill{background:#eef; padding:2px 8px; border-radius:999px;} .code{font-family: monospace;}"))),
  titlePanel("Feature Selection Tutor: LASSO & Tree Importance"),
  
  sidebarLayout(
    sidebarPanel(width = 3,
                 h4("1) Data"),
                 radioButtons("datasrc", "Choose data source", choices = c(
                   "mtcars (regression)" = "mtcars",
                   "iris (classification)" = "iris",
                   "Boston housing (regression)" = "boston",
                   "Upload CSV" = "upload"
                 ), selected = "mtcars"),
                 conditionalPanel(
                   condition = "input.datasrc == 'upload'",
                   fileInput("csv", "Upload CSV file", accept = c('.csv','.txt','.tsv')),
                   checkboxInput("header", "Header", TRUE),
                   radioButtons("sep", "Separator", choices = c(Comma=",", Semicolon= ";", Tab="\t"), selected=",")
                 ),
                 uiOutput("outcome_ui"),
                 sliderInput("split", "Train/Test split (%)", min=50, max=90, value=75, step=5),
                 tags$hr(),
                 h4("2) LASSO"),
                 sliderInput("alpha", "Elastic Net mixing (α)", min=0, max=1, value=1, step=0.05),
                 numericInput("folds", "CV folds (k)", value=10, min=3, max=20, step=1),
                 checkboxInput("standardize", "Standardize predictors (recommended)", TRUE),
                 actionButton("fit_lasso", "Fit LASSO", class = "btn btn-primary"),
                 tags$p(class="small-note", "Default α=1 is pure LASSO. Lower α adds ridge (Elastic Net)."),
                 tags$hr(),
                 h4("3) Trees"),
                 numericInput("trees", "# Trees", value=300, min=100, step=50),
                 numericInput("mtry", "mtry (features per split)", value=NA),
                 numericInput("min_n", "min node size", value=5, min=1, step=1),
                 selectInput("vi_type", "Importance type", choices=c("permutation","impurity"), selected="permutation"),
                 actionButton("fit_tree", "Fit Random Forest", class = "btn btn-success")
    ),
    
    mainPanel(width = 9,
              tabsetPanel(id = "tabs", type = "tabs",
                          tabPanel("Data", icon = icon("table"),
                                   fluidRow(
                                     column(12, tags$p(class="small-note", "Tip: Pick your outcome, then explore LASSO and Tree tabs.")),
                                     column(12, DTOutput("data_preview"))
                                   )
                          ),
                          tabPanel("LASSO", icon = icon("sliders-h"),
                                   fluidRow(
                                     column(4,
                                            tags$h5("What you're seeing"),
                                            tags$p("LASSO (Least Absolute Shrinkage and Selection Operator) shrinks many coefficients to exactly zero, acting as automatic feature selection. We tune λ with cross-validation."),
                                            tags$p(HTML("<span class='pill'>Blue curve</span>: CV error vs λ. Vertical lines show λ\u2081\u209B (min) and λ\u2081\uFE0E\u209B (1-SE).")),
                                            DTOutput("lasso_selected")
                                     ),
                                     column(8,
                                            h5("Cross-validated error"),
                                            plotOutput("cvplot", height = 320),
                                            h5("Coefficient paths (shrinkage)"),
                                            plotOutput("coefpath", height = 360),
                                            h5("Test performance"),
                                            DTOutput("lasso_metrics")
                                     )
                                   )
                          ),
                          tabPanel("Trees", icon = icon("tree"),
                                   fluidRow(
                                     column(5,
                                            tags$h5("Why tree importance?"),
                                            tags$p("Ensembles of decision trees (Random Forests) rank features by how much they reduce error when used to split the data (impurity) or by how much the model worsens when a feature is permuted (permutation)."),
                                            DTOutput("tree_metrics")
                                     ),
                                     column(7,
                                            h5("Top feature importances"),
                                            plotOutput("vip_plot", height = 420)
                                     )
                                   )
                          ),
                          tabPanel("Notes", icon = icon("book-open"),
                                   fluidRow(
                                     column(12,
                                            tags$h4("Teaching notes"),
                                            tags$ul(
                                              tags$li(HTML("<b>LASSO intuition:</b> Adds an L1 penalty that pulls small coefficients to exactly zero—like a budget that forces you to drop less useful predictors.")),
                                              tags$li(HTML("<b>Elastic Net:</b> α blends L1 (sparsity) and L2 (grouping). α=1 → LASSO; α=0 → Ridge.")),
                                              tags$li(HTML("<b>Choosing λ:</b> Use λ\u2098\u1D62\u1D4F for best validation error or λ\u2081\uFE0E\u209B (1-SE rule) for a simpler model.")),
                                              tags$li(HTML("<b>Tree importance:</b> Prefer <i>permutation</i> importance to avoid bias toward high-cardinality or noisy variables.")),
                                              tags$li(HTML("<b>Fair warning:</b> Importance ≠ causality. Correlated features can share credit; always sanity-check with domain knowledge."))
                                            )
                                     )
                                   )
                          )
              )
    )
  )
)

# ---- Server ----
server <- function(input, output, session){
  
  # Reactive dataset ---------------------------------------------------------
  raw_data <- reactive({
    switch(input$datasrc,
           mtcars = {
             df <- mtcars
             df$cyl <- factor(df$cyl)
             df$gear <- factor(df$gear)
             df$carb <- factor(df$carb)
             df$vs   <- factor(df$vs)
             df$am   <- factor(df$am)
             df
           },
           iris = {
             iris
           },
           boston = {
             MASS::Boston
           },
           upload = {
             req(input$csv)
             read.table(input$csv$datapath, header = input$header, sep = input$sep, stringsAsFactors = TRUE)
           }
    )
  })
  
  # Outcome selection UI -----------------------------------------------------
  output$outcome_ui <- renderUI({
    df <- raw_data()
    vars <- names(df)
    selectInput("outcome", "Outcome (target)", choices = vars, selected = vars[1])
  })
  
  output$data_preview <- renderDT({
    datatable(raw_data(), options = list(pageLength = 8, scrollX = TRUE))
  })
  
  # Train/Test split ---------------------------------------------------------
  split_data <- reactive({
    req(input$outcome)
    set.seed(123)
    df <- raw_data()
    # Drop rows with missing outcome
    df <- df[!is.na(df[[input$outcome]]), , drop = FALSE]
    n <- nrow(df)
    idx <- sample(seq_len(n), size = floor(input$split/100 * n))
    train <- df[idx, , drop = FALSE]
    test  <- df[-idx, , drop = FALSE]
    list(train=train, test=test)
  })
  
  # ------------------- LASSO -------------------
  lasso_fit <- eventReactive(input$fit_lasso, {
    parts <- split_data()
    train <- parts$train
    xy <- build_xy(train, input$outcome)
    y  <- xy$y
    fam <- family_for(y)
    if(fam != "gaussian") y <- as.factor(y)
    cvfit <- cv.glmnet(
      x = xy$x,
      y = y,
      family = fam,
      alpha = input$alpha,
      nfolds = input$folds,
      standardize = input$standardize,
      type.measure = ifelse(fam=="gaussian","mse","class")
    )
    # also fit full path for coef plots
    pathfit <- glmnet(
      x = xy$x,
      y = if(fam=="gaussian") xy$y else as.factor(xy$y),
      family = fam,
      alpha = input$alpha,
      standardize = input$standardize
    )
    list(cvfit=cvfit, pathfit=pathfit, fam=fam)
  })
  
  output$cvplot <- renderPlot({
    req(lasso_fit())
    plot(lasso_fit()$cvfit)
  })
  
  output$coefpath <- renderPlot({
    req(lasso_fit())
    plot(lasso_fit()$pathfit, xvar = "lambda")
  })
  
  output$lasso_selected <- renderDT({
    req(lasso_fit())
    cvfit <- lasso_fit()$cvfit
    tab_min <- nonzero_coefs(cvfit$glmnet.fit, s = cvfit$lambda.min)
    tab_1se <- nonzero_coefs(cvfit$glmnet.fit, s = cvfit$lambda.1se)
    
    # tag rows
    tab_min$Model <- "lambda.min"
    tab_1se$Model <- "lambda.1se"
    
    tab <- rbind(tab_min, tab_1se)
    tab <- tab[, c(setdiff(names(tab), "Model"), "Model")]
    datatable(tab, options=list(pageLength=8), rownames = FALSE)
  })
  
  output$lasso_metrics <- renderDT({
    req(lasso_fit())
    cvfit <- lasso_fit()$cvfit
    fam   <- lasso_fit()$fam
    parts <- split_data()
    
    # Build X for test
    xy_test <- build_xy(parts$test, input$outcome)
    
    if(fam == "gaussian"){
      preds <- as.numeric(predict(cvfit, newx = xy_test$x, s = "lambda.1se"))
      truth <- xy_test$y
    } else if(fam == "binomial"){
      p <- as.numeric(predict(cvfit, newx = xy_test$x, s = "lambda.1se", type = "response"))
      levs <- levels(as.factor(parts$train[[input$outcome]]))
      preds <- factor(ifelse(p > 0.5, levs[2], levs[1]), levels = levs)
      truth <- as.factor(xy_test$y)
    } else {
      # multinomial
      p <- predict(cvfit, newx = xy_test$x, s = "lambda.1se", type = "class")
      preds <- as.factor(p)
      truth <- as.factor(xy_test$y)
    }
    
    datatable(metric_summary(truth, preds, ifelse(fam=="gaussian","regression","classification")),
              options=list(dom='t'), rownames = FALSE)
  })
  
  # ------------------- Random Forest (ranger) -------------------
  tree_fit <- eventReactive(input$fit_tree, {
    parts <- split_data()
    train <- parts$train
    
    # Ensure outcome is factor for classification
    y <- train[[input$outcome]]
    task <- infer_task(y)
    if(task == "classification"){
      train[[input$outcome]] <- as.factor(train[[input$outcome]])
    }
    
    formula <- as.formula(paste(input$outcome, "~ ."))
    
    fit <- ranger(
      formula,
      data = train,
      num.trees = input$trees,
      mtry = ifelse(is.na(input$mtry) || input$mtry <= 0, NULL, input$mtry),
      min.node.size = input$min_n,
      importance = ifelse(input$vi_type=="impurity", "impurity", "permutation"),
      classification = (task == "classification"),
      seed = 123
    )
    
    list(fit = fit, task = task)
  })
  
  output$vip_plot <- renderPlot({
    req(tree_fit())
    imp <- as.data.frame(tree_fit()$fit$variable.importance)
    names(imp) <- c("Importance")
    imp$Feature <- rownames(imp)
    imp <- imp[order(imp$Importance, decreasing = TRUE),]
    imp <- head(imp, 20)
    
    ggplot(imp, aes(x = reorder(Feature, Importance), y = Importance)) +
      geom_col() +
      coord_flip() +
      labs(x = NULL, y = "Importance", title = "Top Features by Random Forest") +
      theme_minimal(base_size = 13)
  })
  
  output$tree_metrics <- renderDT({
    req(tree_fit())
    parts <- split_data()
    test <- parts$test
    fit  <- tree_fit()$fit
    task <- tree_fit()$task
    
    preds <- predict(fit, data = test)
    if(task == "regression"){
      pred <- preds$predictions
      truth <- test[[input$outcome]]
    } else {
      pred <- as.factor(preds$predictions)
      truth <- as.factor(test[[input$outcome]])
    }
    
    datatable(metric_summary(truth, pred, task), options=list(dom='t'), rownames = FALSE)
  })
}

shinyApp(ui, server)
