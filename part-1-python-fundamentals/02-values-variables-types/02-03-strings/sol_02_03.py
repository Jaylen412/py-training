"""Solutions for 02-03 Strings."""


def first_and_last(text):
    """Return the first and last characters of `text` joined together."""
    return text[0] + text[-1]


def initials(first_name, last_name):
    """Return the initials of a name, each followed by a full stop."""
    return first_name[0] + "." + last_name[0] + "."


def reverse_text(text):
    """Return `text` backwards."""
    # A step of -1 walks the string from the end to the start.
    return text[::-1]


def without_ends(text):
    """Return `text` without its first and last characters."""
    return text[1:-1]


def make_tag(name):
    """Return `name` wrapped in angle brackets."""
    return "<" + name + ">"
