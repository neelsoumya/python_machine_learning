import numpy as np
import pandas as pd
import tensorflow as tf
import keras_tuner as kt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Load California housing dataset
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Define a function to build the model for KerasTuner
def build_model(hp):
    model = Sequential()
    
    # Number of hidden layers (between 1 and 3)
    for i in range(hp.Int("num_layers", 1, 3)):  
        model.add(Dense(
            units=hp.Int(f"units_{i}", min_value=32, max_value=256, step=32),  
            activation="relu"
        ))

    # Output layer (single neuron for regression)
    model.add(Dense(1))

    # Compile the model with tunable learning rate
    model.compile(
        optimizer=Adam(learning_rate=hp.Choice("learning_rate", [0.001, 0.0005, 0.0001])),
        loss="mean_squared_error"
    )
    
    return model

# Use KerasTuner to find the best hyperparameters
tuner = kt.RandomSearch(
    build_model,
    objective="val_loss",
    max_trials=10,  # Number of different hyperparameter sets to try
    executions_per_trial=1,
    directory="my_tuning",
    project_name="california_housing"
)

# Perform the hyperparameter search
tuner.search(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Get the best hyperparameters
best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]

# Print the best hyperparameters
print(f"""
Optimal number of layers: {best_hps.get('num_layers')}
Optimal neurons per layer: {[best_hps.get(f'units_{i}') for i in range(best_hps.get('num_layers'))]}
Optimal learning rate: {best_hps.get('learning_rate')}
""")

# Build and train the best model
best_model = tuner.hypermodel.build(best_hps)
history = best_model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate on the test set
test_loss = best_model.evaluate(X_test, y_test)
print(f"Test Loss: {test_loss}")

# Predictions
predictions = best_model.predict(X_test)

# Display first 5 predictions
print(f"Predictions (first 5): {predictions[:5].flatten()}")
