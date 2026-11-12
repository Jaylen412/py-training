# 09-01 Classes and instances


# Example 1: the simplest class, and two instances of it
class Dog:
    pass


rex = Dog()
fido = Dog()
print(type(rex).__name__, rex is fido)


# Example 2: __init__ sets up each new instance's attributes
class BankAccount:
    """A bank account with an owner and a balance."""

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        """Add money to the account."""
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        """Take money out, if there is enough."""
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def describe(self):
        """Return a one-line summary."""
        return f"{self.owner}: {self.balance:.2f}"


account = BankAccount("Ada", 100)
print(account.owner, account.balance)

# Example 3: calling methods changes that instance's state
account.deposit(50)
account.withdraw(30)
print(account.describe())

# Example 4: each instance has its own attributes
other = BankAccount("Alan")
other.deposit(10)
print(account.describe(), "|", other.describe())

# Example 5: a method call is the method with the instance passed as self
print(BankAccount.describe(account))

# Example 6: attributes can be read and changed from outside
account.owner = "Ada Lovelace"
print(account.describe())

# Example 7: methods can return values and call other methods
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def is_square(self):
        return self.width == self.height

    def describe(self):
        kind = "square" if self.is_square() else "rectangle"
        return f"{self.width}x{self.height} {kind} with area {self.area()}"


print(Rectangle(3, 4).describe())
print(Rectangle(5, 5).describe())

# Example 8: a list of objects
shapes = [Rectangle(1, 2), Rectangle(3, 3), Rectangle(2, 5)]
print(sum([shape.area() for shape in shapes]))
print(max([shape.area() for shape in shapes]))
