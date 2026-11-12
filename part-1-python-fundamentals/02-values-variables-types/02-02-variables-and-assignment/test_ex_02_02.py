import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_02_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_02_02"
)


def test_area_of_room():
    assert mod.area_of_room(4, 3.5) == pytest.approx(14.0)


def test_area_of_room_zero_width():
    assert mod.area_of_room(10, 0) == 0


def test_price_after_discount():
    assert mod.price_after_discount(80, 25) == pytest.approx(60.0)


def test_price_after_discount_no_discount():
    assert mod.price_after_discount(19.99, 0) == pytest.approx(19.99)


def test_price_after_discount_full_discount():
    assert mod.price_after_discount(50, 100) == pytest.approx(0.0)


def test_final_balance():
    assert mod.final_balance(100, 50, 30, 0.1) == pytest.approx(132.0)


def test_final_balance_no_interest():
    assert mod.final_balance(200, 0, 50, 0) == pytest.approx(150.0)


def test_final_balance_order_matters():
    # Interest is applied after the deposit, so it grows the deposit too.
    assert mod.final_balance(0, 100, 0, 0.5) == pytest.approx(150.0)


def test_seconds_in_days():
    assert mod.seconds_in_days(1) == 86400


def test_seconds_in_days_zero():
    assert mod.seconds_in_days(0) == 0


def test_seconds_in_a_week():
    assert mod.seconds_in_days(7) == 604800
