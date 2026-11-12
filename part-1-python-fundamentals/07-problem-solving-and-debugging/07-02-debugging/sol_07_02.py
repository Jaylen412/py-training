"""Solutions for 07-02 Debugging."""


def average(numbers):
    """Return the mean of `numbers`, or 0.0 for an empty list."""
    # Bugs: range started at 1 (skipping the first number), and an empty
    # list caused ZeroDivisionError.
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """Return the largest number in a non-empty list."""
    # Bug: starting at 0 beats every negative number. Start from the first item.
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def count_words(text):
    """Return the number of words in `text`."""
    # Bug: split(" ") makes empty strings between repeated spaces.
    return len(text.split())


def is_sorted(items):
    """Return True if `items` is in ascending order."""
    # Bug: the last index has no index + 1. Stop one short of the end.
    for index in range(len(items) - 1):
        if items[index] > items[index + 1]:
            return False
    return True


def capitalise_words(words):
    """Return a new list with every word in title case."""
    # Bug: reassigning the loop variable does not change the list.
    return [word.title() for word in words]
