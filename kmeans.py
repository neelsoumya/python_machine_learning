import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Load the California Housing dataset
california = fetch_california_housing()
X = pd.DataFrame(california.data, columns=california.feature_names)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # You can adjust n_clusters as needed
kmeans.fit(X_scaled)

# Add the cluster labels to the dataframe
X['Cluster'] = kmeans.labels_

# Perform PCA to reduce dimensions to 2 for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Plot the clusters
plt.figure(figsize=(8, 6))

# Plot each cluster in a different color
for i in range(5):  # 5 clusters, adjust as needed
    plt.scatter(X_pca[kmeans.labels_ == i, 0], X_pca[kmeans.labels_ == i, 1], label=f'Cluster {i}')

# Plot centroids
centroids = pca.transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=200, color='black', label='Centroids')

# Labels and Title
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('K-Means Clustering on California Housing Data (PCA Reduced)')

# Show plot
plt.legend()
plt.grid(True)
plt.show()

# Print the cluster centers in original feature space
print("Cluster Centers (in original feature space):")
print(kmeans.cluster_centers_)
