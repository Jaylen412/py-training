"""A shopping basket: the code under test in lesson 11-01."""


class Basket:
    """Holds items and their prices, and applies discount codes."""

    DISCOUNTS = {"SAVE10": 0.10, "HALF": 0.50}

    def __init__(self):
        self.items = {}
        self.discount = 0.0

    def add(self, name, price, quantity=1):
        if price < 0:
            raise ValueError(f"price cannot be negative: {price}")
        if quantity < 1:
            raise ValueError(f"quantity must be at least 1: {quantity}")
        old_price, old_quantity = self.items.get(name, (price, 0))
        self.items[name] = (price, old_quantity + quantity)

    def apply_code(self, code):
        if code not in self.DISCOUNTS:
            raise KeyError(f"unknown discount code: {code}")
        self.discount = self.DISCOUNTS[code]

    def total(self):
        subtotal = sum(price * quantity for price, quantity in self.items.values())
        return round(subtotal * (1 - self.discount), 2)
