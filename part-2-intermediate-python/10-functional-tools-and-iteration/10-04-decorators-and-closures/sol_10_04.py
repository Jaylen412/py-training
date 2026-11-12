"""Solutions for 10-04 Decorators and closures."""
import functools


def make_power(exponent):
    """Return a function that raises its argument to `exponent`."""
    def power(number):
        return number ** exponent
    return power


def make_accumulator(start=0):
    """Return a function that keeps a running total."""
    total = start

    def add(amount):
        nonlocal total
        total += amount
        return total
    return add


def count_calls(function):
    """Decorator that counts calls in a `calls` attribute."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return function(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


def validate_non_negative(function):
    """Decorator that rejects negative positional arguments."""
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        for argument in args:
            if isinstance(argument, (int, float)) and argument < 0:
                raise ValueError(f"{function.__name__} got a negative argument: {argument}")
        return function(*args, **kwargs)
    return wrapper


def memoize(function):
    """Decorator that caches results by positional arguments."""
    cache = {}

    @functools.wraps(function)
    def wrapper(*args):
        # args is a tuple, so it can be used directly as a dictionary key.
        if args not in cache:
            cache[args] = function(*args)
        return cache[args]
    return wrapper
