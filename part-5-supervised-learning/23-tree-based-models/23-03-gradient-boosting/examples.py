# 23-03 Gradient boosting
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Example 1: boosting by hand - each small tree corrects the last one's errors
rng = np.random.default_rng(42)
x = np.sort(rng.uniform(0, 1, 100)).reshape(-1, 1)
y = np.sin(2 * np.pi * x[:, 0]) + rng.normal(0, 0.2, 100)
learning_rate = 0.3
prediction = np.full_like(y, y.mean())
stages = {}
for step in range(1, 51):
    residuals = y - prediction
    small_tree = DecisionTreeRegressor(max_depth=2, random_state=42).fit(x, residuals)
    prediction += learning_rate * small_tree.predict(x)
    if step in (1, 5, 50):
        stages[step] = prediction.copy()
        print(f"after {step:>2} trees: training MSE {np.mean((y - prediction) ** 2):.4f}")

fig, axes = plt.subplots(1, 3, figsize=(13, 3.5), sharey=True)
for ax, (step, values) in zip(axes, stages.items()):
    ax.scatter(x, y, s=10, color="grey")
    ax.plot(x, values, color="tab:red")
    ax.set_title(f"after {step} small trees")
fig.tight_layout()
fig.savefig(FIGURES / "boosting_steps.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: GradientBoostingClassifier on real data
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
boosting = GradientBoostingClassifier(random_state=42).fit(X_train, y_train)
forest = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train, y_train)
print("gradient boosting:", round(boosting.score(X_test, y_test), 3))
print("random forest:    ", round(forest.score(X_test, y_test), 3))

# Example 3: learning rate versus number of trees
for learning_rate, n_trees in [(1.0, 100), (0.1, 100), (0.01, 100), (0.01, 1000)]:
    model = GradientBoostingClassifier(learning_rate=learning_rate, n_estimators=n_trees, random_state=42).fit(X_train, y_train)
    print(f"learning_rate {learning_rate:<5} trees {n_trees:>4}: train {model.score(X_train, y_train):.3f}, "
          f"test {model.score(X_test, y_test):.3f}")

# Example 4: watch test accuracy as trees are added
staged = [np.mean(p == y_test) for p in GradientBoostingClassifier(
    learning_rate=0.1, n_estimators=300, random_state=42).fit(X_train, y_train).staged_predict(X_test)]
print("best number of trees:", int(np.argmax(staged)) + 1, "accuracy:", round(max(staged), 3))

fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(range(1, len(staged) + 1), staged)
ax.set_xlabel("Number of trees")
ax.set_ylabel("Test accuracy")
ax.set_title("Boosting improves quickly, then levels off")
fig.savefig(FIGURES / "staged_accuracy.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: early stopping - hold back some training data and stop when it stops improving
early = GradientBoostingClassifier(n_estimators=1000, validation_fraction=0.2, n_iter_no_change=10,
                                   random_state=42).fit(X_train, y_train)
print("trees actually used:", early.n_estimators_, "test:", round(early.score(X_test, y_test), 3))

# Example 6: HistGradientBoostingClassifier - fast, handles missing values
hist = HistGradientBoostingClassifier(random_state=42).fit(X_train, y_train)
print("hist gradient boosting:", round(hist.score(X_test, y_test), 3), "iterations:", hist.n_iter_)
with_gaps = X_train.copy()
with_gaps[np.random.default_rng(0).random(with_gaps.shape) < 0.1] = np.nan
print("missing values in training data:", int(np.isnan(with_gaps).sum()))
print("still trains:", round(HistGradientBoostingClassifier(random_state=42).fit(with_gaps, y_train).score(X_test, y_test), 3))
