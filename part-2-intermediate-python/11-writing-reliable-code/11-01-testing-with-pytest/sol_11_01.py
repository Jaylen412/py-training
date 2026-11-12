"""Solutions for 11-01 Testing with pytest."""


def parse_score(text):
    """Convert text into an int score from 0 to 100."""
    try:
        score = int(text)
    except ValueError:
        raise ValueError(f"score must be a whole number, got {text!r}")
    if not 0 <= score <= 100:
        raise ValueError(f"score must be between 0 and 100, got {score}")
    return score


class Inventory:
    """Tracks how many of each product are in stock."""

    def __init__(self):
        self.stock = {}

    def add(self, product, amount):
        if amount < 1:
            raise ValueError(f"amount must be at least 1, got {amount}")
        self.stock[product] = self.stock.get(product, 0) + amount

    def remove(self, product, amount):
        if product not in self.stock:
            raise KeyError(f"unknown product: {product}")
        if amount < 1:
            raise ValueError(f"amount must be at least 1, got {amount}")
        if amount > self.stock[product]:
            raise ValueError(f"only {self.stock[product]} {product} in stock")
        self.stock[product] -= amount

    def quantity(self, product):
        return self.stock.get(product, 0)
