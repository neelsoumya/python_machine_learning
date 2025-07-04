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

## Learning Objectives

* Day 1 (half-day): introduction and normalization
* Day 2 (half-day): PCA and tSNE
* Day 3 (half-day): Clustering
* Day 4 (half-day): Practical applications


## Introduction to Unsupervised Learning


- 📓 [Introduction to Unsupervised Learning](https://github.com/neelsoumya/python_machine_learning/blob/main/intro_unsupervised.md)


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
