# 06-04 Raising errors and validating input

## What you will learn

- Raise an exception from your own code with `raise`.
- Choose a suitable built-in exception type and write a helpful message.
- Validate arguments at the top of a function so it fails early.
- Define a simple custom exception class.

## Why it matters

Catching errors is half the story; the other half is reporting them. A function that receives nonsense, such as a negative quantity, should say so loudly rather than return a wrong answer that spreads through the rest of the program. scikit-learn does exactly this: pass it data of the wrong shape and it raises a `ValueError` explaining what it expected.

## Concepts

### raise

The **`raise`** statement creates an exception and raises it, just as Python does for its own errors. You give the exception type and a message:

```python
def set_age(age):
    if age < 0:
        raise ValueError(f"age cannot be negative, got {age}")
    return age


print(set_age(30))
try:
    set_age(-5)
except ValueError as error:
    print("Caught:", error)
```

```
30
Caught: age cannot be negative, got -5
```

When `raise` runs, the function stops immediately, exactly like an error inside Python itself. The caller can catch it with `try`/`except`, or let it crash the program with a clear message.

A good message says **what was wrong** and **what value caused it**. "age cannot be negative, got -5" is far more useful than "bad input".

### Choosing the exception type

Pick the built-in type that best describes the problem. The two you will use most:

- **`ValueError`**: the argument has the right type but an unacceptable value (a negative age, an empty list, the text `"abc"` where a number was expected).
- **`TypeError`**: the argument is the wrong type entirely (a string where a list was expected).

Others you already know have specific meanings: `KeyError` for a missing key, `IndexError` for a bad position, `FileNotFoundError` for a missing file.

To check a type, use the built-in **`isinstance(value, type)`**, which returns `True` or `False`:

```python
def average(numbers):
    if not isinstance(numbers, list):
        raise TypeError(f"expected a list, got {type(numbers).__name__}")
    if len(numbers) == 0:
        raise ValueError("cannot average an empty list")
    return sum(numbers) / len(numbers)


for argument in [[1, 2, 3], [], "123"]:
    try:
        print(average(argument))
    except (TypeError, ValueError) as error:
        print(f"{type(error).__name__}: {error}")
```

```
2.0
ValueError: cannot average an empty list
TypeError: expected a list, got str
```

### Fail early

**Fail early** means checking all the inputs at the very top of a function, before doing any work. The checks act as a fence: below it, the rest of the function can trust its data.

```python
def make_order(item, quantity, unit_price):
    if not item.strip():
        raise ValueError("item name must not be empty")
    if quantity <= 0:
        raise ValueError(f"quantity must be positive, got {quantity}")
    if unit_price < 0:
        raise ValueError(f"unit price cannot be negative, got {unit_price}")
    return {"item": item.strip(), "quantity": quantity, "total": quantity * unit_price}


print(make_order(" pens ", 3, 1.5))
```

```
{'item': 'pens', 'quantity': 3, 'total': 4.5}
```

Without these checks, `make_order("pens", -3, 1.5)` would quietly produce an order with a total of `-4.5`, and the mistake might only be noticed much later, far from its cause.

### Parse and validate in one place

Text from users and files needs both converting and checking. Doing both in one function gives the rest of the program clean values. Here a `ValueError` from `float` is caught and replaced by one with a clearer message. In an f-string, `!r` after the expression shows the value with quotes, like `repr`, which makes empty or space-filled strings visible:

```python
def parse_amount(text):
    try:
        amount = float(text)
    except ValueError:
        raise ValueError(f"not a number: {text!r}")
    if amount <= 0:
        raise ValueError(f"amount must be positive, got {amount}")
    return round(amount, 2)


for text in ["12.499", "abc", "-3"]:
    try:
        print("Amount:", parse_amount(text))
    except ValueError as error:
        print("Rejected:", error)
```

```
Amount: 12.5
Rejected: not a number: 'abc'
Rejected: amount must be positive, got -3.0
```

### Custom exception classes

Sometimes no built-in type fits, and you want callers to be able to catch **your** error specifically. You can define a new exception type in two lines. The `class` syntax is covered properly in Module 09; for now, copy this pattern: a name ending in `Error`, `(Exception)` after it, and a docstring.

```python
class InsufficientFundsError(Exception):
    """Raised when a withdrawal is larger than the balance."""


def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"balance {balance} is less than {amount}")
    return balance - amount


print(withdraw(100, 30))
try:
    withdraw(100, 300)
except InsufficientFundsError as error:
    print("Declined:", error)
```

```
70
Declined: balance 100 is less than 300
```

Because it is built on `Exception`, it behaves like any other exception:

```python
print(issubclass(InsufficientFundsError, Exception))
```

```
True
```

Use custom exceptions sparingly. For most input problems, `ValueError` with a good message is exactly right.

## Common mistakes

- **Returning an error value instead of raising.** A function that returns `-1` or `"error"` on bad input forces every caller to remember to check. Raising makes the problem impossible to ignore.
- **Raising without a message.** `raise ValueError` prints just `ValueError:` with nothing after it. Always say what was wrong and include the value.
- **Raising inside `except` without care.** If you raise a new exception inside an `except` block and nobody catches it, the traceback shows both errors, joined by "During handling of the above exception, another exception occurred". That is expected; read the last one first.
- **Checking with `type(x) == list`.** This rejects things that should be accepted, such as subclasses of list. Use `isinstance(x, list)`.

## Try it

Add validation to `withdraw` so that a negative or zero `amount` raises a `ValueError`. Make sure the check runs before the balance check. Why does the order of the checks matter for the error the caller sees?

## Exercises

Open `ex_06_04.py`:

1. `validate_age`: check an age's type and range, returning it if valid.
2. `parse_quantity`: turn text into a positive whole number, or raise `ValueError`.
3. `withdraw`: take money from a balance, raising a custom exception if there is not enough.
4. `require_fields`: check that a dictionary has every required key.

Run the tests:

```
python -m pytest part-1-python-fundamentals/06-files-and-errors/06-04-raising-errors
```

## Summary

- `raise SomeError("message")` stops the function and reports a problem to the caller.
- Use `ValueError` for bad values and `TypeError` for wrong types; check types with `isinstance`.
- Fail early: validate all inputs at the top of the function, with messages that include the bad value.
- `!r` in an f-string shows a value with quotes, like `repr`.
- `class MyError(Exception):` defines a custom exception type that callers can catch specifically.
