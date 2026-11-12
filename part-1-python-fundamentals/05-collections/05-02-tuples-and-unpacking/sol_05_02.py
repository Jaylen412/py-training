"""Solutions for 05-02 Tuples and unpacking."""


def min_max(numbers):
    """Return (smallest, largest)."""
    return min(numbers), max(numbers)


def swap_pair(pair):
    """Return the pair in the opposite order."""
    first, second = pair
    return second, first


def split_name(full_name):
    """Return (first_name, last_name)."""
    first_name, last_name = full_name.split()
    return first_name, last_name


def pair_up(names, scores):
    """Return a list of (name, score) tuples."""
    return list(zip(names, scores))


def distance(point_a, point_b):
    """Return the straight-line distance between two points."""
    x_a, y_a = point_a
    x_b, y_b = point_b
    return ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** 0.5
