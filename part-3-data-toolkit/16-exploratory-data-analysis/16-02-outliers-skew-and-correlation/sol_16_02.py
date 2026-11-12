"""Solutions for 16-02 Outliers, skew and correlation."""
import numpy as np
import pandas as pd


def iqr_bounds(values):
    """Return the IQR outlier fences."""
    q1, q3 = values.quantile(0.25), values.quantile(0.75)
    iqr = q3 - q1
    return q1 - 1.5 * iqr, q3 + 1.5 * iqr


def iqr_outliers(values):
    """Return the values outside the IQR fences."""
    low, high = iqr_bounds(values)
    return values[(values < low) | (values > high)]


def zscore_outliers(values, threshold=3.0):
    """Return the values with |z| above `threshold`."""
    z_scores = (values - values.mean()) / values.std()
    return values[z_scores.abs() > threshold]


def log_transform(values):
    """Return log(1 + values), refusing negative values."""
    if (values < 0).any():
        raise ValueError("log_transform needs values of 0 or more")
    return np.log1p(values)


def success_rates(frame, by, total_column, success_column):
    """Return the success rate of each group."""
    totals = frame.groupby(by)[[total_column, success_column]].sum()
    return (totals[success_column] / totals[total_column]).round(3)
