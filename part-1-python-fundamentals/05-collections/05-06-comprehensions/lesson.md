# 05-06 Comprehensions

## What you will learn

- Build a new list from an old one in a single line with a list comprehension.
- Filter items with an `if` clause.
- Write dictionary and set comprehensions.
- Decide when a plain loop is clearer than a comprehension.

## Why it matters

"Make a new list by doing something to each item" is so common that Python has a dedicated syntax for it. Comprehensions are everywhere in data-science code: building lists of feature names, cleaning a list of strings, creating a dictionary of model scores. Reading them fluently is essential for understanding other people's code.

## Concepts

### List comprehensions

Here is the build-a-list pattern from 05-01:

```python
squares = []
for number in range(1, 6):
    squares.append(number ** 2)
print(squares)
```

A **list comprehension** says the same thing in one expression: square brackets around *what to put in the list*, then the `for` clause.

```python
squares = [number ** 2 for number in range(1, 6)]
print(squares)
```

```
[1, 4, 9, 16, 25]
[1, 4, 9, 16, 25]
```

Read it as "a list of `number ** 2` for each `number` in `range(1, 6)`". The expression at the front can be anything:

```python
names = ["ada", "alan", "grace"]
print([name.title() for name in names])
print([len(name) for name in names])
```

```
['Ada', 'Alan', 'Grace']
[3, 4, 5]
```

### Filtering with if

Adding `if condition` at the end keeps only the items for which the condition is true:

```python
numbers = [5, -2, 8, 0, -7, 3]
print([number for number in numbers if number > 0])
print([number * 10 for number in numbers if number % 2 == 0])
```

```
[5, 8, 3]
[-20, 80, 0]
```

The filter is applied first, then the expression: `-2`, `8` and `0` are even, and each is multiplied by 10.

### Choosing a value instead of filtering

To keep every item but choose what to put in, use a conditional expression (03-01) at the **front**:

```python
print(["even" if number % 2 == 0 else "odd" for number in numbers])
```

```
['odd', 'even', 'even', 'even', 'odd', 'odd']
```

Remember the difference: an `if` at the **end** filters (the list may get shorter); `if ... else` at the **front** chooses (the list stays the same length).

### Dictionary comprehensions

A **dictionary comprehension** uses curly brackets and a `key: value` pair:

```python
print({name: len(name) for name in names})
prices = {"apple": 0.5, "bread": 1.2, "milk": 0.9}
print({item: round(price * 1.2, 2) for item, price in prices.items()})
print({item: price for item, price in prices.items() if price > 0.6})
```

```
{'ada': 3, 'alan': 4, 'grace': 5}
{'apple': 0.6, 'bread': 1.44, 'milk': 1.08}
{'bread': 1.2, 'milk': 0.9}
```

The second line transforms every value; the third keeps only some entries.

### Set comprehensions

Curly brackets with a single expression (no colon) make a **set comprehension**, which drops duplicates:

```python
words = ["apple", "avocado", "banana", "blueberry", "cherry"]
print(sorted({word[0] for word in words}))
```

```
['a', 'b', 'c']
```

### Two for clauses

A comprehension can have more than one `for`. They are read in the same order as nested loops, outer first. The most common use is **flattening** a list of lists into one list:

```python
grid = [[1, 2, 3], [4, 5, 6]]
print([value for row in grid for value in row])
```

```
[1, 2, 3, 4, 5, 6]
```

This means: for each `row` in `grid`, for each `value` in `row`, take `value`.

### Feeding comprehensions into functions

`sum`, `max` and `min` accept the list a comprehension builds. So do two new built-ins: **`any`** returns `True` if at least one item is truthy, and **`all`** returns `True` if every item is truthy. They replace the flag patterns from 03-05.

```python
print(sum([number ** 2 for number in range(1, 6)]))
print(max([len(word) for word in words]))
print(any([number < 0 for number in numbers]))
print(all([len(word) > 4 for word in words]))
```

```
55
9
True
True
```

### When a plain loop is clearer

Comprehensions are for **simple** transformations and filters. If each item needs several steps, temporary variables, or nested conditions, write a loop. This is easy to follow:

```python
report = []
for word in words:
    first_letter = word[0].upper()
    length = len(word)
    if length > 5:
        report.append(f"{first_letter}: {word} ({length})")
print(report)
```

```
['A: avocado (7)', 'B: banana (6)', 'B: blueberry (9)', 'C: cherry (6)']
```

Squeezing that into one comprehension would work, but nobody would enjoy reading it. A good rule: if the comprehension does not fit comfortably on one line, or you have to read it twice, use a loop. Also, never use a comprehension just for its side effects (such as printing); comprehensions are for building collections.

## Common mistakes

- **Putting a filter `if` at the front without `else`.** `[x if x > 0 for x in numbers]` is a `SyntaxError`. A filter goes at the end: `[x for x in numbers if x > 0]`.
- **Forgetting the closing bracket.** `[x for x in range(3)` gives `SyntaxError: '[' was never closed`.
- **Writing the two `for` clauses in the wrong order.** `[value for value in row for row in grid]` fails with `NameError`, because `row` is used before it is defined. Outer loop first.
- **Overly clever comprehensions.** If you need comments to explain one, rewrite it as a loop.

## Try it

Using one comprehension, make a list of the numbers from 1 to 50 that are divisible by 7 but not by 2. Then write a dictionary comprehension mapping each of those numbers to its square.

## Exercises

Open `ex_05_06.py`. Use a comprehension in each function.

1. `squares_of_evens`: the squares of the even numbers in a list.
2. `clean_words`: stripped, lower-cased words, dropping empty ones.
3. `word_lengths`: a dictionary mapping each word to its length.
4. `initials_set`: the set of first letters, in upper case.
5. `flatten`: a list of lists turned into one list.
6. `apply_discount`: a price dictionary with discounted prices for items above a threshold.

Run the tests:

```
python -m pytest part-1-python-fundamentals/05-collections/05-06-comprehensions
```

## Summary

- `[expression for item in sequence]` builds a list; add `if condition` at the end to filter.
- `a if condition else b` at the front chooses a value; `if` at the end filters.
- `{key: value for ...}` builds a dictionary; `{expression for ...}` builds a set.
- Multiple `for` clauses are read in nested-loop order, outer first.
- `any` and `all` answer "is there any?" and "are they all?"; use a plain loop when a comprehension gets complicated.
