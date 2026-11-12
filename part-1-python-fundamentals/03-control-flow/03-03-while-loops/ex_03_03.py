"""Exercises for 03-03 while loops. Use a while loop in each function."""


def countdown_text(start):
    """Return a countdown from `start` down to 1, with each number followed
    by a space, then the word "Go!".
    If `start` is 0 or less, return just "Go!".

    Example: countdown_text(3) returns "3 2 1 Go!"
    """
    raise NotImplementedError


def sum_of_digits(number):
    """Return the sum of the digits of a whole number that is 0 or more.
    Use % 10 and // 10.

    Example: sum_of_digits(2026) returns 10
    """
    raise NotImplementedError


def count_halvings(number):
    """Return how many times `number` can be divided by 2 before the
    result is less than 1.

    Example: count_halvings(10) returns 4
    (10 -> 5 -> 2.5 -> 1.25 -> 0.625: four halvings)
    """
    raise NotImplementedError


def first_power_of_two_over(limit):
    """Return the smallest power of two (1, 2, 4, 8, 16, ...) that is
    strictly greater than `limit`.

    Example: first_power_of_two_over(100) returns 128
    """
    raise NotImplementedError


def collatz_steps(number):
    """Starting from a whole number of 1 or more, repeat this rule until the
    number is 1: if it is even, halve it (use //); if it is odd,
    multiply by 3 and add 1. Return how many steps it took.

    Example: collatz_steps(6) returns 8
    (6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1)
    """
    raise NotImplementedError
