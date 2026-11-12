"""Exercises for 13-04 Aggregations and axes. Do not use loops."""
import numpy as np


def column_means(table):
    """Return a 1-D array with the mean of each column.

    Example: column_means(np.array([[1, 10], [3, 20]])) returns array([2., 15.])
    """
    raise NotImplementedError


def row_totals(table):
    """Return a 1-D array with the sum of each row.

    Example: row_totals(np.array([[1, 10], [3, 20]])) returns array([11, 23])
    """
    raise NotImplementedError


def best_column(table):
    """Return the index (an int) of the column with the largest total.

    Example: best_column(np.array([[1, 10], [3, 20]])) returns 1
    """
    raise NotImplementedError


def row_shares(table):
    """Return each value divided by its row's total, so each row sums to 1.

    Example: row_shares(np.array([[1, 3], [2, 2]])) returns array([[0.25, 0.75], [0.5, 0.5]])
    """
    raise NotImplementedError


def count_above(table, threshold):
    """Return a 1-D array: for each column, how many values are greater than
    `threshold`.

    Example: count_above(np.array([[1, 10], [3, 20]]), 2) returns array([1, 2])
    """
    raise NotImplementedError


def to_column(values):
    """Return the 1-D array `values` reshaped into a single column, shape (n, 1).

    Example: to_column(np.array([1, 2, 3])).shape is (3, 1)
    """
    raise NotImplementedError
