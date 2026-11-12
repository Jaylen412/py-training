"""Exercises for 13-03 Vectorised operations and broadcasting.

Do not use Python loops or comprehensions.
"""
import numpy as np


def celsius_to_fahrenheit(celsius):
    """Convert an array of Celsius temperatures to Fahrenheit.

    Example: celsius_to_fahrenheit(np.array([0, 100])) returns array([32., 212.])
    """
    raise NotImplementedError


def apply_column_rates(table, rates):
    """Multiply each column of the 2-D array `table` by the matching value
    in the 1-D array `rates` (one rate per column).

    Example: apply_column_rates(np.array([[1, 2], [3, 4]]), np.array([10, 0.5]))
    returns array([[10., 1.], [30., 2.]])
    """
    raise NotImplementedError


def subtract_row_means(table):
    """Return `table` with each row's mean subtracted from every value in
    that row, so each row then has mean 0.
    Hint: table.mean(axis=1) gives one mean per row; reshape it to a column.

    Example: subtract_row_means(np.array([[1, 3], [10, 20]]))
    returns array([[-1., 1.], [-5., 5.]])
    """
    raise NotImplementedError


def standardise_columns(table):
    """Return (table - column means) / column standard deviations.
    Use table.mean(axis=0) and table.std(axis=0).

    Example: standardise_columns(np.array([[1.0], [3.0]])) returns array([[-1.], [1.]])
    """
    raise NotImplementedError


def distances_from(point, points):
    """`point` has shape (2,) and `points` has shape (n, 2). Return a 1-D array
    of the straight-line distance from `point` to each row of `points`.

    Example: distances_from(np.array([0, 0]), np.array([[3, 4], [6, 8]]))
    returns array([5., 10.])
    """
    raise NotImplementedError
