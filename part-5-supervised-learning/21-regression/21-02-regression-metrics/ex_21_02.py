"""Exercises for 21-02 Regression metrics.

Write the metrics yourself with NumPy (not sklearn.metrics).
"""
import numpy as np


def mae(actual, predicted):
    """Return the mean absolute error as a float."""
    raise NotImplementedError


def rmse(actual, predicted):
    """Return the root mean squared error as a float."""
    raise NotImplementedError


def r_squared(actual, predicted):
    """Return 1 - (sum of squared residuals) / (sum of squared differences
    between `actual` and its mean), as a float.

    Example: r_squared(np.array([1, 2, 3]), np.array([1, 2, 3])) returns 1.0
    """
    raise NotImplementedError


def evaluate(model, X_test, y_test):
    """Return {"mae": ..., "rmse": ..., "r2": ...} for the fitted model's
    predictions on X_test, each rounded to 3 decimal places."""
    raise NotImplementedError


def pick_metric(large_errors_much_worse):
    """Return "rmse" if large errors are disproportionately costly
    (large_errors_much_worse is True), otherwise "mae"."""
    raise NotImplementedError
