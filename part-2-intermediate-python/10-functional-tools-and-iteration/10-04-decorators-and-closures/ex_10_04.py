"""Exercises for 10-04 Decorators and closures."""
import functools


def make_power(exponent):
    """Return a function that raises its argument to `exponent`.

    Example: make_power(3)(2) returns 8
    """
    raise NotImplementedError


def make_accumulator(start=0):
    """Return a function add(amount) that adds `amount` to a running total
    (beginning at `start`) and returns the new total. Each accumulator keeps
    its own total.

    Example: add = make_accumulator(10); add(5) returns 15; add(5) returns 20
    """
    raise NotImplementedError


def count_calls(function):
    """Decorator. The decorated function behaves exactly like the original,
    but has an attribute `calls` counting how many times it has been called
    (starting at 0). Keep the original __name__ with functools.wraps.
    Hint: functions are objects, so you can set wrapper.calls = 0 and update
    wrapper.calls inside the wrapper.

    Example: after decorating f and calling it twice, f.calls is 2
    """
    raise NotImplementedError


def validate_non_negative(function):
    """Decorator. Before calling the function, raise ValueError if any
    positional argument is a number below zero. Keep the original __name__.

    Example: a decorated sqrt(-4) raises ValueError
    """
    raise NotImplementedError


def memoize(function):
    """Decorator. Remember the result for each tuple of positional
    arguments, so the original function runs only once per distinct set of
    arguments. Keep the original __name__.

    Example: a decorated slow add(2, 3) computes once; a second add(2, 3)
    returns the stored 5 without calling the original again
    """
    raise NotImplementedError
