"""Exercises for 08-03 Standard library tour.

Add the imports you need at the top of the file.
"""


def days_between(start, end):
    """`start` and `end` are dates written as "YYYY-MM-DD". Return the number
    of days from start to end (negative if end is earlier).

    Example: days_between("2026-11-11", "2026-12-25") returns 44
    """
    raise NotImplementedError


def weekday_name(date_text):
    """Return the English weekday name for a "YYYY-MM-DD" date.

    Example: weekday_name("2026-11-11") returns "Wednesday"
    """
    raise NotImplementedError


def top_words(text, count):
    """Return the `count` most common lower-cased words in `text` as a list of
    (word, number) tuples, most common first. Use collections.Counter.
    (Counter keeps first-seen order for ties.)

    Example: top_words("the cat and THE hat and the bat", 2)
    returns [("the", 3), ("and", 2)]
    """
    raise NotImplementedError


def group_by_length(words):
    """Return an ordinary dict mapping each word length to the list of words
    with that length, in their original order. Use collections.defaultdict.

    Example: group_by_length(["hi", "hey", "yo"]) returns {2: ["hi", "yo"], 3: ["hey"]}
    """
    raise NotImplementedError


def all_pairs(items):
    """Return a list of every pair (as a tuple) of different items, where order
    does not matter, using itertools.combinations.

    Example: all_pairs(["a", "b", "c"]) returns [("a", "b"), ("a", "c"), ("b", "c")]
    """
    raise NotImplementedError


def roll_dice(rolls, seed):
    """Return a list of `rolls` dice rolls (whole numbers from 1 to 6) from a
    random.Random generator created with `seed`. The same seed must always
    give the same list.

    Example: roll_dice(3, 42) returns [6, 1, 1]
    """
    raise NotImplementedError
