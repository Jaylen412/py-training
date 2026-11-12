"""Exercises for 17-02 Dot product and similarity."""
import numpy as np


def cosine_similarity(first, second):
    """Return first . second / (|first| |second|) as a float.
    Raise ValueError if either vector has length 0.

    Example: cosine_similarity(np.array([1, 0]), np.array([0, 5])) returns 0.0
    """
    raise NotImplementedError


def angle_between(first, second):
    """Return the angle between the vectors in degrees. Clip the cosine to
    the range -1 to 1 before using np.arccos.

    Example: angle_between(np.array([1, 0]), np.array([1, 1])) returns 45.0
    """
    raise NotImplementedError


def most_similar(query, documents):
    """`documents` has shape (n, d). Return the row index (an int) of the
    document with the highest cosine similarity to `query`.

    Example: most_similar(np.array([1, 0]), np.array([[0, 1], [5, 1], [1, 1]]))
    returns 1
    """
    raise NotImplementedError


def project(vector, onto):
    """Return the projection of `vector` onto the direction of `onto`:
    (vector . onto / onto . onto) * onto.

    Example: project(np.array([3, 4]), np.array([2, 0])) returns array([3., 0.])
    """
    raise NotImplementedError


def are_orthogonal(first, second, tolerance=1e-9):
    """Return True if the dot product is within `tolerance` of zero."""
    raise NotImplementedError
