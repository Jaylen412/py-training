# 11-02 Type hints

## What you will learn

- Annotate parameters, return values and variables with types.
- Describe collections precisely: `list[float]`, `dict[str, int]`, `tuple[int, int]`.
- Mark values that might be `None` with `Optional` or `X | None`.
- Explain what hints do and do not do at runtime.

## Why it matters

You met type hints briefly in 04-04. In larger code, they are documentation that cannot go out of date without tools noticing. Your editor uses them to autocomplete and to underline mistakes before you run anything, and dedicated checkers such as mypy can scan a whole project. Most modern libraries, including pandas and scikit-learn, publish hints, which is why your editor knows what `train_test_split` returns.

## Concepts

### Basic hints

A **type hint** (or annotation) follows a parameter after a colon, and the return type follows `->`:

```python
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


print(average([1.0, 2.0, 6.0]))
print(average.__annotations__)
```

```
3.0
{'numbers': list[float], 'return': <class 'float'>}
```

Python stores the hints in the function's `__annotations__` dictionary, but otherwise ignores them.

### Collection types

Square brackets say what a collection contains:

| Hint | Meaning |
|------|---------|
| `list[int]` | a list of ints |
| `dict[str, int]` | a dictionary with string keys and int values |
| `set[str]` | a set of strings |
| `tuple[int, int]` | a tuple of exactly two ints |
| `tuple[int, ...]` | a tuple of any number of ints |

```python
def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


print(count_words("a b a"))
print(min_max([4, 1, 9]))
```

```
{'a': 2, 'b': 1}
(1, 9)
```

`counts: dict[str, int] = {}` annotates a variable. This is rarely needed, except for empty collections, where a tool cannot guess what will go in them.

### Optional values

A function that sometimes returns `None` should say so. There are two spellings that mean the same thing: `Optional[int]` from the `typing` module, and the newer `int | None` (read "int or None"):

```python
from typing import Optional


def find_index(items: list[str], target: str) -> Optional[int]:
    for index, item in enumerate(items):
        if item == target:
            return index
    return None


def find_index_new_style(items: list[str], target: str) -> int | None:
    return items.index(target) if target in items else None


print(find_index(["a", "b"], "b"), find_index(["a", "b"], "z"))
print(find_index_new_style(["a", "b"], "z"))
```

```
1 None
None
```

This matters: a caller who sees `-> int | None` knows to check for `None` before doing arithmetic. `|` also works for any union, such as `int | float`.

### Functions and iterables

`Callable[[argument types], return type]` describes a function. `Iterable[int]` means "anything you can loop over that gives ints", which is more flexible than `list[int]` when you only need to loop. Both come from `collections.abc`:

```python
from collections.abc import Callable, Iterable


def apply_to_all(function: Callable[[int], int], values: Iterable[int]) -> list[int]:
    return [function(value) for value in values]


print(apply_to_all(abs, (-1, 2, -3)))
```

```
[1, 2, 3]
```

A good habit: accept general types (`Iterable`) and return specific ones (`list`).

### Hints are not enforced

Python does not check hints when the code runs:

```python
print(average([1, 2]))
try:
    count_words(["not", "a", "string"])
except AttributeError as error:
    print("AttributeError:", error)
```

```
1.5
AttributeError: 'list' object has no attribute 'split'
```

Passing ints where floats are expected is harmless. Passing a list where a string is expected is accepted at the call and crashes inside the function, exactly as it would without hints. Hints help you **before** running, through your editor and checkers; they do not replace validation (06-04) when bad input is possible.

### Reading hints with tools

`typing.get_type_hints` returns a function's hints as a dictionary, which is how tools (and this lesson's tests) inspect them:

```python
print(get_type_hints(find_index))
```

```
{'items': list[str], 'target': <class 'str'>, 'return': typing.Optional[int]}
```

### Checking hints with mypy

**mypy** is a separate program that reads your code and reports type mistakes without running it. It is not part of this course's requirements, but you can try it with `pip install mypy` then `mypy your_file.py`. For `count_words(["not", "a", "string"])` it reports something like `error: Argument 1 to "count_words" has incompatible type "list[str]"; expected "str"`. Many teams run it alongside their tests.

## Common mistakes

- **Using capitalised `List`, `Dict` from `typing` in new code.** These still work, but since Python 3.9 the built-in `list[int]` and `dict[str, int]` are preferred.
- **Forgetting `None` in the return type.** A function annotated `-> int` that can return `None` misleads callers. Write `-> int | None`.
- **Hinting the value instead of the type.** `def f(x: 5)` is legal but meaningless. Hints are types, such as `int`.
- **Expecting a hint to reject bad arguments.** As shown above, Python ignores hints at runtime. Validate explicitly when it matters.

## Try it

Add hints to three functions you wrote in earlier modules (for example in your expense tracker). If you install mypy, run it on that file and fix whatever it reports.

## Exercises

Open `ex_11_02.py`. Write each function body **and** add type hints exactly as described in its docstring. The tests check both the behaviour and the hints.

1. `mean`: the average of a list of floats.
2. `word_lengths`: a dictionary of word lengths.
3. `first_long_word`: the first word at least a given length, or `None`.
4. `split_pair`: split text into exactly two parts.

Run the tests:

```
python -m pytest part-2-intermediate-python/11-writing-reliable-code/11-02-type-hints
```

## Summary

- `def f(x: int) -> str:` annotates parameters and the return value; `name: type = value` annotates variables.
- `list[int]`, `dict[str, int]`, `set[str]` and `tuple[int, int]` describe collections.
- `Optional[int]` and `int | None` mean "an int or None"; `Callable` and `Iterable` describe functions and loopable things.
- Hints are stored but not enforced at runtime; editors and mypy use them to catch mistakes early.
