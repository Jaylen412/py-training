"""Exercises for 21-04 Feature scaling."""
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def standardise(X_train, X_test):
    """Fit a StandardScaler on X_train only. Return (scaled X_train,
    scaled X_test, the fitted scaler)."""
    raise NotImplementedError


def min_max_scale(X_train, X_test):
    """Fit a MinMaxScaler on X_train only. Return (scaled X_train,
    scaled X_test, the fitted scaler)."""
    raise NotImplementedError


def knn_accuracy(X_train, X_test, y_train, y_test, scaler=None):
    """If `scaler` (an unfitted scaler object) is given, fit it on X_train
    and transform both sets. Then fit KNeighborsClassifier() and return its
    test accuracy rounded to 3 places."""
    raise NotImplementedError


def widest_feature(frame):
    """`frame` is a DataFrame of numeric features. Return the name of the
    column with the largest range (max - min)."""
    raise NotImplementedError
