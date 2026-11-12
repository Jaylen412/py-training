"""Solutions for 05-06 Comprehensions."""


def squares_of_evens(numbers):
    """Return the squares of the even numbers."""
    return [number ** 2 for number in numbers if number % 2 == 0]


def clean_words(words):
    """Return stripped, lower-cased, non-empty words."""
    return [word.strip().lower() for word in words if word.strip()]


def word_lengths(words):
    """Return a dictionary mapping each word to its length."""
    return {word: len(word) for word in words}


def initials_set(names):
    """Return the set of upper-case first letters."""
    return {name[0].upper() for name in names}


def flatten(grid):
    """Turn a list of lists into a single list."""
    return [value for row in grid for value in row]


def apply_discount(prices, threshold, rate):
    """Return prices with a discount on items above `threshold`."""
    # The if/else is at the front: every item is kept, only its value changes.
    return {
        item: round(price * (1 - rate), 2) if price > threshold else price
        for item, price in prices.items()
    }
