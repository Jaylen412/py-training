"""Solutions for 18-02 Gradients."""
import numpy as np


def partial_derivative(function, point, index, step=1e-5):
    """Estimate the partial derivative along one input."""
    forward = np.array(point, dtype=float)   # np.array copies, so `point` is untouched
    backward = np.array(point, dtype=float)
    forward[index] += step
    backward[index] -= step
    return (function(forward) - function(backward)) / (2 * step)


def numerical_gradient(function, point, step=1e-5):
    """Return all the partial derivatives as a vector."""
    return np.array([partial_derivative(function, point, i, step) for i in range(len(point))])


def steepest_descent_direction(function, point):
    """Return the unit vector pointing downhill."""
    gradient = numerical_gradient(function, point)
    length = np.linalg.norm(gradient)
    if length < 1e-9:
        raise ValueError("the gradient is zero here: there is no downhill direction")
    return -gradient / length


def is_near_minimum(function, point, tolerance=1e-4):
    """Return True if the gradient is almost zero."""
    return bool(np.linalg.norm(numerical_gradient(function, point)) < tolerance)
