# Logistic Regression Practical Exercises for Biology Students

## Overview
This document contains hands-on exercises designed to help biology students understand and apply logistic regression to real biological problems. Each exercise builds on previous concepts and includes both guided analysis and independent exploration.

---

## **Exercise 1: Basic Logistic Regression - Butterfly Habitat Preference**

### Background
You are studying butterfly habitat preferences in a nature reserve. You have collected data on butterfly presence/absence at 200 different sites, along with environmental measurements.

### Dataset Variables
- `temperature`: Average temperature (°C)
- `humidity`: Average humidity (%)
- `flower_density`: Number of flowering plants per m²
- `butterfly_presence`: 1 if butterflies observed, 0 if not

### Tasks

#### Part A: Exploratory Data Analysis (20 points)
1. Load the butterfly dataset using the provided Python code
2. Calculate descriptive statistics for all variables
3. Create histograms for each predictor variable
4. Calculate the proportion of sites where butterflies were present
5. Create boxplots comparing environmental conditions between sites with and without butterflies

**Questions to Answer:**
- What is the overall detection rate for butterflies?
- Which environmental variables show the clearest differences between presence/absence sites?
- Are there any obvious outliers in the data?

#### Part B: Simple Logistic Regression (25 points)
1. Fit a logistic regression model with temperature as the only predictor
2. Extract and interpret the coefficient
3. Calculate the odds ratio and 95% confidence interval
4. Create a log-odds plot for temperature
5. Plot the predicted probability curve over the raw data

**Questions to Answer:**
- What is the effect of a 1°C temperature increase on butterfly presence odds?
- At what temperature is the predicted probability of butterfly presence 50%?
- Is the relationship between temperature and butterfly presence statistically significant?

#### Part C: Multiple Logistic Regression (30 points)
1. Fit a model with all three predictors (temperature, humidity, flower_density)
2. Compare AIC values between the simple and multiple regression models
3. Interpret all coefficients and odds ratios
4. Check for multicollinearity using correlation matrix
5. Evaluate model fit using residual plots

**Questions to Answer:**
- Which predictors are statistically significant in the full model?
- How do the coefficients change when moving from simple to multiple regression?
- Which model would you recommend and why?

#### Part D: Model Validation (25 points)
1. Split data into training (80%) and testing (20%) sets
2. Fit model on training data and evaluate on test data
3. Create confusion matrix and calculate accuracy, sensitivity, specificity
4. Plot ROC curve and calculate AUC
5. Perform 5-fold cross-validation

**Questions to Answer:**
- How well does the model perform on unseen data?
- What is the optimal probability threshold for classification?
- Are there signs of overfitting?

---

## **Exercise 2: Advanced Analysis - Disease Risk Prediction**

### Background
You are analyzing a medical dataset to identify risk factors for a particular disease. The dataset contains patient information and biomarker measurements.

### Dataset Variables
- `age`: Patient age (years)
- `bmi`: Body Mass Index
- `cholesterol`: Total cholesterol (mg/dL)
- `blood_pressure`: Systolic blood pressure (mmHg)
- `inflammation_marker`: C-reactive protein level
- `disease_status`: 1 if disease present, 0 if absent

### Tasks

#### Part A: Data Preprocessing (15 points)
1. Check for missing values and outliers
2. Standardize continuous predictors (z-scores)
3. Create age groups (e.g., <40, 40-60, >60) for categorical analysis
4. Examine class balance (disease vs. no disease)

#### Part B: Model Building Strategy (25 points)
1. Start with univariate models for each predictor
2. Use forward stepwise selection to build multivariable model
3. Test for interactions between significant predictors
4. Compare nested models using likelihood ratio tests

#### Part C: Advanced Diagnostics (35 points)
1. Check model assumptions using diagnostic plots
2. Identify influential observations using Cook's distance
3. Test for linearity assumption using cubic splines
4. Assess goodness of fit using Hosmer-Lemeshow test

#### Part D: Clinical Interpretation (25 points)
1. Convert all results to clinically meaningful units
2. Create a risk calculator for new patients
3. Determine optimal cutoff for clinical decision making
4. Discuss limitations and potential confounding factors

---

## **Exercise 3: Ecological Application - Species Distribution Modeling**

### Background
You are modeling the probability of finding a rare plant species across different forest plots based on environmental gradients.

### Dataset Variables
- `elevation`: Plot elevation (m)
- `slope`: Terrain slope (degrees)
- `aspect`: Slope direction (degrees from north)
- `canopy_cover`: Percentage canopy coverage
- `soil_ph`: Soil pH
- `distance_water`: Distance to nearest water source (m)
- `species_present`: 1 if species found, 0 if absent

### Tasks

#### Part A: Ecological Hypothesis Testing (30 points)
1. Formulate biological hypotheses about species-environment relationships
2. Transform variables as needed (e.g., log-transform distance)
3. Create derived variables (e.g., northerness from aspect)
4. Test each hypothesis using appropriate statistical models

