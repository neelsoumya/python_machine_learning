## Table of Contents

1. [Clustering Overview](#clustering-overview)
2. [Hierarchical Clustering](#hierarchical-clustering)
    - [Agglomerative (Bottom‑Up)](#agglomerative-bottomup)
    - [Divisive (Top‑Down)](#divisive-topdown)
    - [Dendrogram](#dendrogram)
    - [Practical](#practical)
3. [K‑Means Clustering](#k-means-clustering)
    - [Algorithm Steps](#algorithm-steps)
    - [Pseudocode](#pseudocode)
    - [Pros & Cons](#pros--cons)
4. [Choosing Between Methods](#choosing-between-methods)
    - [Hierarchical Clustering](#hierarchical-clustering-1)
    - [K‑Means](#k-means)
5. [References & Further Reading](#references--further-reading)




## Clustering Overview

Clustering is an **unsupervised learning** technique used to group similar data points together. Unlike classification, there are no pre-defined labels. Instead, the algorithm tries to discover structure in the data by maximizing intra-cluster similarity and minimizing inter-cluster similarity.

**Key points:**
- **Objective:** Identify natural groupings in the data.  
- **Applications:** Customer segmentation, image compression, anomaly detection, document clustering.

---

## Hierarchical Clustering

Hierarchical clustering builds a tree (dendrogram) of clusters using either a **bottom‑up** (agglomerative) or **top‑down** (divisive) approach.

### Agglomerative (Bottom‑Up)

1. **Initialization:** Start with each data point as its own cluster.  
2. **Merge Steps:**  
   - Compute distance between every pair of clusters.  
   - Merge the two closest clusters.  
   - Update the distance matrix.  
3. **Termination:** Repeat until all points are in a single cluster or a stopping criterion (e.g., desired number of clusters) is met.

### Divisive (Top‑Down)

1. **Initialization:** Start with all data points in one cluster.  
2. **Split Steps:**  
   - Choose a cluster to split (e.g., the one with highest variance).  
   - Partition it into two sub-clusters using a simple method (e.g., k‑means with k=2).  
3. **Termination:** Continue splitting until each point is its own cluster or the desired number of clusters is reached.

### Dendrogram

```text
        [ALL POINTS]
         /      \
    Cluster A   Cluster B
     /    \       /    \
    …      …     …      …
```


- **Cutting the tree** at different levels yields different numbers of clusters.
- **Linkage methods** determine how distance between clusters is computed:
  - **Single linkage:** Minimum pairwise distance  
  - **Complete linkage:** Maximum pairwise distance  
  - **Average linkage:** Average pairwise distance  

---

#### Practical

[Hierarchical Clustering in Python](https://github.com/neelsoumya/python_machine_learning/blob/main/hierarchical_clustering_python.ipynb)


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

### Animation

![Animation of k-means](images/animation_kmeans.gif)

<!-- created using kmeans_movie.py and kmeans_animation.ipynb -->

---


<!--
If you’re authoring for a site you control,
make sure you have MathJax loaded in the page’s <head>:
-->
<script>
window.MathJax = {
  tex: {
    inlineMath: [['$', '$'], ['\\(', '\\)']]
  }
};
</script>
<script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>


### Within–Cluster Variation

In **$K$**‑means clustering, we partition our $n$ observations into $K$ disjoint clusters
$\{C_1, C_2, \dots, C_K\}$.  A “good” clustering is one for which the _within‑cluster variation_ is minimized.

---

### Objective

Let

$$
W(C_k)
$$

be our measure of cluster‐$k$’s internal variation.  Then the $K$‑means objective is

$$
\min_{C_1,\dots,C_K}
\;\sum_{k=1}^{K} W(C_k).
$$

> _In words_: partition the data into $K$ clusters so the **total** within‐cluster variation is as small as possible.

---

### Defining $W(C_k)$

By far the most common choice is **squared Euclidean distance**.  If $C_k$ contains $|C_k|$ points
$\{x_i\}_{i\in C_k}\subset\mathbb R^p$, define

$$
W(C_k)
=
\frac{1}{|C_k|}
\sum_{\,i,i'\in C_k}
\sum_{\,j=1}^{p}
\bigl(x_{ij} - x_{i'j}\bigr)^{2}.
$$

Here:

- $|C_k|$ is the number of points in cluster $k$.  
- $x_{ij}$ is the $j$th coordinate of observation $i$.  
- We sum over all pairs of observations in $C_k$, and over all feature‐indices $j=1,\dots,p$.

Putting things together, the full optimization becomes:

$$
\min_{C_1,\dots,C_K}
\sum_{k=1}^{K}
\frac{1}{|C_k|}
\sum_{\,i,i'\in C_k}
\sum_{\,j=1}^{p}
\bigl(x_{ij} - x_{i'j}\bigr)^{2}.
$$


### Exercise

[IPython notebook for simple example of k-means](https://github.com/neelsoumya/python_machine_learning/blob/main/kmeans_simple.ipynb)

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

- Requires pre-specifying K.

---

## References & Further Reading

- [Introduction to Statistical Learning in Python (ISLP)](https://www.statlearning.com/)
- [IPython notebook from ISLP book](https://github.com/intro-stat-learning/ISLP_labs/blob/stable/Ch12-unsup-lab.ipynb)
- Scikit‑learn documentation:
  - [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
  - [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
