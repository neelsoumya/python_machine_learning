# Lecture Notes: Principal Component Analysis (PCA) for Biologists

## 🧬 Overview

Principal Component Analysis (PCA) is a **dimensionality reduction technique**. It transforms a large set of variables into a smaller one that still contains most of the information in the large set.

It is widely used in biology for:

* Gene expression analysis
* Population genetics
* Imaging data
* Single-cell RNA-seq

---

## 🧠 Intuition

Imagine you have a dataset with many variables (e.g. expression levels of 10,000 genes). PCA helps us:

* Reduce the number of variables
* Identify patterns
* Remove noise
* Visualize high-dimensional data

PCA finds **new axes** (called **principal components**) that capture the maximum variance in the data.

*Step 1*: Center the data
Subtract the mean so the data is centered at the origin.

*Step 2*: Find the direction of maximum variance
PCA finds a new axis (PC1) that goes through the direction where the data varies the most:


Y-axis
  |
  |\        *
  |  \*  *       *
  |    \    *      *
  |      \     *
  |_______\_________________ X-axis
         /
        /
    PC1 /

*Step 3*: Project the data onto the new axes
Each data point is now described by its position along PC1 and (optionally) PC2.

Y-axis
  |
  |       .  .       .
  |    .      .  .      .
  |        .
  |________________________ X-axis
     <--- PC1 axis --->

PC1 captures the most variance in the data.
PC2 (perpendicular to PC1) captures the next most variance.

*Summary*:

PCA rotates the axes of your data so the greatest variation comes along the first principal components, allowing you to reduce dimensionality while keeping the most important information.


---


# Lecture Notes: Principal Component Analysis (PCA) for Biologists

## 🧬 Overview

Principal Component Analysis (PCA) is a **dimensionality reduction technique**. It transforms a large set of variables into a smaller one that still contains most of the information in the large set.

It is widely used in biology for:

* Gene expression analysis
* Population genetics
* Imaging data
* Single-cell RNA-seq

---

## 🧠 Intuition

Imagine you have a dataset with many variables (e.g. expression levels of 10,000 genes). PCA helps us:

* Reduce the number of variables
* Identify patterns
* Remove noise
* Visualize high-dimensional data

PCA finds **new axes** (called **principal components**) that capture the maximum variance in the data.

---

## 📊 Key Concepts



## 📊 Key Concepts

### 1. **Variance**

* Variance = how spread out the data is.
* PCA finds directions (principal components) that maximize variance.

Formula for variance of variable $x$:

$$
\text{Var}(x) = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
$$

### 2. **Covariance Matrix**

* Tells us how variables vary together.
* PCA uses this to find directions where the data varies the most.

Covariance between variables $x$ and $y$:

$$
\text{Cov}(x, y) = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})
$$

### 3. **Eigenvectors and Eigenvalues**

* Eigenvectors = directions (principal components)
* Eigenvalues = amount of variance explained by each component

---

## 🧪 Step-by-Step PCA Procedure

Given a dataset with samples (rows) and features (columns):

1. **Standardize** the data (mean = 0, variance = 1)
2. **Compute the covariance matrix**
3. **Calculate eigenvectors and eigenvalues**
4. **Sort** eigenvectors by decreasing eigenvalues
5. **Choose top k** eigenvectors (components)
6. **Project data** onto these components

---

## 🔬 Example: Gene Expression Data

* Rows = samples (patients)
* Columns = gene expression levels

### Goal:

* Reduce dimensionality from 20,000 genes to 2-3 PCs
* Visualize patterns between patient groups (e.g., healthy vs. cancer)

```python
# Sample Python code (requires numpy, sklearn, matplotlib)
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

X = ...  # gene expression matrix
X_scaled = StandardScaler().fit_transform(X)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA of Gene Expression')
plt.show()
```

---

## 📈 Interpreting the Output

* **Scree plot**: plots variance explained by each PC
* **Loadings**: show how much each original variable contributes to each PC
* **Biplots**: show samples and variables in the same plot

---

## 🧠 PCA vs. Other Techniques

* PCA is **unsupervised** (no labels used)
* Works best for **linear** relationships
* Alternatives:

  * t-SNE / UMAP for nonlinear structures
  * LDA (Linear Discriminant Analysis) for classification tasks

---

## 🧬 In Practice: Tips for Biologists

* Always **standardize** data before PCA
* Use **log-transformation** for count data (e.g., RNA-seq)
* Be cautious interpreting PCs biologically—PCs are **mathematical constructs**

---

## 📚 Further Reading

* "Principal Component Analysis" by Jolliffe
* scikit-learn documentation: [https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
* Bioinformatics tutorials on PCA:

  * [https://bioconductor.org](https://bioconductor.org)
  * [https://towardsdatascience.com](https://towardsdatascience.com) (search "PCA biology")

---

## ❓ Q\&A

* Q: Can PCA tell me which genes are important?

  * A: It shows which genes contribute most to the components (loadings), but doesn't test statistical significance.

* Q: How many PCs should I keep?

  * A: Use the **elbow rule** on the scree plot or **choose enough PCs to explain \~90% variance**.

---

## ✅ Summary

* PCA = powerful tool for reducing and visualizing high-dimensional data
* Especially useful in biology for gene expression and population structure
* Remember: PCA simplifies data, but interpretation must remain biologically grounded
