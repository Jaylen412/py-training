"""Solutions for 05-03 Dictionaries."""


def word_counts(text):
    """Return a dictionary of lower-cased word counts."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def most_common_word(text):
    """Return the most common word, or None for an empty text."""
    counts = word_counts(text)
    best_word = None
    best_count = 0
    # Dictionaries keep insertion order, so on a tie (count == best_count)
    # the word seen first in the text is kept.
    for word, count in counts.items():
        if count > best_count:
            best_word = word
            best_count = count
    return best_word


def invert(mapping):
    """Return a dictionary with keys and values swapped."""
    inverted = {}
    for key, value in mapping.items():
        inverted[value] = key
    return inverted


def merge_inventory(first, second):
    """Return a new dictionary with quantities from both added together."""
    merged = {}
    for item, quantity in first.items():
        merged[item] = merged.get(item, 0) + quantity
    for item, quantity in second.items():
        merged[item] = merged.get(item, 0) + quantity
    return merged


def price_of_basket(prices, basket):
    """Return the total price of the items in `basket`."""
    total = 0
    for item in basket:
        total += prices.get(item, 0)
    return total
