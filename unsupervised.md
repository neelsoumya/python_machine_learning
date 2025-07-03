# Unsupervised Machine Learning: Table of Contents

Welcome to the Unsupervised Machine Learning module! This guide will help you navigate the key concepts and resources.

## Table of Contents

1. [Introduction to Unsupervised Learning](#introduction-to-unsupervised-learning)
2. [Normalization](#normalization)
3. [Dimensionality Reduction](#dimensionality-reduction)
    - [Principal Component Analysis (PCA)](#principal-component-analysis-pca)
    - [t-SNE and UMAP](#t-sne-and-umap)
4. [Clustering Algorithms](#clustering-algorithms)
    - [K-Means Clustering](#k-means-clustering)
    - [Hierarchical Clustering](#hierarchical-clustering)
5. [Applications in Biology](#applications-in-biology)
6. [Exercise: where PCA does better than tSNE](#exercise-where-PCA-does-better-than-tSNE)
7. [Best Practices and Tips](#best-practices-and-tips)
8. [Q&A and Further Reading](#qa-and-further-reading)

---


## Introduction to Unsupervised Learning

Unsupervised learning is a branch of machine learning that deals with finding hidden patterns or intrinsic structures in data without the use of labeled responses. Unlike supervised learning, where the model learns from labeled data to predict outcomes, unsupervised learning works with input data that does not have any corresponding output variables. The primary goal is to explore the underlying structure, groupings, or features in the data.

One of the most common applications of unsupervised learning is clustering, where the algorithm groups similar data points together based on their characteristics. This is particularly useful in scenarios such as customer segmentation, anomaly detection, and image compression. Another key technique is dimensionality reduction, which aims to reduce the number of variables under consideration, making it easier to visualize and interpret large datasets.

Unsupervised learning is valuable because it can reveal insights that may not be immediately apparent, uncovering relationships and patterns that might otherwise go unnoticed. It is commonly used in exploratory data analysis and as a preprocessing step for other algorithms. As data continues to grow in complexity and volume, unsupervised learning plays a critical role in making sense of unstructured information.

### Motivation

Here is a picture I took of a pavement in Cambridge the day after Valentine's Day. Why did this picture capture my attention? The starkness of the grey pavement contrasted with the bright red rose. It may have triggered some unsupervised learning mechanism in my brain that allows me to pick anomalies!

![Rose after Valentine's Day](images/rose_after_valentines_day.png)

### Resources

[PCA intuition](https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues)

## Normalization

Normalization is a crucial preprocessing step in machine learning that ensures each feature contributes equally to analysis by scaling data to have a mean of 0 and a standard deviation of 1. This is especially important for algorithms sensitive to the scale of input data.

- 📓 [Notebook: Normalization (Z-score Standardization)](https://github.com/neelsoumya/python_machine_learning/blob/main/normalising_data.ipynb)

---



## Principal Component Analysis (PCA)

- 📓 [Lecture Notes and Notebook on PCA](https://github.com/neelsoumya/python_machine_learning/blob/main/pca_notes.ipynb)
- 📓 [Lecture Notes and Notebook on tSNE](https://github.com/neelsoumya/python_machine_learning/blob/main/tsne_simple.ipynb)
- 📓 [When *not* to do PCA, and alternatives (tSNE, clustering, heatmaps)](https://github.com/neelsoumya/python_machine_learning/blob/main/pca_when_not_to_do.ipynb)

---

## Clustering algorithms

- 📓 [Lecture Notes and Notebook on Hierarchical Clustering and k-means](https://github.com/neelsoumya/python_machine_learning/blob/main/clustering.md)


## Applications in Biology

### Single-Cell Analysis

Single-cell analysis is a powerful application of unsupervised machine learning in biology, enabling the exploration of cell diversity in complex tissues. This approach often involves clustering and dimensionality reduction techniques to reveal distinct cell populations based on their gene expression profiles.

The notebook [Single-Cell Unsupervised Analysis](https://github.com/neelsoumya/python_machine_learning/blob/main/singlcecell_unsupervised.ipynb) demonstrates:

- Loading real single-cell transcriptome data from 10x Genomics (PBMC 3K dataset)
- Preprocessing and quality control
- Dimensionality reduction using PCA and t-SNE/UMAP
- Clustering with the Leiden algorithm
- Visualization of results in reduced dimensions

This hands-on notebook is ideal for those interested in applying unsupervised learning to biological data.

### Electronic healthcare records (EHR) data

The notebook [EHR data analysis](https://github.com/neelsoumya/python_machine_learning/blob/main/EHR_data_unsupervised_learning.ipynb) demonstrates:

- Loading EHR data
- Preprocessing and quality control
- Dimensionality reduction using PCA and t-SNE/UMAP
- Clustering
- Visualization of results in reduced dimensions


## Exercise: where PCA does better than tSNE

The notebook [movie ratings](https://github.com/neelsoumya/python_machine_learning/blob/main/PCA_movie_ratings.ipynb) shows:

- How to generate synthetic movie ratings
- Preprocessing and quality control
- Dimensionality reduction using PCA and t-SNE/UMAP
- PCA does better than tSNE!
## Resources

- [ISLP book](https://www.statlearning.com/)
