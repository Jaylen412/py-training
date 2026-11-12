# 22-04 k-nearest neighbours
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer, make_moons
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Example 1: a tiny worked example by hand
training_points = np.array([[1, 1], [2, 1], [1, 2], [5, 5], [6, 5], [5, 6]])
training_labels = np.array(["red", "red", "red", "blue", "blue", "blue"])
new_point = np.array([2, 2])
distances = np.sqrt(((training_points - new_point) ** 2).sum(axis=1))
print(np.round(distances, 2))
nearest = np.argsort(distances)[:3]
print(nearest, training_labels[nearest])

# Example 2: the scikit-learn version
knn = KNeighborsClassifier(n_neighbors=3).fit(training_points, training_labels)
print(knn.predict([[2, 2], [5.5, 5.5]]))
distances_found, indexes_found = knn.kneighbors([[2, 2]])
print(np.round(distances_found, 2), indexes_found)

# Example 3: choosing k - small k overfits, large k underfits
X, y = make_moons(n_samples=300, noise=0.3, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
for k in [1, 5, 15, 51, 151]:
    model = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    print(f"k={k:>3}: train {model.score(X_train, y_train):.3f}, test {model.score(X_test, y_test):.3f}")

xs, ys = np.meshgrid(np.linspace(-2, 3, 200), np.linspace(-1.5, 2, 200))
grid = np.column_stack([xs.ravel(), ys.ravel()])
fig, axes = plt.subplots(1, 3, figsize=(13, 3.8))
for ax, k in zip(axes, [1, 15, 151]):
    model = KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train)
    ax.contourf(xs, ys, model.predict(grid).reshape(xs.shape), alpha=0.3, cmap="coolwarm")
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap="coolwarm", s=10, edgecolor="k", linewidth=0.3)
    ax.set_title(f"k = {k}: test accuracy {model.score(X_test, y_test):.2f}")
fig.tight_layout()
fig.savefig(FIGURES / "k_boundaries.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 4: scaling is essential
cancer = load_breast_cancer()
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
unscaled = KNeighborsClassifier().fit(Xc_train, yc_train).score(Xc_test, yc_test)
scaler = StandardScaler().fit(Xc_train)
scaled = KNeighborsClassifier().fit(scaler.transform(Xc_train), yc_train).score(scaler.transform(Xc_test), yc_test)
print(f"unscaled {unscaled:.3f}, scaled {scaled:.3f}")

# Example 5: distance weighting - closer neighbours count more
weighted = KNeighborsClassifier(n_neighbors=15, weights="distance").fit(scaler.transform(Xc_train), yc_train)
print(round(weighted.score(scaler.transform(Xc_test), yc_test), 3))

# Example 6: the curse of dimensionality - in many dimensions, everything is far away
rng = np.random.default_rng(42)
for dimensions in [2, 10, 100, 1000]:
    points = rng.random((500, dimensions))
    gaps = np.sqrt(((points[1:] - points[0]) ** 2).sum(axis=1))
    print(f"{dimensions:>4} dimensions: nearest {gaps.min():.2f}, farthest {gaps.max():.2f}, "
          f"ratio {gaps.min() / gaps.max():.2f}")
