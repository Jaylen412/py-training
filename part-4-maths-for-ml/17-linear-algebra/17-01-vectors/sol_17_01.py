"""Solutions for 17-01 Vectors."""
import numpy as np


def norm(vector):
    """Return the length of a vector."""
    return float(np.sqrt((np.asarray(vector, dtype=float) ** 2).sum()))


def unit_vector(vector):
    """Return the vector scaled to length 1."""
    length = norm(vector)
    if length == 0:
        raise ValueError("the zero vector has no direction")
    return np.asarray(vector, dtype=float) / length


def distance(first, second):
    """Return the Euclidean distance between two points."""
    return norm(np.asarray(second, dtype=float) - np.asarray(first, dtype=float))


def nearest_index(target, points):
    """Return the index of the point nearest to `target`."""
    # One squared distance per row; the square root is not needed to rank them.
    squared = ((points - target) ** 2).sum(axis=1)
    return int(squared.argmin())  # argmin returns the first index on a tie
