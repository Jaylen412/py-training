# 04-03 Scope

## What you will learn

- Explain the difference between local and global variables.
- Predict what happens when a function assigns to a name that also exists outside it.
- Recognise the `global` keyword, and explain why to avoid it.
- Pass data into functions as arguments and get it out with `return`.

## Why it matters

When a program grows past a few dozen lines, the biggest source of bugs is code that changes something far away from where you are looking. Scope rules keep each function's working variables private. Writing functions that take everything they need as arguments makes them predictable, easy to test, and easy to reuse in the projects later in this course.

## Concepts

### Local variables

The **scope** of a variable is the part of the program where its name can be used. A variable created inside a function, including its parameters, is **local**: it exists only while that function is running and cannot be seen from outside.

```python
def make_greeting(name):
    message = f"Hello, {name}"
    return message


print(make_greeting("Ada"))
```

```
Hello, Ada
```

After the call finishes, `message` and `name` are gone. Writing `print(message)` after the function would give `NameError: name 'message' is not defined`. The only way to get the value out is the one the function provides: `return`.

### Global variables

A variable created at the top level of a file, outside any function, is **global**. Functions can **read** global variables:

```python
TAX_RATE = 0.2


def price_with_tax(price):
    return price * (1 + TAX_RATE)


print(price_with_tax(50))
```

```
60.0
```

Reading a global **constant** like this is fine: it never changes, so the function always behaves the same way.

### Assigning creates a local

If a function **assigns** to a name, Python treats that name as local for the whole function, even if a global with the same name exists. The global is untouched:

```python
counter = 0


def increase_counter():
    counter = 100   # a local variable that happens to share the name
    return counter


print(increase_counter())
print(counter)
```

```
100
0
```

The same applies to parameters. Changing a parameter changes only the function's local copy of the name:

```python
number = 5


def double(number):
    number = number * 2
    return number


print(double(number))
print(number)
```

```
10
5
```

Inside `double`, `number` is a separate local variable that starts with the value 5. Reassigning it does not affect the global `number`.

### The global keyword

The `global` statement tells Python that a name inside a function refers to the global variable, so assignment changes the global. You will see it in other people's code, so recognise it, but avoid writing it:

```python
score = 0


def add_point_global():
    global score
    score += 1


add_point_global()
add_point_global()
print("score is now", score)
```

```
score is now 2
```

### The better way: data in, data out

Instead of reaching out to a global, take the current value as a parameter and return the new value. The caller decides what to do with it:

```python
def add_point(current_score):
    return current_score + 1


score = 0
score = add_point(score)
score = add_point(score)
print("score is now", score)
```

```
score is now 2
```

The result is the same, but now everything `add_point` depends on is visible in its call.

### Why globals cause bugs

A function that reads a changing global gives different answers to the same call, depending on hidden state:

```python
discount = 0.1


def sale_price(price):
    return price * (1 - discount)


print(sale_price(100))
discount = 0.5   # somewhere far away in a bigger program...
print(sale_price(100))
```

```
90.0
50.0
```

`sale_price(100)` returned two different answers, and nothing in the call explains why. Making the dependency a parameter fixes that:

```python
def sale_price_clear(price, discount):
    return price * (1 - discount)


print(sale_price_clear(100, 0.1))
```

```
90.0
```

Rule of thumb: a function may read global **constants** (written in capitals), but everything else it needs should come in through its parameters.

## Common mistakes

- **Using a local variable outside its function.** `print(message)` after the function gives `NameError: name 'message' is not defined`. Return the value and store it.
- **Updating a global without `global`.** `counter += 1` inside a function, with `counter` only defined outside, gives `UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value`. The `+=` makes `counter` local, and the local has no value yet. Pass it in and return it instead.
- **Expecting a function to change the caller's variable.** `double(number)` on its own line leaves `number` unchanged. Write `number = double(number)`.

## Try it

Remove the line `global score` from Example 5 and run the file. Read the error, then explain in one sentence why Python thinks `score` is local.

## Exercises

Open `ex_04_03.py`. Each docstring describes a version that relied on global variables. Write a version that takes everything as parameters and returns its result.

1. `add_points`: return a new score.
2. `price_with_tax`: a price with tax, where the rate is a parameter with a default.
3. `count_long_words`: how many words are at least a given length.
4. `apply_transaction`: a new balance after a deposit or withdrawal.

Run the tests:

```
python -m pytest part-1-python-fundamentals/04-functions/04-03-scope
```

## Summary

- Variables created inside a function, including parameters, are local and vanish when it returns.
- Functions can read globals, but assigning to a name inside a function makes it local.
- The `global` keyword lets a function change a global; avoid it.
- Pass data in as arguments and return results; read only global constants.
