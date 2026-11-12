import importlib
import os

mod = importlib.import_module(
    "sol_04_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_04_04"
)


def test_has_uppercase():
    assert mod.has_uppercase("hello World") is True
    assert mod.has_uppercase("hello world") is False


def test_has_uppercase_empty_and_digits():
    assert mod.has_uppercase("") is False
    assert mod.has_uppercase("123") is False


def test_has_digit():
    assert mod.has_digit("abc123") is True
    assert mod.has_digit("abc") is False


def test_has_digit_empty():
    assert mod.has_digit("") is False


def test_is_long_enough_default():
    assert mod.is_long_enough("abcdefgh") is True
    assert mod.is_long_enough("abcdefg") is False


def test_is_long_enough_custom_minimum():
    assert mod.is_long_enough("abc", minimum=3) is True
    assert mod.is_long_enough("", minimum=0) is True


def test_password_strength_strong():
    assert mod.password_strength("Secret123") == "strong"


def test_password_strength_medium():
    assert mod.password_strength("secret123") == "medium"   # no capital
    assert mod.password_strength("Secret12") == "strong"    # exactly 8
    assert mod.password_strength("Secr1") == "medium"       # too short


def test_password_strength_weak():
    assert mod.password_strength("secret") == "weak"
    assert mod.password_strength("") == "weak"
