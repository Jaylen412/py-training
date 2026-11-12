# 20-04 Overfitting and underfitting
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.tree import DecisionTreeClassifier

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Example 1: noisy data from a curved relationship
rng = np.random.default_rng(42)
x = np.sort(rng.uniform(0, 1, 30))
y = np.sin(2 * np.pi * x) + rng.normal(0, 0.25, size=30)
x_test = np.sort(rng.uniform(0, 1, 30))
y_test = np.sin(2 * np.pi * x_test) + rng.normal(0, 0.25, size=30)

# Example 2: polynomials of increasing complexity
for degree in [1, 3, 15]:
    coefficients = np.polyfit(x, y, degree)
    train_error = np.mean((np.polyval(coefficients, x) - y) ** 2)
    test_error = np.mean((np.polyval(coefficients, x_test) - y_test) ** 2)
    print(f"degree {degree:>2}: train MSE {train_error:.3f}, test MSE {test_error:.3f}")

grid = np.linspace(0, 1, 300)
fig, axes = plt.subplots(1, 3, figsize=(13, 3.5), sharey=True)
for ax, degree, label in zip(axes, [1, 3, 15], ["underfit", "good fit", "overfit"]):
    coefficients = np.polyfit(x, y, degree)
    ax.scatter(x, y, s=15, color="black", label="training data")
    ax.plot(grid, np.sin(2 * np.pi * grid), ":", color="grey", label="true curve")
    ax.plot(grid, np.polyval(coefficients, grid), color="tab:red", label=f"degree {degree}")
    ax.set_ylim(-2, 2)
    ax.set_title(f"Degree {degree}: {label}")
axes[0].legend(loc="lower left", fontsize=8)
fig.tight_layout()
fig.savefig(FIGURES / "polynomial_fits.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 3: training and test error against complexity
degrees = range(1, 16)
train_errors, test_errors = [], []
for degree in degrees:
    coefficients = np.polyfit(x, y, degree)
    train_errors.append(np.mean((np.polyval(coefficients, x) - y) ** 2))
    test_errors.append(np.mean((np.polyval(coefficients, x_test) - y_test) ** 2))
best_degree = degrees[int(np.argmin(test_errors))]
print("best degree on test data:", best_degree)

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(degrees, train_errors, "o-", label="training error")
ax.plot(degrees, test_errors, "o-", label="test error")
ax.set_yscale("log")
ax.set_xlabel("Polynomial degree (model complexity)")
ax.set_ylabel("Mean squared error")
ax.set_title("Training error keeps falling; test error turns back up")
ax.legend()
fig.savefig(FIGURES / "complexity_curve.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 4: the same pattern with decision trees on real data
data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
)
for depth in [1, 3, 5, None]:
    tree = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train, y_train)
    print(f"max_depth {str(depth):>4}: train {tree.score(X_train, y_train):.3f}, test {tree.score(X_test, y_test):.3f}")

# Example 5: learning curves - how scores change with more training data
sizes, train_scores, validation_scores = learning_curve(
    DecisionTreeClassifier(max_depth=3, random_state=42),
    data.data, data.target, train_sizes=np.linspace(0.1, 1.0, 8), cv=5,
)
print(sizes)
print(np.round(validation_scores.mean(axis=1), 3))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(sizes, train_scores.mean(axis=1), "o-", label="training score")
ax.plot(sizes, validation_scores.mean(axis=1), "o-", label="validation score")
ax.set_xlabel("Number of training samples")
ax.set_ylabel("Accuracy")
ax.set_title("Learning curve: the gap narrows with more data")
ax.legend()
fig.savefig(FIGURES / "learning_curve.png", dpi=100, bbox_inches="tight")
plt.close(fig)
