"""Exercises for 02-04 String methods and f-strings."""


def clean_name(raw_name):
    """Remove spaces from both ends and put the name in title case.

    Example: clean_name("  ada LOVELACE ") returns "Ada Lovelace"
    """
    raise NotImplementedError


def count_words(sentence):
    """Return the number of words in `sentence`.
    Words are separated by any amount of whitespace.

    Example: count_words("the quick  brown fox") returns 4
    """
    raise NotImplementedError


def slugify(title):
    """Turn a title into a slug: strip the ends, make it lower case,
    and replace each space with a hyphen.

    Example: slugify(" Intro To Python ") returns "intro-to-python"
    """
    raise NotImplementedError


def format_price(amount):
    """Return `amount` as a price: a dollar sign, commas between
    thousands and exactly two decimal places. Use an f-string.

    Example: format_price(1234.5) returns "$1,234.50"
    """
    raise NotImplementedError


def format_percentage(fraction):
    """Return `fraction` as a percentage with one decimal place.

    Example: format_percentage(0.4567) returns "45.7%"
    """
    raise NotImplementedError


def is_mentioned(text, word):
    """Return True if `word` appears anywhere in `text`, ignoring
    upper and lower case. Otherwise return False.

    Example: is_mentioned("I love Python", "python") returns True
    """
    raise NotImplementedError
