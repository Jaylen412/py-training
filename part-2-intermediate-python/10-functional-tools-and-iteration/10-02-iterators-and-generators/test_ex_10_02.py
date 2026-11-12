import importlib
import inspect
import itertools
import os

import pytest

mod = importlib.import_module(
    "sol_10_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_10_02"
)


def test_countdown():
    assert list(mod.countdown(3)) == [3, 2, 1]


def test_countdown_is_a_generator_and_handles_zero():
    assert inspect.isgeneratorfunction(mod.countdown)
    assert list(mod.countdown(0)) == []


def test_parse_numbers():
    assert list(mod.parse_numbers(["1", "", "# note", " 2.5 "])) == [1.0, 2.5]


def test_parse_numbers_is_lazy():
    # A bad line further on must not cause an error until it is reached.
    numbers = mod.parse_numbers(["1", "oops"])
    assert next(numbers) == 1.0
    with pytest.raises(ValueError):
        next(numbers)


def test_chunked():
    assert list(mod.chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_chunked_exact_and_empty():
    assert list(mod.chunked([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]
    assert list(mod.chunked([], 3)) == []


def test_chunked_bad_size():
    with pytest.raises(ValueError):
        list(mod.chunked([1, 2], 0))


def test_running_average():
    assert list(mod.running_average([2, 4, 9])) == pytest.approx([2.0, 3.0, 5.0])


def test_running_average_empty_and_generator_input():
    assert list(mod.running_average([])) == []
    assert list(mod.running_average(n for n in [10, 20])) == pytest.approx([10.0, 15.0])


def test_take():
    assert mod.take([1, 2, 3, 4], 2) == [1, 2]


def test_take_endless_generator():
    assert mod.take(itertools.count(5), 3) == [5, 6, 7]


def test_take_more_than_available():
    assert mod.take("ab", 5) == ["a", "b"]
    assert mod.take([], 0) == []
