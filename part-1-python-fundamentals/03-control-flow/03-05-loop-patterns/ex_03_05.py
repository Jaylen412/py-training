"""Exercises for 03-05 Loop patterns.

Write each one with a loop. Do not use the string methods count, find,
rfind, index or isdigit on the whole text; the point is to practise the
patterns. (Calling isdigit on a single character is fine.)
"""


def count_char(text, target):
    """Return how many times the single character `target` appears in `text`.

    Example: count_char("banana", "a") returns 3
    """
    raise NotImplementedError


def index_of(text, target):
    """Return the index of the first occurrence of `target` in `text`,
    or -1 if it does not appear. Use enumerate.

    Example: index_of("hello", "l") returns 2
    """
    raise NotImplementedError


def largest_digit(digits):
    """`digits` is a non-empty string made only of digits.
    Return the largest digit as an int.

    Example: largest_digit("4719362") returns 9
    """
    raise NotImplementedError


def is_prime(number):
    """Return True if `number` is prime: a whole number greater than 1
    whose only divisors are 1 and itself. Return False otherwise.

    Example: is_prime(29) returns True
    """
    raise NotImplementedError


def all_digits(text):
    """Return True if every character in `text` is a digit.
    Return False for the empty string.

    Example: all_digits("2026") returns True
    """
    raise NotImplementedError


def last_index_of(text, target):
    """Return the index of the LAST occurrence of `target` in `text`,
    or -1 if it does not appear.

    Example: last_index_of("hello", "l") returns 3
    """
    raise NotImplementedError
