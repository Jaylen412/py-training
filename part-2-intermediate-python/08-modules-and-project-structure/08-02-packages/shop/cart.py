"""Shopping cart totals. Uses a relative import to reach a sibling module."""
from .pricing import with_tax


def cart_total(prices):
    """Return the total of a list of prices, including tax."""
    return round(sum([with_tax(price) for price in prices]), 2)
