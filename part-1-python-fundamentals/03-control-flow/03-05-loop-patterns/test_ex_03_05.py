import importlib
import os

mod = importlib.import_module(
    "sol_03_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_03_05"
)


def test_count_char():
    assert mod.count_char("banana", "a") == 3


def test_count_char_case_sensitive():
    assert mod.count_char("Banana", "b") == 0


def test_count_char_empty_text():
    assert mod.count_char("", "a") == 0


def test_index_of():
    assert mod.index_of("hello", "l") == 2
    assert mod.index_of("hello", "h") == 0


def test_index_of_missing():
    assert mod.index_of("hello", "z") == -1
    assert mod.index_of("", "a") == -1


def test_largest_digit():
    assert mod.largest_digit("4719362") == 9


def test_largest_digit_single():
    assert mod.largest_digit("0") == 0


def test_largest_digit_first_is_largest():
    assert mod.largest_digit("91111") == 9


def test_is_prime_true():
    assert mod.is_prime(2) is True
    assert mod.is_prime(29) is True
    assert mod.is_prime(97) is True


def test_is_prime_false():
    assert mod.is_prime(27) is False
    assert mod.is_prime(100) is False


def test_is_prime_small_numbers():
    assert mod.is_prime(1) is False
    assert mod.is_prime(0) is False
    assert mod.is_prime(-7) is False


def test_all_digits():
    assert mod.all_digits("2026") is True


def test_all_digits_false():
    assert mod.all_digits("20a6") is False
    assert mod.all_digits("12 3") is False


def test_all_digits_empty():
    assert mod.all_digits("") is False


def test_last_index_of():
    assert mod.last_index_of("hello", "l") == 3
    assert mod.last_index_of("banana", "a") == 5


def test_last_index_of_missing():
    assert mod.last_index_of("hello", "z") == -1
