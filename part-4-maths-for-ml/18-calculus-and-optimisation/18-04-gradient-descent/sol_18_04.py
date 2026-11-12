"""Solutions for 18-04 Gradient descent."""
import numpy as np


def gradient_descent_1d(derivative, start, learning_rate, steps):
    """Return the x values visited by gradient descent."""
    path = [start]
    for _ in range(steps):
        path.append(path[-1] - learning_rate * derivative(path[-1]))
    return path


def mse_gradient(x, y, w, b):
    """Return the partial derivatives of the MSE for a line."""
    errors = (w * x + b) - y
    return 2 * np.mean(errors * x), 2 * np.mean(errors)


def fit_line(x, y, learning_rate, epochs):
    """Fit a line by gradient descent and return (w, b, history)."""
    w, b = 0.0, 0.0
    history = []
    for _ in range(epochs):
        dw, db = mse_gradient(x, y, w, b)   # both from the same old w and b
        w -= learning_rate * dw
        b -= learning_rate * db
        history.append(float(np.mean((y - (w * x + b)) ** 2)))
    return w, b, history


def has_diverged(history):
    """Return True if the loss is not finite or has grown."""
    return bool(not np.isfinite(history[-1]) or history[-1] > history[0])
