"""Exercises for 08-01 Imports and modules.

Add the imports you need here, at the top of the file.
"""


def circle_area(radius):
    """Return the area of a circle (pi times radius squared), using math.pi.

    Example: circle_area(1) returns 3.141592653589793
    """
    raise NotImplementedError


def round_up(value):
    """Return the smallest whole number that is >= value, using math.ceil.

    Example: round_up(3.2) returns 4
    """
    raise NotImplementedError


def median_of(numbers):
    """Return the median of a non-empty list, using statistics.median.

    Example: median_of([5, 1, 3]) returns 3
    """
    raise NotImplementedError


def distance(point_a, point_b):
    """Return the straight-line distance between two points (tuples of
    coordinates), using math.dist.

    Example: distance((0, 0), (3, 4)) returns 5.0
    """
    raise NotImplementedError


def imported_modules(source):
    """`source` is Python code as a string. Return a list of the module names
    it imports, in order, from lines of these three forms (ignore all other
    lines, and any leading spaces):
        import name
        import name as alias
        from name import something

    Example: imported_modules("import math\\nfrom pathlib import Path\\nx = 1")
    returns ["math", "pathlib"]
    """
    raise NotImplementedError
