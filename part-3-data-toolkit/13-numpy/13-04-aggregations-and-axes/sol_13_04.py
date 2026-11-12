"""Solutions for 13-04 Aggregations and axes."""
import numpy as np


def column_means(table):
    """Return the mean of each column."""
    return table.mean(axis=0)


def row_totals(table):
    """Return the sum of each row."""
    return table.sum(axis=1)


def best_column(table):
    """Return the index of the column with the largest total."""
    return int(table.sum(axis=0).argmax())


def row_shares(table):
    """Return each value as a fraction of its row total."""
    return table / table.sum(axis=1, keepdims=True)


def count_above(table, threshold):
    """Count values above `threshold` in each column."""
    return (table > threshold).sum(axis=0)


def to_column(values):
    """Reshape a 1-D array into a column."""
    return values.reshape(-1, 1)
