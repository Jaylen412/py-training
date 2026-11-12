# 10-03 `*args`, `**kwargs` and unpacking

## What you will learn

- Write functions that accept any number of positional arguments with `*args`.
- Accept any number of keyword arguments with `**kwargs`.
- Unpack lists and dictionaries into a function call with `*` and `**`.
- Force arguments to be passed by keyword.

## Why it matters

Many functions you use every day take a variable number of arguments: `print("a", "b", "c")`, `max(3, 9, 4)`, `dict(name="Ada", age=36)`. Data-science libraries lean heavily on this: plotting functions pass `**kwargs` through to lower-level drawing code, and scikit-learn models take many settings, most of which should be passed by keyword. Decorators (next lesson) depend on `*args` and `**kwargs` to wrap any function.

## Concepts

### `*args`

A parameter written with a single star, by convention `*args`, collects **all extra positional arguments** into a tuple:

```python
def total(*numbers):
    print("  numbers is", numbers)
    return sum(numbers)


print(total(1, 2, 3))
print(total())
```

```
  numbers is (1, 2, 3)
6
  numbers is ()
0
```

The name after the star can be anything; `args` is just the common default. Choose a descriptive one, like `numbers`, when you can. Ordinary parameters come first and take their arguments before the rest are collected:

```python
def greet(greeting, *names):
    return [f"{greeting}, {name}!" for name in names]


print(greet("Hello", "Ada", "Alan"))
```

```
['Hello, Ada!', 'Hello, Alan!']
```

### `**kwargs`

A parameter with two stars, by convention `**kwargs`, collects **all extra keyword arguments** into a dictionary:

```python
def make_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile


print(make_profile("Ada", born=1815, field="mathematics"))
```

```
{'name': 'Ada', 'born': 1815, 'field': 'mathematics'}
```

(`dictionary.update(other)` copies every key and value from `other` into `dictionary`.)

### Putting them together

The order in a definition is fixed: ordinary parameters, then `*args`, then keyword parameters, then `**kwargs`:

```python
def describe(first, *rest, sep=", ", **options):
    return f"first={first} rest={rest} sep={sep!r} options={options}"


print(describe(1, 2, 3, sep="; ", colour="red"))
```

```
first=1 rest=(2, 3) sep='; ' options={'colour': 'red'}
```

### Unpacking in a call

The stars also work the other way round, **in a call**. `*sequence` spreads a list or tuple out into separate positional arguments; `**dictionary` spreads a dictionary into keyword arguments:

```python
point = [3, 4]
settings = {"sep": "-", "end": "!\n"}
print(*point)
print("a", "b", **settings)


def area(width, height):
    return width * height


print(area(*point))
print(area(**{"width": 2, "height": 5}))
```

```
3 4
a-b!
12
10
```

`print(*point)` is the same as `print(3, 4)`, and `area(**{"width": 2, "height": 5})` is the same as `area(width=2, height=5)`. This is very handy when the arguments are already in a list or a dictionary, such as settings loaded from a JSON file.

### Keyword-only arguments

Parameters that come after `*args`, or after a bare `*`, can **only** be passed by keyword. A bare `*` in a definition collects nothing; it just marks where keyword-only parameters begin:

```python
def connect(host, *, port=80, timeout=10):
    return f"{host}:{port} (timeout {timeout}s)"


print(connect("example.com", port=8080))
try:
    connect("example.com", 8080)
except TypeError as error:
    print("TypeError:", error)
```

```
example.com:8080 (timeout 10s)
TypeError: connect() takes 1 positional argument but 2 were given
```

Keyword-only arguments make calls self-explanatory and protect against mixing up the order of settings. `connect("example.com", 8080, 30)` would be ambiguous to a reader; `port=8080, timeout=30` is not. scikit-learn makes most model settings keyword-only for exactly this reason.

### Unpacking to build collections

Stars also unpack inside list and dictionary literals. With dictionaries, later keys win, which is a neat way to apply overrides to defaults:

```python
first_half = [1, 2]
second_half = [3, 4]
print([*first_half, *second_half, 5])
defaults = {"colour": "blue", "size": "M"}
choices = {"size": "L"}
print({**defaults, **choices})
```

```
[1, 2, 3, 4, 5]
{'colour': 'blue', 'size': 'L'}
```

### Passing arguments through

Together, `*args` and `**kwargs` let a function accept **any** arguments and pass them on, unchanged, to another function. This is the key to the decorators in the next lesson:

```python
def logged(function, *args, **kwargs):
    print(f"  calling {function.__name__} with {args} {kwargs}")
    return function(*args, **kwargs)


print(logged(area, 3, height=7))
```

```
  calling area with (3,) {'height': 7}
21
```

## Common mistakes

- **Passing a list where separate arguments are expected.** `area(point)` gives `TypeError: area() missing 1 required positional argument: 'height'`, because the whole list went into `width`. Write `area(*point)`.
- **Passing a keyword-only argument by position.** `connect("example.com", 8080)` gives `TypeError: connect() takes 1 positional argument but 2 were given`. Name it: `port=8080`.
- **Wrong parameter order.** `def f(**kwargs, *args)` is a `SyntaxError`. The order is: normal, `*args`, keyword-only, `**kwargs`.
- **Hiding typos with `**kwargs`.** A function that accepts `**kwargs` and ignores unknown keys silently accepts `colur="red"`. Check for unexpected keys, or avoid `**kwargs` when you know the options in advance.

## Try it

Write `average(*numbers)` that returns the mean and raises a `ValueError` when called with no arguments. Then call it with a list of numbers you already have, using `*`.

## Exercises

Open `ex_10_03.py`:

1. `product`: multiply any number of numbers together.
2. `make_tag`: build an HTML tag from a name, any number of children and any attributes.
3. `merge_settings`: combine any number of dictionaries, later ones winning.
4. `call_with_defaults`: call a function with default keyword arguments that the caller can override.
5. `format_money`: a function with keyword-only options.

Run the tests:

```
python -m pytest part-2-intermediate-python/10-functional-tools-and-iteration/10-03-args-kwargs-and-unpacking
```

## Summary

- `*args` collects extra positional arguments into a tuple; `**kwargs` collects extra keyword arguments into a dictionary.
- Definition order: normal parameters, `*args`, keyword-only parameters, `**kwargs`.
- In a call, `*sequence` and `**dictionary` unpack into separate arguments.
- Parameters after `*` or `*args` are keyword-only, which makes calls clearer and safer.
- `[*a, *b]` and `{**a, **b}` build new collections; `function(*args, **kwargs)` passes everything through.
