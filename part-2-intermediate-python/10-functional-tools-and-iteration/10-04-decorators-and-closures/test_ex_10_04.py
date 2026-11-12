import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_10_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_10_04"
)


def test_make_power():
    cube = mod.make_power(3)
    assert cube(2) == 8
    assert mod.make_power(2)(5) == 25


def test_make_power_independent():
    square = mod.make_power(2)
    identity = mod.make_power(1)
    assert (square(7), identity(7)) == (49, 7)


def test_make_accumulator():
    add = mod.make_accumulator(10)
    assert add(5) == 15
    assert add(5) == 20


def test_make_accumulators_are_independent():
    first = mod.make_accumulator()
    second = mod.make_accumulator()
    first(100)
    assert second(1) == 1


def test_count_calls():
    @mod.count_calls
    def greet(name):
        """Say hello."""
        return f"Hello, {name}"

    assert greet.calls == 0
    assert greet("Ada") == "Hello, Ada"
    greet("Alan")
    assert greet.calls == 2


def test_count_calls_keeps_metadata():
    @mod.count_calls
    def greet():
        """Say hello."""

    assert greet.__name__ == "greet"
    assert greet.__doc__ == "Say hello."


def test_validate_non_negative():
    @mod.validate_non_negative
    def square_root(number):
        return number ** 0.5

    assert square_root(16) == pytest.approx(4.0)
    assert square_root(0) == 0
    with pytest.raises(ValueError):
        square_root(-4)
    assert square_root.__name__ == "square_root"


def test_validate_non_negative_checks_every_argument():
    @mod.validate_non_negative
    def add(first, second):
        return first + second

    with pytest.raises(ValueError):
        add(1, -2)


def test_memoize_returns_results():
    @mod.memoize
    def add(first, second):
        return first + second

    assert add(2, 3) == 5
    assert add(2, 3) == 5
    assert add(3, 2) == 5
    assert add.__name__ == "add"


def test_memoize_calls_original_once_per_arguments():
    calls = []

    @mod.memoize
    def slow_square(number):
        calls.append(number)
        return number * number

    slow_square(4)
    slow_square(4)
    slow_square(5)
    assert calls == [4, 5]
