"""Solutions for 13-03 Vectorised operations and broadcasting."""
import numpy as np


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def apply_column_rates(table, rates):
    """Multiply each column by its own rate."""
    return table * rates  # rates has shape (columns,), so it broadcasts across rows


def subtract_row_means(table):
    """Subtract each row's mean from that row."""
    return table - table.mean(axis=1).reshape(-1, 1)


def standardise_columns(table):
    """Give every column mean 0 and standard deviation 1."""
    return (table - table.mean(axis=0)) / table.std(axis=0)


def distances_from(point, points):
    """Return the distance from `point` to each row of `points`."""
    differences = points - point          # shape (n, 2)
    return np.sqrt((differences ** 2).sum(axis=1))
