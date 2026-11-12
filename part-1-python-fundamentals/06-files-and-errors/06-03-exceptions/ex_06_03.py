"""Exercises for 06-03 Exceptions.

Use try/except with a specific exception type in each function.
"""
import json


def safe_divide(numerator, denominator):
    """Return numerator / denominator, or None if the denominator is zero.

    Example: safe_divide(6, 0) returns None
    """
    raise NotImplementedError


def to_int_or_default(text, default=0):
    """Return `text` converted to an int, or `default` if it cannot be
    converted.

    Example: to_int_or_default("12") returns 12
    Example: to_int_or_default("twelve", default=-1) returns -1
    """
    raise NotImplementedError


def read_text_or_empty(path):
    """Return the contents of the file at `path`, or "" if the file does
    not exist.

    Example: read_text_or_empty(Path("missing.txt")) returns ""
    """
    raise NotImplementedError


def parse_numbers(texts):
    """Try to convert each string in `texts` to a float. Return a tuple
    (numbers, bad) where `numbers` is a list of the floats that converted
    and `bad` is a list of the strings that did not, both in order.

    Example: parse_numbers(["1", "x", "2.5"]) returns ([1.0, 2.5], ["x"])
    """
    raise NotImplementedError


def load_json_or_default(path, default):
    """Return the JSON data in the file at `path`. If the file does not
    exist, or does not contain valid JSON (json.JSONDecodeError),
    return `default` instead.

    Example: for a file containing "not json", returns `default`
    """
    raise NotImplementedError
