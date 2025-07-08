## Introduction to Unsupervised Learning

## Learning Objectives

By the end of this module, learners will be able to:

* Define unsupervised learning and explain how it differs from supervised learning in terms of inputs, outputs, and goals.

* Identify common unsupervised techniques, including clustering (e.g., k‑means, hierarchical) and dimensionality reduction (e.g., PCA), and describe when each is appropriate.

* Discuss real‑world applications of unsupervised learning, such as customer segmentation, anomaly detection, and image compression.

* Explain the role of unsupervised learning in exploratory data analysis and as a preprocessing step for downstream tasks.

* Interpret principal component analysis (PCA) intuitively, including the meaning of eigenvectors and eigenvalues, to understand how PCA finds the directions of greatest variance in data.

* Apply dimensionality reduction to a simple multivariate dataset (e.g., crime rates and population by state) to visualize high‑dimensional data in two or three dimensions.

* Differentiate unsupervised from supervised problems by examining datasets and deciding whether the task is to uncover patterns versus predict a known target variable.

* Articulate the value of unsupervised learning in uncovering hidden structure in unlabelled data and its importance as data complexity and volume grow.


## Introduction

Unsupervised learning is a branch of machine learning that deals with finding hidden patterns or intrinsic structures in data without the use of labeled responses. Unlike supervised learning, where the model learns from labeled data to predict outcomes, unsupervised learning works with input data that does not have any corresponding output variables. The primary goal is to explore the underlying structure, groupings, or features in the data.

One of the most common applications of unsupervised learning is clustering, where the algorithm groups similar data points together based on their characteristics. This is particularly useful in scenarios such as customer segmentation, anomaly detection, and image compression. Another key technique is dimensionality reduction, which aims to reduce the number of variables under consideration, making it easier to visualize and interpret large datasets.

Unsupervised learning is valuable because it can reveal insights that may not be immediately apparent, uncovering relationships and patterns that might otherwise go unnoticed. It is commonly used in exploratory data analysis and as a preprocessing step for other algorithms. As data continues to grow in complexity and volume, unsupervised learning plays a critical role in making sense of unstructured information.

### Motivation

Here is a picture I took of a pavement in Cambridge the day after Valentine's Day. Why did this picture capture my attention? The starkness of the grey pavement contrasted with the bright red rose. It may have triggered some unsupervised learning mechanism in my brain that allows me to pick anomalies!

![Rose after Valentine's Day](images/rose_after_valentines_day.png)

### Resources

[PCA intuition](https://stats.stackexchange.com/questions/2691/making-sense-of-principal-component-analysis-eigenvectors-eigenvalues)

Given the data below, how should we reduce the number of features and/or visualize it? This is an **unsupervised** machine learning problem.


| State       | Murder (per 100k) | Robbery (per 100k) | Population     |
|-------------|-------------------|--------------------|----------------|
| California  | 9.1               | 45.3               | 39,512,223     |
| Texas       | 7.8               | 38.6               | 28,995,881     |
| Florida     | 5.9               | 31.7               | 21,477,737     |
| New York    | 3.4               | 26.4               | 19,453,561     |
| Illinois    | 6.4               | 35.1               | 12,671,821     |
| Pennsylvania| 4.8               | 22.9               | 12,801,989     |


Importantly, we are not trying to predict anything. For example, say in the data below we can try to predict the number of people who moved to that state last year. This is a **supervised** machine learning problem.

| State        | Murder (per 100k) | Robbery (per 100k) | Population   | People Who Moved (per 100k) |
|--------------|-------------------|--------------------|--------------|-----------------------------|
| California   | 9.1               | 45.3               | 39,512,223   | 5,400                       |
| Texas        | 7.8               | 38.6               | 28,995,881   | 4,100                       |
| Florida      | 5.9               | 31.7               | 21,477,737   | 6,200                       |
| New York     | 3.4               | 26.4               | 19,453,561   | 3,800                       |
| Illinois     | 6.4               | 35.1               | 12,671,821   | 2,900                       |
| Pennsylvania | 4.8               | 22.9               | 12,801,989   | 2,500                       |
