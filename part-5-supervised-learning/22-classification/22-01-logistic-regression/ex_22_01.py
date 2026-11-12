"""Exercises for 22-01 Logistic regression."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def sigmoid(z):
    """Return 1 / (1 + e^(-z)), working on single numbers and arrays.

    Example: sigmoid(0) returns 0.5
    """
    raise NotImplementedError


def classify(probabilities, threshold=0.5):
    """`probabilities` is a 1-D array of P(class 1). Return an int array:
    1 where the probability is at least `threshold`, otherwise 0."""
    raise NotImplementedError


def boundary_value(model):
    """For a LogisticRegression fitted on ONE feature, return (as a float)
    the feature value where P(class 1) is exactly 0.5: -intercept / coefficient."""
    raise NotImplementedError


def fit_scaled_logistic(X_train, y_train, C=1.0):
    """Fit a StandardScaler on X_train, then LogisticRegression(C=C,
    max_iter=5000) on the scaled training data. Return (scaler, model)."""
    raise NotImplementedError


def most_likely_names(probabilities, class_names):
    """`probabilities` has one row per sample and one column per class.
    Return a list with the name of the most probable class for each row.

    Example: most_likely_names(np.array([[0.2, 0.8]]), ["no", "yes"]) returns ["yes"]
    """
    raise NotImplementedError
