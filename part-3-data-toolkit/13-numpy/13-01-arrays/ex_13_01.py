"""Exercises for 13-01 Arrays."""
import numpy as np


def to_array(values):
    """Return `values` (a list of numbers) as a NumPy array with dtype float64.

    Example: to_array([1, 2, 3]) returns array([1., 2., 3.])
    """
    raise NotImplementedError


def describe(array):
    """Return a tuple (shape, number of dimensions, dtype name as a string).
    Hint: array.dtype.name gives the name, such as "float64".

    Example: describe(np.zeros((2, 3))) returns ((2, 3), 2, "float64")
    """
    raise NotImplementedError


def evenly_spaced(start, stop, count):
    """Return `count` evenly spaced floats from start to stop, including both.

    Example: evenly_spaced(0, 1, 5) returns array([0., 0.25, 0.5, 0.75, 1.])
    """
    raise NotImplementedError


def multiples(number, limit):
    """Return an int array of the positive multiples of `number` that are
    less than or equal to `limit`.

    Example: multiples(3, 10) returns array([3, 6, 9])
    """
    raise NotImplementedError


def filled_grid(rows, columns, value):
    """Return a 2-D array with shape (rows, columns) where every element is
    `value`.

    Example: filled_grid(2, 3, 7) returns array([[7, 7, 7], [7, 7, 7]])
    """
    raise NotImplementedError
