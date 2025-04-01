import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler

# Load the California Housing dataset
california = fetch_california_housing()
X = pd.DataFrame(california.data, columns=california.feature_names)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Create a biplot
plt.figure(figsize=(8, 6))

# Plot the PCA-transformed data
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, color='blue', label='Data Points')

# Plot the principal components as arrows
for i in range(X.shape[1]):
    plt.arrow(0, 0, pca.components_[0, i], pca.components_[1, i],
              color='red', alpha=0.8, width=0.005, head_width=0.1)
    plt.text(pca.components_[0, i] * 1.15, pca.components_[1, i] * 1.15,
             X.columns[i], color='black', ha='center', va='center')

# Labels and Title
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Biplot for California Housing Data')

# Show plot
plt.grid(True)
plt.show()

# Explained variance ratio
print("Explained variance ratio:", pca.explained_variance_ratio_)
