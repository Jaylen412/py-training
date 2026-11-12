# 02-05 Booleans, None and type conversion

## What you will learn

- Compare values with comparison operators and get `True` or `False`.
- Use `None` to mean "no value yet".
- Convert between strings and numbers with `int`, `float` and `str`.
- Predict the truthiness of a value, and read input from the user.

## Why it matters

Programs make decisions, and every decision comes down to a `True` or `False`. Converting types is constant work with real data: numbers read from a file or typed by a user arrive as text and must be turned into `int` or `float` before you can do maths with them. In Part 5, a classifier's prediction is often literally a boolean: spam or not spam.

## Concepts

### Booleans

A **boolean** (type `bool`) has only two possible values: `True` and `False`. They are written with a capital letter and no quotes.

```python
is_raining = True
has_umbrella = False
print(is_raining, has_umbrella)
print(type(is_raining))
```

```
True False
<class 'bool'>
```

### Comparison operators

A **comparison operator** compares two values and gives a boolean.

| Operator | Meaning |
|----------|---------|
| `==` | equal to |
| `!=` | not equal to |
| `<`, `>` | less than, greater than |
| `<=`, `>=` | less than or equal to, greater than or equal to |

```python
age = 20
print(age > 18)
print(age < 18)
print(age >= 20)
print(age == 21)
print(age != 21)
```

```
True
False
True
False
True
```

Note the double equals sign. `=` assigns a value; `==` asks whether two values are equal.

Strings can be compared too. `==` is case-sensitive, and `<` compares alphabetically (strictly, by character codes, where all capitals come before all lower-case letters):

```python
print("apple" == "apple")
print("apple" == "Apple")
print("apple" < "banana")
```

```
True
False
True
```

### None

**`None`** is a special value meaning "nothing here" or "no value yet". It is the only value of its type, `NoneType`. To check whether something is `None`, use the `is` operator:

```python
middle_name = None
print(middle_name)
print(type(middle_name))
print(middle_name is None)
```

```
None
<class 'NoneType'>
True
```

`None` is different from `0` and from `""`. A shop's stock of 0 is a known amount; a stock of `None` means you do not know. You will meet missing values again in pandas, where they matter a lot.

### Type conversion

`int()`, `float()` and `str()` build a value of their type from another value:

```python
print(int("42") + 1)
print(float("3.5") * 2)
print(str(42) + "!")
print(int(3.99))
print(float(7))
```

```
43
7.0
42!
3
7.0
```

`int()` on a float **chops off** the decimal part (`3.99` becomes `3`); it does not round. Use `round()` when you want rounding. `int()` on a string only works if the string looks like a whole number.

### Checking types

`type()` tells you a value's type. It is the first thing to check when an operation behaves strangely:

```python
print(type("42"), type(42), type(42.0))
```

```
<class 'str'> <class 'int'> <class 'float'>
```

`"42"` and `42` print the same way, but one is text and the other a number.

### Truthiness

Python can treat any value as true or false. `bool()` shows how a value would be treated. Values that count as false are called **falsy**: `0`, `0.0`, the empty string `""`, `None`, and `False` itself. Almost everything else is **truthy**.

```python
print(bool(0), bool(1), bool(-5))
print(bool(""), bool("hello"), bool(" "))
print(bool(None))
```

```
False True True
False True True
False
```

A string containing just a space is truthy, because it is not empty. Truthiness becomes useful in Module 03, where `if name:` means "if the name is not empty".

Booleans also behave like the numbers 1 and 0, which makes counting easy:

```python
print(True + True + False)
```

```
2
```

### Reading input

`input(prompt)` shows the prompt, waits for the user to type a line and press Enter, and gives back what they typed **as a string**, always. To do maths with it, convert it:

```python
typed_age = input("How old are you? ")
age_next_year = int(typed_age) + 1
print(f"Next year you will be {age_next_year}")
```

`examples.py` cannot stop and wait for you, so it uses a fixed string in place of `input`:

```python
typed_age = "20"
print(type(typed_age))
age_next_year = int(typed_age) + 1
print(f"Next year you will be {age_next_year}")
```

```
<class 'str'>
Next year you will be 21
```

## Common mistakes

- **Doing maths on input without converting it.** `age = input(...)` then `age > 18` gives `TypeError: '>' not supported between instances of 'str' and 'int'`. Convert first: `age = int(input(...))`.
- **Converting a decimal string with `int`.** `int("3.5")` gives `ValueError: invalid literal for int() with base 10: '3.5'`. Use `float("3.5")`, or `int(float("3.5"))` if you really want a whole number.
- **Expecting `bool("False")` to be `False`.** It is `True`, because the string is not empty. Compare instead: `text == "True"`.
- **Using `None` in arithmetic.** `None + 1` gives `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. A value you forgot to set is often the cause.

## Try it

Write a small script that asks for two numbers with `input`, converts them with `float`, and prints their sum with two decimal places. Run it and type `2.5` and `4`. Then run it again and type `two`. Read the traceback.

## Exercises

Open `ex_02_05.py`:

1. `is_adult`: whether an age is 18 or over.
2. `parse_price`: convert a price written as text into a float.
3. `add_text_numbers`: add two whole numbers that are given as strings.
4. `matches_number`: whether a string holds a given whole number.
5. `is_missing`: whether a value is `None`.
6. `is_blank`: whether a string is empty or contains only spaces.

Run the tests:

```
python -m pytest part-1-python-fundamentals/02-values-variables-types/02-05-booleans-none-conversion
```

## Summary

- Booleans are `True` or `False`; comparisons such as `==`, `!=`, `<` and `>=` produce them.
- `None` means "no value"; check for it with `is None`.
- `int()`, `float()` and `str()` convert values; `int()` chops off decimals.
- `0`, `""`, `None` and `False` are falsy; most other values are truthy.
- `input()` always returns a string, so convert it before doing maths.
