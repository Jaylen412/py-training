# 04-05 Reading and writing tests

## What you will learn

- Check that code behaves as expected with `assert`.
- Explain how the course's test files load your exercises and the reference solutions.
- Read pytest's output, including a failure report.
- Write your own pytest test file, including edge cases.

## Why it matters

You have been running tests since Module 01; now you will understand them and write your own. Tests are how you know code works, and how you find out when a change breaks something that used to work. Every part project in this course comes with tests, and the capstone asks you to write them for your own data-preparation code.

## Concepts

### assert

An **`assert` statement** checks that a condition is true. If it is, nothing happens. If it is not, Python stops with an `AssertionError`.

```python
def clamp(value, low, high):
    """Return value, pushed into the range low to high."""
    if value < low:
        return low
    if value > high:
        return high
    return value


assert clamp(5, 0, 10) == 5
assert clamp(-3, 0, 10) == 0
assert clamp(42, 0, 10) == 10
print("All asserts passed")
```

```
All asserts passed
```

You can add a message after a comma. It is shown only when the assert fails, so make it explain what went wrong:

```python
result = clamp(15, 0, 10)
assert result == 10, f"expected 10 but got {result}"
print("Still passing")
```

```
Still passing
```

If `clamp` were broken, you would see `AssertionError: expected 10 but got 15`.

### Test functions

A **test** is a small function that calls the code being tested with a known input and asserts that the output is correct. With pytest, a test is just a function whose name starts with `test_`, in a file whose name starts with `test_`.

```python
def test_clamp_inside_range():
    assert clamp(5, 0, 10) == 5


def test_clamp_below_range():
    assert clamp(-3, 0, 10) == 0


def test_clamp_on_the_edges():
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10
```

pytest finds these functions and calls them for you. (`examples.py` calls them by hand, and prints `All test functions passed`.) Give each test a name that says what it checks; when one fails, the name is the first clue.

### Choosing test cases

Good tests cover three kinds of input:

1. **Typical** values: an ordinary case, like `clamp(5, 0, 10)`.
2. **Edge cases**: values on a boundary, such as exactly `low` or `high`, `0`, an empty string, a single character. Bugs cluster at edges.
3. **Unusual** values: negative numbers, very large numbers, or anything the function might receive but you did not plan for.

Every exercise in this course has at least one edge-case test. Now you know why.

### Comparing floats

Because of float rounding (02-01), never compare floats with `==` in a test. Check that the difference is tiny instead. `abs` gives the distance from zero, and `1e-9` means 0.000000001.

```python
total = 0.1 + 0.2
assert abs(total - 0.3) < 1e-9
print("Float comparison passed")
```

```
Float comparison passed
```

pytest offers a shortcut, `pytest.approx`, which you will see in the course's test files: `assert total == pytest.approx(0.3)`.

### Reading pytest output

Suppose `clamp` had a bug, returning `value` instead of `high` when the value is too big. Running `python -m pytest test_clamp.py` gives:

```
collected 3 items

test_clamp.py ..F                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_clamp_above_range ____________________________

    def test_clamp_above_range():
>       assert clamp(42, 0, 10) == 10
E       assert 42 == 10
E        +  where 42 = clamp(42, 0, 10)

test_clamp.py:18: AssertionError
=========================== short test summary info ============================
FAILED test_clamp.py::test_clamp_above_range - assert 42 == 10
========================= 1 failed, 2 passed in 0.02s ==========================
```

Read it like this:

- `..F`: one character per test. `.` passed, `F` failed.
- The `FAILURES` section names the failing test, shows the line marked with `>`, and the `E` lines explain: the function returned `42`, but the test expected `10`.
- The last line is the summary. Add `-q` (quiet) for shorter output.

### How the course tests work

Open any test file in this course, for example `test_ex_04_01.py`. The top looks like this:

```python
import importlib
import os

mod = importlib.import_module(
    "sol_04_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_04_01"
)
```

This chooses which file to test. Normally it loads your exercise file, `ex_04_01.py`. If the environment variable `COURSE_SOLUTIONS` is set, it loads the reference solution instead, which is how the course itself is checked. Either way the module is called `mod`, so the tests call `mod.square(7)` and so on. You will learn about `import` in Module 08. Some tests also take a parameter called `capsys`, a pytest tool that captures what a function prints.

## Common mistakes

- **Test file or function not named `test_...`.** pytest silently ignores it and reports `no tests ran`. Both the file and the function names must start with `test_`.
- **Putting brackets round assert.** `assert (result == 10, "message")` asserts a pair of values, which is always truthy, so it never fails. Python warns `SyntaxWarning: assertion is always true, perhaps remove parentheses?`. Write `assert result == 10, "message"`.
- **Testing only the happy path.** Tests that only use typical values miss the boundary bugs. Add at least one edge case per function.
- **Comparing floats with `==`.** `assert 0.1 + 0.2 == 0.3` fails. Use `pytest.approx` or check that the difference is tiny.

## Try it

Create a file `test_my_clamp.py` in this lesson's folder containing the `clamp` function and the three test functions above. Run `python -m pytest` on it. Then break `clamp` on purpose, run again, and read the failure report.

## Exercises

Open `ex_04_05.py`. Before writing each function, read its tests in `test_ex_04_05.py` to see exactly what is expected, including the edge cases.

1. `clamp`: push a value into a range.
2. `is_palindrome`: whether text reads the same backwards, ignoring case and spaces.
3. `median_of_three`: the middle value of three numbers.

Run the tests:

```
python -m pytest part-1-python-fundamentals/04-functions/04-05-reading-and-writing-tests
```

## Summary

- `assert condition, message` stops with `AssertionError` when the condition is false.
- A pytest test is a function named `test_...` in a file named `test_...`.
- Test typical values, edge cases and unusual values.
- In pytest output, `.` is a pass and `F` a failure; the `E` lines explain what was expected.
- Compare floats with `pytest.approx` or a tiny tolerance, never with `==`.
