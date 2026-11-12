"""Solutions for 04-02 Arguments in depth."""


def greet(name, greeting="Hello"):
    """Return a greeting such as "Hello, Ada!"."""
    return f"{greeting}, {name}!"


def power(base, exponent=2):
    """Return `base` raised to `exponent`."""
    return base ** exponent


def full_name(first, last, middle=""):
    """Return the full name with single spaces between the parts."""
    if middle:
        return f"{first} {middle} {last}"
    return f"{first} {last}"


def repeat_text(text, times=2, separator=" "):
    """Return `text` repeated `times` times with `separator` between."""
    # Adding the separator after every copy leaves one too many at the end,
    # so build it by putting the separator BEFORE every copy except the first.
    result = ""
    for count in range(times):
        if count > 0:
            result += separator
        result += text
    return result


def add_item(item, basket=None):
    """Append `item` to `basket` (or a new list) and return it."""
    if basket is None:
        basket = []
    basket.append(item)
    return basket
