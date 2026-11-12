"""Solutions for 13-01 Arrays."""
import numpy as np


def to_array(values):
    """Return `values` as a float64 array."""
    return np.array(values, dtype=float)


def describe(array):
    """Return (shape, ndim, dtype name)."""
    return array.shape, array.ndim, array.dtype.name


def evenly_spaced(start, stop, count):
    """Return evenly spaced floats including both ends."""
    return np.linspace(start, stop, count)


def multiples(number, limit):
    """Return the multiples of `number` up to `limit`."""
    # stop is limit + 1 so that `limit` itself is included when it is a multiple.
    return np.arange(number, limit + 1, number)


def filled_grid(rows, columns, value):
    """Return a (rows, columns) array filled with `value`."""
    return np.full((rows, columns), value)
