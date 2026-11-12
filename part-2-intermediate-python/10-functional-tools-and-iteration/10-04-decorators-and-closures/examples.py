# 10-04 Decorators and closures
import functools
import time


# Example 1: a function defined inside another function
def outer():
    message = "hello from outer"

    def inner():
        return message

    return inner


get_message = outer()
print(get_message())


# Example 2: a closure remembers values from the function that made it
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))


# Example 3: nonlocal lets a closure update a remembered variable
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


clicks = make_counter()
print(clicks(), clicks(), clicks())
other = make_counter()
print(other())


# Example 4: a decorator takes a function and returns a new one
def announce(function):
    def wrapper(*args, **kwargs):
        print(f"  calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


def add(first, second):
    return first + second


add = announce(add)
print(add(2, 3))


# Example 5: the @ syntax does the same thing
@announce
def multiply(first, second):
    return first * second


print(multiply(4, 5))
print(multiply.__name__)


# Example 6: functools.wraps keeps the original name and docstring
def announce_properly(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"  calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@announce_properly
def subtract(first, second):
    """Return first minus second."""
    return first - second


print(subtract(9, 4), subtract.__name__, subtract.__doc__)


# Example 7: a timing decorator
def timed(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {function.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper


@timed
def slow_sum(limit):
    return sum(range(limit))


total = slow_sum(1_000_000)
print(total)


# Example 8: a decorator that stores results (a cache)
def remember(function):
    cache = {}

    @functools.wraps(function)
    def wrapper(number):
        if number not in cache:
            cache[number] = function(number)
        return cache[number]
    return wrapper


@remember
def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(80))
