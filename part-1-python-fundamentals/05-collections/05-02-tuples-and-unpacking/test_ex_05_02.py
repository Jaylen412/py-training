import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_05_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_02"
)


def test_min_max():
    assert mod.min_max([7, 2, 9, 4]) == (2, 9)


def test_min_max_single_item():
    assert mod.min_max([5]) == (5, 5)


def test_min_max_returns_tuple():
    assert type(mod.min_max([1, 2])) is tuple


def test_swap_pair():
    assert mod.swap_pair(("a", "b")) == ("b", "a")


def test_swap_pair_same_values():
    assert mod.swap_pair((1, 1)) == (1, 1)


def test_split_name():
    assert mod.split_name("Ada Lovelace") == ("Ada", "Lovelace")


def test_split_name_returns_tuple():
    assert type(mod.split_name("Alan Turing")) is tuple


def test_pair_up():
    assert mod.pair_up(["Ada", "Alan"], [95, 72]) == [("Ada", 95), ("Alan", 72)]


def test_pair_up_uneven_and_empty():
    assert mod.pair_up(["Ada", "Alan", "Grace"], [95]) == [("Ada", 95)]
    assert mod.pair_up([], []) == []


def test_distance():
    assert mod.distance((0, 0), (3, 4)) == pytest.approx(5.0)


def test_distance_same_point_and_negative():
    assert mod.distance((2, 2), (2, 2)) == pytest.approx(0.0)
    assert mod.distance((-1, -1), (2, 3)) == pytest.approx(5.0)
