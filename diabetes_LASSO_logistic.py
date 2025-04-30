# Import required libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dynamically construct the file path using the os package
current_directory = os.getcwd()  # Get the current working directory
file_name = "diabetes_kaggle.csv"  # Name of the CSV file
file_path = os.path.join(current_directory, "data", file_name)  # Construct the full file path

# Load the dataset using pandas
data = pd.read_csv(file_path)

# Display the first few rows of the dataset to understand its structure
print("Dataset preview:")
print(data.head())

# Separate features (X) and target variable (y)
X = data.drop(columns=['Outcome'])  # All columns except 'Outcome'
y = data['Outcome']                # The 'Outcome' column

# Normalize the features using StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the dataset into training and testing sets
# 80% of the data will be used for training, and 20% for testing
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Initialize the Logistic Regression model with LASSO (L1 regularization)
log_reg_lasso = LogisticRegression(penalty='l1', solver='liblinear', random_state=42, max_iter=1000)

# Train the model
log_reg_lasso.fit(X_train, y_train)

# Evaluate the model on the testing set
y_pred = log_reg_lasso.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Test Accuracy with LASSO: {accuracy:.2f}")

# Predict on new data (optional)
predictions = log_reg_lasso.predict_proba(X_test)[:, 1]  # Probability of the positive class
print(predictions)
