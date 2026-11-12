"""Exercises for 23-02 Random forests."""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


def bagged_vote(X_train, y_train, X_test, n_trees, seed):
    """Bagging by hand for a 0/1 target. Create rng = np.random.default_rng(seed).
    For each of n_trees trees: draw bootstrap row positions with
    rng.choice(len(X_train), size=len(X_train), replace=True), fit
    DecisionTreeClassifier(random_state=42) on those rows, and predict X_test.
    Return an int array: 1 where at least half the trees voted 1, else 0.
    """
    raise NotImplementedError


def forest_scores(X_train, X_test, y_train, y_test, tree_counts):
    """Return {n: test accuracy} for RandomForestClassifier(n_estimators=n,
    random_state=42), each rounded to 3 places."""
    raise NotImplementedError


def top_features(model, feature_names, count):
    """Return a list of the `count` feature names with the highest
    feature_importances_ in the fitted forest, most important first."""
    raise NotImplementedError


def oob_accuracy(X_train, y_train, n_trees=200):
    """Fit RandomForestClassifier(n_estimators=n_trees, oob_score=True,
    random_state=42) and return its out-of-bag accuracy rounded to 3 places."""
    raise NotImplementedError
