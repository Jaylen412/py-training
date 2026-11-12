"""Exercises for 05-03 Dictionaries."""


def word_counts(text):
    """Return a dictionary mapping each word in `text` (lower-cased)
    to the number of times it appears. Words are separated by whitespace.

    Example: word_counts("The cat the hat") returns {"the": 2, "cat": 1, "hat": 1}
    """
    raise NotImplementedError


def most_common_word(text):
    """Return the word (lower-cased) that appears most often in `text`.
    If several words tie, return the one that appears first in the text.
    Return None for an empty text.

    Example: most_common_word("a b b a b") returns "b"
    """
    raise NotImplementedError


def invert(mapping):
    """Return a new dictionary with keys and values swapped.
    You can assume the values are all different.

    Example: invert({"a": 1, "b": 2}) returns {1: "a", 2: "b"}
    """
    raise NotImplementedError


def merge_inventory(first, second):
    """Both arguments map item names to quantities. Return a NEW dictionary
    containing every item from both, with quantities added together.
    Do not change either argument.

    Example: merge_inventory({"apple": 3}, {"apple": 2, "pear": 1})
    returns {"apple": 5, "pear": 1}
    """
    raise NotImplementedError


def price_of_basket(prices, basket):
    """`prices` maps item names to prices. `basket` is a list of item names
    (an item can appear more than once). Return the total price.
    Items that are not in `prices` count as 0.

    Example: price_of_basket({"apple": 0.5, "milk": 0.9}, ["apple", "apple", "milk"])
    returns 1.9
    """
    raise NotImplementedError
