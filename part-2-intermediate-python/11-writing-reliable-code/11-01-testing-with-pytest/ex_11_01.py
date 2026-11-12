"""Exercises for 11-01 Testing with pytest.

Read test_ex_11_01.py first: the tests describe every case.
"""


def parse_score(text):
    """Convert `text` (which may have spaces around it) into an int score.
    Raise ValueError if it is not a whole number, or is outside 0 to 100.

    Example: parse_score(" 85 ") returns 85
    """
    raise NotImplementedError


class Inventory:
    """Tracks how many of each product are in stock."""

    def __init__(self):
        """Start with no stock."""
        raise NotImplementedError

    def add(self, product, amount):
        """Add `amount` of `product`. Raise ValueError if amount < 1."""
        raise NotImplementedError

    def remove(self, product, amount):
        """Remove `amount` of `product`.
        Raise KeyError if the product has never been added.
        Raise ValueError if amount < 1 or there is not enough in stock.
        """
        raise NotImplementedError

    def quantity(self, product):
        """Return how many of `product` are in stock (0 if never added)."""
        raise NotImplementedError
