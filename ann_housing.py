import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load the California Housing dataset
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the artificial neural network model
model = Sequential()

# Input layer with 8 neurons (since there are 8 features)
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))

# Hidden layer with 32 neurons
model.add(Dense(32, activation='relu'))

# Output layer with 1 neuron (since we're predicting a continuous value)
model.add(Dense(1))

# Compile the model with Mean Squared Error loss and Adam optimizer
model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=0.001))

# Train the model
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model on the test set
test_loss = model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}")

# Predictions on the test set
predictions = model.predict(X_test)

# Display the first 5 predictions
print(f"Predictions (first 5): {predictions[:5].flatten()}")
