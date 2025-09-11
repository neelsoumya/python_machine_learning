# Logistic Regression for Biologists: Teaching Resources

## Overview
This resource provides a comprehensive introduction to logistic regression for biology students, with practical examples using biological data.

## Learning Objectives
By the end of this module, students will be able to:
- Understand when to use logistic regression vs linear regression
- Implement logistic regression in Python
- Interpret coefficients and odds ratios
- Create and interpret log-odds plots
- Evaluate model performance using appropriate metrics

## 1. Introduction to Logistic Regression

### When to Use Logistic Regression
- **Binary outcomes**: Disease/No disease, Survival/Death, Presence/Absence of species
- **Categorical outcomes**: Species classification, Treatment response categories
- **Probability modeling**: Predicting probability of an event occurring

### Key Concepts
- **Logit function**: ln(p/(1-p)) where p is probability
- **Odds**: p/(1-p) - ratio of probability of success to probability of failure
- **Log-odds**: Natural logarithm of odds
- **Sigmoid function**: Maps any real number to value between 0 and 1

## 2. Mathematical Foundation

The logistic regression equation:
```
logit(p) = ln(p/(1-p)) = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

Where:
- p = probability of positive outcome
- β₀ = intercept
- βᵢ = coefficients for predictors
- xᵢ = predictor variables

## 3. Practical Examples

### Example 1: Predicting Disease Presence
Dataset: Patient data with biomarkers predicting disease presence

### Example 2: Species Survival Analysis
Dataset: Environmental factors predicting species survival

### Example 3: Gene Expression Classification
Dataset: Gene expression levels predicting cancer type

## 4. Code Implementation

See the accompanying Python notebook for complete implementations including:
- Data preprocessing
- Model fitting
- Coefficient interpretation
- Log-odds plotting
- Model evaluation
- Cross-validation

## 5. Interpretation Guidelines

### Coefficients
- Positive coefficient: Increases log-odds (increases probability)
- Negative coefficient: Decreases log-odds (decreases probability)
- Magnitude: Strength of effect

### Odds Ratios
- OR = e^β
- OR > 1: Positive association
- OR < 1: Negative association
- OR = 1: No association

## 6. Model Evaluation Metrics

### Classification Metrics
- **Accuracy**: Overall correct predictions
- **Precision**: True positives / (True positives + False positives)
- **Recall (Sensitivity)**: True positives / (True positives + False negatives)
- **Specificity**: True negatives / (True negatives + False positives)
- **F1-Score**: Harmonic mean of precision and recall

### Probability Metrics
- **Log-likelihood**: Goodness of fit measure
- **AIC/BIC**: Model selection criteria
- **ROC-AUC**: Area under ROC curve

## 7. Common Pitfalls and Solutions

### Pitfall 1: Linear Separability
**Problem**: Perfect classification leads to infinite coefficients
**Solution**: Regularization (Ridge/Lasso) or collect more data

### Pitfall 2: Multicollinearity
**Problem**: Correlated predictors inflate standard errors
**Solution**: Remove correlated variables or use PCA

### Pitfall 3: Sample Size
**Problem**: Small samples lead to unstable estimates
**Solution**: Rule of thumb - at least 10 events per predictor

## 8. Extensions

### Multinomial Logistic Regression
For outcomes with >2 categories (e.g., species classification)

### Ordinal Logistic Regression
For ordered categorical outcomes (e.g., disease severity: mild/moderate/severe)

### Mixed-Effects Logistic Regression
For hierarchical data (e.g., patients within hospitals)

## 9. Practical Exercises

### Exercise 1: Basic Implementation
Fit a logistic regression model to predict butterfly presence based on temperature and humidity.

### Exercise 2: Model Comparison
Compare logistic regression with decision trees for species classification.

### Exercise 3: Feature Selection
Use stepwise selection to identify important biomarkers for disease prediction.

## 10. Further Reading

### Key Papers
- Hosmer, D.W. & Lemeshow, S. (2013). Applied Logistic Regression, 3rd Edition
- Agresti, A. (2018). An Introduction to Categorical Data Analysis, 3rd Edition

### Online Resources
- scikit-learn documentation for LogisticRegression
- statsmodels documentation for detailed statistical output
- Biological applications in ecology and epidemiology journals

## Assessment Ideas

### Formative Assessment
- Quick quizzes on interpreting coefficients
- Coding exercises with immediate feedback
- Peer review of log-odds plots

### Summative Assessment
- Analysis of provided biological dataset
- Written interpretation of results
- Comparison with alternative methods
- Critical evaluation of assumptions
