# 09-03 Inheritance and composition

## What you will learn

- Create a subclass that inherits attributes and methods from a base class.
- Override methods, and extend them with `super()`.
- Check relationships with `isinstance` and `issubclass`.
- Choose between inheritance ("is a") and composition ("has a").

## Why it matters

Classes often come in families: a rectangle and a circle are both shapes, with different areas but the same way of being described. Inheritance lets them share code. scikit-learn is built this way: every classifier inherits common behaviour (such as `score`) from shared base classes, which is why they all work the same way. Composition, building objects out of other objects, is how a scikit-learn `Pipeline` combines several steps into one model.

## Concepts

### Inheritance

**Inheritance** lets a new class, the **subclass** (or child), take everything from an existing class, the **base class** (or parent), and then add or change parts. You write the base class in brackets after the subclass name.

```python
import math


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("subclasses must implement area()")

    def describe(self):
        return f"{self.name} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
```

`Shape` defines what every shape can do. Its `area` raises `NotImplementedError` because a generic shape has no area; this is a signal that subclasses must provide their own.

### Overriding and inheriting

A subclass **overrides** a method by defining one with the same name; its version is used instead of the parent's. Methods it does not define are **inherited** from the parent.

```python
shapes = [Rectangle(3, 4), Circle(1)]
for shape in shapes:
    print(shape.describe())
```

```
rectangle with area 12.00
circle with area 3.14
```

`describe` is written once, in `Shape`. When it calls `self.area()`, Python looks up `area` on the actual object, so a rectangle uses `Rectangle.area` and a circle uses `Circle.area`. The loop does not need to know what kind of shape each one is. This ability to treat different classes the same way, because they share an interface, is called **polymorphism**.

### super()

**`super()`** gives access to the parent class's version of a method. In `Rectangle.__init__`, `super().__init__("rectangle")` runs `Shape.__init__`, which sets `self.name`, before `Rectangle` adds its own attributes. If you override `__init__` and forget to call `super().__init__`, the parent's setup never happens.

### isinstance and issubclass

A subclass instance **is** an instance of its parent class too:

```python
print(isinstance(shapes[0], Rectangle), isinstance(shapes[0], Shape))
print(isinstance(shapes[0], Circle), issubclass(Circle, Shape))
```

```
True True
False True
```

### Extending a method

Inheritance can go several levels deep. An override can call `super()` to **extend** the parent's behaviour rather than replace it:

```python
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "square"

    def describe(self):
        return super().describe() + f" (side {self.width})"


print(Square(2).describe())
print([cls.__name__ for cls in Square.__mro__])
```

```
square with area 4.00 (side 2)
['Square', 'Rectangle', 'Shape', 'object']
```

`Square.__mro__` (method resolution order) is the list of classes Python searches, in order, when looking up a method. Every class ultimately inherits from `object`.

### Composition

Inheritance models an **"is a"** relationship: a square *is a* rectangle. **Composition** models a **"has a"** relationship: an object holds other objects as attributes and uses them.

```python
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
        self.running = False

    def start(self):
        self.running = True


class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)   # a Car has an Engine

    def start(self):
        self.engine.start()
        return f"{self.model} started ({self.engine.horsepower} hp)"


car = Car("Roadster", 300)
print(car.start(), car.engine.running)
```

```
Roadster started (300 hp) True
```

A car is not a kind of engine, so `Car(Engine)` would be wrong. `Car` **delegates** starting to its engine. Composition also works with collections of parts:

```python
class Drawing:
    def __init__(self):
        self.shapes = []

    def add(self, shape):
        self.shapes.append(shape)

    def total_area(self):
        return sum([shape.area() for shape in self.shapes])


drawing = Drawing()
drawing.add(Rectangle(2, 3))
drawing.add(Square(2))
print(drawing.total_area())
```

```
10
```

### Which to choose

Prefer **composition** by default. It keeps classes small and independent, and you can swap parts (a different engine) without changing the class. Use **inheritance** when the subclass genuinely is a specialised version of the parent and can be used anywhere the parent can, and keep hierarchies shallow, one or two levels.

## Common mistakes

- **Forgetting `super().__init__(...)`.** The parent's attributes are never set, giving errors such as `AttributeError: 'Rectangle' object has no attribute 'name'`.
- **Inheriting for code reuse alone.** Making `Car` inherit from `Engine` just to get `start` produces nonsense such as `isinstance(car, Engine)` being `True`. Ask "is it a ...?" before inheriting.
- **Misspelling an override.** A method called `Area` in a subclass does not override `area`, so the parent's `NotImplementedError` is raised. Names must match exactly.
- **Deep hierarchies.** Five levels of inheritance are hard to follow, because a method may be defined in any of them. Keep it shallow.

## Try it

Add a `Triangle(Shape)` with a base and a height, then add one to the `Drawing` and print the new total area. Which methods did you have to write, and which came for free?

## Exercises

Open `ex_09_03.py`. The base class `Employee` is written for you.

1. `SalariedEmployee`: monthly pay from an annual salary.
2. `HourlyEmployee`: pay from hours worked, with overtime.
3. `Manager`: a salaried employee with a bonus, extending `describe` with `super()`.
4. `Team`: holds employees (composition) and totals their pay.

Run the tests:

```
python -m pytest part-2-intermediate-python/09-object-oriented-programming/09-03-inheritance-and-composition
```

## Summary

- `class Child(Parent):` inherits all of Parent's methods; defining a method with the same name overrides it.
- `super().method(...)` calls the parent's version, to extend rather than replace it; always call `super().__init__` when overriding `__init__`.
- A subclass instance passes `isinstance(obj, Parent)`, so shared code works on all subclasses.
- Inheritance means "is a"; composition (objects as attributes) means "has a". Prefer composition.
