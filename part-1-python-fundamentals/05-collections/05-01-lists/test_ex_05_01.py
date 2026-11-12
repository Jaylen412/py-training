import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_05_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_01"
)


def test_average():
    assert mod.average([2, 4, 9]) == pytest.approx(5.0)


def test_average_empty():
    assert mod.average([]) == 0.0


def test_remove_all():
    assert mod.remove_all([1, 2, 1, 3], 1) == [2, 3]


def test_remove_all_does_not_change_input():
    original = [1, 2, 1]
    mod.remove_all(original, 1)
    assert original == [1, 2, 1]


def test_remove_all_missing_and_empty():
    assert mod.remove_all([4, 5], 9) == [4, 5]
    assert mod.remove_all([], 1) == []


def test_top_three():
    assert mod.top_three([50, 90, 70, 80]) == [90, 80, 70]


def test_top_three_short_list():
    assert mod.top_three([5, 9]) == [9, 5]
    assert mod.top_three([]) == []


def test_top_three_does_not_change_input():
    original = [3, 1, 2]
    mod.top_three(original)
    assert original == [3, 1, 2]


def test_rotate_left():
    assert mod.rotate_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]


def test_rotate_left_zero_and_full():
    assert mod.rotate_left([1, 2, 3], 0) == [1, 2, 3]
    assert mod.rotate_left([1, 2, 3], 3) == [1, 2, 3]


def test_running_totals():
    assert mod.running_totals([1, 2, 3, 4]) == [1, 3, 6, 10]


def test_running_totals_empty_and_negative():
    assert mod.running_totals([]) == []
    assert mod.running_totals([5, -5, 2]) == [5, 0, 2]


def test_insert_sorted_middle():
    assert mod.insert_sorted([1, 3, 5], 4) == [1, 3, 4, 5]


def test_insert_sorted_ends():
    assert mod.insert_sorted([1, 3, 5], 0) == [0, 1, 3, 5]
    assert mod.insert_sorted([1, 3, 5], 9) == [1, 3, 5, 9]
    assert mod.insert_sorted([], 7) == [7]


def test_insert_sorted_does_not_change_input():
    original = [1, 3, 5]
    mod.insert_sorted(original, 2)
    assert original == [1, 3, 5]
