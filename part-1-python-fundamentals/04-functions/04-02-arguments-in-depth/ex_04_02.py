"""Exercises for 04-02 Arguments in depth."""


def greet(name, greeting="Hello"):
    """Return a greeting such as "Hello, Ada!".

    Example: greet("Ada") returns "Hello, Ada!"
    Example: greet("Ada", greeting="Hi") returns "Hi, Ada!"
    """
    raise NotImplementedError


def power(base, exponent=2):
    """Return `base` raised to `exponent`. Squares by default.

    Example: power(3) returns 9
    """
    raise NotImplementedError


def full_name(first, last, middle=""):
    """Return the full name with single spaces between the parts.
    If there is no middle name, there must be only one space.

    Example: full_name("Ada", "Lovelace") returns "Ada Lovelace"
    Example: full_name("Ada", "Lovelace", middle="King") returns "Ada King Lovelace"
    """
    raise NotImplementedError


def repeat_text(text, times=2, separator=" "):
    """Return `text` repeated `times` times with `separator` between copies.
    Return "" if `times` is 0.

    Example: repeat_text("ha", times=3, separator="-") returns "ha-ha-ha"
    """
    raise NotImplementedError


def add_item(item, basket=None):
    """Append `item` to `basket` and return the basket.
    If no basket is given, start a NEW empty list each time.

    Example: add_item("apple") returns ["apple"]
    Example: add_item("milk", ["bread"]) returns ["bread", "milk"]
    """
    raise NotImplementedError
