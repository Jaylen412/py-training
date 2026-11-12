# 05-01 Lists

## What you will learn

- Create lists and read items with indexing and slicing.
- Change lists in place with `append`, `extend`, `insert`, `pop` and `remove`.
- Summarise a list with `len`, `sum`, `min` and `max`.
- Choose between `sort()` and `sorted()`.

## Why it matters

A single value is rarely interesting; data comes in collections. A column of a spreadsheet, the scores of every student, the predictions of a model for a thousand customers: all of these start life as lists. NumPy arrays and pandas columns, which you will use from Part 3 onwards, are built on the same ideas.

## Concepts

### Creating lists

A **list** is an ordered collection of values, written in square brackets and separated by commas. Each value is an **item** (or element). A list can hold any types, even a mixture, and can be empty.

```python
scores = [72, 95, 88, 61]
names = ["Ada", "Grace", "Alan"]
mixed = [1, "two", 3.0, True]
empty = []
print(scores)
print(len(scores), len(empty))
```

```
[72, 95, 88, 61]
4 0
```

In practice, keep one type per list. A list of scores should contain only numbers.

### Indexing and slicing

Lists are sequences, like strings, so indexing and slicing work exactly the same way: indexes start at 0, negative indexes count from the end, and slices exclude the stop index.

```python
print(scores[0], scores[-1])
print(scores[1:3])
print(names[::-1])
```

```
72 61
[95, 88]
['Alan', 'Grace', 'Ada']
```

A slice of a list is a new list.

### Lists are mutable

Unlike strings, lists are **mutable**: you can change them in place. Assigning to an index replaces that item:

```python
scores[0] = 75
print(scores)
```

```
[75, 95, 88, 61]
```

### Adding items

- `append(item)` adds one item to the end.
- `extend(other_list)` adds every item from another list to the end.
- `insert(index, item)` puts an item at a position, shifting the rest along.

```python
scores.append(80)
print(scores)
scores.extend([90, 55])
print(scores)
scores.insert(1, 100)
print(scores)
```

```
[75, 95, 88, 61, 80]
[75, 95, 88, 61, 80, 90, 55]
[75, 100, 95, 88, 61, 80, 90, 55]
```

These methods change the list and return `None`. They do not give back a new list.

### Removing items

- `pop()` removes the last item **and returns it**; `pop(index)` removes the item at that index.
- `remove(value)` removes the first item equal to `value`.

```python
last = scores.pop()
print("Popped:", last, "->", scores)
first = scores.pop(0)
print("Popped:", first, "->", scores)
scores.remove(100)
print("Removed 100 ->", scores)
```

```
Popped: 55 -> [75, 100, 95, 88, 61, 80, 90]
Popped: 75 -> [100, 95, 88, 61, 80, 90]
Removed 100 -> [95, 88, 61, 80, 90]
```

### Searching

`in` checks membership, `index(value)` gives the position of the first match, and `count(value)` counts matches:

```python
print(88 in scores)
print(scores.index(88))
print(scores.count(90))
```

```
True
1
1
```

### Built-in summaries

`sum`, `min` and `max` work on any list of numbers. Together with `len`, they give you an average:

```python
print(sum(scores), min(scores), max(scores))
print(sum(scores) / len(scores))
```

```
414 61 95
82.8
```

In Module 03 you wrote these loops by hand. Now you know what the built-ins do underneath.

### sort() versus sorted()

There are two ways to sort, and mixing them up is a classic bug:

- `my_list.sort()` sorts the list **in place** and returns `None`.
- `sorted(my_list)` returns a **new** sorted list and leaves the original alone.

```python
numbers = [3, 1, 2]
result = numbers.sort()
print(numbers, result)
letters = ["c", "a", "b"]
ordered = sorted(letters)
print(letters, ordered)
print(sorted(scores, reverse=True))
```

```
[1, 2, 3] None
['c', 'a', 'b'] ['a', 'b', 'c']
[95, 90, 88, 80, 61]
```

Both accept `reverse=True` for largest-first. Use `sorted` when you want to keep the original order too.

### Building a new list in a loop

A very common pattern: start with an empty list and `append` to it inside a loop. This is the accumulator pattern from 03-04 with a list as the accumulator.

```python
prices = [4.99, 12.50, 3.25]
with_tax = []
for price in prices:
    with_tax.append(round(price * 1.2, 2))
print(with_tax)
```

```
[5.99, 15.0, 3.9]
```

`list()` turns any sequence into a list:

```python
print(list("abc"))
print(list(range(5)))
```

```
['a', 'b', 'c']
[0, 1, 2, 3, 4]
```

## Common mistakes

- **Storing the result of `sort()`.** `numbers = numbers.sort()` sets `numbers` to `None`. Call `numbers.sort()` on its own line, or use `numbers = sorted(numbers)`.
- **Index out of range.** `[1, 2, 3][3]` gives `IndexError: list index out of range`. The last index is `len - 1`.
- **Removing something that is not there.** `remove(9)` gives `ValueError: list.remove(x): x not in list`, and `pop()` on an empty list gives `IndexError: pop from empty list`. Check with `in` or `len` first.
- **`append` where you meant `extend`.** `[1, 2].append([3, 4])` gives `[1, 2, [3, 4]]`, a list inside a list. Use `extend` to add the items one by one.

## Try it

Start with `queue = []`. Use `append` to add three names, then `pop(0)` twice. Who is left? You have just built a first-in, first-out queue.

## Exercises

Open `ex_05_01.py`:

1. `average`: the mean of a list of numbers, or 0.0 for an empty list.
2. `remove_all`: a new list with every copy of a value taken out.
3. `top_three`: the three largest values, largest first.
4. `rotate_left`: move the first items to the end.
5. `running_totals`: a list of cumulative sums.
6. `insert_sorted`: put a value into an already sorted list, keeping it sorted.

Run the tests:

```
python -m pytest part-1-python-fundamentals/05-collections/05-01-lists
```

## Summary

- A list is an ordered, mutable collection: `[item, item, ...]`.
- Indexing and slicing work as for strings; assigning to an index changes the list.
- `append`, `extend`, `insert`, `pop` and `remove` change the list in place.
- `len`, `sum`, `min`, `max`, `in`, `index` and `count` summarise and search.
- `list.sort()` sorts in place and returns `None`; `sorted(list)` returns a new list.
