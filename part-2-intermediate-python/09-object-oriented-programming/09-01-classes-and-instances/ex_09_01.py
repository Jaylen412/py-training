"""Exercises for 09-01 Classes and instances."""


class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        """Store width and height as attributes called width and height."""
        raise NotImplementedError

    def area(self):
        """Return width times height.

        Example: Rectangle(3, 4).area() returns 12
        """
        raise NotImplementedError

    def perimeter(self):
        """Return the distance all the way round.

        Example: Rectangle(3, 4).perimeter() returns 14
        """
        raise NotImplementedError

    def scale(self, factor):
        """Multiply both width and height by `factor`, changing this rectangle.
        Return nothing.

        Example: after r.scale(2), Rectangle(3, 4) has width 6 and height 8
        """
        raise NotImplementedError


class TallyCounter:
    """A clicker counter, like the ones used to count people at a door."""

    def __init__(self):
        """Start with attributes count = 0 and highest = 0."""
        raise NotImplementedError

    def click(self, times=1):
        """Add `times` to count, update highest if count is now larger,
        and return the new count.

        Example: a new counter's click() returns 1
        """
        raise NotImplementedError

    def reset(self):
        """Set count back to 0. `highest` keeps its value."""
        raise NotImplementedError


class BankAccount:
    """A bank account that counts its transactions."""

    def __init__(self, owner, balance=0):
        """Store owner and balance, and start transactions at 0."""
        raise NotImplementedError

    def deposit(self, amount):
        """Add `amount` to the balance and count one transaction.
        Raise ValueError if amount is not positive.
        """
        raise NotImplementedError

    def withdraw(self, amount):
        """Subtract `amount` and count one transaction.
        Raise ValueError if amount is not positive or is more than the balance.
        A failed withdrawal must not change the balance or the count.
        """
        raise NotImplementedError

    def describe(self):
        """Return "<owner>: <balance with 2 decimal places>".

        Example: BankAccount("Ada", 5).describe() returns "Ada: 5.00"
        """
        raise NotImplementedError