#### Part B: Non-linear Relationships (35 points)
1. Test for quadratic relationships (e.g., optimal elevation range)
2. Use polynomial terms and GAMs for complex relationships
3. Compare linear vs. non-linear models using AIC
4. Create response curves showing probability vs. environmental gradients

#### Part C: Spatial Considerations (35 points)
1. Check for spatial autocorrelation in residuals
2. Include spatial coordinates as predictors
3. Compare with and without spatial terms
4. Create prediction maps across the landscape

---

## **Exercise 4: Comparative Study - Method Comparison**

### Background
Compare logistic regression with other classification methods using the same biological dataset.

### Tasks

#### Part A: Benchmark Comparison (40 points)
1. Implement logistic regression, decision trees, and random forest
2. Use same train/test splits for fair comparison
3. Compare performance using multiple metrics
4. Create learning curves showing performance vs. sample size

#### Part B: Feature Importance (30 points)
1. Extract feature importance from each method
2. Compare variable rankings across methods
3. Identify consistently important predictors
4. Discuss biological interpretation of important features

#### Part C: Model Interpretability (30 points)
1. Compare ease of interpretation across methods
2. Create partial dependence plots for complex models
3. Discuss trade-offs between accuracy and interpretability
4. Make recommendations for different use cases

---

## **Assessment Rubric**

### Excellent (A: 90-100%)
- Comprehensive analysis with all components completed correctly
- Clear biological interpretation of statistical results
- Appropriate use of visualization and diagnostic tools
- Critical thinking about assumptions and limitations
- Professional quality code with good documentation

### Proficient (B: 80-89%)
- Most components completed correctly with minor errors
- Generally appropriate interpretation of results
- Good use of statistical methods and visualizations
- Some consideration of assumptions and limitations
- Well-organized code with adequate documentation

### Developing (C: 70-79%)
- Basic analysis completed with some significant errors
- Limited interpretation of biological significance
- Basic use of statistical methods
- Minimal consideration of assumptions
- Functional but poorly documented code

### Needs Improvement (D: 60-69%)
- Incomplete analysis with major errors or omissions
- Poor or incorrect interpretation of results
- Inappropriate use of statistical methods
- No consideration of assumptions or limitations
- Poorly written or non-functional code

---

## **Submission Requirements**

### Format
- Jupyter notebook with code, output, and interpretations
- Maximum 15 pages including figures and tables
- Professional formatting with clear section headers

### Content Requirements
1. **Executive Summary** (1 page): Key findings and conclusions
2. **Methods** (2-3 pages): Statistical approach and justification
3. **Results** (4-6 pages): Statistical output with biological interpretation
4. **Discussion** (2-3 pages): Broader implications and limitations
5. **Code Appendix**: Well-commented, reproducible code

### Evaluation Criteria
- **Statistical Accuracy (40%)**: Correct implementation and interpretation
- **Biological Insight (30%)**: Meaningful biological conclusions
- **Communication (20%)**: Clear writing and effective visualizations
- **Code Quality (10%)**: Reproducible, well-documented code

---

## **Additional Resources**

### Required Reading
1. Hosmer, D.W. & Lemeshow, S. (2013). Applied Logistic Regression, Chapters 1-4
2. Zuur, A.F. et al. (2009). Mixed Effects Models in Ecology, Chapter 6
3. James, G. et al. (2013). Introduction to Statistical Learning, Chapter 4

### Optional Reading
1. Harrell, F.E. (2015). Regression Modeling Strategies, Chapters 10-12
2. Agresti, A. (2018). Introduction to Categorical Data Analysis, Chapters 5-6

### Online Resources
- scikit-learn documentation: Logistic Regression
- statsmodels documentation: GLM and Logit
- Cross Validated (Stack Exchange) for statistical questions
- Towards Data Science articles on logistic regression

### Software Requirements
- Python 3.7+ with packages: pandas, numpy, matplotlib, seaborn, scikit-learn, statsmodels
- Jupyter Notebook or JupyterLab
- Optional: R with packages: glm, car, pROC, ggplot2

---

## **Extension Activities**

### For Advanced Students
1. **Regularized Regression**: Implement Ridge and Lasso logistic regression
2. **Bayesian Approach**: Compare with Bayesian logistic regression
3. **Multilevel Models**: Account for hierarchical data structure
4. **Time Series**: Logistic regression with temporal autocorrelation

### Real-World Applications
1. **Conservation Biology**: Species at risk assessment
2. **Epidemiology**: Disease outbreak prediction
3. **Agricultural Science**: Crop disease susceptibility
4. **Ecology**: Climate change impact modeling

### Programming Challenges
1. Implement logistic regression from scratch using gradient descent
2. Create interactive web app for exploring logistic regression
3. Build automated report generation system
4. Develop cross-platform mobile app for field predictions
