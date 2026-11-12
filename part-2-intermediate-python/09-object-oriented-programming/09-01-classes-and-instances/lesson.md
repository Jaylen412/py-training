# 09-01 Classes and instances

## What you will learn

- Define a class and create instances of it.
- Set up each instance's attributes in `__init__`.
- Write methods that read and change an instance's state through `self`.
- Decide when bundling data and functions into a class is worth it.

## Why it matters

So far data (dictionaries, lists) and the functions that work on it have lived separately. A **class** bundles them together: an account knows its balance **and** how to deposit. Everything in Python is an object of some class: strings, lists, even functions. In Part 5, every scikit-learn model is an object whose methods (`fit`, `predict`) change and use its internal state.

## Concepts

### Classes and instances

A **class** is a blueprint for a kind of object. An **instance** (or **object**) is one thing built from that blueprint. You define a class with `class`, a name in **CamelCase** (capital at the start of each word, by convention), and a block. You create an instance by calling the class like a function:

```python
class Dog:
    pass


rex = Dog()
fido = Dog()
print(type(rex).__name__, rex is fido)
```

```
Dog False
```

`pass` is a placeholder meaning "nothing here yet". `rex` and `fido` are two separate instances of the same class.

### `__init__`, `self` and attributes

An **attribute** is a variable that belongs to an object, read and written with a dot: `account.balance`. A **method** is a function defined inside a class. The special method **`__init__`** runs automatically each time a new instance is created; its job is to give the instance its starting attributes.

```python
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
```

Every method's first parameter is **`self`**: the instance the method is working on. `self.owner = owner` creates an attribute called `owner` on this particular instance and stores the argument in it.

```python
account = BankAccount("Ada", 100)
print(account.owner, account.balance)
```

```
Ada 100
```

`BankAccount("Ada", 100)` creates a new, empty instance, calls `__init__` with `self` set to it, `owner="Ada"` and `balance=100`, and gives the instance back. You never pass `self` yourself.

### Methods change state

The values of an object's attributes at a given moment are called its **state**. Methods can change it:

```python
account.deposit(50)
account.withdraw(30)
print(account.describe())
```

```
Ada: 120.00
```

When you write `account.deposit(50)`, Python calls `BankAccount.deposit` with `self` set to `account` and `amount` set to 50. These two lines are exactly equivalent:

```python
print(BankAccount.describe(account))
```

```
Ada: 120.00
```

### Each instance has its own state

Attributes set through `self` belong to one instance. Changing one account does not touch another:

```python
other = BankAccount("Alan")
other.deposit(10)
print(account.describe(), "|", other.describe())
```

```
Ada: 120.00 | Alan: 10.00
```

Attributes can also be read and changed from outside, although it is usually better to go through methods so that rules (like "no negative deposits") are enforced:

```python
account.owner = "Ada Lovelace"
print(account.describe())
```

```
Ada Lovelace: 120.00
```

### Methods calling methods

Inside a class, methods call each other through `self`:

```python
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
```

```
3x4 rectangle with area 12
5x5 square with area 25
```

Objects work in collections like any other value:

```python
shapes = [Rectangle(1, 2), Rectangle(3, 3), Rectangle(2, 5)]
print(sum([shape.area() for shape in shapes]))
print(max([shape.area() for shape in shapes]))
```

```
21
10
```

### When to write a class

A class is worth it when some data and the operations on it naturally belong together, and especially when the data changes over time (an account's balance, a model's learned parameters) and rules must be enforced as it does. For a one-off calculation, a function is simpler. For a simple record with no behaviour, a dictionary or a dataclass (09-04) is enough.

## Common mistakes

- **Forgetting `self` in a method definition.** `def describe():` inside a class, called as `account.describe()`, gives `TypeError: BankAccount.describe() takes 0 positional arguments but 1 was given`. The "1 given" is the instance. Always list `self` first.
- **Forgetting `self.` when setting an attribute.** `owner = owner` inside `__init__` only creates a local variable, so later `account.owner` gives `AttributeError: 'BankAccount' object has no attribute 'owner'`. Write `self.owner = owner`.
- **Missing arguments when creating an instance.** `BankAccount()` gives `TypeError: BankAccount.__init__() missing 1 required positional argument: 'owner'`. The class call takes `__init__`'s parameters, minus `self`.
- **Calling a method on the class without an instance.** `BankAccount.describe()` fails because there is no `self`. Create an instance first.

## Try it

Add a method `transfer(self, other, amount)` to `BankAccount` that withdraws from this account and deposits into `other`. Test it with two accounts. What happens when the withdrawal fails? Does the other account still receive the money?

## Exercises

Open `ex_09_01.py`. Each method raises `NotImplementedError`; write the bodies, including `__init__`.

1. `Rectangle`: area, perimeter and scaling.
2. `TallyCounter`: a clicker that counts up, can be reset, and remembers its highest count.
3. `BankAccount`: deposits, withdrawals with validation, and a transaction count.

Run the tests:

```
python -m pytest part-2-intermediate-python/09-object-oriented-programming/09-01-classes-and-instances
```

## Summary

- A class is a blueprint; calling it creates an instance.
- `__init__(self, ...)` runs on creation and sets attributes with `self.name = value`.
- Methods are functions in a class; their first parameter, `self`, is the instance.
- `instance.method(args)` is the same as `Class.method(instance, args)`.
- Each instance has its own attributes; methods are the safe way to change them.
