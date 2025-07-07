
# Unsupervised Learning in High Dimensions and the Curse of Dimensionality

---

## Motivation & Objectives

**Learning Objectives**
- Understand how volume concentrates in high dimensions.  
- See why distance–based clustering (k‑Means) degrades as \(n\) grows.  
- Discover how t‑SNE leverages local similarities to bypass some issues.

---

## Curse of Dimensionality

### Volume in High Dimensions

- In $\([-1,1]^n\)$, most volume lives near the corners; an inscribed ball is tiny.  
 $ \[
    V_n \;=\; \frac{\pi^{n/2}}{\Gamma\!\bigl(\tfrac n2+1\bigr)},
  \]
  \[
    V_{10}\approx2.5\times10^{-3},\quad V_{50}\approx10^{-28}.
  \] $
- Although $\(V_n>0\)$ for each finite $\(n\)$, $\(\lim_{n\to\infty}V_n=0\)$: for any $\(\varepsilon>0\)$, large enough $\(n\)$ gives $\(V_n<\varepsilon\)$.

![Volume in High Dimensions](hyperball_corners.png)

---

## Implications for Distance

- Pairwise distances between random points in high‑$\(n\)$ concentrate:
 $ \[
    \frac{\max d - \min d}{\min d}\;\to\;0.
  \] $
- “Nearest” vs “farthest” becomes less distinct.  
- A fixed‑radius ball contains almost no points.

*Show a plot of min/max distance ratio vs. dimension.*

---

## k‑Means & High Dimensions

### k‑Means Recap

- **Objective:** minimize within‑cluster squared distances.  
- **Relies on:** meaningful notion of “closest centroid.”  

**Curse effect:** if all distances look the same, assignment becomes noisy.

---

### Demo: Distance Concentration

**Exercise:**  
- Sample 1,000 points in $\(\mathbb{R}^n\)$ with $\(n = 2, 10, 50, 200\)$.  
- Compute min and max Euclidean distances; plot $\((\max-\min)/\min\)$ vs. $\(n\)$.

[Demo of distance concentration](https://github.com/neelsoumya/python_machine_learning/blob/main/high_dimensions_pairwise_distances.ipynb)

```python
import numpy as np

def distance_ratio(n, N=1000, seed=0):
    rng = np.random.default_rng(seed)
    X = rng.standard_normal((N, n))
    sum_sq = np.sum(X**2, axis=1, keepdims=True)
    D2 = sum_sq + sum_sq.T - 2 * X.dot(X.T)
    D2 = np.clip(D2, 0, None)
    i, j = np.triu_indices(N, k=1)
    d = np.sqrt(D2[i, j])
    return (d.max() - d.min()) / d.min()

for n in [2, 10, 50, 200]:
    ratio = distance_ratio(n)
    print(f"Dimension {n}: ratio = {ratio:.4f}")
````

---

### k‑Means Failure Mode

* In high‑$n$, clusters defined by small shifts in centroids barely change assignments.
* Algorithms get stuck: *no clear gradients* in assignment.

![k‑Means in High Dimensions](kmeans_highdim.png)

---

## t‑SNE to the Rescue

### t‑Distributed Stochastic Neighbor Embedding

* Builds pairwise affinities $p_{ij}$ based on local Gaussian kernels in high‑dim.
* Seeks low‑dim map where Student‑t affinities $q_{ij}$ match $p_{ij}$.
* Emphasis on preserving *local* structure.

---

### Why t‑SNE Works in High Dimensions

* Bypasses global distance concentration by focusing on nearest neighbors.
* Heavy‑tailed low‑dim distribution allows moderate repulsion of dissimilar points.
* Visualizes clusters even when Euclidean distances are uninformative.

![t‑SNE Example](tsne_example.png)

---

## Hands‑On Lab

**Dataset:** Hand‑written digits (e.g. MNIST, $n=784$).

1. Run k‑Means with $k=10$; report inertia and 2‑D PCA plot colored by cluster.
2. Compute t‑SNE embedding (perplexity=30); plot and compare cluster separation.
3. Write a short reflection: how did the curse manifest? how did t‑SNE help?

[Hands-on Lab curse of dimensionality](https://github.com/neelsoumya/python_machine_learning/blob/main/lab_mnist_curse_dimensionality.ipynb)

---

## Wrap‑Up & Discussion

**Takeaways**

* High dimensions make global distances meaningless.
* Algorithms like k‑Means suffer because cluster assignments become noisy.
* Methods that leverage *local* structure (t‑SNE, UMAP) can still find patterns.

---

# Questions?



