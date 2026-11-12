"""Exercises for 10-03 *args, **kwargs and unpacking.

Write the parameter lists yourself where the comments say so.
"""


def product(*numbers):
    """Return all the numbers multiplied together, or 1 if there are none.

    Example: product(2, 3, 4) returns 24
    """
    raise NotImplementedError


def make_tag(name, *children, **attributes):
    """Return an HTML tag as a string. Attributes go in the opening tag as
    key="value" pairs separated by spaces, in the order given; children are
    joined with no separator between the opening and closing tags.

    Example: make_tag("a", "Click", " here", href="/home", id="link")
    returns '<a href="/home" id="link">Click here</a>'
    Example: make_tag("br") returns "<br></br>"
    """
    raise NotImplementedError


def merge_settings(*dictionaries):
    """Return ONE new dictionary combining all the dictionaries; when keys
    clash, later dictionaries win. Do not change any of the arguments.

    Example: merge_settings({"a": 1, "b": 2}, {"b": 3}, {"c": 4})
    returns {"a": 1, "b": 3, "c": 4}
    """
    raise NotImplementedError


def call_with_defaults(function, *args, **kwargs):
    """Call function(*args, **options), where `options` starts as
    {"verbose": False, "retries": 3} and is overridden by `kwargs`.
    Return the function's result.

    Example: call_with_defaults(dict, retries=5)
    returns {"verbose": False, "retries": 5}
    """
    raise NotImplementedError


# Change the parameter list below so that `currency` and `decimals` are
# KEYWORD-ONLY, with defaults "$" and 2.
def format_money(amount, currency="$", decimals=2):
    """Return the currency symbol followed by the amount with `decimals`
    decimal places and commas between thousands.

    Example: format_money(1234.5) returns "$1,234.50"
    Example: format_money(1234.5, currency="EUR ", decimals=0) returns "EUR 1,234"
    format_money(10, "EUR ") must raise TypeError (keyword-only).
    """
    raise NotImplementedError
