# 23-02 Random forests
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)

# Example 1: bagging by hand - many trees on bootstrap samples, then vote
rng = np.random.default_rng(42)
votes = []
for _ in range(25):
    rows = rng.choice(len(X_train), size=len(X_train), replace=True)
    tree = DecisionTreeClassifier(random_state=42).fit(X_train[rows], y_train[rows])
    votes.append(tree.predict(X_test))
votes = np.array(votes)
majority = (votes.mean(axis=0) >= 0.5).astype(int)
single = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
print("one tree:", round(single.score(X_test, y_test), 3))
print("25 bagged trees:", round(np.mean(majority == y_test), 3))
print("individual bagged trees range:", round(np.mean(votes == y_test, axis=1).min(), 3), "to",
      round(np.mean(votes == y_test, axis=1).max(), 3))

# Example 2: a random forest also picks a random subset of features at each split
forest = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train, y_train)
print("random forest:", round(forest.score(X_test, y_test), 3))
print(len(forest.estimators_), forest.estimators_[0].get_depth())

# Example 3: more trees - better, then flat; never worse
for n in [1, 5, 25, 100, 400]:
    model = RandomForestClassifier(n_estimators=n, random_state=42).fit(X_train, y_train)
    print(f"{n:>3} trees: test {model.score(X_test, y_test):.3f}")

# Example 4: max_features - how many features each split may consider
for max_features in ["sqrt", 0.5, None]:
    model = RandomForestClassifier(n_estimators=200, max_features=max_features, random_state=42).fit(X_train, y_train)
    print(f"max_features {str(max_features):<5}: test {model.score(X_test, y_test):.3f}")

# Example 5: the out-of-bag score - a free validation estimate
oob_forest = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=42).fit(X_train, y_train)
print("out-of-bag accuracy:", round(oob_forest.oob_score_, 3))

# Example 6: impurity-based feature importances
importances = pd.Series(forest.feature_importances_, index=cancer.feature_names).sort_values(ascending=False)
print(importances.head(5).round(3))

fig, ax = plt.subplots(figsize=(6, 4))
importances.head(10).sort_values().plot.barh(ax=ax)
ax.set_title("Random forest feature importances (top 10)")
ax.set_xlabel("Mean decrease in impurity")
fig.savefig(FIGURES / "importances.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 7: permutation importance on the test set
result = permutation_importance(forest, X_test, y_test, n_repeats=10, random_state=42)
permutation = pd.Series(result.importances_mean, index=cancer.feature_names).sort_values(ascending=False)
print(permutation.head(5).round(3))

# Example 8: the limits - pure noise still gets a non-zero importance
noisy_train = np.column_stack([X_train, np.random.default_rng(1).normal(size=len(X_train))])
noisy_forest = RandomForestClassifier(n_estimators=200, random_state=42).fit(noisy_train, y_train)
print(f"importance of a random noise feature: {noisy_forest.feature_importances_[-1]:.4f}")
print(f"real features with lower importance: {(noisy_forest.feature_importances_[:-1] < noisy_forest.feature_importances_[-1]).sum()}")
