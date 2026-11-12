import importlib
import os

mod = importlib.import_module(
    "sol_05_06" if os.environ.get("COURSE_SOLUTIONS") else "ex_05_06"
)


def test_squares_of_evens():
    assert mod.squares_of_evens([1, 2, 3, 4]) == [4, 16]


def test_squares_of_evens_none_and_negative():
    assert mod.squares_of_evens([1, 3]) == []
    assert mod.squares_of_evens([-2, 0]) == [4, 0]


def test_clean_words():
    assert mod.clean_words([" Apple", "", "  ", "BANANA "]) == ["apple", "banana"]


def test_clean_words_empty_list():
    assert mod.clean_words([]) == []


def test_word_lengths():
    assert mod.word_lengths(["hi", "hello"]) == {"hi": 2, "hello": 5}


def test_word_lengths_repeated_word():
    assert mod.word_lengths(["a", "a"]) == {"a": 1}


def test_initials_set():
    assert mod.initials_set(["ada", "Alan", "grace"]) == {"A", "G"}


def test_initials_set_empty():
    assert mod.initials_set([]) == set()


def test_flatten():
    assert mod.flatten([[1, 2], [3], []]) == [1, 2, 3]


def test_flatten_empty():
    assert mod.flatten([]) == []


def test_apply_discount():
    assert mod.apply_discount({"tv": 500, "pen": 2}, 100, 0.1) == {"tv": 450.0, "pen": 2}


def test_apply_discount_threshold_is_exclusive():
    assert mod.apply_discount({"a": 100}, 100, 0.5) == {"a": 100}


def test_apply_discount_does_not_change_input():
    prices = {"tv": 500}
    mod.apply_discount(prices, 100, 0.1)
    assert prices == {"tv": 500}
