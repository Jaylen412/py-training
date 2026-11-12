"""Solutions for 23-02 Random forests."""
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


def bagged_vote(X_train, y_train, X_test, n_trees, seed):
    """Majority vote of trees trained on bootstrap samples."""
    rng = np.random.default_rng(seed)
    votes = []
    for _ in range(n_trees):
        rows = rng.choice(len(X_train), size=len(X_train), replace=True)
        votes.append(DecisionTreeClassifier(random_state=42).fit(X_train[rows], y_train[rows]).predict(X_test))
    # The mean of 0/1 votes is the fraction of trees voting 1.
    return (np.mean(votes, axis=0) >= 0.5).astype(int)


def forest_scores(X_train, X_test, y_train, y_test, tree_counts):
    """Return {number of trees: test accuracy}."""
    return {
        n: round(RandomForestClassifier(n_estimators=n, random_state=42).fit(X_train, y_train).score(X_test, y_test), 3)
        for n in tree_counts
    }


def top_features(model, feature_names, count):
    """Return the most important feature names."""
    importances = pd.Series(model.feature_importances_, index=feature_names)
    return importances.sort_values(ascending=False).index[:count].tolist()


def oob_accuracy(X_train, y_train, n_trees=200):
    """Return the out-of-bag accuracy."""
    forest = RandomForestClassifier(n_estimators=n_trees, oob_score=True, random_state=42).fit(X_train, y_train)
    return round(forest.oob_score_, 3)
