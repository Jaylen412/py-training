"""Exercises for 23-01 Decision trees."""
import numpy as np
from sklearn.tree import DecisionTreeClassifier


def gini(labels):
    """Return the Gini impurity: 1 minus the sum of squared class proportions.

    Example: gini(["a", "a", "b", "b"]) returns 0.5
    """
    raise NotImplementedError


def entropy(labels):
    """Return the entropy: minus the sum of p * log2(p) over the classes
    present. A pure group has entropy 0.0 (not -0.0).

    Example: entropy(["a", "b"]) returns 1.0
    """
    raise NotImplementedError


def best_threshold(values, labels):
    """Try each distinct value of `values` as a threshold, splitting into
    values <= threshold and values > threshold (skip thresholds that leave
    one side empty). Return (threshold, weighted Gini) for the split with
    the lowest size-weighted Gini of the two sides. On a tie, keep the
    smaller threshold.

    Example: best_threshold([1, 2, 10, 11], ["a", "a", "b", "b"]) returns (2, 0.0)
    """
    raise NotImplementedError


def depth_scores(X_train, X_test, y_train, y_test, depths):
    """Return {depth: (training accuracy, test accuracy)} for
    DecisionTreeClassifier(max_depth=depth, random_state=42), each score
    rounded to 3 places."""
    raise NotImplementedError
