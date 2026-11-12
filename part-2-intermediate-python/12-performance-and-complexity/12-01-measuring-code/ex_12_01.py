"""Exercises for 12-01 Measuring code.

The timing functions take a `clock` argument. Call clock() wherever you
would call time.perf_counter(); the tests pass in a fake clock.
"""
import time


def time_call(function, *args, clock=time.perf_counter):
    """Call function(*args) and return a tuple (result, seconds taken),
    reading clock() once before and once after the call.

    Example: time_call(sum, [1, 2, 3]) returns (6, <a small number>)
    """
    raise NotImplementedError


def best_time(function, repeats, clock=time.perf_counter):
    """Call function() `repeats` times, timing each call with clock()
    before and after, and return the shortest time.
    Raise ValueError if repeats < 1.
    """
    raise NotImplementedError


def slowest_step(timings):
    """`timings` maps step names to seconds. Return the name of the slowest
    step, or None if the dictionary is empty.

    Example: slowest_step({"load": 0.5, "clean": 2.0}) returns "clean"
    """
    raise NotImplementedError


def format_duration(seconds):
    """Return the duration with 1 decimal place in the most suitable unit:
    "s" for 1 second or more, "ms" for 0.001 seconds or more, else "us".

    Examples: format_duration(2.5) returns "2.5 s"
              format_duration(0.0123) returns "12.3 ms"
              format_duration(0.0000456) returns "45.6 us"
    """
    raise NotImplementedError
