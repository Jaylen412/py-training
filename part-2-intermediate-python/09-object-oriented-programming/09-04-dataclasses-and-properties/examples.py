# 09-04 Dataclasses and properties
from dataclasses import dataclass, field


# Example 1: a dataclass writes __init__, __repr__ and __eq__ for you
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


# Example 2: mutable defaults need field(default_factory=...)
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


# Example 3: @property - a method that is read like an attribute
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


# Example 4: a property with a setter that validates
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


# Example 5: class attributes are shared by every instance
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


# Example 6: frozen dataclasses cannot be changed after creation
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
