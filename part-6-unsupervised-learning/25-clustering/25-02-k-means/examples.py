# 25-02 k-means
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
DATA = Path(__file__).resolve().parents[3] / "data"

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.9, random_state=7)


# Example 1: the algorithm in NumPy - assign each point, then move each centre
def kmeans(X, k, steps=20, seed=0):
    rng = np.random.default_rng(seed)
    centres = X[rng.choice(len(X), size=k, replace=False)]
    for step in range(steps):
        distances = np.sqrt(((X[:, None, :] - centres[None, :, :]) ** 2).sum(axis=2))
        labels = distances.argmin(axis=1)
        new_centres = np.array([X[labels == j].mean(axis=0) for j in range(k)])
        if np.allclose(new_centres, centres):
            break
        centres = new_centres
    inertia = ((X - centres[labels]) ** 2).sum()
    return labels, centres, inertia, step + 1


labels, centres, inertia, steps = kmeans(X, 3)
print("steps until nothing moved:", steps)
print("centres:\n", centres.round(2))
print("inertia:", round(inertia, 1))
print("cluster sizes:", np.bincount(labels).tolist())

# Example 2: the shapes behind the broadcasting
print((X[:, None, :] - centres[None, :, :]).shape)

# Example 3: scikit-learn's KMeans
model = KMeans(n_clusters=3, n_init=10, random_state=42).fit(X)
print("sklearn inertia:", round(model.inertia_, 1))
print("sklearn centres:\n", model.cluster_centers_[np.argsort(model.cluster_centers_[:, 0])].round(2))
print(model.predict([[0, 0], [5, 5]]))

# Example 4: different starting points can give different answers
for seed in range(5):
    labels_s, _, inertia_s, _ = kmeans(X, 3, seed=seed)
    print(f"seed {seed}: inertia {inertia_s:.1f}")
many, _ = make_blobs(n_samples=600, centers=6, cluster_std=0.7, random_state=3)
for seed in range(5):
    single = KMeans(n_clusters=6, n_init=1, init="random", random_state=seed).fit(many)
    print(f"6 clusters, one random start, seed {seed}: inertia {single.inertia_:.1f}")
best_of_ten = KMeans(n_clusters=6, n_init=10, random_state=0).fit(many)
print("best of 10 starts:", round(best_of_ten.inertia_, 1))

# Example 5: k-means++ initialisation (the default) spreads the starting centres out
plus = [KMeans(n_clusters=6, n_init=1, init="k-means++", random_state=seed).fit(many).inertia_ for seed in range(5)]
print("k-means++ single starts:", np.round(plus, 1).tolist())

# Example 6: scaling matters - customer data
customers = pd.read_csv(DATA / "customers.csv")
features = customers[["annual_spend", "visits_per_month", "days_since_last_visit", "avg_basket_size"]]
raw = KMeans(n_clusters=4, n_init=10, random_state=42).fit(features)
scaled_features = StandardScaler().fit_transform(features)
scaled = KMeans(n_clusters=4, n_init=10, random_state=42).fit(scaled_features)
print("unscaled sizes:", sorted(np.bincount(raw.labels_).tolist()))
print("scaled sizes:  ", sorted(np.bincount(scaled.labels_).tolist()))
spend_only = np.corrcoef(raw.labels_, features["annual_spend"])[0, 1]
print("unscaled labels correlate with spend:", round(abs(spend_only), 2))

# Example 7: profile the scaled clusters in original units
profile = features.assign(cluster=scaled.labels_).groupby("cluster").mean().round(1)
print(profile.to_string())

fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
for ax, k in zip(axes, [2, 3, 6]):
    data = X if k < 6 else many
    fit = KMeans(n_clusters=k, n_init=10, random_state=42).fit(data)
    ax.scatter(data[:, 0], data[:, 1], c=fit.labels_, s=10, cmap="tab10")
    ax.scatter(fit.cluster_centers_[:, 0], fit.cluster_centers_[:, 1], marker="X", s=140, c="black")
    ax.set_title(f"k = {k}")
fig.savefig(FIGURES / "kmeans.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 8: where k-means fails - clusters that are not round
from sklearn.datasets import make_moons  # noqa: E402

moons, moon_truth = make_moons(n_samples=300, noise=0.07, random_state=42)
moon_labels = KMeans(n_clusters=2, n_init=10, random_state=42).fit_predict(moons)
agree = max(np.mean(moon_labels == moon_truth), np.mean(moon_labels != moon_truth))
print("k-means agrees with the true moons on", round(agree, 3), "of the points")
