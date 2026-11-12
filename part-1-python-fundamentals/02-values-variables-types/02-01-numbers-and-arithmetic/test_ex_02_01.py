import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_02_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_02_01"
)


def test_total_cost():
    assert mod.total_cost(2.5, 4) == pytest.approx(10.0)


def test_total_cost_zero_quantity():
    assert mod.total_cost(9.99, 0) == 0


def test_whole_hours():
    assert mod.whole_hours(135) == 2


def test_whole_hours_less_than_an_hour():
    assert mod.whole_hours(59) == 0


def test_whole_hours_exact():
    assert mod.whole_hours(120) == 2


def test_leftover_minutes():
    assert mod.leftover_minutes(135) == 15


def test_leftover_minutes_exact_hours():
    assert mod.leftover_minutes(180) == 0


def test_average_of_three():
    assert mod.average_of_three(1, 2, 6) == pytest.approx(3.0)


def test_average_of_three_not_whole():
    assert mod.average_of_three(1, 2, 2) == pytest.approx(5 / 3)


def test_average_of_three_negative():
    assert mod.average_of_three(-3, 0, 3) == pytest.approx(0.0)


def test_celsius_to_fahrenheit_boiling():
    assert mod.celsius_to_fahrenheit(100) == pytest.approx(212.0)


def test_celsius_to_fahrenheit_freezing():
    assert mod.celsius_to_fahrenheit(0) == pytest.approx(32.0)


def test_celsius_to_fahrenheit_minus_forty():
    # -40 is the same in both scales.
    assert mod.celsius_to_fahrenheit(-40) == pytest.approx(-40.0)


def test_compound_growth():
    assert mod.compound_growth(100, 0.1, 2) == pytest.approx(121.0)


def test_compound_growth_zero_years():
    assert mod.compound_growth(500, 0.05, 0) == pytest.approx(500.0)
