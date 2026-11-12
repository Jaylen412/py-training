import importlib
import os

mod = importlib.import_module(
    "sol_04_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_04_05"
)


def test_clamp_inside_range():
    assert mod.clamp(5, 0, 10) == 5


def test_clamp_below_range():
    assert mod.clamp(-3, 0, 10) == 0


def test_clamp_above_range():
    assert mod.clamp(42, 0, 10) == 10


def test_clamp_on_the_edges():
    assert mod.clamp(0, 0, 10) == 0
    assert mod.clamp(10, 0, 10) == 10


def test_clamp_floats():
    assert mod.clamp(0.5, 0.0, 1.0) == 0.5
    assert mod.clamp(1.5, 0.0, 1.0) == 1.0


def test_is_palindrome_simple():
    assert mod.is_palindrome("racecar") is True
    assert mod.is_palindrome("python") is False


def test_is_palindrome_ignores_case_and_spaces():
    assert mod.is_palindrome("Never odd or even") is True


def test_is_palindrome_edge_cases():
    assert mod.is_palindrome("") is True
    assert mod.is_palindrome("a") is True
    assert mod.is_palindrome("ab") is False


def test_median_of_three_each_position():
    assert mod.median_of_three(5, 2, 9) == 5
    assert mod.median_of_three(2, 5, 9) == 5
    assert mod.median_of_three(9, 2, 5) == 5


def test_median_of_three_ties():
    assert mod.median_of_three(4, 4, 1) == 4
    assert mod.median_of_three(7, 7, 7) == 7
    assert mod.median_of_three(1, 3, 3) == 3


def test_median_of_three_negative():
    assert mod.median_of_three(-1, -5, -3) == -3
