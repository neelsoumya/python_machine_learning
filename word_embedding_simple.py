pip install gensim matplotlib scikit-learn

import gensim.downloader as api
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

# Load a pre-trained word embedding model (Word2Vec)
model = api.load("word2vec-google-news-300")

# Choose a set of words
words = ["king", "queen", "man", "woman", "prince", "princess", "kingdom", "throne", "crown"]

# Get word embeddings
embeddings = np.array([model[word] for word in words])

# Reduce dimensions using t-SNE
tsne = TSNE(n_components=2, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

# Plot the word embeddings
plt.figure(figsize=(8, 6))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], color="red")

# Annotate points
for i, word in enumerate(words):
    plt.annotate(word, (embeddings_2d[i, 0], embeddings_2d[i, 1]), fontsize=12)

plt.title("t-SNE Visualization of Word Embeddings")
plt.xlabel("t-SNE Dimension 1")
plt.ylabel("t-SNE Dimension 2")
plt.grid(True)
plt.show()
