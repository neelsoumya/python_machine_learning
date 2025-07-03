
- **Cutting the tree** at different levels yields different numbers of clusters.
- **Linkage methods** determine how distance between clusters is computed:
  - **Single linkage:** Minimum pairwise distance  
  - **Complete linkage:** Maximum pairwise distance  
  - **Average linkage:** Average pairwise distance  

---

## K‑Means Clustering

K‑Means is a **partitional** clustering algorithm that aims to partition the data into **K** disjoint clusters.

### Algorithm Steps

1. **Choose K**, the number of clusters.  
2. **Initialization:** Randomly select K initial centroids (or use k‑means++ for better seeding).  
3. **Assignment Step:**  
   ```pseudo
   for each data point x_i:
       assign x_i to cluster j whose centroid μ_j is nearest (minimize ||x_i - μ_j||²)
   ```
4. **Update Step:**
   ```pseudo
   for each cluster j:
       μ_j = (1 / |C_j|) * sum_{x_i in C_j} x_i
   ```
5. **Convergence Check:**
   - Stop when assignments no longer change, OR
   - The change in centroids is below a threshold, OR
   - A maximum number of iterations is reached.

#### Pseudocode

```pseudo
function KMeans(X, K, max_iters):
    # X: dataset of n points
    # K: desired number of clusters
    # max_iters: max number of iterations

    # 1. Initialize centroids μ randomly from X
    μ = initialize_centroids(X, K)

    for t in 1…max_iters:
        # 2. Assignment step
        for i in 1…n:
            cluster[i] = argmin_j ||X[i] - μ[j]||²

        # 3. Update step
        for j in 1…K:
            μ[j] = mean of all X[i] assigned to cluster j

        # 4. Check for convergence
        if centroids did not change:
            break

    return cluster, μ
```

---

### Pros & Cons

| Pros                      | Cons                                 |
|---------------------------|--------------------------------------|
| Fast and scalable         | Must choose K in advance             |
| Easy to implement         | Sensitive to initialization          |
| Works well on spherical data | Cannot capture non‑convex clusters |

---

## Choosing Between Methods

### Hierarchical Clustering

- No need to pre-specify number of clusters (can decide by cutting dendrogram).
- Computationally expensive for large datasets (O(n² log n)).
- Produces a full hierarchy of clusters.

### K‑Means

- Efficient: O(n K d · T) where d is dimensionality, T is iterations.
- Requires pre-specifying K.
- Best for well-separated, spherical clusters.

---

## References & Further Reading

- J. Han, M. Kamber, J. Pei. *Data Mining: Concepts and Techniques*.
- B. Everitt, S. Landau, M. Leese, D. Stahl. *Cluster Analysis*.
- Scikit‑learn documentation:
  - [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
  - [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
