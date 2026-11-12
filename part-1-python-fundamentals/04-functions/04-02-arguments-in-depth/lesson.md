# 04-02 Arguments in depth

## What you will learn

- Pass arguments by position and by keyword.
- Give parameters default values to make them optional.
- Avoid the mutable default trap by using `None` as a default.

## Why it matters

Real functions have many settings, and most of them should have sensible defaults. scikit-learn models are a prime example: `KMeans(n_clusters=3, random_state=42)` sets two of over a dozen options by keyword and leaves the rest at their defaults. Knowing how arguments work lets you read and write calls like that with confidence.

## Concepts

### Positional arguments

A **positional argument** is matched to a parameter by its position: the first argument goes to the first parameter, and so on. Swapping them swaps the meaning:

```python
def describe_pet(animal, name):
    return f"{name} is a {animal}"


print(describe_pet("dog", "Rex"))
print(describe_pet("Rex", "dog"))
```

```
Rex is a dog
dog is a Rex
```

### Keyword arguments

A **keyword argument** names the parameter it is for, as `name=value`. Order no longer matters, and the call explains itself:

```python
print(describe_pet(name="Rex", animal="dog"))
print(describe_pet("cat", name="Tom"))
```

```
Rex is a dog
Tom is a cat
```

You can mix the two, but positional arguments must come first.

### Default values

A parameter can have a **default value**, written `parameter=value` in the definition. If the caller leaves that argument out, the default is used:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Ada"))
print(greet("Ada", "Good morning"))
print(greet("Ada", greeting="Hi"))
```

```
Hello, Ada!
Good morning, Ada!
Hi, Ada!
```

Parameters with defaults must come after those without. With several defaults, keywords let you set just the ones you care about and skip the rest:

```python
def format_number(value, decimals=2, prefix="", suffix=""):
    return f"{prefix}{value:.{decimals}f}{suffix}"


print(format_number(3.14159))
print(format_number(3.14159, 4))
print(format_number(19.5, prefix="$"))
print(format_number(0.25, decimals=0, suffix=" kg"))
```

```
3.14
3.1416
$19.50
0 kg
```

(`{decimals}` inside the format specification puts the number of decimal places in from a variable.)

You have been using this all along: `sep` and `end` are keyword parameters of `print` with defaults `" "` and `"\n"`.

```python
print("a", "b", "c", sep="|", end="!\n")
```

```
a|b|c!
```

### The mutable default trap

There is one famous trap with defaults. To show it, we need a **list**, which you will study properly in Module 05. For now: `[]` is an empty list, and `.append(item)` adds an item to the end of it. Unlike strings, lists are **mutable**: they can be changed in place.

```python
def add_item_broken(item, basket=[]):
    basket.append(item)
    return basket


print(add_item_broken("apple"))
print(add_item_broken("bread"))
```

```
['apple']
['apple', 'bread']
```

The second call should have returned a basket containing only bread. What went wrong? Python creates the default value **once**, when the function is defined, not each time it is called. Every call that relies on the default shares the very same list, so items pile up between calls.

The fix is to use `None` as the default and create a fresh list inside the function:

```python
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("bread"))
```

```
['apple']
['bread']
```

The rule: **never use a mutable value (list, dictionary or set) as a default**. Numbers, strings, `True`, `False` and `None` are immutable, so they are safe.

## Common mistakes

- **Positional after keyword.** `greet(name="Ada", "Hello")` gives `SyntaxError: positional argument follows keyword argument`. Put positional arguments first, or name them all.
- **Default before non-default.** `def greet(greeting="Hi", name):` gives `SyntaxError: parameter without a default follows parameter with a default`. Move parameters with defaults to the end.
- **Misspelling a keyword.** `greet(nme="Ada")` gives `TypeError: greet() got an unexpected keyword argument 'nme'. Did you mean 'name'?`.
- **Mutable default.** `def f(items=[])` shares one list between calls. Use `items=None` and create the list inside.

## Try it

Call `format_number(1234.5678, 1, "~", " units")`, then rewrite the same call using only keyword arguments, in a different order. Check that both give the same result.

## Exercises

Open `ex_04_02.py`. Each function's parameters, including defaults, are already written for you.

1. `greet`: a greeting with an optional greeting word.
2. `power`: a number raised to a power, squaring by default.
3. `full_name`: a full name with an optional middle name.
4. `repeat_text`: text repeated with a separator, both optional.
5. `add_item`: add an item to a basket, creating a new basket if none is given.

Run the tests:

```
python -m pytest part-1-python-fundamentals/04-functions/04-02-arguments-in-depth
```

## Summary

- Positional arguments are matched by order; keyword arguments by name.
- Positional arguments come before keyword arguments in a call.
- `parameter=value` in a definition gives a default; defaults come after required parameters.
- Default values are created once, so never use a list, dictionary or set as a default; use `None`.
