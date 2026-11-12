import importlib
import os

mod = importlib.import_module(
    "sol_03_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_03_04"
)


def test_sum_up_to():
    assert mod.sum_up_to(4) == 10
    assert mod.sum_up_to(100) == 5050


def test_sum_up_to_zero_and_one():
    assert mod.sum_up_to(0) == 0
    assert mod.sum_up_to(1) == 1


def test_factorial():
    assert mod.factorial(5) == 120
    assert mod.factorial(10) == 3628800


def test_factorial_zero_and_one():
    assert mod.factorial(0) == 1
    assert mod.factorial(1) == 1


def test_count_vowels():
    assert mod.count_vowels("Machine Learning") == 6


def test_count_vowels_upper_case():
    assert mod.count_vowels("AEIOU") == 5


def test_count_vowels_none():
    assert mod.count_vowels("rhythm") == 0
    assert mod.count_vowels("") == 0


def test_times_table_row():
    assert mod.times_table_row(3) == "3 6 9 12 15 18 21 24 27 30"


def test_times_table_row_no_trailing_space():
    row = mod.times_table_row(1)
    assert row == "1 2 3 4 5 6 7 8 9 10"


def test_times_table_row_zero():
    assert mod.times_table_row(0) == "0 0 0 0 0 0 0 0 0 0"


def test_triangle():
    assert mod.triangle(3) == "*\n**\n***\n"


def test_triangle_zero():
    assert mod.triangle(0) == ""


def test_sum_of_multiples():
    assert mod.sum_of_multiples(10) == 23
    assert mod.sum_of_multiples(1000) == 233168


def test_sum_of_multiples_counts_fifteen_once():
    # 15 is a multiple of both 3 and 5 but must be added only once.
    assert mod.sum_of_multiples(16) == 60


def test_sum_of_multiples_small_limit():
    assert mod.sum_of_multiples(3) == 0
