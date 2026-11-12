"""Solutions for 18-01 Functions, slopes and derivatives."""


def slope_between(point_a, point_b):
    """Return rise over run between two points."""
    (x1, y1), (x2, y2) = point_a, point_b
    if x1 == x2:
        raise ValueError("a vertical line has no slope")
    return (y2 - y1) / (x2 - x1)


def numerical_derivative(function, x, step=1e-5):
    """Return the central-difference derivative estimate."""
    return (function(x + step) - function(x - step)) / (2 * step)


def tangent_line(function, x0):
    """Return (slope, intercept) of the tangent line at x0."""
    slope = numerical_derivative(function, x0)
    # The line passes through (x0, f(x0)), so f(x0) = slope * x0 + intercept.
    intercept = function(x0) - slope * x0
    return slope, intercept


def downhill_direction(function, x, tolerance=1e-6):
    """Return which way is downhill: "left", "right" or "flat"."""
    d = numerical_derivative(function, x)
    if abs(d) < tolerance:
        return "flat"
    return "right" if d < 0 else "left"
