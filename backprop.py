import numpy as np

# Activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Input and true output
x = np.array([[0.5], [0.1]])  # shape (2, 1)
y_true = np.array([[1]])      # target output

# Initialize weights and biases randomly
np.random.seed(42)
W1 = np.random.randn(2, 2)    # weights for input to hidden
b1 = np.random.randn(2, 1)    # bias for hidden layer
W2 = np.random.randn(1, 2)    # weights for hidden to output
b2 = np.random.randn(1, 1)    # bias for output layer

# --- FORWARD PASS ---
z1 = W1 @ x + b1             # linear combination (hidden layer)
a1 = sigmoid(z1)             # activation (hidden layer)
z2 = W2 @ a1 + b2            # linear combination (output layer)
y_pred = sigmoid(z2)         # output activation

# --- LOSS ---
loss = 0.5 * (y_pred - y_true) ** 2
print("Loss:", loss.item())

# --- BACKWARD PASS ---
# Output layer gradient
dL_dy = y_pred - y_true                   # derivative of loss w.r.t. prediction
dy_dz2 = sigmoid_derivative(z2)
dz2_dW2 = a1.T
dz2_db2 = 1

dL_dz2 = dL_dy * dy_dz2                   # shape (1, 1)
dL_dW2 = dL_dz2 @ dz2_dW2                 # shape (1, 2)
dL_db2 = dL_dz2 * dz2_db2                 # shape (1, 1)

# Hidden layer gradient
dz2_da1 = W2.T
da1_dz1 = sigmoid_derivative(z1)
dz1_dW1 = x.T
dz1_db1 = 1

dL_dz1 = dz2_da1 @ dL_dz2 * da1_dz1       # shape (2, 1)
dL_dW1 = dL_dz1 @ dz1_dW1                 # shape (2, 2)
dL_db1 = dL_dz1 * dz1_db1                 # shape (2, 1)

# Print gradients
print("\nGradients:")
print("dL/dW2:\n", dL_dW2)
print("dL/db2:\n", dL_db2)
print("dL/dW1:\n", dL_dW1)
print("dL/db1:\n", dL_db1)

# --- PARAMETER UPDATE (Gradient Descent Step) ---
alpha = 0.1
W2 -= alpha * dL_dW2
b2 -= alpha * dL_db2
W1 -= alpha * dL_dW1
b1 -= alpha * dL_db1
