"""Solutions for 05-01 Lists."""


def average(numbers):
    """Return the mean of `numbers`, or 0.0 if the list is empty."""
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)


def remove_all(items, target):
    """Return a new list with every `target` removed."""
    kept = []
    for item in items:
        if item != target:
            kept.append(item)
    return kept


def top_three(scores):
    """Return the three largest scores, largest first."""
    # Slicing past the end is safe, so short lists just come back whole.
    return sorted(scores, reverse=True)[:3]


def rotate_left(items, steps):
    """Return a new list with the first `steps` items moved to the end."""
    return items[steps:] + items[:steps]


def running_totals(numbers):
    """Return the cumulative sums of `numbers`."""
    totals = []
    total = 0
    for number in numbers:
        total += number
        totals.append(total)
    return totals


def insert_sorted(sorted_items, value):
    """Return a new sorted list with `value` inserted."""
    result = sorted_items[:]      # a slice is a new list, so the caller's is untouched
    position = len(result)        # default: goes at the end
    for index, item in enumerate(result):
        if item > value:
            position = index
            break
    result.insert(position, value)
    return result
