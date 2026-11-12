"""Exercises for 18-01 Functions, slopes and derivatives."""


def slope_between(point_a, point_b):
    """Return the slope of the line through two (x, y) points.
    Raise ValueError if the x values are equal (a vertical line).

    Example: slope_between((1, 3), (4, 9)) returns 2.0
    """
    raise NotImplementedError


def numerical_derivative(function, x, step=1e-5):
    """Return the central-difference estimate of the derivative of
    `function` at `x`: (f(x + step) - f(x - step)) / (2 * step).

    Example: numerical_derivative(lambda x: x ** 2, 3) returns about 6.0
    """
    raise NotImplementedError


def tangent_line(function, x0):
    """Return (slope, intercept) of the tangent line to `function` at x0, so
    that the line is y = slope * x + intercept. Use numerical_derivative.

    Example: tangent_line(lambda x: x ** 2, 1) returns about (2.0, -1.0)
    """
    raise NotImplementedError


def downhill_direction(function, x, tolerance=1e-6):
    """Return "right" if moving right makes the function smaller, "left" if
    moving left does, or "flat" if the derivative's size is below `tolerance`.

    Example: downhill_direction(lambda x: (x - 3) ** 2, 0) returns "right"
    """
    raise NotImplementedError
