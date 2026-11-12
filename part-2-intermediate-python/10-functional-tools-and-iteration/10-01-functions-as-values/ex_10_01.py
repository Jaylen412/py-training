"""Exercises for 10-01 Functions as values."""


def apply_twice(function, value):
    """Return function(function(value)).

    Example: apply_twice(lambda n: n + 3, 10) returns 16
    """
    raise NotImplementedError


def sort_by_length(words):
    """Return the words sorted shortest first; words of the same length are
    in alphabetical order. Use sorted with a key that returns a tuple.

    Example: sort_by_length(["pear", "fig", "kiwi", "apple"])
    returns ["fig", "kiwi", "pear", "apple"]
    """
    raise NotImplementedError


def sort_people(people):
    """`people` is a list of {"name": ..., "age": ...} dictionaries.
    Return a new list sorted oldest first; people of the same age are in
    alphabetical order of name.

    Example: Ada 36, Alan 41, Grace 36 sorts to Alan, Ada, Grace
    """
    raise NotImplementedError


def longest_by(items, key):
    """Return the item for which key(item) is largest (the first one if
    there is a tie). Return None for an empty list.

    Example: longest_by(["a", "abc", "ab"], len) returns "abc"
    """
    raise NotImplementedError


def count_matching(items, test):
    """Return how many items make test(item) truthy.

    Example: count_matching([1, 2, 3, 4], lambda n: n % 2 == 0) returns 2
    """
    raise NotImplementedError
