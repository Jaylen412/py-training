import importlib
import os

mod = importlib.import_module(
    "sol_03_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_03_03"
)


def test_countdown_text():
    assert mod.countdown_text(3) == "3 2 1 Go!"


def test_countdown_text_one():
    assert mod.countdown_text(1) == "1 Go!"


def test_countdown_text_zero():
    assert mod.countdown_text(0) == "Go!"


def test_sum_of_digits():
    assert mod.sum_of_digits(2026) == 10
    assert mod.sum_of_digits(999) == 27


def test_sum_of_digits_single_and_zero():
    assert mod.sum_of_digits(7) == 7
    assert mod.sum_of_digits(0) == 0


def test_count_halvings():
    assert mod.count_halvings(10) == 4
    assert mod.count_halvings(1) == 1


def test_count_halvings_below_one():
    assert mod.count_halvings(0.5) == 0


def test_first_power_of_two_over():
    assert mod.first_power_of_two_over(100) == 128
    assert mod.first_power_of_two_over(5) == 8


def test_first_power_of_two_over_exact_power():
    # 64 is not strictly greater than 64.
    assert mod.first_power_of_two_over(64) == 128


def test_first_power_of_two_over_zero():
    assert mod.first_power_of_two_over(0) == 1


def test_collatz_steps():
    assert mod.collatz_steps(6) == 8
    assert mod.collatz_steps(27) == 111


def test_collatz_steps_already_one():
    assert mod.collatz_steps(1) == 0
