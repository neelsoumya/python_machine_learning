# Import required libraries
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import BinaryCrossentropy

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

# Build the MLP model
model = Sequential([
    Dense(32, input_dim=X_train.shape[1], activation='relu'),  # First hidden layer with 32 neurons
    Dense(16, activation='relu'),                             # Second hidden layer with 16 neurons
    Dense(1, activation='sigmoid')                            # Output layer with 1 neuron (binary classification)
])

# Compile the model
model.compile(optimizer=Adam(learning_rate=0.001),           # Optimizer
              loss=BinaryCrossentropy(),                    # Loss function for binary classification
              metrics=['accuracy'])                         # Metric to monitor during training

# Display the model's architecture
model.summary()

# Train the model
# Use 20% of the training data as validation data
history = model.fit(X_train, y_train, 
                    validation_split=0.2, 
                    epochs=50, 
                    batch_size=16, 
                    verbose=1)

# Evaluate the model on the testing set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy:.2f}")

# Save the model for future use
model.save("diabetes_mlp_model.h5")
print("Model saved as 'diabetes_mlp_model.h5'.")

# Predict on new data (optional)
predictions = model.predict(X_test)
print(predictions)
