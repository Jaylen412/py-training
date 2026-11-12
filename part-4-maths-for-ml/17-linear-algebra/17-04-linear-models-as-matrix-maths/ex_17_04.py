"""Exercises for 17-04 Linear models as matrix maths."""
import numpy as np


def predict(features, weights, bias):
    """Return features @ weights + bias.

    Example: predict(np.array([[1, 2]]), np.array([3, 4]), 5) returns array([16])
    """
    raise NotImplementedError


def add_bias_column(features):
    """Return `features` with a column of ones added as the FIRST column.

    Example: add_bias_column(np.array([[2, 3]])) returns array([[1., 2., 3.]])
    """
    raise NotImplementedError


def solve_system(coefficients, right_hand_side):
    """Solve the square system coefficients @ v = right_hand_side and return v.
    Raise ValueError (not LinAlgError) with a clear message if the system
    has no unique solution.

    Example: solve_system(np.array([[2, 1], [1, 3]]), np.array([5, 10])) returns array([1., 3.])
    """
    raise NotImplementedError


def fit_least_squares(features, targets):
    """Return (bias, weights) that minimise the squared error of
    features @ weights + bias against `targets`. Use add_bias_column and
    np.linalg.lstsq. `bias` is a float and `weights` a 1-D array.
    """
    raise NotImplementedError
