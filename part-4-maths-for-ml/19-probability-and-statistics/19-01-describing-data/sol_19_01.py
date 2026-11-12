"""Solutions for 19-01 Describing data."""
import numpy as np


def median(values):
    """Return the middle value."""
    if len(values) == 0:
        raise ValueError("median of an empty array")
    ordered = np.sort(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return float(ordered[middle])
    return float((ordered[middle - 1] + ordered[middle]) / 2)


def mode(values):
    """Return the most common value, the smallest on a tie."""
    distinct, counts = np.unique(values, return_counts=True)
    return distinct[counts.argmax()]  # np.unique sorts, so argmax picks the smallest tie


def variance(values, sample=False):
    """Return the population (or sample) variance."""
    deviations = values - values.mean()
    divisor = len(values) - 1 if sample else len(values)
    return float((deviations ** 2).sum() / divisor)


def z_scores(values):
    """Return each value as a number of standard deviations from the mean."""
    return (values - values.mean()) / np.sqrt(variance(values))


def percentile_rank(values, value):
    """Return the percentage of values below `value`."""
    return float(np.mean(values < value) * 100)
