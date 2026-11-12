"""Exercises for 18-03 Loss functions.

`actual` and `predicted` are NumPy arrays of the same length.
"""
import numpy as np


def mean_squared_error(actual, predicted):
    """Return the mean of the squared residuals.

    Example: mean_squared_error(np.array([1, 2]), np.array([1, 4])) returns 2.0
    """
    raise NotImplementedError


def root_mean_squared_error(actual, predicted):
    """Return the square root of the mean squared error."""
    raise NotImplementedError


def mean_absolute_error(actual, predicted):
    """Return the mean of the absolute residuals.

    Example: mean_absolute_error(np.array([1, 2]), np.array([1, 4])) returns 1.0
    """
    raise NotImplementedError


def loss_curve(x, y, intercept, slopes):
    """For each slope in `slopes`, compute the MSE of the model
    prediction = intercept + slope * x against y. Return a NumPy array of
    the losses, one per slope.
    """
    raise NotImplementedError


def best_parameter(candidates, losses):
    """Return the candidate (as a float) whose loss is smallest. On a tie,
    return the first.

    Example: best_parameter([1, 2, 3], [5.0, 0.5, 2.0]) returns 2.0
    """
    raise NotImplementedError
