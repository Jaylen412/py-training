"""Solutions for 17-03 Matrices."""
import numpy as np


def result_shape(shape_a, shape_b):
    """Return the shape of A @ B, or None if it is not defined."""
    if shape_a[1] != shape_b[0]:
        return None
    return shape_a[0], shape_b[1]


def weighted_scores(features, weights):
    """Return one dot product per row."""
    return features @ weights


def column_means_by_matmul(features):
    """Return the column means using a matrix product."""
    rows = features.shape[0]
    ones = np.ones(rows)          # shape (n,): sums each column when used on the left
    return ones @ features / rows


def gram_matrix(features):
    """Return X transpose times X."""
    return features.T @ features


def is_symmetric(matrix, tolerance=1e-9):
    """Return True if the matrix equals its transpose."""
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        return False
    return bool(np.all(np.abs(matrix - matrix.T) <= tolerance))
