# 01-02 Your first program

## What you will learn

- Display text and numbers with `print`, including several values at once.
- Write comments that explain code without running.
- Predict the order in which statements run.
- Read a traceback to find which line failed and why.

## Why it matters

`print` is how a program talks to you. Through the whole course you will print values to check that your code does what you think, from a single number now to the accuracy of a trained model in Part 5. Reading tracebacks calmly is the most useful debugging skill you can learn on day one.

## Concepts

### print

A **statement** is one complete instruction, usually one line. The most common first statement is a call to `print`, which shows a value on the screen. A **value** is a piece of data, such as the text `"Hello, world!"` or the number `42`. Text in quotes is called a **string**.

```python
print("Hello, world!")
print(42)
print(3.5)
```

Output:

```
Hello, world!
42
3.5
```

The quotes tell Python where the string begins and ends; they are not printed. Numbers need no quotes.

### Printing several values

Give `print` several values separated by commas and it prints them on one line with a space between each:

```python
print("I am", 30, "years old")
```

```
I am 30 years old
```

### sep and end

`print` has two settings you can change. `sep` (separator) is what goes **between** values, and is a space by default. `end` is what goes **after** the last value, and is a new line by default.

```python
print("2026", "11", "11", sep="-")
print("Loading", end="...")
print("done")
```

```
2026-11-11
Loading...done
```

Because the second `print` ended with `"..."` instead of a new line, the third `print` continued on the same line. An empty `print()` prints just the `end`, which gives you a blank line:

```python
print("Above the gap")
print()
print("Below the gap")
```

```
Above the gap

Below the gap
```

### Comments

A **comment** starts with `#` and runs to the end of the line. Python ignores comments completely. They are notes for humans: what the code is for, or why it is written a certain way.

```python
# This whole line is a comment.
print("Comments do not run")  # this part of the line is a comment too
# print("This line is switched off")
```

```
Comments do not run
```

Putting `#` in front of a line of code is called **commenting it out**. It is a quick way to switch a line off while you experiment.

### Top to bottom

Python runs the statements in a file in order, from the first line to the last. Changing the order of the lines changes the order of the output.

```python
print("Step 1: boil the water")
print("Step 2: add the pasta")
print("Step 3: drain and serve")
```

```
Step 1: boil the water
Step 2: add the pasta
Step 3: drain and serve
```

### Reading a traceback

When Python hits a problem it cannot handle, it stops and prints a **traceback**: a report of where it was and what went wrong. (This example is not in `examples.py`, because it would stop the file.) Suppose `greet.py` contains:

```python
print("Start")
prnt("Hello")
print("End")
```

Running it gives:

```
Start
Traceback (most recent call last):
  File "greet.py", line 2, in <module>
    prnt("Hello")
    ^^^^
NameError: name 'prnt' is not defined. Did you mean: 'print'?
```

Read a traceback **from the bottom up**:

1. **The last line** is the error type (`NameError`) and a message. Python does not know the name `prnt`, and even suggests `print`.
2. **The lines above** show where: file `greet.py`, line 2, with the offending code and `^^^^` markers under the problem.
3. **The output before the traceback** shows that line 1 ran ("Start" was printed) and line 3 never ran. Python stops at the first error.

Some errors are found before anything runs. A **syntax error** means the code breaks Python's grammar rules, so Python refuses to start:

```
  File "quote.py", line 1
    print("Hello)
          ^
SyntaxError: unterminated string literal (detected at line 1)
```

Here the closing quote is missing, so the string never ends.

### About the exercises

The exercise files wrap each task in a **function**: a named block of code that starts with `def`. You will learn how functions work in Module 04. For now, treat each one as a box: delete the line `raise NotImplementedError` and write your `print` statements in its place, indented by four spaces like the line you deleted.

## Common mistakes

- **Misspelling or capitalising `print`.** `Print("Hello")` gives `NameError: name 'Print' is not defined. Did you mean: 'print'?`. Python is case-sensitive, so `Print` and `print` are different names.
- **Leaving out the brackets.** `print "Hello"` gives `SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?`. Older Python 2 tutorials wrote it this way; Python 3 needs the brackets.
- **Missing quote.** `print("Hello)` gives `SyntaxError: unterminated string literal`. Every string needs a quote at both ends, of the same kind.
- **Forgetting that `sep` and `end` are text.** `print("a", "b", sep=-)` is a syntax error. Write `sep="-"` with quotes.

## Try it

In `examples.py`, change `sep="-"` to `sep="/"`, and change `end="..."` to `end=" "`. Predict the output, then run the file to check.

## Exercises

Open `ex_01_02.py` and replace each `raise NotImplementedError` with your `print` statements.

1. `print_greeting`: print `Hello, world!`.
2. `print_name_card`: print a three-line name card.
3. `print_date`: print a date with `/` between the parts, using `sep`.
4. `print_progress`: print `Loading...done` using two `print` calls and `end`.
5. `print_box`: print a small box drawn with `+`, `-` and `|`.

Run the tests from the repository root:

```
python -m pytest part-1-python-fundamentals/01-getting-started/01-02-first-program
```

## Summary

- `print` shows values; separate several values with commas.
- `sep` controls what goes between values, `end` what goes after them.
- `#` starts a comment, which Python ignores.
- Statements run from top to bottom, and Python stops at the first error.
- Read tracebacks from the bottom up: error type and message, then file and line.
