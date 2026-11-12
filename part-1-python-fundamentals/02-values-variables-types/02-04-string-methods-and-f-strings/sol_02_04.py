"""Solutions for 02-04 String methods and f-strings."""


def clean_name(raw_name):
    """Remove spaces from both ends and put the name in title case."""
    return raw_name.strip().title()


def count_words(sentence):
    """Return the number of words in `sentence`."""
    # split() with no argument ignores runs of whitespace, so no empty words.
    return len(sentence.split())


def slugify(title):
    """Turn a title into a lower-case, hyphen-separated slug."""
    return title.strip().lower().replace(" ", "-")


def format_price(amount):
    """Return `amount` as a price such as $1,234.50."""
    return f"${amount:,.2f}"


def format_percentage(fraction):
    """Return `fraction` as a percentage with one decimal place."""
    return f"{fraction:.1%}"


def is_mentioned(text, word):
    """Return True if `word` appears in `text`, ignoring case."""
    # Lower-case both sides so that "Python" and "python" match.
    return word.lower() in text.lower()
