"""Exercises for 07-02 Debugging.

Each docstring shows a BUGGY version of the function. Copy it into a
scratch file, find the bug, then write a correct version here.
"""


def average(numbers):
    """Return the mean of `numbers`, or 0.0 for an empty list.

    Buggy version:
        total = 0
        for index in range(1, len(numbers)):
            total += numbers[index]
        return total / len(numbers)

    Example: average([10, 20, 30]) returns 20.0
    """
    raise NotImplementedError


def find_max(numbers):
    """Return the largest number in a non-empty list.

    Buggy version:
        largest = 0
        for number in numbers:
            if number > largest:
                largest = number
        return largest

    Example: find_max([-5, -2, -9]) returns -2
    """
    raise NotImplementedError


def count_words(text):
    """Return the number of words in `text`, however many spaces
    separate them.

    Buggy version:
        return len(text.split(" "))

    Example: count_words("  the  quick fox ") returns 3
    """
    raise NotImplementedError


def is_sorted(items):
    """Return True if `items` is in ascending order (equal neighbours are
    allowed). Empty and one-item lists count as sorted.

    Buggy version:
        for index in range(len(items)):
            if items[index] > items[index + 1]:
                return False
        return True

    Example: is_sorted([1, 2, 2, 5]) returns True
    """
    raise NotImplementedError


def capitalise_words(words):
    """Return a NEW list with every word in title case.

    Buggy version:
        for word in words:
            word = word.title()
        return words

    Example: capitalise_words(["ada", "LOVELACE"]) returns ["Ada", "Lovelace"]
    """
    raise NotImplementedError
