pip install gensim plotly scikit-learn

import gensim.downloader as api
import numpy as np
import plotly.express as px
from sklearn.manifold import TSNE
import pandas as pd

# Load pre-trained Word2Vec model
model = api.load("word2vec-google-news-300")

# Select a set of related words
words = ["king", "queen", "man", "woman", "prince", "princess", "kingdom", "throne", "crown", 
         "dog", "cat", "lion", "tiger", "apple", "banana", "car", "bus", "train", "doctor", "nurse"]

# Get word embeddings
embeddings = np.array([model[word] for word in words])

# Reduce dimensions using t-SNE
tsne = TSNE(n_components=2, random_state=42, perplexity=5)
embeddings_2d = tsne.fit_transform(embeddings)

# Create a DataFrame for visualization
df = pd.DataFrame(embeddings_2d, columns=["x", "y"])
df["word"] = words

# Plot using Plotly
fig = px.scatter(df, x="x", y="y", text="word", title="Interactive t-SNE Word Embeddings Visualization")

# Update layout for better readability
fig.update_traces(textposition="top center", marker=dict(size=8, color="red"))
fig.update_layout(
    width=800, height=600,
    xaxis_title="t-SNE Dimension 1",
    yaxis_title="t-SNE Dimension 2",
    hovermode="closest"
)

# Show the plot
fig.show()
