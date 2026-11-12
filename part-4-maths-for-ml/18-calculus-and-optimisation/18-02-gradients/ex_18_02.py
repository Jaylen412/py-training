"""Exercises for 18-02 Gradients.

Each `function` takes a 1-D NumPy array of inputs and returns a number.
"""
import numpy as np


def partial_derivative(function, point, index, step=1e-5):
    """Return the central-difference estimate of the partial derivative of
    `function` with respect to input number `index`, at `point`.
    Do not change `point` (work on float copies).

    Example: for f(p) = p[0] ** 2 + 3 * p[1] ** 2 at (1, 1), index 1 gives about 6.0
    """
    raise NotImplementedError


def numerical_gradient(function, point, step=1e-5):
    """Return the gradient as a 1-D float array: one partial derivative per input.

    Example: for the same f at (2, -1) returns about array([4., -6.])
    """
    raise NotImplementedError


def steepest_descent_direction(function, point):
    """Return the UNIT vector pointing in the direction of steepest decrease
    (the negative gradient divided by its length). Raise ValueError if the
    gradient is (almost) zero, with length below 1e-9.

    Example: for f(p) = p[0] ** 2 + p[1] ** 2 at (3, 4) returns about array([-0.6, -0.8])
    """
    raise NotImplementedError


def is_near_minimum(function, point, tolerance=1e-4):
    """Return True if the length of the gradient at `point` is below `tolerance`."""
    raise NotImplementedError
