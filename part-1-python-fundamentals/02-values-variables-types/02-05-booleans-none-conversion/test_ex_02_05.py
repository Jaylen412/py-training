import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_02_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_02_05"
)


def test_is_adult_exactly_eighteen():
    assert mod.is_adult(18) is True


def test_is_adult_under():
    assert mod.is_adult(17) is False


def test_is_adult_over():
    assert mod.is_adult(65) is True


def test_parse_price():
    assert mod.parse_price(" 12.50 ") == pytest.approx(12.5)


def test_parse_price_whole_number():
    result = mod.parse_price("3")
    assert result == pytest.approx(3.0)
    assert type(result) is float


def test_add_text_numbers():
    assert mod.add_text_numbers("3", "4") == 7


def test_add_text_numbers_negative():
    assert mod.add_text_numbers("-10", "4") == -6


def test_matches_number():
    assert mod.matches_number("42", 42) is True


def test_matches_number_different():
    assert mod.matches_number("42", 24) is False


def test_is_missing_none():
    assert mod.is_missing(None) is True


def test_is_missing_zero_is_not_missing():
    assert mod.is_missing(0) is False


def test_is_missing_empty_string_is_not_missing():
    assert mod.is_missing("") is False


def test_is_blank_spaces():
    assert mod.is_blank("   ") is True


def test_is_blank_empty():
    assert mod.is_blank("") is True


def test_is_blank_text():
    assert mod.is_blank("  hi  ") is False
