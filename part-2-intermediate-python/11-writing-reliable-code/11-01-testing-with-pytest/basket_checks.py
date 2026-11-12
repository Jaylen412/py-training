"""Tests for basket.py, run by examples.py.

In a real project this file would be called test_basket.py so that pytest
finds it automatically. It has a different name here so that the course's
own test run does not pick it up.
"""
import pytest

from basket import Basket


# A fixture: pytest calls this and passes the result to any test that
# names `basket` as a parameter. Each test gets a fresh basket.
@pytest.fixture
def basket():
    new_basket = Basket()
    new_basket.add("pen", 1.50, quantity=2)
    new_basket.add("pad", 4.00)
    return new_basket


def test_empty_basket_total_is_zero():
    assert Basket().total() == 0


def test_total(basket):
    assert basket.total() == 7.00


def test_adding_same_item_increases_quantity(basket):
    basket.add("pen", 1.50)
    assert basket.items["pen"] == (1.50, 3)


@pytest.mark.parametrize(
    "code, expected",
    [("SAVE10", 6.30), ("HALF", 3.50)],
)
def test_discount_codes(basket, code, expected):
    basket.apply_code(code)
    assert basket.total() == pytest.approx(expected)


def test_unknown_code_raises(basket):
    with pytest.raises(KeyError, match="unknown discount code"):
        basket.apply_code("FREE")


@pytest.mark.parametrize("price, quantity", [(-1, 1), (2.0, 0)])
def test_invalid_items_rejected(basket, price, quantity):
    with pytest.raises(ValueError):
        basket.add("bad", price, quantity)
