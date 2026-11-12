"""Solutions for 08-03 Standard library tour."""
import itertools
import random
from collections import Counter, defaultdict
from datetime import date


def days_between(start, end):
    """Return the number of days from `start` to `end`."""
    return (date.fromisoformat(end) - date.fromisoformat(start)).days


def weekday_name(date_text):
    """Return the weekday name for a date."""
    return date.fromisoformat(date_text).strftime("%A")


def top_words(text, count):
    """Return the most common lower-cased words."""
    return Counter(text.lower().split()).most_common(count)


def group_by_length(words):
    """Group words by their length."""
    groups = defaultdict(list)
    for word in words:
        groups[len(word)].append(word)
    return dict(groups)


def all_pairs(items):
    """Return every unordered pair of items."""
    return list(itertools.combinations(items, 2))


def roll_dice(rolls, seed):
    """Return repeatable dice rolls."""
    rng = random.Random(seed)
    return [rng.randint(1, 6) for _ in range(rolls)]
