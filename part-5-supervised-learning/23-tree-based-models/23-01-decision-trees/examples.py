# 23-01 Decision trees
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)


# Example 1: Gini impurity - how mixed is a group?
def gini(labels):
    _, counts = np.unique(labels, return_counts=True)
    proportions = counts / counts.sum()
    return 1 - np.sum(proportions ** 2)


def entropy(labels):
    _, counts = np.unique(labels, return_counts=True)
    proportions = counts / counts.sum()
    return -np.sum(proportions * np.log2(proportions)) + 0.0  # + 0.0 turns -0.0 into 0.0


for group in [["a"] * 10, ["a"] * 5 + ["b"] * 5, ["a"] * 9 + ["b"]]:
    print(f"{''.join(group):<12} gini {gini(group):.3f}  entropy {entropy(group):.3f}")

# Example 2: finding the best split by hand on one feature
iris = load_iris()
petal_length = iris.data[:, 2]
species = iris.target
best = None
for threshold in np.unique(petal_length):
    left, right = species[petal_length <= threshold], species[petal_length > threshold]
    if len(left) == 0 or len(right) == 0:
        continue
    weighted = (len(left) * gini(left) + len(right) * gini(right)) / len(species)
    if best is None or weighted < best[1]:
        best = (threshold, weighted)
print("best threshold:", best[0], "weighted gini:", round(best[1], 3), "starting gini:", round(gini(species), 3))

# Example 3: scikit-learn finds the same split
stump = DecisionTreeClassifier(max_depth=1, random_state=42).fit(iris.data[:, [2]], species)
print(round(stump.tree_.threshold[0], 2))

# Example 4: a depth-2 tree on all iris features, as text and as a picture
tree = DecisionTreeClassifier(max_depth=2, random_state=42).fit(iris.data, species)
print(export_text(tree, feature_names=list(iris.feature_names)))
fig, ax = plt.subplots(figsize=(10, 5))
plot_tree(tree, feature_names=iris.feature_names, class_names=list(iris.target_names), filled=True, ax=ax)
fig.savefig(FIGURES / "iris_tree.png", dpi=90, bbox_inches="tight")
plt.close(fig)

# Example 5: depth and overfitting on the breast cancer data
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
for depth in [1, 2, 3, 4, 6, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train, y_train)
    print(f"max_depth {str(depth):>4}: {model.get_n_leaves():>2} leaves, "
          f"train {model.score(X_train, y_train):.3f}, test {model.score(X_test, y_test):.3f}")

# Example 6: other ways to stop a tree growing too far
for name, params in [("min_samples_leaf=10", {"min_samples_leaf": 10}),
                     ("min_samples_split=40", {"min_samples_split": 40}),
                     ("ccp_alpha=0.01", {"ccp_alpha": 0.01})]:
    model = DecisionTreeClassifier(random_state=42, **params).fit(X_train, y_train)
    print(f"{name:<22} {model.get_n_leaves():>2} leaves, test {model.score(X_test, y_test):.3f}")

# Example 7: trees are unstable - a slightly different sample, a different tree
for seed in [0, 2, 4, 5]:
    rows = np.random.default_rng(seed).choice(len(X_train), size=len(X_train), replace=True)
    model = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_train[rows], y_train[rows])
    root = cancer.feature_names[model.tree_.feature[0]]
    print(f"sample {seed}: root split on '{root}' at {model.tree_.threshold[0]:.3f}, "
          f"test {model.score(X_test, y_test):.3f}")
