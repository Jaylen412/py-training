# 02-01 Numbers and arithmetic

## What you will learn

- Tell the difference between whole numbers (`int`) and decimal numbers (`float`).
- Use the arithmetic operators, including `//`, `%` and `**`.
- Predict the order in which Python works out a calculation.
- Recognise and handle float rounding surprises.

## Why it matters

Machine learning is arithmetic at scale: averages, errors, distances and percentages. Every model you train in Part 5 reports its quality as a number that you must read correctly. Knowing why `0.1 + 0.2` is not exactly `0.3` will save you from confusing bugs later.

## Concepts

### Two kinds of number

Python has two main number **types** (kinds of value). An **`int`** (integer) is a whole number such as `7` or `-120`. A **`float`** (floating-point number) has a decimal point, such as `7.0` or `3.14`. The built-in `type` tells you which type a value has.

```python
print(7)
print(7.0)
print(type(7))
print(type(7.0))
```

```
7
7.0
<class 'int'>
<class 'float'>
```

### The basic operators

An **operator** is a symbol that combines values. An **expression** is a combination of values and operators that Python can work out, giving a single value.

```python
print(7 + 2)
print(7 - 2)
print(7 * 2)
print(7 / 2)
```

```
9
5
14
3.5
```

`*` is multiplication. `/` is division and always gives a float, even when the answer is whole: `10 / 5` is `2.0`.

### Floor division and remainder

`//` is **floor division**: divide, then round down to a whole number. `%` (called **modulo**) gives the **remainder** left over. Together they split a quantity into whole units and leftovers.

```python
print(7 // 2)
print(7 % 2)
print(135 // 60, "hours and", 135 % 60, "minutes")
```

```
3
1
2 hours and 15 minutes
```

Seven divided by two is three, remainder one. 135 minutes is 2 whole hours with 15 minutes left over. A common use of `%`: a number is even when `number % 2` is `0`.

### Powers

`**` raises a number to a power. Raising to the power `0.5` gives a square root.

```python
print(2 ** 10)
print(9 ** 0.5)
```

```
1024
3.0
```

### Mixing int and float

If either side of an operator is a float, the answer is a float:

```python
print(3 + 1.5)
print(10 / 5)
```

```
4.5
2.0
```

### Operator precedence

**Precedence** is the order in which Python works out operators in an expression. As in school maths, powers come first, then `*`, `/`, `//` and `%`, then `+` and `-`. Brackets override everything.

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 * 3 ** 2)
print(-2 ** 2)
print((-2) ** 2)
```

```
14
20
18
-4
4
```

`2 + 3 * 4` multiplies first, giving `2 + 12`. `2 * 3 ** 2` does the power first: `2 * 9`. The surprise is `-2 ** 2`, which is `-4`: Python squares `2` first and then applies the minus sign. When in doubt, add brackets. They cost nothing and make your intention clear.

### Float rounding surprises

Computers store floats in binary, and most decimal fractions, such as 0.1, cannot be stored exactly. The tiny errors usually stay hidden, but sometimes they show:

```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2))
print(round(3.14159, 3))
print(round(2.5), round(3.5))
```

```
0.30000000000000004
False
0.3
3.142
2 4
```

This is not a Python bug: every programming language that uses standard floats behaves this way. Two lessons follow from it. First, round a float **when you display it**, using `round(value, digits)`. Second, never test two floats for exact equality; check whether they are close enough instead (you will see how in later modules).

The last line shows that `round` sends exact halves to the nearest **even** number, so `2.5` becomes `2` and `3.5` becomes `4`. This is called banker's rounding, and it avoids a bias towards rounding up.

### About the exercises

Each exercise in `ex_02_01.py` is a **function**: a named piece of code that receives some values and gives back an answer. You will learn to write functions in Module 04. For now, all you need to know is:

- The names in brackets after the function name, such as `price` and `quantity`, are the values the function receives. Use them like numbers.
- Replace `raise NotImplementedError` with `return` followed by an expression, for example `return price * quantity`. `return` hands that value back as the function's answer.

## Common mistakes

- **Dividing by zero.** `10 / 0` stops the program with `ZeroDivisionError: division by zero`. Check the divisor before dividing, as you will learn in Module 03.
- **Forgetting precedence.** Writing the average of three numbers as `a + b + c / 3` divides only `c` by 3. Write `(a + b + c) / 3`.
- **Expecting `/` to give an `int`.** `10 / 2` is `2.0`, not `2`. Use `//` when you need a whole number, and check that the division is exact.
- **Comparing floats with `==`.** `0.1 + 0.2 == 0.3` is `False`. Compare rounded values or check that the difference is tiny.

## Try it

In the REPL, work out how many whole weeks and leftover days there are in 100 days using `//` and `%`. Then try `-7 // 2` and predict the answer before you press Enter. (Hint: "round down" means towards minus infinity.)

## Exercises

Open `ex_02_01.py`:

1. `total_cost`: price times quantity.
2. `whole_hours`: how many whole hours are in a number of minutes.
3. `leftover_minutes`: the minutes left over after the whole hours.
4. `average_of_three`: the average of three numbers.
5. `celsius_to_fahrenheit`: convert a temperature.
6. `compound_growth`: the value of savings after some years of interest.

Run the tests:

```
python -m pytest part-1-python-fundamentals/02-values-variables-types/02-01-numbers-and-arithmetic
```

## Summary

- `int` holds whole numbers, `float` holds decimals; `/` always gives a float.
- `//` divides and rounds down; `%` gives the remainder; `**` raises to a power.
- Powers first, then multiplication and division, then addition and subtraction. Use brackets to be clear.
- Floats are stored approximately: round them for display and never compare them with `==`.
