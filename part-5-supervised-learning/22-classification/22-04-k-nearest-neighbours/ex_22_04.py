"""Exercises for 22-04 k-nearest neighbours."""
from collections import Counter

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def knn_predict_one(train_X, train_y, point, k):
    """Classify `point` by hand: find the k training rows with the smallest
    Euclidean distance (use np.argsort with kind="stable" so ties keep their
    original order), then return the most common label among them. If labels
    tie in the vote, return the tied label whose neighbour is closest
    (Counter.most_common keeps first-seen order, and the neighbours are in
    distance order).

    Example: with three red points near (1, 1) and three blue near (5, 5),
    knn_predict_one(X, y, np.array([2, 2]), 3) returns "red"
    """
    raise NotImplementedError


def best_k(X_train, X_test, y_train, y_test, ks):
    """Return the k from `ks` whose KNeighborsClassifier(n_neighbors=k) has
    the highest test accuracy (the first such k on a tie)."""
    raise NotImplementedError


def scaled_knn_accuracy(X_train, X_test, y_train, y_test, k=5):
    """Standardise with a StandardScaler fitted on X_train, then return the
    test accuracy of KNeighborsClassifier(n_neighbors=k), rounded to 3 places."""
    raise NotImplementedError


def distance_ratio(point, others):
    """Return (distance to the nearest row of `others`) divided by (distance
    to the farthest row), as a float."""
    raise NotImplementedError
