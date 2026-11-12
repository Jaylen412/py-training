import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_11_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_11_01"
)


@pytest.mark.parametrize(
    "text, expected",
    [("85", 85), (" 85 ", 85), ("0", 0), ("100", 100)],
)
def test_parse_score_valid(text, expected):
    assert mod.parse_score(text) == expected


@pytest.mark.parametrize("text", ["-1", "101", "85.5", "eighty", ""])
def test_parse_score_invalid(text):
    with pytest.raises(ValueError):
        mod.parse_score(text)


@pytest.fixture
def inventory():
    """An inventory holding 5 pens and 2 pads."""
    stock = mod.Inventory()
    stock.add("pen", 5)
    stock.add("pad", 2)
    return stock


def test_new_inventory_is_empty():
    assert mod.Inventory().quantity("pen") == 0


def test_quantity_after_adding(inventory):
    assert inventory.quantity("pen") == 5
    inventory.add("pen", 3)
    assert inventory.quantity("pen") == 8


def test_remove(inventory):
    inventory.remove("pen", 2)
    assert inventory.quantity("pen") == 3


def test_remove_everything(inventory):
    inventory.remove("pad", 2)
    assert inventory.quantity("pad") == 0


def test_remove_unknown_product(inventory):
    with pytest.raises(KeyError):
        inventory.remove("stapler", 1)


@pytest.mark.parametrize("amount", [0, -1, 6])
def test_remove_bad_amount(inventory, amount):
    with pytest.raises(ValueError):
        inventory.remove("pen", amount)
    assert inventory.quantity("pen") == 5


@pytest.mark.parametrize("amount", [0, -3])
def test_add_bad_amount(inventory, amount):
    with pytest.raises(ValueError):
        inventory.add("pen", amount)
