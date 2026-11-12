"""Solutions for 09-04 Dataclasses and properties."""
from dataclasses import dataclass, field


@dataclass
class LineItem:
    description: str
    unit_price: float
    quantity: int = 1

    @property
    def total(self):
        return self.unit_price * self.quantity


@dataclass
class Invoice:
    customer: str
    tax_rate: float = 0.2
    items: list = field(default_factory=list)

    def add(self, item):
        self.items.append(item)

    @property
    def subtotal(self):
        return sum([item.total for item in self.items])

    @property
    def tax(self):
        return round(self.subtotal * self.tax_rate, 2)

    @property
    def total(self):
        return round(self.subtotal + self.tax, 2)


class BoundedValue:
    def __init__(self, value, minimum, maximum):
        if minimum > maximum:
            raise ValueError(f"minimum {minimum} is greater than maximum {maximum}")
        self.minimum = minimum
        self.maximum = maximum
        self.value = value  # runs the setter, so the starting value is clamped too

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = min(max(new_value, self.minimum), self.maximum)
