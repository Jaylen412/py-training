"""Solutions for 05-04 Sets."""

ALPHABET = set("abcdefghijklmnopqrstuvwxyz")


def unique_count(items):
    """Return how many different values are in `items`."""
    return len(set(items))


def has_duplicates(items):
    """Return True if any value appears more than once."""
    # Duplicates disappear in the set, so it ends up shorter than the list.
    return len(set(items)) < len(items)


def common_items(first, second):
    """Return a sorted list of values in both lists."""
    return sorted(set(first) & set(second))


def only_in_first(first, second):
    """Return a sorted list of values in `first` but not `second`."""
    return sorted(set(first) - set(second))


def missing_fields(record, required):
    """Return a sorted list of required fields missing from `record`."""
    return sorted(set(required) - set(record))


def is_pangram(sentence):
    """Return True if `sentence` uses every letter a to z."""
    return ALPHABET <= set(sentence.lower())
