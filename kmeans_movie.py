#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 12:05:31 2025

@author: soumyabanerjee
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#import matplotlib
#matplotlib.use('TkAgg')  # or 'Qt5Agg'

import matplotlib
matplotlib.use('Qt5Agg')  # or 'MacOSX' if you have it
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)
X = np.vstack([
    np.random.randn(50, 2) + np.array([0, 0]),
    np.random.randn(50, 2) + np.array([5, 5]),
    np.random.randn(50, 2) + np.array([0, 5])
])

# K-means parameters
K = 3
max_iters = 10

# Randomly initialize centroids
centroids = X[np.random.choice(len(X), K, replace=False)]

# Store history for animation
history = []

for _ in range(max_iters):
    # Assign clusters
    distances = np.linalg.norm(X[:, None, :] - centroids[None, :, :], axis=2)
    labels = np.argmin(distances, axis=1)
    history.append((centroids.copy(), labels.copy()))
    # Update centroids
    new_centroids = np.array([X[labels == k].mean(axis=0) if np.any(labels == k) else centroids[k] for k in range(K)])
    if np.allclose(centroids, new_centroids):
        break
    centroids = new_centroids

# Add final state
history.append((centroids.copy(), labels.copy()))

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
colors = ['r', 'g', 'b']
scat = ax.scatter(X[:, 0], X[:, 1], c=[colors[0]]*len(X), s=30)  # Set initial color
cent_scat = ax.scatter([], [], s=200, marker='X', edgecolor='k', linewidth=2)
title = ax.text(0.5, 1.05, '', transform=ax.transAxes, ha='center')

def animate(i):
    centroids, labels = history[i]
    # Set the color of each point according to its label
    scat.set_color([colors[l] for l in labels])
    # Set the centroid positions and their colors
    cent_scat.set_offsets(centroids)
    cent_scat.set_color(colors[:len(centroids)])
    title.set_text(f'Iteration {i+1}/{len(history)}')
    fig.canvas.draw_idle()  # Force redraw (may help in some environments)
    return scat, cent_scat, title

ani = FuncAnimation(fig, animate, frames=len(history), interval=1000, repeat=False)
ani.save('ani.gif')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-means Clustering Progress')
plt.show()