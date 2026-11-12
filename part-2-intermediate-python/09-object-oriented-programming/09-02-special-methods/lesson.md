# 09-02 Special methods

## What you will learn

- Control how objects are displayed with `__repr__` and `__str__`.
- Make `==` compare objects by value with `__eq__`.
- Support built-in functions and operators such as `len()` and `+`.
- Make objects sortable with `__lt__`.

## Why it matters

Python's built-in operations, such as `print`, `==`, `len`, `+` and `sorted`, work on your own classes if you tell them how. This is why a pandas DataFrame prints as a neat table, and why you can add two NumPy arrays with `+`. Good `__repr__` methods alone will save you hours of debugging, because you can see what is inside your objects.

## Concepts

### Special methods

A **special method** (often called a **dunder method**, for the **d**ouble **under**scores) has a name like `__init__` or `__len__`. You rarely call them yourself; Python calls them when you use the matching built-in feature. You have already written one: `__init__` is called when you create an instance.

### The default display

Without any special methods, objects print unhelpfully and compare by identity:

```python
class PlainPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print(repr(PlainPoint(1, 2)).startswith("<__main__.PlainPoint object at 0x"))
print(PlainPoint(1, 2) == PlainPoint(1, 2))
```

```
True
False
```

Printing one shows something like `<__main__.PlainPoint object at 0x102b12a50>`. And two points with the same coordinates are not "equal", because by default `==` checks whether they are the **same object** (like `is`).

### `__repr__` and `__str__`

- **`__repr__`** returns an unambiguous description for programmers, used by `repr()`, the REPL and when objects are inside lists. The convention is to make it look like the code that would create the object.
- **`__str__`** returns a friendly description for users, used by `print()`, `str()` and f-strings. If you only write `__repr__`, Python uses it for both.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
```

```python
point = Point(1, 2)
print(repr(point))
print(str(point))
print(point)
print([point, Point(3, 4)])
print(f"The point is {point}")
```

```
Point(1, 2)
(1, 2)
(1, 2)
[Point(1, 2), Point(3, 4)]
The point is (1, 2)
```

Note that the list used `__repr__` for its items. If you write only one of the two, write `__repr__`.

### `__eq__`

**`__eq__(self, other)`** decides what `==` means. Here two points are equal if their coordinates match. If `other` is not a `Point`, returning the special value `NotImplemented` tells Python "I don't know how to compare with that", and Python falls back to `False`:

```python
print(Point(1, 2) == Point(1, 2), Point(1, 2) == Point(2, 1))
print(Point(1, 2) == "not a point")
```

```
True False
False
```

### Operators: `__add__`

Arithmetic operators have special methods too: `__add__` for `+`, `__sub__` for `-`, `__mul__` for `*`, and so on. `a + b` calls `a.__add__(b)`:

```python
print(Point(1, 2) + Point(10, 20))
```

```
(11, 22)
```

Only define operators whose meaning is obvious. Adding two points is clear; "adding" two bank accounts is not.

### `__len__`

**`__len__`** makes `len()` work. It must return a whole number of 0 or more. Python also uses it for truthiness: an object with length 0 counts as false, just like an empty list.

```python
class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = list(songs)

    def __len__(self):
        return len(self.songs)

    def __repr__(self):
        return f"Playlist({self.name!r}, {len(self)} songs)"


road_trip = Playlist("Road trip", ["Song A", "Song B", "Song C"])
print(len(road_trip))
print(road_trip)
print(bool(Playlist("Empty", [])))
```

```
3
Playlist('Road trip', 3 songs)
False
```

`list(songs)` copies whatever was passed in, so the playlist owns its own list (05-05).

### Sortable objects: `__lt__`

`sorted`, `min` and `max` compare items with `<`. Defining **`__lt__`** ("less than") is enough to make objects sortable:

```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Student({self.name!r}, {self.grade})"

    def __lt__(self, other):
        return self.grade < other.grade


students = [Student("Ada", 91), Student("Alan", 78), Student("Grace", 85)]
print(sorted(students))
print(max(students))
```

```
[Student('Alan', 78), Student('Grace', 85), Student('Ada', 91)]
Student('Ada', 91)
```

Module 10 shows another way to sort, with `key=`, which does not require changing the class at all.

## Common mistakes

- **Printing instead of returning.** `__repr__` and `__str__` must **return** a string. If they print and return `None`, you get `TypeError: __str__ returned non-string (type NoneType)`.
- **Sorting objects with no `__lt__`.** `sorted([A(), A()])` gives `TypeError: '<' not supported between instances of 'A' and 'A'`.
- **Defining `__eq__` and then using objects in a set or as dictionary keys.** Defining `__eq__` switches off the default hashing, so `{Point(1, 2)}` gives `TypeError: unhashable type: 'Point'`. Use a frozen dataclass (09-04) when you need that.
- **Assuming `other` has your attributes.** In `__eq__`, `other` might be anything. Check with `isinstance` and return `NotImplemented` if it is the wrong type.

## Try it

Add `__sub__` to `Point` so that `Point(5, 5) - Point(1, 2)` gives `Point(4, 3)`, and a method `distance_to(self, other)`. Then sort a list of points by their distance from the origin by adding an `__lt__` that compares distances.

## Exercises

Open `ex_09_02.py`:

1. `Money`: an amount in a currency, with `__repr__`, `__str__`, `__eq__`, `__lt__` and `__add__`.
2. `Deck`: a collection of cards with `__len__` and `__repr__`.

Run the tests:

```
python -m pytest part-2-intermediate-python/09-object-oriented-programming/09-02-special-methods
```

## Summary

- Special (dunder) methods let built-in operations work with your classes.
- `__repr__` is for programmers (and lists, the REPL); `__str__` is for `print`. Write `__repr__` at least.
- `__eq__` defines `==`; return `NotImplemented` for unfamiliar types.
- `__add__` and friends define operators; `__len__` defines `len()` and truthiness.
- `__lt__` makes objects work with `sorted`, `min` and `max`.
