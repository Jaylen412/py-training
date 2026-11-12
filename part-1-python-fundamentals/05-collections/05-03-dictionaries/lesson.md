# 05-03 Dictionaries

## What you will learn

- Store and look up values by key in a dictionary.
- Use `get` to look up a key that might be missing.
- Add, change and delete entries.
- Loop over keys, values and items, and count things with the counting pattern.

## Why it matters

Lists find things by position; dictionaries find things by name. That makes them the natural way to represent a record (a customer with a name, an age and a city), to count how often things occur, and to map one value to another. JSON files (Module 06) are dictionaries on disk, and a pandas DataFrame can be built straight from a dictionary of columns.

## Concepts

### Keys and values

A **dictionary** (type `dict`) stores **key-value pairs**. Each **key** is a label, and it maps to a **value**. You write a dictionary in curly brackets, with a colon between each key and its value:

```python
ages = {"Ada": 36, "Alan": 41, "Grace": 85}
print(ages)
print(ages["Alan"])
print(len(ages))
```

```
{'Ada': 36, 'Alan': 41, 'Grace': 85}
41
3
```

Square brackets with a key **look up** its value. Keys are unique: a dictionary cannot hold `"Ada"` twice. Dictionaries remember the order in which keys were added.

### get

Looking up a key that does not exist raises a `KeyError`. **`get(key)`** returns `None` instead, or a default value that you choose:

```python
print(ages.get("Grace"))
print(ages.get("Linus"))
print(ages.get("Linus", 0))
```

```
85
None
0
```

`in` checks whether a **key** exists (it does not look at the values):

```python
print("Ada" in ages, "Linus" in ages)
```

```
True False
```

### Adding, changing and deleting

Assigning to a key adds it if it is new, or replaces its value if it already exists. `del` removes a key, and `pop` removes it and returns its value.

```python
ages["Linus"] = 55
ages["Ada"] = 37
print(ages)
del ages["Grace"]
print(ages)
removed = ages.pop("Linus")
print(removed, ages)
```

```
{'Ada': 37, 'Alan': 41, 'Grace': 85, 'Linus': 55}
{'Ada': 37, 'Alan': 41, 'Linus': 55}
55 {'Ada': 37, 'Alan': 41}
```

### Looping

Looping over a dictionary gives its keys. The methods `keys()`, `values()` and `items()` let you choose; `items()` gives `(key, value)` tuples, which you unpack in the `for` line.

```python
prices = {"apple": 0.5, "bread": 1.2, "milk": 0.9}
for item in prices:
    print(item, end=" ")
print()
for item in prices.keys():
    print(item, end=" ")
print()
for price in prices.values():
    print(price, end=" ")
print()
for item, price in prices.items():
    print(f"{item} costs {price:.2f}")
```

```
apple bread milk 
apple bread milk 
0.5 1.2 0.9 
apple costs 0.50
bread costs 1.20
milk costs 0.90
```

### The counting pattern

To count how many times each thing occurs, use a dictionary whose keys are the things and whose values are the counts. `get(word, 0)` returns the current count, or 0 the first time a word is seen:

```python
words = "the cat and the hat and the bat".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)
```

```
{'the': 3, 'cat': 1, 'and': 2, 'hat': 1, 'bat': 1}
```

This one line, `counts[key] = counts.get(key, 0) + 1`, is one of the most useful in Python. To find the most common item, combine it with the maximum pattern from 03-05:

```python
best_word = None
best_count = 0
for word, count in counts.items():
    if count > best_count:
        best_word = word
        best_count = count
print("Most common:", best_word, best_count)
```

```
Most common: the 3
```

### What can be a key

Keys must be **immutable**: strings, numbers and tuples work, lists do not. Values can be anything, including lists and other dictionaries.

```python
locations = {(51.5, -0.1): "London", (48.9, 2.4): "Paris"}
print(locations[(51.5, -0.1)])
inventory = {"fruit": ["apple", "pear"], "count": 2}
print(inventory["fruit"][1])
```

```
London
pear
```

`inventory["fruit"][1]` reads left to right: get the value for `"fruit"` (a list), then item 1 of that list.

### Building a dictionary from pairs

`dict()` turns a sequence of pairs into a dictionary, which combines nicely with `zip`:

```python
keys = ["name", "language"]
values = ["Ada", "Python"]
record = dict(zip(keys, values))
print(record)
```

```
{'name': 'Ada', 'language': 'Python'}
```

## Common mistakes

- **Looking up a missing key.** `{"a": 1}["b"]` gives `KeyError: 'b'`. Use `get`, or check with `in` first.
- **Using a list as a key.** `{["a"]: 1}` gives `TypeError: unhashable type: 'list'`. Use a tuple instead.
- **Adding keys while looping over the same dictionary.** This gives `RuntimeError: dictionary changed size during iteration`. Collect the changes in a separate dictionary and apply them after the loop.
- **Expecting `in` to search values.** `36 in ages` is `False` even if someone is 36, because `in` checks keys. Use `36 in ages.values()`.

## Try it

Count the letters in `"mississippi"` with the counting pattern. Then use the maximum pattern to find the most common letter. There is a tie: which letter does your loop report, and why?

## Exercises

Open `ex_05_03.py`:

1. `word_counts`: count each word in a text, ignoring case.
2. `most_common_word`: the word that appears most often.
3. `invert`: swap keys and values.
4. `merge_inventory`: combine two stock dictionaries, adding quantities.
5. `price_of_basket`: the total price of a basket, ignoring unknown items.

Run the tests:

```
python -m pytest part-1-python-fundamentals/05-collections/05-03-dictionaries
```

## Summary

- A dictionary maps unique, immutable keys to values: `{"key": value}`.
- `d[key]` looks up (and raises `KeyError` if missing); `d.get(key, default)` is the safe version.
- Assigning to `d[key]` adds or replaces; `del` and `pop` remove.
- Loop with `keys()`, `values()` or `items()`; `in` checks keys.
- The counting pattern: `counts[key] = counts.get(key, 0) + 1`.
