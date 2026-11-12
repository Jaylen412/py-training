"""Solutions for 02-05 Booleans, None and type conversion."""


def is_adult(age):
    """Return True if `age` is 18 or more, otherwise False."""
    return age >= 18


def parse_price(text):
    """Convert a price written as text into a float."""
    return float(text.strip())


def add_text_numbers(first_text, second_text):
    """Add two whole numbers given as strings."""
    # Without int(), + would join the strings: "3" + "4" is "34".
    return int(first_text) + int(second_text)


def matches_number(text, number):
    """Return True if the whole number in `text` equals `number`."""
    return int(text) == number


def is_missing(value):
    """Return True if `value` is None, otherwise False."""
    return value is None


def is_blank(text):
    """Return True if `text` is empty or contains only whitespace."""
    # After stripping, a blank string becomes "", whose length is 0.
    return len(text.strip()) == 0
