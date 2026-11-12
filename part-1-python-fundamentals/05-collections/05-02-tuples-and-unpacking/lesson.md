# 05-02 Tuples and unpacking

## What you will learn

- Create tuples and explain how they differ from lists.
- Unpack a sequence into separate variables, including swapping two values.
- Return several values from one function.
- Pair up items from several sequences with `zip`.

## Why it matters

Tuples are how Python groups a few related values that belong together: a point's x and y, a row's name and score. You will see them constantly in data work. A NumPy array's shape is a tuple such as `(150, 4)`, and scikit-learn's `train_test_split` returns four values that you unpack in one line: `X_train, X_test, y_train, y_test = ...`.

## Concepts

### Creating tuples

A **tuple** is an ordered collection, like a list, but **immutable**: once created it cannot be changed. Tuples are written with round brackets.

```python
point = (3, 4)
colour = ("red", 255, 0, 0)
single = (42,)
print(point, colour, single)
print(type(point), len(colour))
```

```
(3, 4) ('red', 255, 0, 0) (42,)
<class 'tuple'> 4
```

A one-item tuple needs a trailing comma: `(42,)`. Without the comma, `(42)` is just the number 42 in brackets.

Indexing and slicing work as usual, but assigning to an item does not:

```python
print(point[0], colour[-1])
```

```
3 0
```

`point[0] = 10` would fail with `TypeError: 'tuple' object does not support item assignment`.

### When to use a tuple

Use a **list** for a collection of similar things whose length may change: all the scores in a class. Use a **tuple** for a fixed group of values that together describe one thing: a single point, a single date as (year, month, day). Because tuples are immutable, they can also be dictionary keys, as you will see in 05-03.

### Packing and unpacking

It is actually the **commas** that make a tuple; the brackets are often optional. Writing several values separated by commas **packs** them into a tuple:

```python
packed = 1, 2, 3
print(packed)
```

```
(1, 2, 3)
```

The reverse is **unpacking**: assign a sequence to the same number of names, separated by commas, and each name gets one item.

```python
x, y = point
print("x is", x, "and y is", y)
name, red, green, blue = colour
print(name, red, green, blue)
```

```
x is 3 and y is 4
red 255 0 0
```

Unpacking works on any sequence (lists, strings, tuples), as long as the number of names matches the number of items.

### Swapping

Packing and unpacking together give a neat way to swap two variables without a temporary one:

```python
left = "L"
right = "R"
left, right = right, left
print(left, right)
```

```
R L
```

The right-hand side is packed into a tuple `("R", "L")` first, then unpacked into `left` and `right`.

### Returning several values

A function can only return one value, but that value can be a tuple. The caller can then unpack it:

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)


lowest, highest = min_and_max([7, 2, 9, 4])
print(lowest, highest)
print(min_and_max([7, 2, 9, 4]))
```

```
2 9
(2, 9)
```

### Star unpacking

A name with a `*` in front collects "everything else" into a list:

```python
first, *rest = [10, 20, 30, 40]
print(first, rest)
```

```
10 [20, 30, 40]
```

### zip

**`zip`** takes several sequences and pairs up their items by position, producing tuples. It is perfect for looping over two lists side by side:

```python
names = ["Ada", "Grace", "Alan"]
scores = [95, 88, 72]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
print(list(zip(names, scores)))
```

```
Ada: 95
Grace: 88
Alan: 72
[('Ada', 95), ('Grace', 88), ('Alan', 72)]
```

`zip` produces its pairs one at a time, so wrap it in `list()` to see them all at once. If the sequences have different lengths, `zip` stops at the shortest, without warning:

```python
print(list(zip([1, 2, 3], ["a", "b"])))
```

```
[(1, 'a'), (2, 'b')]
```

### Unpacking in loops

When a loop goes over a list of tuples, you can unpack each tuple directly in the `for` line. This is what you were doing with `enumerate` in 03-05: it produces `(index, item)` tuples.

```python
students = [("Ada", 36), ("Alan", 41)]
for name, age in students:
    print(name, "is", age)
print(list(enumerate(["x", "y"])))
```

```
Ada is 36
Alan is 41
[(0, 'x'), (1, 'y')]
```

## Common mistakes

- **Wrong number of names.** `a, b = (1, 2, 3)` gives `ValueError: too many values to unpack (expected 2)`; `a, b, c = (1, 2)` gives `ValueError: not enough values to unpack (expected 3, got 2)`.
- **Forgetting the comma in a one-item tuple.** `type((42))` is `<class 'int'>`. Write `(42,)`.
- **Trying to change a tuple.** `point[0] = 5` gives `TypeError: 'tuple' object does not support item assignment`. Build a new tuple, or use a list if the values need to change.
- **Silent truncation with `zip`.** If one list is accidentally shorter, `zip` quietly drops the extra items. Check that the lengths match when it matters.

## Try it

Given `dates = [(2026, 1, 15), (2025, 12, 3), (2026, 1, 2)]`, print `sorted(dates)`. Tuples are compared item by item, so dates written as (year, month, day) sort correctly. Why would (day, month, year) not work?

## Exercises

Open `ex_05_02.py`:

1. `min_max`: the smallest and largest values, as a tuple.
2. `swap_pair`: a two-item tuple with its items swapped.
3. `split_name`: first and last name from a full name, as a tuple.
4. `pair_up`: names and scores zipped into a list of tuples.
5. `distance`: the straight-line distance between two points given as tuples.

Run the tests:

```
python -m pytest part-1-python-fundamentals/05-collections/05-02-tuples-and-unpacking
```

## Summary

- A tuple is an ordered, immutable collection; a one-item tuple needs a trailing comma.
- Use tuples for fixed groups of related values, lists for collections that change.
- Unpacking assigns each item to its own name: `x, y = point`. `a, b = b, a` swaps.
- Return several values as a tuple and unpack them at the call.
- `zip` pairs up items from several sequences and stops at the shortest.
