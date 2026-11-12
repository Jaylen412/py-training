import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_05_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_05"
)

PRODUCTS = [
    {"name": "Pen", "price": 1.50, "quantity": 10},
    {"name": "Notebook", "price": 3.25, "quantity": 4},
    {"name": "Stapler", "price": 7.00, "quantity": 1},
]


def test_total_value():
    assert mod.total_value(PRODUCTS) == pytest.approx(35.0)


def test_total_value_empty():
    assert mod.total_value([]) == 0


def test_cheapest_product():
    assert mod.cheapest_product(PRODUCTS) == "Pen"


def test_cheapest_product_tie_and_empty():
    tied = [{"name": "A", "price": 2, "quantity": 1}, {"name": "B", "price": 2, "quantity": 1}]
    assert mod.cheapest_product(tied) == "A"
    assert mod.cheapest_product([]) is None


def test_names_by_city():
    people = [("Ada", "London"), ("Alan", "Leeds"), ("Grace", "London")]
    assert mod.names_by_city(people) == {"London": ["Ada", "Grace"], "Leeds": ["Alan"]}


def test_names_by_city_empty():
    assert mod.names_by_city([]) == {}


def test_doubled():
    assert mod.doubled([1, 2, 3]) == [2, 4, 6]


def test_doubled_leaves_original_alone():
    original = [1, 2, 3]
    result = mod.doubled(original)
    assert original == [1, 2, 3]
    assert result is not original


def test_copy_grid_equal():
    assert mod.copy_grid([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]


def test_copy_grid_is_independent():
    original = [[1, 2], [3, 4]]
    copied = mod.copy_grid(original)
    copied[0][0] = 99
    copied.append([5])
    assert original == [[1, 2], [3, 4]]


def test_copy_grid_empty():
    assert mod.copy_grid([]) == []
