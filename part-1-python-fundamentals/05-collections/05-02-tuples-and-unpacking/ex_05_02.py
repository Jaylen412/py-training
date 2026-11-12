"""Exercises for 05-02 Tuples and unpacking."""


def min_max(numbers):
    """Return a tuple (smallest, largest) for a non-empty list of numbers.

    Example: min_max([7, 2, 9, 4]) returns (2, 9)
    """
    raise NotImplementedError


def swap_pair(pair):
    """Return a new two-item tuple with the items in the opposite order.
    Use unpacking.

    Example: swap_pair(("a", "b")) returns ("b", "a")
    """
    raise NotImplementedError


def split_name(full_name):
    """`full_name` contains exactly one space. Return a tuple
    (first_name, last_name), using split and unpacking.

    Example: split_name("Ada Lovelace") returns ("Ada", "Lovelace")
    """
    raise NotImplementedError


def pair_up(names, scores):
    """Return a list of (name, score) tuples, pairing items by position.
    Stop at the shorter list.

    Example: pair_up(["Ada", "Alan"], [95, 72]) returns [("Ada", 95), ("Alan", 72)]
    """
    raise NotImplementedError


def distance(point_a, point_b):
    """Each point is a tuple (x, y). Return the straight-line distance
    between them: the square root of (x difference squared plus
    y difference squared). Unpack the points first.

    Example: distance((0, 0), (3, 4)) returns 5.0
    """
    raise NotImplementedError
