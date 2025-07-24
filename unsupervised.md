# Unsupervised Machine Learning

Welcome to the Applied Unsupervised Machine Learning module! This guide will help you navigate the key concepts and resources.

## Table of Contents

1. [Learning Objectives](#learning-objectives)
2. [Introduction to Unsupervised Learning](#introduction-to-unsupervised-learning)
3. [Normalization](#normalization)
4. [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
5. [Curse of dimensionality](#curse-of-dimensionality) 
6. [tSNE](#tSNE)
5. [Clustering Algorithms](#clustering-algorithms)
    - [K-Means Clustering](#k-means-clustering)
    - [Hierarchical Clustering](#hierarchical-clustering)
6. [Applications in Biology](#applications-in-biology)
7. [Q&A and Further Reading](#qa-and-further-reading)

---

## Learning Objectives

### Day 1 (half‑day) *Introduction to unsupervised learning*

1. **Introduction to unsupervised learning and normalization:**  
   Understand the fundamental principles of unsupervised learning and recognize the role that data normalization plays in preparing datasets for analysis.

2. **Why normalization is required:**  
   Explain why normalization is necessary to ensure that features with different scales do not unduly influence unsupervised learning algorithms.

3. **Why dimensionality reduction is required**
   Why you need dimensionality reduction. 


4. **Basics of PCA:**  
   Describe the core concepts of Principal Component Analysis (PCA), including how it reduces dimensionality by identifying directions of maximum variance.

5. **Evaluating unsupervised learning methods**
   

---

### Day 2 (half‑day) *Basics of dimensionality reduction*

1. **PCA and t‑SNE:**  
   Compare and contrast PCA and t‑Distributed Stochastic Neighbor Embedding (t‑SNE) as two popular techniques for dimensionality reduction and data visualization.

2. **Basic applications of PCA:**  
   Apply PCA to real datasets, interpret the resulting principal components, and discuss how these components can reveal underlying structure.

3. **Curse of dimensionality:**  
   Explain the concept of the curse of dimensionality and its implications for the performance and interpretability of clustering and dimensionality‑reduction algorithms.


4. **Basics of t‑SNE:**  
   Explain how t‑SNE projects high‑dimensional data into two or three dimensions while preserving local similarities between points.

5. **Applications to data:**  
   Demonstrate the use of both PCA and t‑SNE on sample datasets to visualize clustering tendencies and uncover hidden patterns.

6. **When *not* to apply PCA and t‑SNE:**  
   Identify situations where PCA or t‑SNE may produce misleading results or be computationally infeasible, and propose alternative strategies.

---

### Day 3 (half‑day) *Basics of Clustering*

1. **Clustering:**  
   Define clustering in the context of unsupervised learning and outline its importance in discovering groupings within data.

2. **Basics of k‑means:**  
   Describe the k‑means clustering algorithm, including how cluster centroids are initialized and updated to minimize within‑cluster variance.

3. **Basics of hierarchical clustering:**  
   Explain the steps of hierarchical clustering, heatmaps, agglomerative approaches, and interpret dendrograms.

4. **Deciding on your clustering approach:**  
   Situations in which you would want to apply hierarchical clustering. Discuss specific use cases: such as when the number of clusters is unknown or when a tree‑based representation is desired—where hierarchical clustering is advantageous.

---

### Day 4 (half‑day) *Practical applications (hands-on)*

1. **Practical applications:**  
   Explore real‑world scenarios where unsupervised learning methods provide actionable insights across various domains.

2. **Practical applications of PCA, t‑SNE and hierarchical clustering to biological data:**  
   Apply PCA, t‑SNE, and hierarchical clustering to biological datasets (e.g., gene expression or single‑cell data), interpret the results, and discuss biological insights gained.

3. **Evaluating unsupervised learning methods**   
   How to evaluate these techniques on different kinds of data (single-cell data, electronic healthcare records, social sciences data): these are used to generate hypotheses. Motivations for next steps.



## Introduction to Unsupervised Learning


- 📓 [Introduction to Unsupervised Learning](https://github.com/neelsoumya/python_machine_learning/blob/main/intro_unsupervised.md)


## Normalization

Normalization is a crucial preprocessing step in machine learning that ensures each feature contributes equally to analysis by scaling data to have a mean of 0 and a standard deviation of 1. This is especially important for algorithms sensitive to the scale of input data.

- 📓 [Notebook: Normalization (Z-score Standardization)](https://github.com/neelsoumya/python_machine_learning/blob/main/normalising_data.ipynb)

---



## Principal Component Analysis (PCA)

- 📓 [Lecture Notes and Notebook on PCA](https://github.com/neelsoumya/python_machine_learning/blob/main/pca_notes.ipynb)


## Curse of dimensionality

- 📓 [Lecture Notes and Notebook on Curse of Dimensionality](https://github.com/neelsoumya/python_machine_learning/blob/main/curse_dimensionality.md)



## tSNE

- 📓 [Lecture Notes and Notebook on tSNE](https://github.com/neelsoumya/python_machine_learning/blob/main/tsne_simple.ipynb)
- 📓 [When *not* to do PCA, and alternatives (tSNE, clustering, heatmaps)](https://github.com/neelsoumya/python_machine_learning/blob/main/pca_when_not_to_do.ipynb)

---

## Clustering algorithms

- 📓 [Lecture Notes and Notebook on Hierarchical Clustering and k-means](https://github.com/neelsoumya/python_machine_learning/blob/main/clustering.md)



## Applications in Biology

📓 [Applications of Unsupervised Learning in Biology](https://github.com/neelsoumya/python_machine_learning/blob/main/applications_unsupervised.md
)


## Resources

- [ISLP book](https://www.statlearning.com/)

- https://www.statlearning.com/

- [Video lectures by the authors of the book Introduction to Statistical Learning in Python](https://www.youtube.com/playlist?list=PLoROMvodv4rNHU1-iPeDRH-J0cL-CrIda)

- https://github.com/neelsoumya/public_teaching_unsupervised_learning

- https://mlu-explain.github.io
