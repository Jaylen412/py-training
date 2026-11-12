# 03-04 for loops and range

## What you will learn

- Loop over each character of a string with `for`.
- Generate sequences of numbers with `range`, including start, stop and step.
- Build up a result with the accumulator pattern.
- Put one loop inside another to work with rows and columns.

## Why it matters

Most data work is "do this to every item": every character in a string, every row in a file, every sample in a dataset. A `for` loop expresses that directly. The accumulator pattern you learn here, starting from zero and adding as you go, is how you will compute totals, averages and errors by hand before NumPy does them for you in Part 3.

## Concepts

### for over a string

A **`for` loop** takes the items of a sequence one at a time. Each time round, the **loop variable** refers to the next item, and the body runs once for it.

```python
for letter in "cat":
    print(letter)
```

```
c
a
t
```

You choose the name of the loop variable. Pick one that says what each item is: `letter`, `number`, `row`.

Unlike `while`, a `for` loop cannot accidentally run forever: it stops when the items run out.

### range

`range` produces a sequence of whole numbers to loop over. It works like slicing: the stop value is **not** included.

- `range(stop)` counts from 0 up to `stop - 1`.
- `range(start, stop)` counts from `start` up to `stop - 1`.
- `range(start, stop, step)` counts in jumps of `step`; a negative step counts down.

```python
for number in range(4):
    print(number, end=" ")
print()
for number in range(2, 6):
    print(number, end=" ")
print()
for number in range(0, 20, 5):
    print(number, end=" ")
print()
for number in range(5, 0, -1):
    print(number, end=" ")
print()
```

```
0 1 2 3 
2 3 4 5 
0 5 10 15 
5 4 3 2 1 
```

`range(4)` gives four numbers, 0 to 3. The plain `print()` after each loop ends the line, because the loop used `end=" "`.

When you just want to repeat something and do not need the number, name the variable `_` (underscore). By convention this means "I will not use this":

```python
for _ in range(3):
    print("Hip hip hooray!")
```

```
Hip hip hooray!
Hip hip hooray!
Hip hip hooray!
```

### The accumulator pattern

An **accumulator** is a variable that collects a result as the loop runs. Set it up **before** the loop, update it **inside**, and use it **after**:

```python
total = 0
for number in range(1, 101):
    total += number
print("1 + 2 + ... + 100 =", total)
```

```
1 + 2 + ... + 100 = 5050
```

The accumulator does not have to be a number. Start from the empty string to build text:

```python
shout = ""
for letter in "hello":
    shout += letter.upper() + "!"
print(shout)
```

```
H!E!L!L!O!
```

Put an `if` inside the loop to accumulate only some items:

```python
vowel_count = 0
for letter in "machine learning":
    if letter in "aeiou":
        vowel_count += 1
print("Vowels:", vowel_count)
```

```
Vowels: 6
```

### Nested loops

A loop inside another loop is a **nested loop**. The inner loop runs completely for **each** iteration of the outer one. This is the natural way to work through rows and columns:

```python
for row in range(1, 4):
    line = ""
    for column in range(1, 6):
        line += f"{row * column:4}"
    print(line)
```

```
   1   2   3   4   5
   2   4   6   8  10
   3   6   9  12  15
```

The outer loop runs 3 times and the inner loop 5 times for each, so the multiplication happens 15 times in total. `:4` in the f-string pads each number to a width of 4 so the columns line up.

Often one loop is enough if you use string repetition:

```python
for size in range(1, 5):
    print("*" * size)
```

```
*
**
***
****
```

### for or while?

Use `for` when you are going through a known collection or a known number of steps. Use `while` when you loop until something happens and cannot say in advance how many times that will take.

## Common mistakes

- **Expecting `range` to include the stop value.** `range(1, 10)` stops at 9. To count from 1 to 10, write `range(1, 11)`.
- **Looping over a number.** `for n in 5:` gives `TypeError: 'int' object is not iterable`. Write `for n in range(5):`.
- **Giving `range` a float.** `range(1.5)` gives `TypeError: 'float' object cannot be interpreted as an integer`. Convert with `int()` first.
- **Resetting the accumulator inside the loop.** If `total = 0` is inside the loop body, it is reset every time, and you end up with only the last value. Put it before the loop.

## Try it

Change the multiplication table so it prints rows 1 to 10 and columns 1 to 10. Then make each row start with its row number followed by `|`.

## Exercises

Open `ex_03_04.py`:

1. `sum_up_to`: the sum of the whole numbers from 1 to n.
2. `factorial`: n multiplied by every whole number below it, down to 1.
3. `count_vowels`: the number of vowels in a text, ignoring case.
4. `times_table_row`: one row of a times table as a string.
5. `triangle`: a right-angled triangle of stars, as a single string.
6. `sum_of_multiples`: the sum of the numbers below a limit that are multiples of 3 or 5.

Run the tests:

```
python -m pytest part-1-python-fundamentals/03-control-flow/03-04-for-loops-and-range
```

## Summary

- `for item in sequence:` runs the body once per item and stops when the items run out.
- `range(start, stop, step)` produces whole numbers up to, but not including, `stop`.
- The accumulator pattern: set up before the loop, update inside, use after.
- An inner loop runs completely for each pass of the outer loop.
- Prefer `for` for a known number of steps, `while` for "until something happens".
