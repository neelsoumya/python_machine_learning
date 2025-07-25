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

### Important Concepts


- **Metric**  
  The *metric* (or distance function or dissimilarity function) defines how you measure the distance between individual data points. Common choices include Euclidean, Manhattan (cityblock), or cosine distance. This metric determines the “raw” pairwise distances.

*Euclidean distance*

![Euclidean distance](images/euclidean_distance.png)

*Manhattan distance*

![Manhattan distance](images/manhattan_distance.png)


- **Linkage**  
  The *linkage* method defines how to compute the distance between two clusters based on the pairwise distances of their members. Examples:  
  - **Single**: the distance between the closest pair of points (one from each cluster).  
  - **Complete**: the distance between the farthest pair of points.  
  - **Average**: the average of all pairwise distances.  
  - **Ward**: the merge that minimizes the increase in total within‑cluster variance.  

*Linkage function*

![Linkage function](images/linkage_function.png)


| Linkage Method        | How It Works                                                                                     | Intuition                                                                                       |
|-----------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Single**            | Distance = minimum pairwise distance between points in the two clusters                         | “Friends‑of‑friends” – clusters join if any two points are close, yielding chain‑like clusters  |
| **Complete**          | Distance = maximum pairwise distance between points in the two clusters                         | “Everyone must be close” – only merge when all points are relatively near, producing compact clusters |
| **Average (UPGMA)**   | Distance = average of all pairwise distances between points in the two clusters                 | Balances single and complete by averaging close and far pairs                                  |
| **Weighted (WPGMA)**  | Distance = average of the previous cluster’s distance to the new cluster (equal weight per cluster) | Prevents large clusters from dominating, giving equal say to each cluster                      |
| **Centroid**          | Distance = distance between the centroids (mean vectors) of the two clusters                    | Merges based on “centers of mass,” but centroids can shift non‑monotonically                   |
| **Median (WPGMC)**    | Distance = distance between the medians of the two clusters                                      | More robust to outliers than centroid linkage, but can also invert dendrogram order            |
| **Ward’s**            | Merge that minimizes the increase in total within‑cluster sum of squares (variance)             | Keeps clusters as tight and homogeneous as possible, often resulting in evenly sized groups     |


### Single Linkage
- **How it works**: Measures the distance between two clusters as the smallest distance between any single point in one cluster and any single point in the other.  
- **Intuition**: “Friends‑of‑friends” clustering—if any two points (one from each cluster) are close, the clusters join. Can produce long, straggly chains of points.

### Complete Linkage
- **How it works**: Measures the distance between two clusters as the largest distance between any point in one cluster and any point in the other.  
- **Intuition**: “Everyone must be close”—clusters merge only when all their points are relatively near each other, leading to tight, compact groups.

### Average Linkage (UPGMA)
- **How it works**: Takes the average of all pairwise distances between points in the two clusters.  
- **Intuition**: A middle‑ground between single and complete linkage—balances the effect of very close and very far pairs by averaging them.

### Weighted Linkage (WPGMA)
- **How it works**: Similar to average linkage, but treats each cluster as a single entity by averaging the distance from each original cluster to the target cluster, regardless of cluster size.  
- **Intuition**: Prevents larger clusters from dominating the average—gives each cluster equal say in how far apart they are.

### Centroid Linkage
- **How it works**: Computes the distance between the centroids (mean vectors) of the two clusters.  
- **Intuition**: Clusters merge based on whether their “centers of mass” are close. Can sometimes lead to non‑monotonic merges if centroids shift oddly.

### Median Linkage (WPGMC)
- **How it works**: Uses the median point of each cluster instead of the mean when computing distance between clusters.  
- **Intuition**: Like centroid linkage but more robust to outliers, since the median isn’t pulled by extreme values—though can also cause inversion issues.

### Ward’s Method
- **How it works**: At each step, merges the two clusters whose union leads to the smallest possible increase in total within‑cluster variance (sum of squared deviations).  
- **Intuition**: Always chooses the merge that keeps clusters as tight and homogeneous as possible, often yielding groups of similar size and shape.


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

$$ W(C_k) $$

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


---

## Choosing Between Methods

### Hierarchical Clustering

- No need to pre-specify number of clusters (can decide by cutting dendrogram).
- Produces a full hierarchy of clusters.

### K‑Means

- Requires pre-specifying $K$.

---

## References & Further Reading

- [Introduction to Statistical Learning in Python (ISLP)](https://www.statlearning.com/)
- [IPython notebook from ISLP book](https://github.com/intro-stat-learning/ISLP_labs/blob/stable/Ch12-unsup-lab.ipynb)
- Scikit‑learn documentation:
  - [AgglomerativeClustering](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html)
  - [KMeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)
