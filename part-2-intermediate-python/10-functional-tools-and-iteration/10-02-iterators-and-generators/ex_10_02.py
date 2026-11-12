"""Exercises for 10-02 Iterators and generators."""


def countdown(start):
    """Generator: yield start, start - 1, ..., 1. Yield nothing if start < 1.

    Example: list(countdown(3)) returns [3, 2, 1]
    """
    raise NotImplementedError


def parse_numbers(lines):
    """Generator: for each string in `lines` (any iterable, such as an open
    file), strip it; skip it if it is blank or starts with "#"; otherwise
    yield it converted to a float.

    Example: list(parse_numbers(["1", "", "# note", " 2.5 "])) returns [1.0, 2.5]
    """
    raise NotImplementedError


def chunked(items, size):
    """Generator: yield lists of `size` consecutive items from the list
    `items`. The last chunk may be shorter. Raise ValueError if size < 1.

    Example: list(chunked([1, 2, 3, 4, 5], 2)) returns [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError


def running_average(numbers):
    """Generator: after each number, yield the average of all numbers so far.

    Example: list(running_average([2, 4, 9])) returns [2.0, 3.0, 5.0]
    """
    raise NotImplementedError


def take(iterable, count):
    """Return a list of the first `count` items of `iterable` (fewer if it
    runs out). Must work on endless generators, so do not call list() on
    the whole iterable.

    Example: take(countdown(10), 3) returns [10, 9, 8]
    """
    raise NotImplementedError
