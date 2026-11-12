"""Exercises for 05-01 Lists.

None of these functions should change the list that is passed in.
"""


def average(numbers):
    """Return the mean of `numbers`, or 0.0 if the list is empty.

    Example: average([2, 4, 9]) returns 5.0
    """
    raise NotImplementedError


def remove_all(items, target):
    """Return a NEW list with every item equal to `target` removed.

    Example: remove_all([1, 2, 1, 3], 1) returns [2, 3]
    """
    raise NotImplementedError


def top_three(scores):
    """Return the three largest scores, largest first.
    If there are fewer than three, return them all, largest first.

    Example: top_three([50, 90, 70, 80]) returns [90, 80, 70]
    """
    raise NotImplementedError


def rotate_left(items, steps):
    """Return a new list where the first `steps` items have moved to the end.
    `steps` is between 0 and len(items). Use slicing.

    Example: rotate_left([1, 2, 3, 4, 5], 2) returns [3, 4, 5, 1, 2]
    """
    raise NotImplementedError


def running_totals(numbers):
    """Return a list where each item is the sum of all numbers up to and
    including that position.

    Example: running_totals([1, 2, 3, 4]) returns [1, 3, 6, 10]
    """
    raise NotImplementedError


def insert_sorted(sorted_items, value):
    """`sorted_items` is sorted smallest first. Return a NEW list with
    `value` inserted at the right place, so the result is still sorted.
    Do not call sort() or sorted(); find the position with a loop.

    Example: insert_sorted([1, 3, 5], 4) returns [1, 3, 4, 5]
    """
    raise NotImplementedError
