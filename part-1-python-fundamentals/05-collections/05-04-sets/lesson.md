# 05-04 Sets

## What you will learn

- Create sets and use them to remove duplicates.
- Test membership quickly with `in`.
- Combine sets with union, intersection and difference.
- Check whether one set is contained in another.

## Why it matters

"How many different customers bought something?", "Which products appear in both shops?", "Which required columns are missing from this file?" are all set questions. Sets answer them in one line. In Part 5, checking which category values appear in the test data but never in the training data is a set difference.

## Concepts

### Creating sets

A **set** is an unordered collection of **unique** values, written in curly brackets. Adding a value that is already there does nothing.

```python
colours = {"red", "green", "blue", "red"}
print(len(colours))
print(sorted(colours))
```

```
3
['blue', 'green', 'red']
```

Because sets have **no order**, printing a set can show its items in any order, and it may differ between runs. In this course we wrap sets in `sorted()` when printing so the output is predictable. `sorted` always returns a list.

### Removing duplicates

`set()` turns any sequence into a set, dropping the duplicates:

```python
visits = ["home", "about", "home", "blog", "home"]
unique_pages = set(visits)
print(len(visits), len(unique_pages))
print(sorted(unique_pages))
```

```
5 3
['about', 'blog', 'home']
```

`len(set(items))` is the standard way to count distinct values.

An **empty** set must be written `set()`, because `{}` makes an empty dictionary:

```python
empty_set = set()
empty_dict = {}
print(type(empty_set), type(empty_dict))
```

```
<class 'set'> <class 'dict'>
```

### Adding and removing

`add` puts in one value. `discard` removes a value if it is present and quietly does nothing if it is not. (`remove` also exists, but raises a `KeyError` for a missing value.)

```python
tags = {"python"}
tags.add("data")
tags.add("python")
print(sorted(tags))
tags.discard("data")
tags.discard("missing")
print(sorted(tags))
```

```
['data', 'python']
['python']
```

### Fast membership tests

Checking `value in my_set` is extremely fast, even for millions of items, because of how sets are stored. Checking `value in my_list` has to look through the list item by item. (Module 12 measures this difference.) Whenever you mainly ask "is this in the collection?", use a set.

```python
allowed = {"admin", "editor", "viewer"}
print("editor" in allowed, "guest" in allowed)
```

```
True False
```

### Set operations

Sets support the operations from maths, written with operators:

| Operator | Name | Result |
|----------|------|--------|
| `a \| b` | union | items in either set |
| `a & b` | intersection | items in both sets |
| `a - b` | difference | items in `a` but not in `b` |
| `a ^ b` | symmetric difference | items in exactly one of the sets |

```python
python_fans = {"Ada", "Alan", "Grace", "Linus"}
java_fans = {"Grace", "James", "Linus"}
print(sorted(python_fans | java_fans))
print(sorted(python_fans & java_fans))
print(sorted(python_fans - java_fans))
print(sorted(python_fans ^ java_fans))
```

```
['Ada', 'Alan', 'Grace', 'James', 'Linus']
['Grace', 'Linus']
['Ada', 'Alan']
['Ada', 'Alan', 'James']
```

The same operations exist as methods with readable names:

```python
print(sorted(python_fans.union(java_fans)))
print(sorted(python_fans.intersection(java_fans)))
print(sorted(python_fans.difference(java_fans)))
```

```
['Ada', 'Alan', 'Grace', 'James', 'Linus']
['Grace', 'Linus']
['Ada', 'Alan']
```

### Subsets

`a <= b` (or `a.issubset(b)`) is `True` if every item of `a` is also in `b`. A typical use is checking that all required fields are present:

```python
required = {"name", "email"}
provided = {"name", "email", "phone"}
print(required <= provided)
print(required.issubset(provided))
```

```
True
True
```

### No indexes

Because sets have no order, they have no indexes. You can loop over a set, check membership and get its length, but `my_set[0]` is an error. Like dictionary keys, set items must be immutable.

```python
letters = set("hello")
print(len(letters), "l" in letters)
```

```
4 True
```

## Common mistakes

- **Indexing a set.** `{1, 2}[0]` gives `TypeError: 'set' object is not subscriptable`. Convert to a sorted list first if you need positions.
- **Writing `{}` for an empty set.** It creates a dictionary. Write `set()`.
- **Putting a list in a set.** `{[1, 2]}` gives `TypeError: unhashable type: 'list'`. Use a tuple.
- **Relying on set order.** Never assume a set prints or loops in any particular order. Sort it when order matters.

## Try it

A pangram is a sentence that uses every letter of the alphabet. Build `set("abcdefghijklmnopqrstuvwxyz")` and use a subset test to check whether `"The quick brown fox jumps over the lazy dog"` is a pangram. Remember to lower-case it.

## Exercises

Open `ex_05_04.py`:

1. `unique_count`: how many distinct values a list contains.
2. `has_duplicates`: whether a list contains any value more than once.
3. `common_items`: the items two lists share, sorted.
4. `only_in_first`: the items in one list but not the other, sorted.
5. `missing_fields`: which required fields a record is missing, sorted.
6. `is_pangram`: whether a sentence uses every letter of the alphabet.

Run the tests:

```
python -m pytest part-1-python-fundamentals/05-collections/05-04-sets
```

## Summary

- A set is an unordered collection of unique, immutable values; `set()` is the empty set.
- `set(sequence)` removes duplicates; `len(set(items))` counts distinct values.
- `in` is very fast on sets.
- `|`, `&`, `-` and `^` give union, intersection, difference and symmetric difference.
- `a <= b` tests whether `a` is a subset of `b`; sets have no indexes or order.
