"""Price calculations for the shop package."""

TAX_RATE = 0.2


def with_tax(price):
    """Return the price with tax added."""
    return round(price * (1 + TAX_RATE), 2)


def apply_discount(price, rate):
    """Return the price with `rate` (0.1 means 10%) taken off."""
    return round(price * (1 - rate), 2)
