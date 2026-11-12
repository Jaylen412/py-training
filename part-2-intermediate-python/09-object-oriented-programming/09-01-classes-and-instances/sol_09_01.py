"""Solutions for 09-01 Classes and instances."""


class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        self.width *= factor
        self.height *= factor


class TallyCounter:
    """A clicker counter."""

    def __init__(self):
        self.count = 0
        self.highest = 0

    def click(self, times=1):
        self.count += times
        if self.count > self.highest:
            self.highest = self.count
        return self.count

    def reset(self):
        self.count = 0


class BankAccount:
    """A bank account that counts its transactions."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.transactions = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError(f"deposit must be positive, got {amount}")
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        # Check everything before changing anything, so a failure leaves no trace.
        if amount <= 0:
            raise ValueError(f"withdrawal must be positive, got {amount}")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
        self.transactions += 1

    def describe(self):
        return f"{self.owner}: {self.balance:.2f}"
