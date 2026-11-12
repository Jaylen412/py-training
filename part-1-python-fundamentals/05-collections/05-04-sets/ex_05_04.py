"""Exercises for 05-04 Sets. Use sets in every function."""


def unique_count(items):
    """Return how many different values are in the list `items`.

    Example: unique_count(["a", "b", "a"]) returns 2
    """
    raise NotImplementedError


def has_duplicates(items):
    """Return True if any value appears more than once in `items`.

    Example: has_duplicates([1, 2, 3, 2]) returns True
    """
    raise NotImplementedError


def common_items(first, second):
    """Return a sorted list of the values that appear in both lists,
    each value once.

    Example: common_items([3, 1, 2, 2], [2, 3, 4]) returns [2, 3]
    """
    raise NotImplementedError


def only_in_first(first, second):
    """Return a sorted list of the values in `first` that are not in
    `second`, each value once.

    Example: only_in_first(["a", "b", "c"], ["b"]) returns ["a", "c"]
    """
    raise NotImplementedError


def missing_fields(record, required):
    """`record` is a dictionary; `required` is a list of field names.
    Return a sorted list of the required names that are not keys of `record`.
    Hint: set(record) gives the set of the dictionary's keys.

    Example: missing_fields({"name": "Ada"}, ["name", "email", "age"])
    returns ["age", "email"]
    """
    raise NotImplementedError


def is_pangram(sentence):
    """Return True if `sentence` contains every letter from a to z at least
    once, ignoring case.

    Example: is_pangram("The quick brown fox jumps over the lazy dog") returns True
    """
    raise NotImplementedError
