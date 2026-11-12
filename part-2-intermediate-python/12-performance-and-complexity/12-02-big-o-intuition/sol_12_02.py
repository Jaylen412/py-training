"""Solutions for 12-02 Big-O intuition."""


def linear_search(items, target):
    """Return (index or -1, comparisons)."""
    comparisons = 0
    for index, item in enumerate(items):
        comparisons += 1
        if item == target:
            return index, comparisons
    return -1, comparisons


def binary_search(sorted_items, target):
    """Return (index or -1, middle items examined)."""
    low, high = 0, len(sorted_items) - 1
    examined = 0
    while low <= high:
        middle = (low + high) // 2
        examined += 1
        if sorted_items[middle] == target:
            return middle, examined
        if sorted_items[middle] < target:
            low = middle + 1      # the target can only be in the right half
        else:
            high = middle - 1     # the target can only be in the left half
    return -1, examined


def common_elements(first, second):
    """Return the sorted distinct values in both lists."""
    return sorted(set(first) & set(second))


def two_sum(numbers, target):
    """Return the first pair of indices whose values add up to target."""
    seen = {}  # value -> index of its first appearance
    for index, number in enumerate(numbers):
        needed = target - number
        if needed in seen:
            return seen[needed], index
        if number not in seen:
            seen[number] = index
    return None
