import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_04_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_04_01"
)


def test_square():
    assert mod.square(7) == 49
    assert mod.square(-3) == 9


def test_square_zero_and_float():
    assert mod.square(0) == 0
    assert mod.square(1.5) == pytest.approx(2.25)


def test_make_greeting():
    assert mod.make_greeting("Ada") == "Hello, Ada!"


def test_make_greeting_returns_not_prints(capsys):
    result = mod.make_greeting("Grace")
    assert result == "Hello, Grace!"
    assert capsys.readouterr().out == ""


def test_is_even():
    assert mod.is_even(10) is True
    assert mod.is_even(7) is False


def test_is_even_zero_and_negative():
    assert mod.is_even(0) is True
    assert mod.is_even(-4) is True
    assert mod.is_even(-3) is False


def test_bmi():
    assert mod.bmi(70, 1.75) == 22.9


def test_bmi_rounds_to_one_place():
    assert mod.bmi(80, 1.8) == 24.7


def test_format_duration():
    assert mod.format_duration(3723) == "1h 2m 3s"


def test_format_duration_zero():
    assert mod.format_duration(0) == "0h 0m 0s"


def test_format_duration_exact_hours():
    assert mod.format_duration(7200) == "2h 0m 0s"
    assert mod.format_duration(59) == "0h 0m 59s"
