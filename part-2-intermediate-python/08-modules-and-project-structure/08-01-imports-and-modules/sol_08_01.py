"""Solutions for 08-01 Imports and modules."""
import math
import statistics


def circle_area(radius):
    """Return the area of a circle."""
    return math.pi * radius ** 2


def round_up(value):
    """Return the smallest whole number that is >= value."""
    return math.ceil(value)


def median_of(numbers):
    """Return the median of a non-empty list."""
    return statistics.median(numbers)


def distance(point_a, point_b):
    """Return the straight-line distance between two points."""
    return math.dist(point_a, point_b)


def imported_modules(source):
    """Return the module names imported in `source`."""
    modules = []
    for line in source.splitlines():
        words = line.split()
        # "import x" and "from x import y" both have the module as word 2.
        if len(words) >= 2 and words[0] in ("import", "from"):
            modules.append(words[1])
    return modules
