"""Solutions for 11-02 Type hints."""


def mean(values: list[float]) -> float:
    """Return the average, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def word_lengths(words: list[str]) -> dict[str, int]:
    """Return each word mapped to its length."""
    return {word: len(word) for word in words}


def first_long_word(words: list[str], minimum: int) -> str | None:
    """Return the first word with at least `minimum` characters, or None."""
    for word in words:
        if len(word) >= minimum:
            return word
    return None


def split_pair(text: str, separator: str = ",") -> tuple[str, str]:
    """Split `text` at the first separator into two stripped parts."""
    if separator not in text:
        raise ValueError(f"{separator!r} not found in {text!r}")
    left, right = text.split(separator, 1)
    return left.strip(), right.strip()
