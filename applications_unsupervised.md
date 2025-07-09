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


## Other exercise ideas for hierarchical clustering and heatmaps


## 1. Single‑Cell RNA‑Seq of Immune Cells

**Dataset Examples:**
- **Human PBMC 10x Genomics** (public 68K PBMCs)  
- **Tabula Muris** (mouse single‑cell atlas)  

**Problem:**
- Hierarchically cluster cells (columns) based on their expression of marker genes to identify cell types and states.
- Cluster genes (rows) to find gene modules defining each immune cell subtype.

**Why Heatmaps?**
- Easily visualize lineage relationships and activation states across hundreds to thousands of cells.

[Exercise for loading single cell data and performing PCA and tSNE](https://github.com/neelsoumya/python_machine_learning/blob/main/exercise_singlecell_pcatsne.ipynb)

[Exercise for loading single cell data and using hierarchical clustering and heatmaps]
(https://github.com/neelsoumya/python_machine_learning/blob/main/exercise_singlecell_clustering.ipynb)
---


## 2. Gene Expression Microarray / RNA‑Seq Profiles

**Dataset Examples:**
- **TCGA Breast Cancer** (e.g. BRCA RNA‑Seq counts)  
- **GEO Series GSE2034** (lymph node metastasis in breast cancer)  

**Problem:**
- Cluster patient samples by overall expression pattern to uncover molecular subtypes.
- Cluster genes to identify co‑expression modules (e.g. proliferation vs. immune signatures).

**Why Heatmaps?**
- Intuitive display of up‑/down‑regulated clusters of genes across patients.

---

## 3. Microbiome 16S rRNA OTU Tables

**Dataset Examples:**
- **Earth Microbiome Project** subset (human gut samples)  
- **HMP (Human Microbiome Project)** stool / oral microbiome OTU tables  

**Problem:**
- Cluster samples by microbial composition to see how diet, disease status, or geography group together.
- Cluster OTUs (or genera) to reveal co‑occurring microbial communities (enterotypes).

**Why Heatmaps?**
- Depicts relative abundance patterns; highlights clusters of taxa enriched or depleted across sample groups.

---

## 4. Proteomics / Phospho‑Proteomics

**Dataset Examples:**
- **CPTAC** (Clinical Proteomic Tumor Analysis Consortium) breast or ovarian tumor proteomes  
- **ProteomeXchange** datasets on signaling pathway perturbations  

**Problem:**
- Hierarchically cluster phosphorylation sites (rows) to find modules co‑regulated across treatment conditions or tumor grades.
- Cluster patient samples to stratify responders vs. non‑responders.

**Why Heatmaps?**
- Visualize global shifts in protein or phospho‑site abundance; detect signaling modules.

---

## 5. DNA Methylation Arrays

**Dataset Examples:**
- **TCGA Lung Adenocarcinoma Methylation** (450K array)  
- **GEO Series GSE37020** (glioblastoma methylation)  

**Problem:**
- Cluster CpG sites to find differential methylation modules associated with survival.
- Cluster tumor samples vs. normal to reveal epigenetic subtypes.

**Why Heatmaps?**
- Capture large‑scale CpG methylation patterns; display hypo‑ vs. hyper‑methylated clusters.

---

### Tips for Effective Use

1. **Pre‑processing:**
   - Log‑transform or variance‑stabilize counts (for RNA‑Seq).
   - Normalize (e.g. TMM, TPM, or quantile) to make features comparable.

2. **Feature Selection:**
   - Use most variable genes/OTUs/sites (e.g. top 1,000 by MAD) to avoid noise.

3. **Distance Metrics & Linkage:**
   - Try Pearson distance for expression, Bray–Curtis for microbiome, and complete or average linkage.

4. **Annotation Tracks:**
   - Add metadata (e.g. phenotype, batch, cluster assignment) as colored sidebars for interpretation.
