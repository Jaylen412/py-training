"""Solutions for 22-04 k-nearest neighbours."""
from collections import Counter

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def knn_predict_one(train_X, train_y, point, k):
    """Classify one point by majority vote of its k nearest neighbours."""
    distances = np.sqrt(((np.asarray(train_X) - np.asarray(point)) ** 2).sum(axis=1))
    nearest = np.argsort(distances, kind="stable")[:k]
    # most_common keeps first-seen order on ties, and nearest is sorted by distance.
    return Counter(np.asarray(train_y)[nearest].tolist()).most_common(1)[0][0]


def best_k(X_train, X_test, y_train, y_test, ks):
    """Return the k with the highest test accuracy."""
    scores = [KNeighborsClassifier(n_neighbors=k).fit(X_train, y_train).score(X_test, y_test) for k in ks]
    return ks[int(np.argmax(scores))]


def scaled_knn_accuracy(X_train, X_test, y_train, y_test, k=5):
    """Return k-NN test accuracy after standardising."""
    scaler = StandardScaler().fit(X_train)
    model = KNeighborsClassifier(n_neighbors=k).fit(scaler.transform(X_train), y_train)
    return round(model.score(scaler.transform(X_test), y_test), 3)


def distance_ratio(point, others):
    """Return nearest distance divided by farthest distance."""
    distances = np.sqrt(((np.asarray(others) - np.asarray(point)) ** 2).sum(axis=1))
    return float(distances.min() / distances.max())
