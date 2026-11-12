"""Exercises for 04-03 Scope.

Do not use `global` or any variable defined outside the function.
"""


def add_points(score, points):
    """An old version did `global score; score += points`.
    Instead, return the new score.

    Example: add_points(10, 5) returns 15
    """
    raise NotImplementedError


def price_with_tax(price, tax_rate=0.2):
    """An old version read a changeable global TAX. Use the parameter.
    Return the price with tax added.

    Example: price_with_tax(100) returns 120.0
    Example: price_with_tax(100, tax_rate=0.05) returns 105.0
    """
    raise NotImplementedError


def count_long_words(text, min_length):
    """Return how many words in `text` have at least `min_length` letters.
    Words are separated by whitespace.
    Hint: `for word in text.split():` loops over the words one at a time.

    Example: count_long_words("the quick brown fox", 5) returns 2
    """
    raise NotImplementedError


def apply_transaction(balance, amount, is_deposit):
    """Return the new balance: add `amount` if `is_deposit` is True,
    otherwise subtract it.

    Example: apply_transaction(100, 30, False) returns 70
    """
    raise NotImplementedError
