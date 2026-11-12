# 12-01 Measuring code

## What you will learn

- Time a piece of code with `time.perf_counter`.
- Get reliable timings with repetition and `timeit`.
- Find which part of a program is actually slow before trying to speed it up.
- Report timings in sensible units.

## Why it matters

Training a model can take seconds or hours, and data preparation on a large file can be painfully slow if written carelessly. Before you change code to make it faster, you need to know how fast it is now and where the time goes. Guessing is usually wrong. This lesson gives you the measuring tools; the next two explain why some code is slow.

## Concepts

All timings in this lesson came from one laptop. **Your numbers will be different**, and will vary a little every time you run the file. What matters is the comparisons.

### time.perf_counter

`time.perf_counter()` returns a number of seconds from a precise clock. The number itself means nothing; the **difference** between two readings is the elapsed time:

```python
def build_squares(count):
    squares = []
    for number in range(count):
        squares.append(number * number)
    return squares


start = time.perf_counter()
build_squares(1_000_000)
elapsed = time.perf_counter() - start
print(f"build_squares took {elapsed:.3f} seconds")
```

```
build_squares took 0.022 seconds
```

Use `perf_counter` rather than `time.time()` for measuring durations: it is more precise and is not affected by the computer's clock being adjusted.

### Timings are noisy

Your computer is doing many other things at once, so the same code takes a slightly different time on every run. Measure several times:

```python
times = []
for _ in range(5):
    start = time.perf_counter()
    build_squares(200_000)
    times.append(time.perf_counter() - start)
print("five runs (ms):", [round(t * 1000, 1) for t in times])
print(f"best: {min(times) * 1000:.1f} ms")
```

```
five runs (ms): [4.4, 4.5, 4.6, 4.4, 14.4]
best: 4.4 ms
```

One run took three times as long as the others, because something else interrupted it. The **minimum** of several runs is the most stable summary: it is the time the code takes when nothing gets in the way. (The mean is distorted by occasional slow runs like that one.)

### timeit

The standard library's **`timeit`** module does the repetition for you. `timeit.timeit(function, number=n)` calls the function `n` times and returns the **total** time, so divide by `n` for the time per call:

```python
loop_time = timeit.timeit(lambda: build_squares(10_000), number=100)
comprehension_time = timeit.timeit(lambda: [n * n for n in range(10_000)], number=100)
print(f"loop:          {loop_time / 100 * 1000:.3f} ms per call")
print(f"comprehension: {comprehension_time / 100 * 1000:.3f} ms per call")
```

```
loop:          0.312 ms per call
comprehension: 0.179 ms per call
```

The `lambda` wraps the code to be timed into a function with no arguments. Here the comprehension is noticeably faster than the loop with `append`, because the comprehension avoids looking up and calling `append` a million times.

`timeit.repeat` does several rounds and returns a list of totals; take the minimum:

```python
results = timeit.repeat(lambda: sum(range(10_000)), number=200, repeat=5)
print(f"sum(range(10_000)): best {min(results) / 200 * 1e6:.1f} microseconds per call")
```

```
sum(range(10_000)): best 67.4 microseconds per call
```

A **microsecond** (µs, often written `us`) is a millionth of a second; a **millisecond** (ms) is a thousandth. In the REPL or a notebook, `python -m timeit "sum(range(10_000))"` from the terminal gives the same kind of measurement.

### Measure before optimising

The most important rule of performance work: **find where the time goes before changing anything**. Programmers are notoriously bad at guessing. Timing each step of a task separately shows which one deserves attention:

```python
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
```

```
format      15.9 ms
build        5.6 ms
sum          1.8 ms
```

Turning numbers into text takes far longer than computing them. Speeding up the sum would be wasted effort. (The `Timer` context manager from 11-04 is a tidier way to time steps.)

For bigger programs, Python's built-in **profiler** does this automatically for every function: `python -m cProfile -s cumulative your_script.py` lists the functions that took the most time.

### When to care

Most code is fast enough. Optimise only when something is actually too slow for its purpose, and only the part that measurement shows to be slow. Clear code that is fast enough is better than clever code that is slightly faster.

## Common mistakes

- **Timing once.** A single measurement can be off by a factor of three, as shown above. Repeat, and use the minimum.
- **Timing the wrong thing.** Including set-up (such as building the test data) inside the timed code makes the result meaningless. Prepare data before starting the clock.
- **Forgetting to divide by `number`.** `timeit.timeit(..., number=100)` returns the total for 100 calls.
- **Optimising without measuring.** Rewriting the "obviously slow" part often makes no difference, because the real cost was elsewhere.

## Try it

Use `timeit` to compare `", ".join(words)` with building the same string using `+=` in a loop, for a list of 10,000 words. Then try 100,000 words. Does the gap grow?

## Exercises

Open `ex_12_01.py`. Each timing function takes a `clock` argument, defaulting to `time.perf_counter`. The tests pass in a fake clock that returns numbers they choose, so that results are exact. Call `clock()` wherever you would call `time.perf_counter()`.

1. `time_call`: call a function and return its result with the elapsed time.
2. `best_time`: the fastest of several runs.
3. `slowest_step`: the name of the step that took the longest.
4. `format_duration`: show a number of seconds in a sensible unit.

Run the tests:

```
python -m pytest part-2-intermediate-python/12-performance-and-complexity/12-01-measuring-code
```

## Summary

- `time.perf_counter()` differences measure elapsed time.
- Timings are noisy: repeat, and use the minimum.
- `timeit.timeit(function, number=n)` returns the total for `n` calls; `timeit.repeat` gives several totals.
- Measure each step to find where the time actually goes before optimising.
- Only optimise code that measurement shows is too slow.
