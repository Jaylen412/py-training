# 03-02 Boolean logic

## What you will learn

- Combine conditions with `and`, `or` and `not`.
- Predict how Python groups a mix of `and`, `or` and `not`.
- Use short-circuiting to guard against errors.
- Write range checks as chained comparisons.

## Why it matters

Real rules are rarely a single comparison: "a customer churns if they have been inactive for 60 days **and** have no active subscription". Boolean logic lets you write such rules directly. In Part 3 you will use the same logic, with slightly different symbols, to filter rows of a pandas DataFrame.

## Concepts

### and, or, not

The three **logical operators** combine or flip booleans:

- `a and b` is `True` only when **both** are true.
- `a or b` is `True` when **at least one** is true.
- `not a` is the opposite of `a`.

```python
print(True and True, True and False)
print(True or False, False or False)
print(not True, not False)
```

```
True False
True False
False True
```

In practice you combine comparisons:

```python
age = 25
has_licence = True
can_rent_car = age >= 21 and has_licence
print("Can rent a car:", can_rent_car)

day = "Sunday"
is_weekend = day == "Saturday" or day == "Sunday"
print("Weekend:", is_weekend)
```

```
Can rent a car: True
Weekend: True
```

Note that each side of `or` is a full comparison: `day == "Saturday" or day == "Sunday"`. See Common mistakes for what happens if you shorten it.

`not` reads naturally in conditions:

```python
is_member = False
if not is_member:
    print("Join today and save 10%!")
```

```
Join today and save 10%!
```

For membership tests, Python has a more readable form: `"@" not in email` means the same as `not "@" in email`. Use `not in` whenever you check that something is absent.

### Precedence

When you mix the operators, Python applies `not` first, then `and`, then `or`, much as `*` comes before `+`. So `True or False and False` means `True or (False and False)`:

```python
print(True or False and False)
print((True or False) and False)
```

```
True
False
```

Comparisons such as `>=` and `==` are applied before any of the three, which is why `age >= 21 and has_licence` works without brackets. When you mix `and` with `or`, add brackets anyway, so readers do not have to remember the rule.

### Chained comparisons

To check that a value lies in a range, Python lets you chain comparisons as in maths. `18 <= temperature <= 25` means `18 <= temperature and temperature <= 25`.

```python
temperature = 22
print(18 <= temperature <= 25)
print(0 < 5 < 3)
```

```
True
False
```

`0 < 5 < 3` is `False` because, although `0 < 5` is true, `5 < 3` is not.

### Short-circuiting

Python stops working out an `and` or `or` as soon as it knows the answer. This is called **short-circuiting**:

- In `a and b`, if `a` is false the whole thing is false, so `b` is never looked at.
- In `a or b`, if `a` is true the whole thing is true, so `b` is never looked at.

This makes `and` a guard. Here, dividing by `count` would crash when it is zero, but the left-hand check stops that from ever happening:

```python
count = 0
total = 10
if count != 0 and total / count > 2:
    print("High average")
else:
    print("No data, or a low average")
```

```
No data, or a low average
```

Swap the two sides (`total / count > 2 and count != 0`) and the program crashes with `ZeroDivisionError`, because the division happens first. Put the safety check on the left.

### Putting it together: leap years

A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400. Translated directly:

```python
year = 2000
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(year, "is a leap year:", is_leap)
year = 1900
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(year, "is a leap year:", is_leap)
```

```
2000 is a leap year: True
1900 is a leap year: False
```

1900 is divisible by 4 and by 100, so the bracketed part is false; it is not divisible by 400 either. 2000 is divisible by 400. Writing the rule as a single expression, with brackets showing the structure, is much clearer than three nested `if` statements.

## Common mistakes

- **Shortening an `or` comparison.** `day == "Saturday" or "Sunday"` is always truthy. Python reads it as `(day == "Saturday") or ("Sunday")`, and the non-empty string `"Sunday"` is truthy. With `day = "Monday"` it gives `Sunday`, not `False`. Write `day == "Saturday" or day == "Sunday"`.
- **Using `&`, `|` or `!`.** In plain Python, write the words `and`, `or` and `not`. (pandas uses `&` and `|`; you will meet that in Module 14.)
- **Guard on the wrong side.** `total / count > 2 and count != 0` crashes with `ZeroDivisionError: division by zero` when `count` is 0. Put the check that prevents the error first.
- **Mixing `and` and `or` without brackets.** `is_admin or is_owner and is_active` means `is_admin or (is_owner and is_active)`, which lets inactive admins through. Add brackets to say what you mean.

## Try it

Write one expression that is `True` for a valid hour on a 24-hour clock (0 to 23) using a chained comparison. Test it with `-1`, `0`, `23` and `24`.

## Exercises

Open `ex_03_02.py`:

1. `is_leap_year`: the leap-year rule.
2. `can_ride`: whether someone may go on a ride, based on height and age.
3. `is_weekend`: whether a day name is Saturday or Sunday, ignoring case.
4. `in_range`: whether a value lies between two limits, inclusive.
5. `is_valid_username`: whether a username meets three rules.

Run the tests:

```
python -m pytest part-1-python-fundamentals/03-control-flow/03-02-boolean-logic
```

## Summary

- `and` needs both sides true, `or` needs at least one, `not` flips a boolean.
- Precedence is `not`, then `and`, then `or`; use brackets when mixing them.
- `low <= value <= high` checks a range in one expression.
- `and` and `or` short-circuit, so put guards such as `count != 0` on the left.
- Each side of `or` must be a full condition.
