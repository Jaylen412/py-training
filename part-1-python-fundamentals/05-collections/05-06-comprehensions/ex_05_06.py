"""Exercises for 05-06 Comprehensions. Use a comprehension in each function."""


def squares_of_evens(numbers):
    """Return a list of the squares of the even numbers, in order.

    Example: squares_of_evens([1, 2, 3, 4]) returns [4, 16]
    """
    raise NotImplementedError


def clean_words(words):
    """Return the words stripped of surrounding spaces and lower-cased,
    leaving out any that are empty after stripping.

    Example: clean_words([" Apple", "", "  ", "BANANA "]) returns ["apple", "banana"]
    """
    raise NotImplementedError


def word_lengths(words):
    """Return a dictionary mapping each word to its length.

    Example: word_lengths(["hi", "hello"]) returns {"hi": 2, "hello": 5}
    """
    raise NotImplementedError


def initials_set(names):
    """Return the set of upper-case first letters of the names.

    Example: initials_set(["ada", "Alan", "grace"]) returns {"A", "G"}
    """
    raise NotImplementedError


def flatten(grid):
    """Turn a list of lists into a single list, row by row.

    Example: flatten([[1, 2], [3], []]) returns [1, 2, 3]
    """
    raise NotImplementedError


def apply_discount(prices, threshold, rate):
    """Return a NEW dictionary with the same keys. Prices above `threshold`
    are reduced by `rate` (0.1 means 10% off) and rounded to 2 decimal
    places; other prices are unchanged.

    Example: apply_discount({"tv": 500, "pen": 2}, 100, 0.1)
    returns {"tv": 450.0, "pen": 2}
    """
    raise NotImplementedError
