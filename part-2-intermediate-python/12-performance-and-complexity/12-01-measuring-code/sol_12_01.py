"""Solutions for 12-01 Measuring code."""
import time


def time_call(function, *args, clock=time.perf_counter):
    """Return (result, seconds taken)."""
    start = clock()
    result = function(*args)
    return result, clock() - start


def best_time(function, repeats, clock=time.perf_counter):
    """Return the shortest of `repeats` timed calls."""
    if repeats < 1:
        raise ValueError(f"repeats must be at least 1, got {repeats}")
    times = []
    for _ in range(repeats):
        start = clock()
        function()
        times.append(clock() - start)
    return min(times)


def slowest_step(timings):
    """Return the name of the slowest step, or None."""
    if not timings:
        return None
    return max(timings, key=timings.get)


def format_duration(seconds):
    """Return the duration in s, ms or us with 1 decimal place."""
    if seconds >= 1:
        return f"{seconds:.1f} s"
    if seconds >= 0.001:
        return f"{seconds * 1_000:.1f} ms"
    return f"{seconds * 1_000_000:.1f} us"
