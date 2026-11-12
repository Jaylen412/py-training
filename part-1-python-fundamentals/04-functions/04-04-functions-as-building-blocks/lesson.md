# 04-04 Functions as building blocks

## What you will learn

- Break a problem into small functions that each do one job.
- Tell pure functions from impure ones, and prefer pure ones.
- Build larger functions by calling smaller ones.
- Document parameter and return types with type hints.

## Why it matters

Every project in this course is too big to write as one long block. The way professionals cope is decomposition: split the problem into pieces small enough to get right, test each piece, and assemble them. A machine learning pipeline in Part 5 is exactly this: load, clean, transform, train, evaluate, each a separate step you can check on its own.

## Concepts

### Decomposing a problem

**Decomposition** means splitting a problem into smaller sub-problems. Take this task: *print a receipt line for an item, giving members a 10% discount and then adding 20% tax*. Reading it carefully, there are three separate jobs hiding inside:

1. Take a discount off a price.
2. Add tax to a price.
3. Format an amount of money for display.

Each becomes its own small function. A function that does one thing is easy to name, easy to test, and easy to reuse.

### Type hints

Below, each parameter is followed by a colon and a type, and `->` before the colon of the `def` line gives the type of the return value. These are **type hints**: notes for humans and tools about what types a function expects and returns.

```python
def apply_discount(price: float, discount_rate: float) -> float:
    """Return the price after taking off discount_rate (0.1 means 10%)."""
    return price * (1 - discount_rate)


def add_tax(price: float, tax_rate: float) -> float:
    """Return the price with tax added (0.2 means 20%)."""
    return price * (1 + tax_rate)


def format_money(amount: float) -> str:
    """Return the amount as a string such as $12.50."""
    return f"${amount:,.2f}"
```

Read `price: float` as "price should be a float" and `-> str` as "returns a string". Your editor uses hints to catch mistakes as you type. Module 11 covers them in more depth.

### Building up from small functions

Now the higher-level function reads almost like the original description, because the details live in the helpers:

```python
def receipt_line(item: str, price: float, is_member: bool) -> str:
    """Return one line of a receipt."""
    discount_rate = 0.1 if is_member else 0.0
    discounted = apply_discount(price, discount_rate)
    final_price = add_tax(discounted, 0.2)
    return f"{item:<10}{format_money(final_price):>10}"


print(receipt_line("Coffee", 3.50, True))
print(receipt_line("Sandwich", 6.00, False))
print(receipt_line("Cake", 2.75, True))
```

```
Coffee         $3.78
Sandwich       $7.20
Cake           $2.97
```

And each small piece can be checked on its own, which makes finding bugs much easier:

```python
print(apply_discount(100, 0.1))
print(add_tax(100, 0.2))
print(format_money(1234.5))
```

```
90.0
120.0
$1,234.50
```

If a receipt total were wrong, you would test these three pieces separately and quickly see which one is at fault.

### Pure functions

A **pure function** is one whose result depends **only** on its arguments, and which changes nothing outside itself (it does not print, write files, or modify globals). Call it twice with the same arguments and you get the same answer twice. An **impure function** has **side effects** or depends on hidden state.

```python
def pure_total(prices_text: str) -> float:
    """Add up comma-separated prices. Depends only on its argument."""
    total = 0.0
    for piece in prices_text.split(","):
        total += float(piece)
    return total


running_total = 0.0


def impure_add(price: float) -> float:
    """Changes a global variable - the same call gives different answers."""
    global running_total
    running_total += price
    return running_total


print(pure_total("1.50,2.25"), pure_total("1.50,2.25"))
print(impure_add(1.5), impure_add(1.5))
```

```
3.75 3.75
1.5 3.0
```

`impure_add(1.5)` returned a different answer the second time. Pure functions are easier to test, easier to reason about, and safe to reuse anywhere. Programs need some impure parts (something has to print the results), so the usual design is: **pure functions for the logic, and a thin impure layer on the outside** for input and output.

### Hints are not enforced

Type hints are documentation only. Python does not check them when the code runs:

```python
print(format_money(7))
print(add_tax("ab", 2))
```

```
$7.00
ababab
```

Passing an `int` where a `float` is expected is harmless. But `add_tax("ab", 2)` happily computed `"ab" * 3` and returned `"ababab"`. The hint says `price: float`, but nothing stopped a string getting in. Hints help you and your editor spot mistakes; they do not prevent them.

## Common mistakes

- **One giant function.** A 60-line function that reads input, calculates and prints cannot be tested in pieces. If you cannot describe a function in one short sentence without "and", split it.
- **Printing inside helpers.** A helper that prints its result instead of returning it cannot be used by other functions. Return values from helpers; print only at the outer layer.
- **Misplacing the return hint.** `def f(x) -> int(x):` is wrong; the hint is just a type: `def f(x: str) -> int:`.
- **Trusting hints to catch bad input.** As shown above, Python ignores them at runtime. Validate inputs explicitly when it matters (Module 06).

## Try it

Add a fourth helper, `apply_voucher(price: float, voucher: float) -> float`, which takes a fixed amount off but never goes below zero. Use it inside `receipt_line` with a new parameter `voucher: float = 0.0`.

## Exercises

Open `ex_04_04.py`. The goal is a password strength checker built from small helpers. Write the helpers first, then use them in `password_strength`.

1. `has_uppercase`: whether the text contains a capital letter.
2. `has_digit`: whether the text contains a digit.
3. `is_long_enough`: whether the text is at least a minimum length.
4. `password_strength`: "weak", "medium" or "strong", using the three helpers.

Run the tests:

```
python -m pytest part-1-python-fundamentals/04-functions/04-04-functions-as-building-blocks
```

## Summary

- Decompose a problem into functions that each do one job, then combine them.
- Pure functions depend only on their arguments and have no side effects; prefer them.
- Keep printing and other side effects in a thin outer layer.
- Type hints (`price: float`, `-> str`) document types but are not checked by Python.
