"""Solutions for 23-01 Decision trees."""
import numpy as np
from sklearn.tree import DecisionTreeClassifier


def _proportions(labels):
    _, counts = np.unique(np.asarray(labels), return_counts=True)
    return counts / counts.sum()


def gini(labels):
    """Gini impurity."""
    return float(1 - np.sum(_proportions(labels) ** 2))


def entropy(labels):
    """Entropy in bits."""
    proportions = _proportions(labels)
    return float(-np.sum(proportions * np.log2(proportions)) + 0.0)


def best_threshold(values, labels):
    """Return (threshold, weighted Gini) of the best split on one feature."""
    values, labels = np.asarray(values), np.asarray(labels)
    best = None
    for threshold in np.unique(values):     # np.unique sorts, so ties keep the smaller one
        left, right = labels[values <= threshold], labels[values > threshold]
        if len(left) == 0 or len(right) == 0:
            continue
        weighted = (len(left) * gini(left) + len(right) * gini(right)) / len(labels)
        if best is None or weighted < best[1]:
            best = (threshold.item(), weighted)
    return best


def depth_scores(X_train, X_test, y_train, y_test, depths):
    """Return {depth: (training accuracy, test accuracy)}."""
    scores = {}
    for depth in depths:
        tree = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train, y_train)
        scores[depth] = (round(tree.score(X_train, y_train), 3), round(tree.score(X_test, y_test), 3))
    return scores
