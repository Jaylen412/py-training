# 04-01 Defining and calling functions

## What you will learn

- Define your own functions with `def` and call them.
- Pass values into a function through parameters.
- Send a result back with `return`, and explain how that differs from `print`.
- Document a function with a docstring.

## Why it matters

Functions let you name a piece of work and reuse it instead of copying code. You have been filling in function bodies since Module 01; now you will write the whole thing. In Part 5, every scikit-learn tool is used through functions and methods like `fit` and `predict`, and you will write your own `fit` in Part 4.

## Concepts

### Defining and calling

A **function** is a named block of code that runs when you ask for it. You **define** it with `def`, a name, brackets and a colon, followed by an indented body. Defining a function does not run it. You run it by **calling** it: writing its name followed by brackets.

```python
def say_hello():
    print("Hello!")


say_hello()
say_hello()
```

```
Hello!
Hello!
```

Each call runs the whole body. Function names follow the same rules and conventions as variable names: snake_case, and descriptive. A good function name is usually a verb: `calculate_total`, `print_report`.

(The two blank lines around each function follow the official Python style guide. They are not required, but they make files easier to read.)

### Parameters and arguments

A **parameter** is a variable listed in the brackets of the definition. An **argument** is the value you give in the call. When the function is called, each parameter is set to the matching argument.

```python
def greet(name):
    print(f"Hello, {name}!")


greet("Ada")
greet("Grace")
```

```
Hello, Ada!
Hello, Grace!
```

Inside the function, `name` is `"Ada"` on the first call and `"Grace"` on the second. A function can have several parameters, separated by commas.

### return

**`return`** ends the function and sends a value back to the place it was called from. The call itself then stands for that value, so you can store it, print it or use it in an expression.

```python
def square(number):
    return number * number


result = square(7)
print(result)
print(square(3) + square(4))
```

```
49
25
```

### return versus print

This is the most important distinction in this lesson. `print` **shows** a value on the screen for a human. `return` **hands** a value back to the program so it can keep working with it. A function with no `return` statement gives back `None`.

```python
def add_and_print(first, second):
    print(first + second)


def add_and_return(first, second):
    return first + second


printed = add_and_print(2, 3)
returned = add_and_return(2, 3)
print("printed is", printed)
print("returned is", returned)
```

```
5
printed is None
returned is 5
```

`add_and_print` displayed 5 but returned `None`, so `printed` holds nothing useful. Prefer functions that return values. The caller can always print the result, but cannot do maths with something that was only printed.

### return ends the function

As soon as a `return` runs, the function stops. This lets you skip `else`:

```python
def describe_age(age):
    if age < 13:
        return "child"
    if age < 18:
        return "teenager"
    return "adult"


print(describe_age(8), describe_age(15), describe_age(40))
```

```
child teenager adult
```

For `age = 8`, the first `return` runs and the other lines are never reached.

### Docstrings

A **docstring** is a string, in triple quotes, placed as the first line of the body. It says what the function does, and tools such as your editor show it when you hover over a call. Python stores it in the function's `__doc__` attribute.

```python
def area_of_circle(radius):
    """Return the area of a circle with the given radius."""
    return 3.14159 * radius ** 2


print(round(area_of_circle(2), 2))
print(area_of_circle.__doc__)
```

```
12.57
Return the area of a circle with the given radius.
```

A one-line docstring starting with a verb ("Return ...") is enough for small functions.

### Functions calling functions

Once defined, a function can be used inside other functions:

```python
def hypotenuse(side_a, side_b):
    """Return the longest side of a right-angled triangle."""
    return (square(side_a) + square(side_b)) ** 0.5


print(hypotenuse(3, 4))
```

```
5.0
```

## Common mistakes

- **Forgetting `return`.** A body of `number * number` without `return` works out the value and throws it away, so `square(3)` gives `None`. Using that later causes errors such as `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`.
- **Forgetting the brackets in a call.** `print(square)` prints something like `<function square at 0x1052f8400>`, the function itself. Call it: `square(3)`.
- **Wrong number of arguments.** `square()` gives `TypeError: square() missing 1 required positional argument: 'number'`, and `square(1, 2)` gives `TypeError: square() takes 1 positional argument but 2 were given`.
- **Not indenting the body.** `def f(n):` followed by an unindented `return n` gives `IndentationError: expected an indented block after function definition on line 1`.

## Try it

Write a function `cube(number)` and use it to print the cubes of 1 to 5 with a `for` loop. Then change it to `print` instead of `return` and see what your loop prints.

## Exercises

Open `ex_04_01.py`. This time you write the bodies with no hints about the structure.

1. `square`: a number multiplied by itself.
2. `make_greeting`: a greeting string for a name.
3. `is_even`: whether a whole number is even.
4. `bmi`: body mass index, rounded to one decimal place.
5. `format_duration`: turn a number of seconds into hours, minutes and seconds.

Run the tests:

```
python -m pytest part-1-python-fundamentals/04-functions/04-01-defining-functions
```

## Summary

- `def name(parameters):` defines a function; `name(arguments)` calls it.
- Parameters are variables that receive the arguments of each call.
- `return` ends the function and hands back a value; without it, the function returns `None`.
- `print` shows a value to a human; `return` gives it to the program. Prefer `return`.
- Start each function with a one-line docstring saying what it does.
