"""Exercises for 22-06 Support vector machines."""
import numpy as np
from sklearn.svm import SVC


def svm_test_accuracy(X_train, X_test, y_train, y_test, kernel="rbf", C=1.0, gamma="scale"):
    """Fit SVC(kernel=kernel, C=C, gamma=gamma) and return its test accuracy
    rounded to 3 places."""
    raise NotImplementedError


def support_vector_count(model):
    """Return how many support vectors the fitted SVC uses (an int)."""
    raise NotImplementedError


def best_gamma(X_train, X_test, y_train, y_test, gammas):
    """Return the gamma from `gammas` whose RBF SVC has the highest test
    accuracy (the first on a tie)."""
    raise NotImplementedError


def add_squared_distance(X):
    """Return X with one extra column on the right: each row's squared
    distance from the origin (the sum of its squared values).

    Example: add_squared_distance(np.array([[3.0, 4.0]])) returns array([[3., 4., 25.]])
    """
    raise NotImplementedError
