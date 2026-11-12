import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_12_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_12_01"
)


def fake_clock(*readings):
    """Return a clock function that gives these readings in turn."""
    values = iter(readings)
    return lambda: next(values)


def test_time_call_with_fake_clock():
    result, seconds = mod.time_call(sum, [1, 2, 3], clock=fake_clock(10.0, 10.25))
    assert result == 6
    assert seconds == pytest.approx(0.25)


def test_time_call_with_real_clock():
    result, seconds = mod.time_call(max, 4, 9)
    assert result == 9
    assert 0 <= seconds < 1


def test_best_time_returns_minimum():
    # Three runs taking 0.5, 0.2 and 0.3 seconds.
    clock = fake_clock(0.0, 0.5, 1.0, 1.2, 2.0, 2.3)
    assert mod.best_time(lambda: None, 3, clock=clock) == pytest.approx(0.2)


def test_best_time_calls_function_each_time():
    calls = []
    mod.best_time(lambda: calls.append(1), 4)
    assert len(calls) == 4


def test_best_time_needs_a_repeat():
    with pytest.raises(ValueError):
        mod.best_time(lambda: None, 0)


def test_slowest_step():
    assert mod.slowest_step({"load": 0.5, "clean": 2.0, "save": 0.1}) == "clean"


def test_slowest_step_empty():
    assert mod.slowest_step({}) is None


@pytest.mark.parametrize(
    "seconds, expected",
    [(2.5, "2.5 s"), (1, "1.0 s"), (0.0123, "12.3 ms"), (0.001, "1.0 ms"), (0.0000456, "45.6 us"), (0, "0.0 us")],
)
def test_format_duration(seconds, expected):
    assert mod.format_duration(seconds) == expected
