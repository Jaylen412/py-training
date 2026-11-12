"""Exercises for 17-01 Vectors.

Use NumPy arrays, but do not use np.linalg.norm: compute lengths yourself.
"""
import numpy as np


def norm(vector):
    """Return the length of `vector`: the square root of the sum of its
    squared components.

    Example: norm(np.array([3.0, 4.0])) returns 5.0
    """
    raise NotImplementedError


def unit_vector(vector):
    """Return `vector` divided by its length. Raise ValueError for a vector
    of length 0.

    Example: unit_vector(np.array([3.0, 4.0])) returns array([0.6, 0.8])
    """
    raise NotImplementedError


def distance(first, second):
    """Return the Euclidean distance between two points.

    Example: distance(np.array([1, 2]), np.array([4, 6])) returns 5.0
    """
    raise NotImplementedError


def nearest_index(target, points):
    """`points` has shape (n, d) and `target` shape (d,). Return the row
    index (an int) of the point closest to `target`. On a tie, return the
    smallest index. Do it without a Python loop.

    Example: nearest_index(np.array([0, 0]), np.array([[5, 5], [1, 1], [2, 0]]))
    returns 1
    """
    raise NotImplementedError
