import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_04_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_04_03"
)


def test_add_points():
    assert mod.add_points(10, 5) == 15


def test_add_points_independent_calls():
    # Same call, same answer: no hidden state carried between calls.
    assert mod.add_points(0, 1) == 1
    assert mod.add_points(0, 1) == 1


def test_price_with_tax_default():
    assert mod.price_with_tax(100) == pytest.approx(120.0)


def test_price_with_tax_custom_rate():
    assert mod.price_with_tax(100, tax_rate=0.05) == pytest.approx(105.0)
    assert mod.price_with_tax(100, tax_rate=0) == pytest.approx(100.0)


def test_count_long_words():
    assert mod.count_long_words("the quick brown fox", 5) == 2


def test_count_long_words_boundary_and_empty():
    assert mod.count_long_words("abc abcd", 4) == 1
    assert mod.count_long_words("", 1) == 0


def test_apply_transaction_withdrawal():
    assert mod.apply_transaction(100, 30, False) == 70


def test_apply_transaction_deposit():
    assert mod.apply_transaction(100, 30, True) == 130


def test_apply_transaction_can_go_negative():
    assert mod.apply_transaction(10, 30, False) == -20
