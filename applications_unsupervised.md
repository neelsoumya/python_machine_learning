## Applications of Unsupervised Learning

### Learning Objectives

In this lesson, we will learn how to apply unsupervised learning to real world data.

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

