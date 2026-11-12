# 02-02 Variables and assignment

## What you will learn

- Store values in variables with `=` and use them in later calculations.
- Predict what happens when a variable is reassigned.
- Choose variable names that follow Python's rules and conventions.
- Update a variable with augmented assignment (`+=`, `-=` and friends).

## Why it matters

Programs need to remember things: a running total, a user's name, the accuracy of a model. Variables are how they remember. Good names are also how you remember what your own code does when you come back to it in a week.

## Concepts

### Assignment

A **variable** is a name that refers to a value. You create one with an **assignment statement**: a name, an `=` sign, and a value or expression.

```python
price = 4.50
quantity = 3
total_price = price * quantity
print(total_price)
```

```
13.5
```

Read `=` as "is set to", not "equals". Python first works out the right-hand side (`4.5 * 3`), then makes the name on the left refer to the result. After that, writing the name anywhere means "the value it refers to".

```python
width = 5
height = 2
area = width * height
print("Area:", area)
```

```
Area: 10
```

### Reassignment

Assigning to a name that already exists makes it refer to the new value. The old value is forgotten.

```python
score = 10
print(score)
score = 25
print(score)
```

```
10
25
```

Because the right-hand side is worked out first, a variable can appear on both sides. This reads the current value, computes a new one, and stores it under the same name:

```python
lives = 3
lives = lives - 1
print(lives)
```

```
2
```

In maths, `lives = lives - 1` would be nonsense. In Python it means "set `lives` to whatever `lives` is now, minus one".

### Assigning one variable to another

`second = first` makes `second` refer to the same value as `first` at that moment. Changing `first` afterwards does not change `second`:

```python
first = 100
second = first
first = 200
print(first, second)
```

```
200 100
```

(Module 05 shows a case where this gets more subtle: values such as lists that can be changed in place.)

### Augmented assignment

Updating a variable based on its current value is so common that Python has a shortcut. `balance += 50` means exactly `balance = balance + 50`. The same works for the other operators:

```python
balance = 100
balance += 50   # same as balance = balance + 50
print(balance)
balance -= 30   # same as balance = balance - 30
print(balance)
balance *= 2    # same as balance = balance * 2
print(balance)
balance /= 4    # same as balance = balance / 4
print(balance)
```

```
150
120
240
60.0
```

The last line is a float because `/` always gives a float.

### Naming rules

Python enforces a few rules on names:

- Use only letters, digits and underscores (`_`).
- Do not start with a digit: `2nd_place` is invalid, `second_place` is fine.
- Do not use Python's reserved words, such as `if`, `for`, `class` or `return`.
- Names are case-sensitive: `total` and `Total` are different variables.

### Naming conventions

Beyond the rules, Python programmers follow conventions (agreed habits) that make code easier to read:

- Use **snake_case**: lower-case words joined by underscores, such as `total_price`.
- Use full, descriptive words. `seconds_per_hour` is better than `sph` or `x`.
- Write **constants**, values that should never change, in capitals: `VAT_RATE`.

```python
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)

VAT_RATE = 0.2
net_price = 80
print(net_price * (1 + VAT_RATE))
```

```
3600
96.0
```

Python does not stop you from changing `VAT_RATE`; the capitals are a signal to other programmers that they should not.

## Common mistakes

- **Using a variable before assigning it, or misspelling it.** `print(totl)` gives `NameError: name 'totl' is not defined`. Check the spelling and that the assignment runs first.
- **Spaces in names.** `total price = 5` gives `SyntaxError: invalid syntax`. Use `total_price`.
- **Starting with a digit.** `2nd_place = "Bo"` gives `SyntaxError: invalid decimal literal`. Use `second_place`.
- **Writing the assignment backwards.** `5 = width` gives `SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?`. The name always goes on the left.

## Try it

Predict the final value of `count` before running this, then check in the REPL:

```python
count = 1
count *= 3
count += count
count -= 2
```

## Exercises

Open `ex_02_02.py`. Use variables with clear names inside each function, then `return` the answer.

1. `area_of_room`: the floor area of a rectangular room.
2. `price_after_discount`: a price with a percentage taken off.
3. `final_balance`: apply a deposit, a withdrawal and a year of interest, in that order.
4. `seconds_in_days`: how many seconds are in a number of days.

Run the tests:

```
python -m pytest part-1-python-fundamentals/02-values-variables-types/02-02-variables-and-assignment
```

## Summary

- `name = value` makes a name refer to a value; the right-hand side is worked out first.
- Reassigning replaces the old value; `x = x + 1` updates a variable.
- `+=`, `-=`, `*=` and `/=` are shortcuts for updating a variable.
- Names use letters, digits and underscores, cannot start with a digit, and are case-sensitive.
- Use descriptive snake_case names, and capitals for constants.
