"""Exercises for 12-02 Big-O intuition."""


def linear_search(items, target):
    """Look through `items` from the start. Return a tuple
    (index of the first match or -1, number of comparisons made).
    A comparison is one check of an item against the target.

    Example: linear_search([5, 8, 2], 8) returns (1, 2)
    """
    raise NotImplementedError


def binary_search(sorted_items, target):
    """`sorted_items` is sorted smallest first. Use binary search: look at
    the middle item, then keep only the half that could contain the target.
    Return (index of a match or -1, number of middle items examined).
    Must examine at most about log2(n) + 1 items.

    Example: binary_search([1, 3, 5, 7, 9], 7) returns (3, 2)
    """
    raise NotImplementedError


def common_elements(first, second):
    """Return a sorted list of the distinct values that appear in both lists.
    Must be O(n + m): no `in` checks against a list inside a loop.

    Example: common_elements([3, 1, 2, 2], [2, 3, 4]) returns [2, 3]
    """
    raise NotImplementedError


def two_sum(numbers, target):
    """Return a tuple (i, j) with i < j such that numbers[i] + numbers[j]
    equals target, choosing the pair whose j is as small as possible.
    Return None if there is no such pair. Must be O(n): use a dictionary
    that remembers the index of each value seen so far.

    Example: two_sum([2, 7, 11, 15], 9) returns (0, 1)
    """
    raise NotImplementedError
