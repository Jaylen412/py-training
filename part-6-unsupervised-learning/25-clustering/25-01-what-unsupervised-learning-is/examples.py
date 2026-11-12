# 25-01 What unsupervised learning is
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.metrics import silhouette_score

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
DATA = Path(__file__).resolve().parents[3] / "data"

# Example 1: supervised data has a target column, unsupervised data does not
customers = pd.read_csv(DATA / "customers.csv")
print(customers.head(3).to_string(index=False))
print(customers.shape)

# Example 2: no labels means no accuracy - what would you compare against?
features = customers.drop(columns=["customer_id", "channel"])
print(features.describe().loc[["mean", "std"]].round(1).to_string())

# Example 3: an algorithm will ALWAYS return groups - even in data with none
rng = np.random.default_rng(42)
uniform = rng.uniform(size=(300, 2))
labels = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(uniform)
print("clusters found in uniform noise:", np.bincount(labels).tolist())

# Example 4: structure that really is there
blobs, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.8, random_state=7)
blob_labels = KMeans(n_clusters=3, n_init=10, random_state=42).fit_predict(blobs)
print("clusters found in real blobs:", np.bincount(blob_labels).tolist())

# Example 5: a number that tells them apart - the silhouette score (25-03 explains it)
print("silhouette, noise:", round(silhouette_score(uniform, labels), 3))
print("silhouette, blobs:", round(silhouette_score(blobs, blob_labels), 3))

fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].scatter(uniform[:, 0], uniform[:, 1], c=labels, s=14, cmap="tab10")
axes[0].set_title("Uniform noise, split into 3 anyway")
axes[1].scatter(blobs[:, 0], blobs[:, 1], c=blob_labels, s=14, cmap="tab10")
axes[1].set_title("Real structure")
fig.savefig(FIGURES / "noise_vs_structure.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 6: the clusters depend on the scale of the features
raw = KMeans(n_clusters=4, n_init=10, random_state=42).fit(features)
print("unscaled cluster sizes:", np.bincount(raw.labels_).tolist())
