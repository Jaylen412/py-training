"""Solutions for 21-04 Feature scaling."""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def standardise(X_train, X_test):
    """Standardise with statistics from the training data."""
    scaler = StandardScaler().fit(X_train)
    return scaler.transform(X_train), scaler.transform(X_test), scaler


def min_max_scale(X_train, X_test):
    """Min-max scale with the training data's range."""
    scaler = MinMaxScaler().fit(X_train)
    return scaler.transform(X_train), scaler.transform(X_test), scaler


def knn_accuracy(X_train, X_test, y_train, y_test, scaler=None):
    """Return k-NN test accuracy, optionally after scaling."""
    if scaler is not None:
        scaler.fit(X_train)
        X_train, X_test = scaler.transform(X_train), scaler.transform(X_test)
    model = KNeighborsClassifier().fit(X_train, y_train)
    return round(model.score(X_test, y_test), 3)


def widest_feature(frame):
    """Return the name of the column with the largest range."""
    return (frame.max() - frame.min()).idxmax()
