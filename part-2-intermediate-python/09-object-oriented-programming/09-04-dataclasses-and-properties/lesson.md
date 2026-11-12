# 09-04 Dataclasses and properties

## What you will learn

- Write data-holding classes quickly with `@dataclass`.
- Give dataclass fields defaults, including safe defaults for lists.
- Compute values on demand, and validate assignments, with `@property`.
- Tell class attributes from instance attributes.

## Why it matters

Many classes exist mainly to hold data: a product, a log record, a configuration. Writing `__init__`, `__repr__` and `__eq__` by hand for each one is tedious and error-prone; dataclasses write them for you. You will use a dataclass for parsed log records in the Part 2 project. Properties let a class keep a simple, attribute-like interface while still enforcing rules.

## Concepts

### Decorators, briefly

The line `@dataclass` above a class is a **decorator**: it hands the class to a function that modifies it. You will learn how decorators work in Module 10. For now, treat `@dataclass` and `@property` as special markers with the effects described below.

### @dataclass

A **dataclass** is a class whose fields you list as **type-annotated names** (02-04's type hints, used on class attributes). The `@dataclass` decorator then writes `__init__`, `__repr__` and `__eq__` for you.

```python
from dataclasses import dataclass, field


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1


pen = Product("Pen", 1.5, 10)
notebook = Product("Notebook", 3.25)
print(pen)
print(notebook.quantity)
print(pen == Product("Pen", 1.5, 10))
```

```
Product(name='Pen', price=1.5, quantity=10)
1
True
```

`quantity: int = 1` gives that field a default. Fields with defaults must come after fields without, just like function parameters. The type annotations are documentation, as always; they are not checked. You can still add your own methods to a dataclass.

### Mutable defaults: default_factory

The mutable default trap from 04-02 applies here too, so dataclasses forbid `items: list = []`. Instead, `field(default_factory=list)` calls `list()` to make a **fresh** empty list for every instance:

```python
@dataclass
class Order:
    customer: str
    items: list = field(default_factory=list)

    def add(self, product):
        self.items.append(product)

    def total(self):
        return sum([item.price * item.quantity for item in self.items])


first = Order("Ada")
second = Order("Alan")
first.add(pen)
print(len(first.items), len(second.items))
print(first.total())
```

```
1 0
15.0
```

### @property

A **property** is a method that is read like an attribute, without brackets. It is ideal for values that are **computed** from other attributes, because they are always up to date:

```python
@dataclass
class Rectangle:
    width: float
    height: float

    @property
    def area(self):
        return self.width * self.height


box = Rectangle(3, 4)
print(box.area)
box.width = 10
print(box.area)
```

```
12
40
```

If `area` were stored as an attribute in `__init__`, changing `width` would leave it out of date. As a property, it is recalculated on every read.

### Properties with setters

A property can also have a **setter**: a method that runs when the attribute is **assigned**. This lets you validate values while keeping simple `object.attribute = value` syntax. The real value is stored in an attribute with a leading underscore, a convention meaning "internal: do not use from outside".

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius    # goes through the setter below

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError(f"below absolute zero: {value}")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


reading = Temperature(25)
print(reading.celsius, reading.fahrenheit)
reading.celsius = 100
print(reading.fahrenheit)
try:
    reading.celsius = -300
except ValueError as error:
    print("Rejected:", error)
```

```
25 77.0
212.0
Rejected: below absolute zero: -300
```

Even `__init__` goes through the setter, so an invalid temperature can never exist. `fahrenheit` has no setter, so it is read-only.

### Class attributes versus instance attributes

An **instance attribute** is set on `self` and belongs to one object. A **class attribute** is set in the class body, outside any method, and is **shared** by all instances:

```python
class Ticket:
    price = 10          # class attribute
    sold = 0            # class attribute used as a shared counter

    def __init__(self, holder):
        self.holder = holder   # instance attribute
        Ticket.sold += 1


tickets = [Ticket("Ada"), Ticket("Alan")]
print(Ticket.sold, tickets[0].price, tickets[1].holder)
Ticket.price = 12
print(tickets[0].price, tickets[1].price)
```

```
2 10 Alan
12 12
```

Changing `Ticket.price` changed it for every ticket. Use class attributes for constants and shared settings; use instance attributes for anything that differs between objects. (In a dataclass, an annotated name is a field, which becomes an instance attribute.)

### Frozen dataclasses

`@dataclass(frozen=True)` makes instances **immutable**: assigning to a field raises an error. A useful side effect is that frozen dataclasses can be put in sets and used as dictionary keys:

```python
@dataclass(frozen=True)
class Point:
    x: float
    y: float


origin = Point(0, 0)
try:
    origin.x = 5
except Exception as error:
    print(type(error).__name__)
print({origin: "start"}[Point(0, 0)])
```

```
FrozenInstanceError
start
```

## Common mistakes

- **A list as a dataclass default.** `items: list = []` gives `ValueError: mutable default <class 'list'> for field items is not allowed: use default_factory`. Use `field(default_factory=list)`.
- **A field without a default after one with a default.** This gives `TypeError: non-default argument 'b' follows default argument 'a'`. Put fields with defaults last.
- **Calling a property with brackets.** `box.area()` gives `TypeError: 'int' object is not callable`, because `box.area` is already the number. Read properties without brackets.
- **Assigning to a property with no setter.** `reading.fahrenheit = 50` gives `AttributeError: property 'fahrenheit' of 'Temperature' object has no setter`. Add a setter, or set the underlying value instead.

## Try it

Add a setter to `Temperature.fahrenheit` that converts the value to Celsius and stores it, so that `reading.fahrenheit = 212` makes `reading.celsius` 100. Check that setting an impossible Fahrenheit value is still rejected.

## Exercises

Open `ex_09_04.py`:

1. `LineItem`: a dataclass with a default quantity and a `total` property.
2. `Invoice`: a dataclass with a list of items, an `add` method and `subtotal`, `tax` and `total` properties.
3. `BoundedValue`: a class whose `value` property is always kept between a minimum and a maximum.

Run the tests:

```
python -m pytest part-2-intermediate-python/09-object-oriented-programming/09-04-dataclasses-and-properties
```

## Summary

- `@dataclass` writes `__init__`, `__repr__` and `__eq__` from annotated fields; fields with defaults come last.
- Use `field(default_factory=list)` for list (or dict) defaults.
- `@property` turns a method into a computed, read-only attribute; `@name.setter` adds validation on assignment.
- Class attributes are shared by all instances; instance attributes (on `self`) belong to one.
- `@dataclass(frozen=True)` makes instances immutable and usable as dictionary keys.
