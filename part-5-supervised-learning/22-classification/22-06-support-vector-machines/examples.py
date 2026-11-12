# 22-06 Support vector machines
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.calibration import CalibratedClassifierCV
from sklearn.datasets import load_breast_cancer, make_blobs, make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)


def draw_boundary(ax, model, X, y, title, show_margin=False):
    xs, ys = np.meshgrid(np.linspace(X[:, 0].min() - 0.5, X[:, 0].max() + 0.5, 300),
                         np.linspace(X[:, 1].min() - 0.5, X[:, 1].max() + 0.5, 300))
    scores = model.decision_function(np.column_stack([xs.ravel(), ys.ravel()])).reshape(xs.shape)
    ax.contourf(xs, ys, scores > 0, alpha=0.25, cmap="coolwarm")
    levels = [-1, 0, 1] if show_margin else [0]
    ax.contour(xs, ys, scores, levels=levels, colors="k", linestyles=["--", "-", "--"][: len(levels)] if show_margin else ["-"])
    ax.scatter(X[:, 0], X[:, 1], c=y, cmap="coolwarm", s=15, edgecolor="k", linewidth=0.3)
    if show_margin:
        sv = model.support_vectors_
        ax.scatter(sv[:, 0], sv[:, 1], s=90, facecolors="none", edgecolors="k")
    ax.set_title(title)


# Example 1: a maximum-margin line between two groups
X, y = make_blobs(n_samples=60, centers=2, cluster_std=1.2, random_state=6)
linear = SVC(kernel="linear", C=1.0).fit(X, y)
print("support vectors:", len(linear.support_vectors_))
fig, ax = plt.subplots(figsize=(5.5, 4.5))
draw_boundary(ax, linear, X, y, "Maximum margin: the circled points are support vectors", show_margin=True)
fig.savefig(FIGURES / "margin.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: C - a narrow, strict margin or a wide, tolerant one
for C in [0.01, 1, 100]:
    model = SVC(kernel="linear", C=C).fit(X, y)
    print(f"C {C:>6}: {len(model.support_vectors_)} support vectors, training accuracy {model.score(X, y):.3f}")

# Example 3: a straight line cannot separate the moons
Xm, ym = make_moons(n_samples=300, noise=0.2, random_state=42)
Xm_train, Xm_test, ym_train, ym_test = train_test_split(Xm, ym, test_size=0.3, random_state=42, stratify=ym)
linear_moons = SVC(kernel="linear").fit(Xm_train, ym_train)
rbf_moons = SVC(kernel="rbf").fit(Xm_train, ym_train)
print("linear kernel:", round(linear_moons.score(Xm_test, ym_test), 3))
print("RBF kernel:   ", round(rbf_moons.score(Xm_test, ym_test), 3))

# Example 4: gamma controls how wiggly the RBF boundary is
fig, axes = plt.subplots(1, 4, figsize=(17, 3.8))
draw_boundary(axes[0], linear_moons, Xm_train, ym_train, f"linear: test {linear_moons.score(Xm_test, ym_test):.2f}")
for ax, gamma in zip(axes[1:], [0.1, 1, 1000]):
    model = SVC(kernel="rbf", gamma=gamma).fit(Xm_train, ym_train)
    print(f"gamma {gamma:>4}: train {model.score(Xm_train, ym_train):.3f}, test {model.score(Xm_test, ym_test):.3f}")
    draw_boundary(ax, model, Xm_train, ym_train, f"RBF, gamma {gamma}: test {model.score(Xm_test, ym_test):.2f}")
fig.tight_layout()
fig.savefig(FIGURES / "kernels.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: the kernel trick - add a feature and a line works
squared_distance = (Xm_train ** 2).sum(axis=1, keepdims=True)
lifted_train = np.hstack([Xm_train, squared_distance])
lifted_test = np.hstack([Xm_test, (Xm_test ** 2).sum(axis=1, keepdims=True)])
print("linear SVM on lifted features:", round(SVC(kernel="linear").fit(lifted_train, ym_train).score(lifted_test, ym_test), 3))

# Example 6: real data - SVMs need scaled features
cancer = load_breast_cancer()
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
scaler = StandardScaler().fit(Xc_train)
print("unscaled:", round(SVC().fit(Xc_train, yc_train).score(Xc_test, yc_test), 3))
print("scaled:  ", round(SVC().fit(scaler.transform(Xc_train), yc_train).score(scaler.transform(Xc_test), yc_test), 3))

# Example 7: probabilities from an SVM need calibration
with_probabilities = CalibratedClassifierCV(SVC(), ensemble=False).fit(scaler.transform(Xc_train), yc_train)
print(np.round(with_probabilities.predict_proba(scaler.transform(Xc_test[:2])), 3))
