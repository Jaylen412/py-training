# 10-04 Decorators and closures

## What you will learn

- Define functions inside functions and return them.
- Explain what a closure remembers, and update it with `nonlocal`.
- Write decorators that add behaviour to any function, using `@` syntax.
- Preserve a decorated function's name and docstring with `functools.wraps`, and write a timing decorator.

## Why it matters

You have already used decorators: `@dataclass` and `@property` in Module 09, and you will meet `@pytest.mark.parametrize` and `@contextmanager` in Module 11. Decorators add behaviour such as timing, logging, caching or validation to a function without changing its code. Closures are what make them work, and they also let you build small "function factories".

## Concepts

### Functions inside functions

A function can define another function in its body and return it. The returned function can still see the variables of the function that made it:

```python
def outer():
    message = "hello from outer"

    def inner():
        return message

    return inner


get_message = outer()
print(get_message())
```

```
hello from outer
```

`outer` has finished running by the time `get_message()` is called, yet `inner` still has access to `message`.

### Closures

A **closure** is a function that remembers values from the scope in which it was created. This makes **function factories** possible: functions that build other functions.

```python
def make_multiplier(factor):
    def multiply(number):
        return number * factor
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))
```

```
20 30
```

Each call to `make_multiplier` creates a new `multiply` with its own remembered `factor`.

### nonlocal

A closure can read remembered variables freely, but assigning to one would create a new local variable (04-03). **`nonlocal`** says "this name belongs to the enclosing function", so the closure can update it:

```python
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


clicks = make_counter()
print(clicks(), clicks(), clicks())
other = make_counter()
print(other())
```

```
1 2 3
1
```

Each counter keeps its own private `count` that nothing else can touch. (A class with a `count` attribute would also work; closures are a lighter alternative for one small piece of state.)

### Decorators

A **decorator** is a function that takes a function and returns a new function, usually one that adds some behaviour and then calls the original. The new function is typically called `wrapper`, and uses `*args, **kwargs` (10-03) so that it accepts whatever the original accepts:

```python
def announce(function):
    def wrapper(*args, **kwargs):
        print(f"  calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


def add(first, second):
    return first + second


add = announce(add)
print(add(2, 3))
```

```
  calling add
5
```

`add = announce(add)` replaces `add` with the wrapper. The wrapper remembers the original `add` (a closure), announces the call, then calls it.

### The @ syntax

Writing `@decorator` on the line above a `def` does exactly the same thing, more neatly:

```python
@announce
def multiply(first, second):
    return first * second


print(multiply(4, 5))
print(multiply.__name__)
```

```
  calling multiply
20
wrapper
```

### functools.wraps

The last line above shows a problem: the decorated function now calls itself `wrapper`, and its docstring is lost. Error messages, help text and tools all become confusing. The standard fix is to decorate the wrapper with **`functools.wraps(function)`**, which copies the original's name and docstring onto it:

```python
def announce_properly(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(f"  calling {function.__name__}")
        return function(*args, **kwargs)
    return wrapper


@announce_properly
def subtract(first, second):
    """Return first minus second."""
    return first - second


print(subtract(9, 4), subtract.__name__, subtract.__doc__)
```

```
  calling subtract
5 subtract Return first minus second.
```

Always use `functools.wraps` in your decorators.

### A timing decorator

`time.perf_counter()` returns a precise time in seconds, so the difference between two readings is how long something took (Module 12 covers measuring in detail). A decorator can time any function:

```python
def timed(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  {function.__name__} took {elapsed:.4f} seconds")
        return result
    return wrapper


@timed
def slow_sum(limit):
    return sum(range(limit))


total = slow_sum(1_000_000)
print(total)
```

```
  slow_sum took 0.0074 seconds
499999500000
```

Your time will be different. The decorator must **return the result** of the original function; forgetting to do so is the most common decorator bug.

### A caching decorator

A decorator can keep data between calls in its closure. This one remembers results, so a slow function never computes the same answer twice:

```python
def remember(function):
    cache = {}

    @functools.wraps(function)
    def wrapper(number):
        if number not in cache:
            cache[number] = function(number)
        return cache[number]
    return wrapper


@remember
def fibonacci(number):
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(80))
```

```
23416728348467685
```

`fibonacci` calls itself (this is called **recursion**). Without the cache it would make billions of calls for `fibonacci(80)`; with it, each value is computed once. The standard library provides a ready-made version, `functools.cache`.

## Common mistakes

- **Forgetting to return the result in the wrapper.** The decorated function then always returns `None`. Write `return function(*args, **kwargs)`.
- **Calling the function when decorating.** `@announce()` with brackets calls `announce` with no arguments, giving `TypeError: announce() missing 1 required positional argument: 'function'`. Write `@announce`.
- **Forgetting `nonlocal`.** `count += 1` in a closure without `nonlocal count` gives `UnboundLocalError: cannot access local variable 'count' where it is not associated with a value`.
- **Leaving out `functools.wraps`.** Everything still runs, but every decorated function is called `wrapper`, which makes tracebacks and test reports confusing.

## Try it

Write a decorator `shout_result` that converts a function's string result to upper case. Apply it to a function that returns a greeting, and check that `__name__` is preserved.

## Exercises

Open `ex_10_04.py`:

1. `make_power`: a function factory for raising numbers to a fixed power.
2. `make_accumulator`: a closure that keeps a running total.
3. `count_calls`: a decorator that counts how many times a function is called.
4. `validate_non_negative`: a decorator that rejects negative arguments.
5. `memoize`: a caching decorator that works for any positional arguments.

Run the tests:

```
python -m pytest part-2-intermediate-python/10-functional-tools-and-iteration/10-04-decorators-and-closures
```

## Summary

- Inner functions can be returned, and remember the variables around them: that is a closure.
- `nonlocal name` lets a closure update a remembered variable.
- A decorator takes a function and returns a wrapper; `@decorator` above `def` applies it.
- Wrappers take `*args, **kwargs`, call the original, and return its result.
- Always decorate wrappers with `@functools.wraps(function)`.
