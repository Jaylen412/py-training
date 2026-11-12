"""Exercises for 19-01 Describing data.

`values` is a 1-D NumPy array. Do not use np.median, np.var or np.std.
"""
import numpy as np


def median(values):
    """Return the middle value after sorting; for an even number of values,
    the mean of the two middle values. Raise ValueError if empty.

    Example: median(np.array([3, 1, 2])) returns 2.0
    """
    raise NotImplementedError


def mode(values):
    """Return the most common value. On a tie, return the smallest of the
    tied values.

    Example: mode(np.array([4, 1, 4, 2, 1])) returns 1
    """
    raise NotImplementedError


def variance(values, sample=False):
    """Return the mean squared deviation from the mean. If `sample` is True,
    divide by n - 1 instead of n.

    Example: variance(np.array([2, 4, 4, 4, 5, 5, 7, 9])) returns 4.0
    """
    raise NotImplementedError


def z_scores(values):
    """Return (values - mean) / standard deviation, using the population
    standard deviation (square root of variance(values))."""
    raise NotImplementedError


def percentile_rank(values, value):
    """Return the percentage (0 to 100) of `values` that are strictly less
    than `value`.

    Example: percentile_rank(np.array([10, 20, 30, 40]), 30) returns 50.0
    """
    raise NotImplementedError
