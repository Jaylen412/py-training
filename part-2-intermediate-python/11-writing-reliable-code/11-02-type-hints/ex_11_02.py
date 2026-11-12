"""Exercises for 11-02 Type hints.

Add the type hints described in each docstring to the `def` line, and
write the body.
"""


def mean(values):
    """Hints: values is a list of floats; returns a float.
    Return the average, or 0.0 for an empty list.

    Example: mean([1.0, 2.0, 6.0]) returns 3.0
    """
    raise NotImplementedError


def word_lengths(words):
    """Hints: words is a list of strings; returns a dict with string keys
    and int values. Return each word mapped to its length.

    Example: word_lengths(["hi", "hello"]) returns {"hi": 2, "hello": 5}
    """
    raise NotImplementedError


def first_long_word(words, minimum):
    """Hints: words is a list of strings, minimum is an int; returns a
    string or None. Return the first word with at least `minimum`
    characters, or None if there is none.

    Example: first_long_word(["a", "abc", "abcd"], 3) returns "abc"
    """
    raise NotImplementedError


def split_pair(text, separator=","):
    """Hints: text and separator are strings; returns a tuple of exactly
    two strings. Split `text` at the FIRST separator, stripping spaces from
    both parts. Raise ValueError if the separator does not appear.

    Example: split_pair("name, Ada") returns ("name", "Ada")
    """
    raise NotImplementedError
