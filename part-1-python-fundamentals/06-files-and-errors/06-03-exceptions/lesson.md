# 06-03 Exceptions

## What you will learn

- Read a traceback and name the exception that was raised.
- Catch specific exceptions with `try` and `except`.
- Use `else` and `finally` to run code after a `try` block.
- Decide which errors to handle and which to let through.

## Why it matters

Real input is messy: users type `forty-two` instead of `42`, files go missing, and a row of data is malformed. A program that crashes on the first bad value is fragile. Exceptions let you decide what should happen instead. Your expense tracker must survive a missing or corrupt data file, and cleaning real datasets in Part 3 is full of values that fail to convert.

## Concepts

### What an exception is

When Python hits an error it cannot continue past, it **raises an exception**: an object describing what went wrong. If nothing handles it, the program stops and prints a traceback. You have met many already: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `ZeroDivisionError`, `FileNotFoundError`. The last line of a traceback always names the exception type, followed by its message.

### try and except

Code that might fail goes in a **`try`** block. If an exception is raised inside it, Python jumps to the matching **`except`** block instead of crashing; this is called **catching** or **handling** the exception.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    result = None
print("Result:", result)
```

```
Result: None
```

If no exception happens, the `except` block is skipped. A loop shows both paths:

```python
for text in ["42", "forty-two", "7"]:
    try:
        number = int(text)
        print("Converted", number)
    except ValueError:
        print("Could not convert", text)
```

```
Converted 42
Could not convert forty-two
Converted 7
```

When `int("forty-two")` fails, the rest of that `try` block (the `print`) is skipped, the `except` runs, and the loop carries on with the next item.

### The exception object

`except ValueError as error:` gives you the exception object itself, whose text is its message:

```python
try:
    int("abc")
except ValueError as error:
    print("Error message:", error)
    print("Error type:", type(error).__name__)
```

```
Error message: invalid literal for int() with base 10: 'abc'
Error type: ValueError
```

### Several kinds of error

You can have several `except` blocks; the first one that matches the exception type runs:

```python
def safe_lookup(data, key):
    try:
        return data[key]
    except KeyError:
        return "missing key"
    except IndexError:
        return "index out of range"
    except TypeError:
        return "wrong kind of key"


print(safe_lookup({"a": 1}, "b"))
print(safe_lookup([1, 2], 5))
print(safe_lookup([1, 2], "x"))
```

```
missing key
index out of range
wrong kind of key
```

To handle several types in the same way, list them in a tuple: `except (KeyError, IndexError):`.

### else and finally

An **`else`** block after the `except` blocks runs only if the `try` block raised **no** exception. It keeps the `try` block small: only the risky line goes inside, and the follow-up work goes in `else`.

```python
try:
    value = int("12")
except ValueError:
    print("Not a number")
else:
    print("Doubled:", value * 2)
```

```
Doubled: 24
```

A **`finally`** block runs **always**: after success, after a handled exception, and even when the function returns from inside the `try`. It is used for clean-up that must happen no matter what.

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
    finally:
        print(f"divide({a}, {b}) finished")


print(divide(6, 3))
print(divide(6, 0))
```

```
divide(6, 3) finished
2.0
divide(6, 0) finished
None
```

(`with` uses the same mechanism to close files, which is why you rarely need `finally` for files.)

### Handling a missing file

A common use: start with empty data if a file does not exist yet.

```python
missing = Path(__file__).parent / "does_not_exist.txt"
try:
    with open(missing) as file:
        content = file.read()
except FileNotFoundError:
    content = ""
    print("No file yet; starting empty")
print(repr(content))
```

```
No file yet; starting empty
''
```

### Keep try blocks small, and catch specific exceptions

Put **only** the line that can fail inside `try`, and catch **only** the exception you expect. Here, bad inputs are skipped and recorded, and everything else stays outside the `try`:

```python
user_inputs = ["3", "x", "5"]
total = 0
bad_inputs = []
for text in user_inputs:
    try:
        number = int(text)
    except ValueError:
        bad_inputs.append(text)
        continue
    total += number
print("Total:", total, "Skipped:", bad_inputs)
```

```
Total: 8 Skipped: ['x']
```

A bare `except:` (or `except Exception:`) catches **everything**, including your own bugs such as a misspelt variable name (`NameError`). The program then carries on silently with wrong results. Only catch the errors you know how to handle, and let the rest crash loudly so you can fix them.

## Common mistakes

- **Catching too broadly.** `except:` hides genuine bugs. Name the exception: `except ValueError:`.
- **Too much code inside `try`.** If the `try` block is long, you cannot tell which line failed, and you may catch an error from a line you did not expect to fail. Wrap just the risky line and use `else` for the rest.
- **Catching the wrong type.** `except ValueError:` does not catch `int(None)`, which raises `TypeError: int() argument must be a string, a bytes-like object or a real number, not 'NoneType'`. Read the traceback to find the actual type.
- **Swallowing errors silently.** `except ValueError: pass` throws away the information that something went wrong. At least record or report the bad value.

## Try it

Write a loop that asks for numbers with `input()` until the user types `done`, skipping (and reporting) anything that is not a number, then prints the total. Try typing `3`, `abc`, `4.5` and `done`.

## Exercises

Open `ex_06_03.py`:

1. `safe_divide`: divide, returning `None` instead of crashing on zero.
2. `to_int_or_default`: convert text to an int, or return a default.
3. `read_text_or_empty`: a file's contents, or `""` if it does not exist.
4. `parse_numbers`: split a list of strings into good numbers and bad strings.
5. `load_json_or_default`: JSON from a file, or a default if the file is missing or corrupt.

Run the tests:

```
python -m pytest part-1-python-fundamentals/06-files-and-errors/06-03-exceptions
```

## Summary

- An exception is raised when an error occurs; unhandled, it stops the program with a traceback.
- `try`/`except SomeError:` catches a specific exception and runs the `except` block instead.
- `except SomeError as error:` gives you the exception and its message.
- `else` runs if nothing was raised; `finally` always runs.
- Keep `try` blocks small, catch specific exceptions, and never silently swallow errors.
