"""Exercises for 13-02 Indexing and slicing. Do not use loops."""
import numpy as np


def column(table, index):
    """Return column `index` of the 2-D array `table` as a 1-D array.

    Example: column(np.array([[1, 2], [3, 4]]), 1) returns array([2, 4])
    """
    raise NotImplementedError


def last_rows(table, count):
    """Return the last `count` rows of the 2-D array `table`.

    Example: last_rows(np.array([[1], [2], [3]]), 2) returns array([[2], [3]])
    """
    raise NotImplementedError


def values_between(values, low, high):
    """Return the elements of the 1-D array `values` that are >= low and
    <= high, in their original order. Use a boolean mask.

    Example: values_between(np.array([5, 12, 8, 20]), 6, 15) returns array([12, 8])
    """
    raise NotImplementedError


def replace_below(values, floor):
    """Return a COPY of `values` where every element below `floor` is replaced
    by `floor`. The original array must not change.

    Example: replace_below(np.array([3, 9, 1]), 5) returns array([5, 9, 5])
    """
    raise NotImplementedError


def rows_where(table, column_index, threshold):
    """Return the rows of `table` whose value in column `column_index` is
    greater than `threshold`.

    Example: rows_where(np.array([[1, 50], [2, 90]]), 1, 60) returns array([[2, 90]])
    """
    raise NotImplementedError


def pick_rows(table, positions):
    """Return the rows of `table` at the given list of positions, in that order.

    Example: pick_rows(np.array([[1], [2], [3]]), [2, 0]) returns array([[3], [1]])
    """
    raise NotImplementedError
