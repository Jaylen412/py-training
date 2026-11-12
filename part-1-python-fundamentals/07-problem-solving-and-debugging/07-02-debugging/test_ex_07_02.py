import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_07_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_07_02"
)


def test_average():
    assert mod.average([10, 20, 30]) == pytest.approx(20.0)


def test_average_empty_and_single():
    assert mod.average([]) == 0.0
    assert mod.average([7]) == pytest.approx(7.0)


def test_find_max():
    assert mod.find_max([3, 9, 4]) == 9


def test_find_max_all_negative():
    assert mod.find_max([-5, -2, -9]) == -2


def test_count_words():
    assert mod.count_words("the quick fox") == 3


def test_count_words_extra_spaces_and_empty():
    assert mod.count_words("  the  quick fox ") == 3
    assert mod.count_words("") == 0


def test_is_sorted():
    assert mod.is_sorted([1, 2, 2, 5]) is True
    assert mod.is_sorted([1, 3, 2]) is False


def test_is_sorted_short_lists():
    assert mod.is_sorted([]) is True
    assert mod.is_sorted([4]) is True


def test_capitalise_words():
    assert mod.capitalise_words(["ada", "LOVELACE"]) == ["Ada", "Lovelace"]


def test_capitalise_words_returns_new_list():
    original = ["ada"]
    result = mod.capitalise_words(original)
    assert original == ["ada"]
    assert result == ["Ada"]
    assert mod.capitalise_words([]) == []
