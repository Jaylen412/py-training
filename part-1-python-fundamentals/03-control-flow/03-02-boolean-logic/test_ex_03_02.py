import importlib
import os

mod = importlib.import_module(
    "sol_03_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_03_02"
)


def test_is_leap_year_ordinary():
    assert mod.is_leap_year(2024) is True
    assert mod.is_leap_year(2023) is False


def test_is_leap_year_centuries():
    assert mod.is_leap_year(1900) is False
    assert mod.is_leap_year(2000) is True


def test_can_ride_tall_enough():
    assert mod.can_ride(120, 5) is True


def test_can_ride_older_and_nearly_tall_enough():
    assert mod.can_ride(115, 12) is True
    assert mod.can_ride(110, 10) is True


def test_can_ride_refused():
    assert mod.can_ride(115, 9) is False
    assert mod.can_ride(109, 30) is False


def test_is_weekend():
    assert mod.is_weekend("Saturday") is True
    assert mod.is_weekend("sunday") is True


def test_is_weekend_weekday():
    assert mod.is_weekend("Monday") is False
    assert mod.is_weekend("SUNDAYS") is False


def test_in_range_inside():
    assert mod.in_range(5, 1, 10) is True


def test_in_range_edges_and_outside():
    assert mod.in_range(1, 1, 10) is True
    assert mod.in_range(10, 1, 10) is True
    assert mod.in_range(0, 1, 10) is False
    assert mod.in_range(11, 1, 10) is False


def test_is_valid_username_good():
    assert mod.is_valid_username("ada_l") is True
    assert mod.is_valid_username("abc") is True


def test_is_valid_username_bad():
    assert mod.is_valid_username("ab") is False
    assert mod.is_valid_username("a_very_long_name") is False
    assert mod.is_valid_username("ada l") is False
    assert mod.is_valid_username("1ada") is False


def test_is_valid_username_empty():
    assert mod.is_valid_username("") is False
