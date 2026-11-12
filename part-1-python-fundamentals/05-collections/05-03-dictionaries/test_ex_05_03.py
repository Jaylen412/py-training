import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_05_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_03"
)


def test_word_counts():
    assert mod.word_counts("The cat the hat") == {"the": 2, "cat": 1, "hat": 1}


def test_word_counts_empty():
    assert mod.word_counts("") == {}


def test_most_common_word():
    assert mod.most_common_word("a b b a b") == "b"


def test_most_common_word_tie_goes_to_first():
    assert mod.most_common_word("x y y x") == "x"


def test_most_common_word_empty():
    assert mod.most_common_word("") is None


def test_invert():
    assert mod.invert({"a": 1, "b": 2}) == {1: "a", 2: "b"}


def test_invert_empty():
    assert mod.invert({}) == {}


def test_merge_inventory():
    result = mod.merge_inventory({"apple": 3}, {"apple": 2, "pear": 1})
    assert result == {"apple": 5, "pear": 1}


def test_merge_inventory_does_not_change_arguments():
    first = {"apple": 3}
    second = {"apple": 2}
    mod.merge_inventory(first, second)
    assert first == {"apple": 3}
    assert second == {"apple": 2}


def test_merge_inventory_empty():
    assert mod.merge_inventory({}, {}) == {}
    assert mod.merge_inventory({"a": 1}, {}) == {"a": 1}


def test_price_of_basket():
    prices = {"apple": 0.5, "milk": 0.9}
    assert mod.price_of_basket(prices, ["apple", "apple", "milk"]) == pytest.approx(1.9)


def test_price_of_basket_unknown_and_empty():
    prices = {"apple": 0.5}
    assert mod.price_of_basket(prices, ["caviar"]) == 0
    assert mod.price_of_basket(prices, []) == 0
