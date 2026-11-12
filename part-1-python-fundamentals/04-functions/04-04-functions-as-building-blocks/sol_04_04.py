"""Solutions for 04-04 Functions as building blocks."""


def has_uppercase(text: str) -> bool:
    """Return True if `text` contains at least one upper-case letter."""
    for character in text:
        if character.isupper():
            return True
    return False


def has_digit(text: str) -> bool:
    """Return True if `text` contains at least one digit."""
    for character in text:
        if character.isdigit():
            return True
    return False


def is_long_enough(text: str, minimum: int = 8) -> bool:
    """Return True if `text` has at least `minimum` characters."""
    return len(text) >= minimum


def password_strength(password: str) -> str:
    """Return "strong", "medium" or "weak"."""
    # True counts as 1 and False as 0, so adding booleans counts the passes.
    checks_passed = (
        has_uppercase(password) + has_digit(password) + is_long_enough(password)
    )
    if checks_passed == 3:
        return "strong"
    if checks_passed == 2:
        return "medium"
    return "weak"
