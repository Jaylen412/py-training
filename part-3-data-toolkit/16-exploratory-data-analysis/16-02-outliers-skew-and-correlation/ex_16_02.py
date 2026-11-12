"""Exercises for 16-02 Outliers, skew and correlation.

Each `values` argument is a pandas Series of numbers.
"""
import numpy as np
import pandas as pd


def iqr_bounds(values):
    """Return a tuple (lower, upper): Q1 - 1.5 * IQR and Q3 + 1.5 * IQR,
    where Q1 and Q3 are values.quantile(0.25) and values.quantile(0.75).

    Example: for [1, 2, 3, 4, 5, 6, 7, 8] returns (-2.5, 11.5)
    """
    raise NotImplementedError


def iqr_outliers(values):
    """Return the values (a Series, keeping their index) that lie outside the
    IQR bounds."""
    raise NotImplementedError


def zscore_outliers(values, threshold=3.0):
    """Return the values whose z-score has an absolute value greater than
    `threshold`. Use (values - values.mean()) / values.std()."""
    raise NotImplementedError


def log_transform(values):
    """Return np.log1p(values). Raise ValueError if any value is negative."""
    raise NotImplementedError


def success_rates(frame, by, total_column, success_column):
    """Return a Series indexed by the column(s) in `by` (a string or list)
    giving sum(success_column) / sum(total_column) for each group, rounded
    to 3 decimal places.

    Example: for the kidney stone table, success_rates(table, "treatment",
    "patients", "recovered") returns A 0.78, B 0.826
    """
    raise NotImplementedError
