"""Exercises for 17-03 Matrices."""
import numpy as np


def result_shape(shape_a, shape_b):
    """Both shapes are 2-tuples. Return the shape of A @ B as a tuple, or
    None if the matrices cannot be multiplied.

    Example: result_shape((150, 4), (4, 2)) returns (150, 2)
    """
    raise NotImplementedError


def weighted_scores(features, weights):
    """Return one score per row of `features`: the dot product of the row
    with `weights`. Use @, not a loop.

    Example: weighted_scores(np.array([[1, 2], [3, 4]]), np.array([10, 1])) returns array([12, 34])
    """
    raise NotImplementedError


def column_means_by_matmul(features):
    """Return the mean of each column, computed as a matrix product: a row
    vector of ones (one per row of `features`), @ features, divided by the
    number of rows. Do not use .mean().

    Example: column_means_by_matmul(np.array([[1, 10], [3, 20]])) returns array([2., 15.])
    """
    raise NotImplementedError


def gram_matrix(features):
    """Return features.T @ features."""
    raise NotImplementedError


def is_symmetric(matrix, tolerance=1e-9):
    """Return True if `matrix` is square and equal to its transpose, within
    `tolerance` for every entry."""
    raise NotImplementedError
