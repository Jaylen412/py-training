"""Exercises for 09-04 Dataclasses and properties.

Replace each `raise NotImplementedError`. For the dataclasses, fill in the
fields where the comments say so.
"""
from dataclasses import dataclass, field


@dataclass
class LineItem:
    """One line on an invoice.

    Fields, in this order: description (str), unit_price (float),
    quantity (int, default 1). Replace the `pass` below with them.
    """
    pass

    @property
    def total(self):
        """unit_price times quantity.

        Example: LineItem("Pen", 1.5, 4).total returns 6.0
        """
        raise NotImplementedError


@dataclass
class Invoice:
    """An invoice for a customer.

    Fields: customer (str), tax_rate (float, default 0.2),
    items (list, default a NEW empty list for every invoice).
    Replace the `pass` below with them.
    """
    pass

    def add(self, item):
        """Append a LineItem to items."""
        raise NotImplementedError

    @property
    def subtotal(self):
        """The sum of every item's total."""
        raise NotImplementedError

    @property
    def tax(self):
        """subtotal times tax_rate, rounded to 2 decimal places."""
        raise NotImplementedError

    @property
    def total(self):
        """subtotal plus tax, rounded to 2 decimal places."""
        raise NotImplementedError


class BoundedValue:
    """A number that is always kept between minimum and maximum (inclusive).
    Values outside the range are clamped to the nearest limit.
    """

    def __init__(self, value, minimum, maximum):
        """Raise ValueError if minimum > maximum. Store minimum and maximum,
        then set self.value = value so the setter does the clamping."""
        raise NotImplementedError

    @property
    def value(self):
        """Return the stored value (keep it in self._value)."""
        raise NotImplementedError

    @value.setter
    def value(self, new_value):
        """Store new_value, clamped to the range.

        Example: with minimum 0 and maximum 10, setting value to 15 stores 10
        """
        raise NotImplementedError
