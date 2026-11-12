"""Solutions for 10-03 *args, **kwargs and unpacking."""


def product(*numbers):
    """Multiply all the numbers together."""
    result = 1
    for number in numbers:
        result *= number
    return result


def make_tag(name, *children, **attributes):
    """Build an HTML tag string."""
    attribute_text = "".join(f' {key}="{value}"' for key, value in attributes.items())
    return f"<{name}{attribute_text}>{''.join(children)}</{name}>"


def merge_settings(*dictionaries):
    """Combine dictionaries, later ones winning."""
    merged = {}
    for dictionary in dictionaries:
        merged = {**merged, **dictionary}
    return merged


def call_with_defaults(function, *args, **kwargs):
    """Call `function` with default options overridden by `kwargs`."""
    options = {"verbose": False, "retries": 3, **kwargs}
    return function(*args, **options)


def format_money(amount, *, currency="$", decimals=2):
    """Format an amount of money; options are keyword-only."""
    return f"{currency}{amount:,.{decimals}f}"
