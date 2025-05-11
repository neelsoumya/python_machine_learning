# script to demonstrate gradient descent
import matplotlib.pyplot as plt
import numpy as np

# Define the cost function J(θ) = (θ - 3)^2
def J(theta):
    return (theta - 3)**2

# Gradient of the cost function
def grad_J(theta):
    return 2 * (theta - 3)

# Initialize parameters
theta = 0.0
alpha = 0.1
iterations = 10

# Store the path of θ updates
theta_history = [theta]
for _ in range(iterations):
    theta = theta - alpha * grad_J(theta)
    theta_history.append(theta)

# Generate θ values for plotting the cost function
theta_vals = np.linspace(-1, 5, 100)
cost_vals = J(theta_vals)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(theta_vals, cost_vals, label=r'$J(\theta) = (\theta - 3)^2$')
plt.scatter(theta_history, J(np.array(theta_history)), color='red', zorder=5)
for i in range(len(theta_history)-1):
    plt.annotate('', xy=(theta_history[i+1], J(theta_history[i+1])),
                 xytext=(theta_history[i], J(theta_history[i])),
                 arrowprops=dict(arrowstyle='->', color='red'))

plt.title('Gradient Descent on $J(\\theta) = (\\theta - 3)^2$')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$J(\theta)$')
plt.grid(True)
plt.legend()
plt.show()
