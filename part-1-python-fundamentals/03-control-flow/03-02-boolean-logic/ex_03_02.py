"""Exercises for 03-02 Boolean logic.

Each of these can be written as a single `return` of a boolean expression.
"""


def is_leap_year(year):
    """Return True if `year` is a leap year: divisible by 4 but not by 100,
    or divisible by 400.

    Example: is_leap_year(2024) returns True
    """
    raise NotImplementedError


def can_ride(height_cm, age):
    """Return True if someone may go on the ride: they must be at least
    120 cm tall, OR be at least 10 years old and at least 110 cm tall.

    Example: can_ride(115, 12) returns True
    """
    raise NotImplementedError


def is_weekend(day):
    """Return True if `day` is "Saturday" or "Sunday", ignoring case.

    Example: is_weekend("sunday") returns True
    """
    raise NotImplementedError


def in_range(value, low, high):
    """Return True if `value` is between `low` and `high`, including both.
    Use a chained comparison.

    Example: in_range(5, 1, 10) returns True
    """
    raise NotImplementedError


def is_valid_username(username):
    """Return True if all three rules hold:
    - it is between 3 and 12 characters long (inclusive),
    - it contains no spaces,
    - it does not start with a digit.
    Hint: "0123456789" contains every digit, so you can use `in`.

    Example: is_valid_username("ada_l") returns True
    """
    raise NotImplementedError
