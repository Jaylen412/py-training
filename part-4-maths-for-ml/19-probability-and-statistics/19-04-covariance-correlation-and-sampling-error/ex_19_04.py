"""Exercises for 19-04 Covariance, correlation and sampling error.

Write covariance and pearson_correlation without np.cov or np.corrcoef.
"""
import numpy as np


def covariance(x, y):
    """Return the population covariance: the mean of
    (x - mean of x) * (y - mean of y).

    Example: covariance(np.array([1, 2, 3]), np.array([2, 4, 6])) returns about 1.333
    """
    raise NotImplementedError


def pearson_correlation(x, y):
    """Return covariance(x, y) divided by the product of the population
    standard deviations of x and y (np.std). Raise ValueError if either has
    zero standard deviation.

    Example: pearson_correlation(np.array([1, 2, 3]), np.array([6, 4, 2])) returns -1.0
    """
    raise NotImplementedError


def bootstrap_statistic(values, statistic, repeats, seed):
    """Return a NumPy array of `repeats` bootstrap values. For each repeat,
    resample `values` WITH replacement (same size) using
    rng.choice(values, size=len(values), replace=True), then apply
    `statistic` (a function such as np.mean). Create rng once with
    np.random.default_rng(seed).
    """
    raise NotImplementedError


def confidence_interval(values, statistic, level=0.95, repeats=5000, seed=42):
    """Return (low, high): the percentile bootstrap confidence interval for
    `statistic`. For level 0.95, these are the 2.5th and 97.5th percentiles
    of bootstrap_statistic(values, statistic, repeats, seed).
    """
    raise NotImplementedError
