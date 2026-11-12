"""Solutions for 10-01 Functions as values."""


def apply_twice(function, value):
    """Return function(function(value))."""
    return function(function(value))


def sort_by_length(words):
    """Sort by length, then alphabetically."""
    return sorted(words, key=lambda word: (len(word), word))


def sort_people(people):
    """Sort oldest first, then by name."""
    # Negating the age sorts it largest first while names still sort A to Z.
    return sorted(people, key=lambda person: (-person["age"], person["name"]))


def longest_by(items, key):
    """Return the item with the largest key value, or None."""
    if not items:
        return None
    return max(items, key=key)


def count_matching(items, test):
    """Return how many items pass the test."""
    return len([item for item in items if test(item)])
