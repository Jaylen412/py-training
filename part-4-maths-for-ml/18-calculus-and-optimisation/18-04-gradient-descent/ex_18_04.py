"""Exercises for 18-04 Gradient descent."""
import numpy as np


def gradient_descent_1d(derivative, start, learning_rate, steps):
    """Run `steps` steps of gradient descent on a function of one variable,
    given its `derivative` function. Return the list of x values visited,
    starting with `start` (so the list has steps + 1 values).

    Example: gradient_descent_1d(lambda x: 2 * (x - 3), 0.0, 0.1, 1) returns [0.0, 0.6]
    """
    raise NotImplementedError


def mse_gradient(x, y, w, b):
    """For the model prediction = w * x + b, return (dw, db): the partial
    derivatives of the mean squared error with respect to w and b.
        dw = 2 * mean((prediction - y) * x)
        db = 2 * mean(prediction - y)
    """
    raise NotImplementedError


def fit_line(x, y, learning_rate, epochs):
    """Fit prediction = w * x + b by gradient descent, starting from w = 0
    and b = 0. Each epoch: compute both gradients from the current w and b,
    then update both. After each update, append the MSE to a history list.
    Return (w, b, history).
    """
    raise NotImplementedError


def has_diverged(history):
    """Return True if training has diverged: the last loss is not a finite
    number (nan or inf), or it is larger than the first loss.

    Example: has_diverged([10.0, 5.0, 2.0]) returns False
    """
    raise NotImplementedError
