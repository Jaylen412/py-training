"""Solutions for 06-03 Exceptions."""
import json


def safe_divide(numerator, denominator):
    """Return numerator / denominator, or None on division by zero."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None


def to_int_or_default(text, default=0):
    """Return `text` as an int, or `default`."""
    try:
        return int(text)
    except ValueError:
        return default


def read_text_or_empty(path):
    """Return the file's contents, or "" if it does not exist."""
    try:
        with open(path) as file:
            return file.read()
    except FileNotFoundError:
        return ""


def parse_numbers(texts):
    """Split strings into converted floats and unconvertible strings."""
    numbers = []
    bad = []
    for text in texts:
        try:
            number = float(text)
        except ValueError:
            bad.append(text)
        else:
            numbers.append(number)
    return numbers, bad


def load_json_or_default(path, default):
    """Return JSON from the file, or `default` if missing or invalid."""
    try:
        with open(path) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return default
