# 12-01 Measuring code
# Timings depend on your computer, so your numbers will differ from the lesson.
import time
import timeit


# Example 1: time.perf_counter() measures elapsed time precisely
def build_squares(count):
    squares = []
    for number in range(count):
        squares.append(number * number)
    return squares


start = time.perf_counter()
build_squares(1_000_000)
elapsed = time.perf_counter() - start
print(f"build_squares took {elapsed:.3f} seconds")

# Example 2: one measurement is noisy - repeat it and look at the spread
times = []
for _ in range(5):
    start = time.perf_counter()
    build_squares(200_000)
    times.append(time.perf_counter() - start)
print("five runs (ms):", [round(t * 1000, 1) for t in times])
print(f"best: {min(times) * 1000:.1f} ms")

# Example 3: timeit runs a statement many times and returns the total
loop_time = timeit.timeit(lambda: build_squares(10_000), number=100)
comprehension_time = timeit.timeit(lambda: [n * n for n in range(10_000)], number=100)
print(f"loop:          {loop_time / 100 * 1000:.3f} ms per call")
print(f"comprehension: {comprehension_time / 100 * 1000:.3f} ms per call")

# Example 4: timeit.repeat gives several totals; take the minimum
results = timeit.repeat(lambda: sum(range(10_000)), number=200, repeat=5)
print(f"sum(range(10_000)): best {min(results) / 200 * 1e6:.1f} microseconds per call")


# Example 5: measure before optimising - find where the time actually goes
def slow_report(count):
    with_timing = {}
    start = time.perf_counter()
    data = build_squares(count)
    with_timing["build"] = time.perf_counter() - start

    start = time.perf_counter()
    total = sum(data)
    with_timing["sum"] = time.perf_counter() - start

    start = time.perf_counter()
    text = ",".join(str(value) for value in data)
    with_timing["format"] = time.perf_counter() - start
    return total, len(text), with_timing


total, length, timing = slow_report(300_000)
for step, seconds in sorted(timing.items(), key=lambda item: -item[1]):
    print(f"{step:<8}{seconds * 1000:8.1f} ms")
