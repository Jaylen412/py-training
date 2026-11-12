"""Exercises for 04-04 Functions as building blocks.

Build a password strength checker from small, pure helper functions.
"""


def has_uppercase(text: str) -> bool:
    """Return True if `text` contains at least one upper-case letter.
    Hint: a character is upper case if character.isupper() is True.

    Example: has_uppercase("hello World") returns True
    """
    raise NotImplementedError


def has_digit(text: str) -> bool:
    """Return True if `text` contains at least one digit.

    Example: has_digit("abc123") returns True
    """
    raise NotImplementedError


def is_long_enough(text: str, minimum: int = 8) -> bool:
    """Return True if `text` has at least `minimum` characters.

    Example: is_long_enough("abcdefgh") returns True
    """
    raise NotImplementedError


def password_strength(password: str) -> str:
    """Count how many of the three checks pass (has_uppercase, has_digit,
    is_long_enough with the default minimum) and return:
    "strong" if all 3 pass, "medium" if 2 pass, otherwise "weak".
    Call your helper functions - do not repeat their code here.

    Example: password_strength("Secret123") returns "strong"
    """
    raise NotImplementedError
