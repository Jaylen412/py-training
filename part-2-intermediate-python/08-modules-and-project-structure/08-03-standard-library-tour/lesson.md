# 08-03 Standard library tour

## What you will learn

- Use `math` for common mathematical functions and safe float comparison.
- Generate repeatable random numbers with `random.Random` and a seed.
- Work with dates, times and durations using `datetime`.
- Count and group with `collections.Counter` and `defaultdict`, and generate combinations with `itertools`.

## Why it matters

Python's **standard library** is the large collection of modules that comes with every installation. Before writing something yourself, check whether it is already there: it will be tested, fast and familiar to other programmers. The modules in this lesson appear constantly in data work. Seeds in particular are essential: from Part 3 onwards every random step is seeded, so that results can be reproduced.

## Concepts

All the examples use these imports:

```python
import itertools
import math
import random
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
```

### math

```python
print(math.sqrt(2), math.pi)
print(math.isclose(0.1 + 0.2, 0.3))
print(math.log10(1000), math.exp(0))
print(math.dist((0, 0), (3, 4)))
```

```
1.4142135623730951 3.141592653589793
True
3.0 1.0
5.0
```

`math.isclose` is the right way to compare floats (02-01): it is `True` when two numbers are equal apart from tiny rounding errors. `math.log10`, `math.log` (natural logarithm) and `math.exp` will reappear when you transform skewed data in Module 16.

### random and seeds

Computers generate **pseudo-random** numbers: a sequence that looks random but is completely determined by a starting value called the **seed**. Same seed, same sequence, every time. Create your own generator with `random.Random(seed)`:

```python
rng = random.Random(42)
print(rng.randint(1, 6), rng.randint(1, 6), rng.randint(1, 6))
print(rng.choice(["rock", "paper", "scissors"]))
cards = ["A", "K", "Q", "J"]
rng.shuffle(cards)
print(cards)
print(rng.sample(range(100), 3))
```

```
6 1 1
scissors
['K', 'J', 'A', 'Q']
[17, 94, 13]
```

- `randint(a, b)` gives a whole number from `a` to `b`, **including** `b`.
- `choice(items)` picks one item; `sample(items, k)` picks `k` different items.
- `shuffle(items)` reorders a list in place.

Run the file again and you get exactly the same numbers, because the seed is fixed. That is what you want for reproducible experiments and tests. Without a seed, each run differs.

### datetime

The `datetime` module represents dates and times as objects, so you can compare them and do arithmetic without worrying about month lengths or leap years.

```python
release = date(2026, 3, 14)
print(release, release.year, release.strftime("%A %d %B %Y"))
print(date.fromisoformat("2026-11-11").weekday())
print(release + timedelta(days=30))
print((date(2026, 12, 25) - date(2026, 11, 11)).days)
```

```
2026-03-14 2026 Saturday 14 March 2026
2
2026-04-13
44
```

- `date(year, month, day)` makes a date; `date.fromisoformat("YYYY-MM-DD")` parses one.
- `weekday()` numbers the days from Monday = 0, so 2 is a Wednesday.
- A **`timedelta`** is a duration. Adding one to a date gives a new date; subtracting two dates gives a `timedelta`, whose `.days` is the gap in days.
- `strftime` formats a date as text using codes: `%A` weekday name, `%d` day, `%B` month name, `%Y` year.

`datetime` objects hold a date **and** a time. `strptime` ("string parse time") reads text in a format you describe:

```python
moment = datetime(2026, 11, 11, 9, 30)
print(moment.isoformat(), moment.hour)
print(datetime.strptime("11/11/2026 14:05", "%d/%m/%Y %H:%M"))
```

```
2026-11-11T09:30:00 9
2026-11-11 14:05:00
```

### Counter

**`Counter`** is the counting pattern from 05-03 in a single call. It behaves like a dictionary of counts, and a missing key counts as 0 instead of raising `KeyError`:

```python
words = "the cat and the hat and the bat".split()
counts = Counter(words)
print(counts["the"], counts["dog"])
print(counts.most_common(2))
```

```
3 0
[('the', 3), ('and', 2)]
```

`most_common(n)` returns the `n` most frequent items as `(item, count)` tuples, most frequent first.

### defaultdict

A **`defaultdict`** is a dictionary that creates a missing value automatically the first time you use a key. `defaultdict(list)` starts each new key with an empty list, so the grouping pattern from 05-05 loses its `if key not in` check:

```python
people = [("Ada", "London"), ("Alan", "Leeds"), ("Grace", "London")]
by_city = defaultdict(list)
for name, city in people:
    by_city[city].append(name)
print(dict(by_city))
```

```
{'London': ['Ada', 'Grace'], 'Leeds': ['Alan']}
```

`defaultdict(int)` starts at 0, which is another way to count. `dict(...)` converts it back to an ordinary dictionary for printing or returning.

### itertools

`itertools` builds sequences from other sequences. Its results are produced one at a time, so wrap them in `list()` to see them.

```python
print(list(itertools.combinations(["a", "b", "c"], 2)))
print(list(itertools.permutations([1, 2, 3], 2))[:4])
print(list(itertools.product(["S", "M"], ["red", "blue"])))
print(list(itertools.chain([1, 2], [3], [4, 5])))
print(list(itertools.accumulate([1, 2, 3, 4])))
```

```
[('a', 'b'), ('a', 'c'), ('b', 'c')]
[(1, 2), (1, 3), (2, 1), (2, 3)]
[('S', 'red'), ('S', 'blue'), ('M', 'red'), ('M', 'blue')]
[1, 2, 3, 4, 5]
[1, 3, 6, 10]
```

- `combinations(items, k)`: every group of `k` where order does not matter.
- `permutations(items, k)`: every ordering of `k` items.
- `product(a, b)`: every pairing of an item from `a` with one from `b`, like nested loops. You will use this idea for hyperparameter grids in Module 24.
- `chain(...)`: one sequence after another.
- `accumulate(items)`: running totals, like your `running_totals` from 05-01.

## Common mistakes

- **Expecting reproducible randomness without a seed.** Unseeded results change every run. Use `random.Random(seed)`.
- **Impossible dates.** `date(2026, 2, 30)` gives `ValueError: day is out of range for month`. `datetime` checks dates for you, which is a feature: catch the `ValueError` when parsing user input.
- **Wrong date format.** `date.fromisoformat("2026/11/11")` gives `ValueError: Invalid isoformat string: '2026/11/11'`. Use `datetime.strptime` with a matching format for non-ISO text.
- **Forgetting that `randint` includes the top value.** `randint(1, 6)` can return 6, unlike `range(1, 6)`.

## Try it

Using `date` and `timedelta`, print the dates of the next five Mondays after today's date (`date.today()`). Then use `Counter` on `[d.strftime("%B") for d in ...]` to count how many fall in each month.

## Exercises

Open `ex_08_03.py`:

1. `days_between`: the number of days between two ISO dates.
2. `weekday_name`: the name of the weekday for an ISO date.
3. `top_words`: the most common words in a text, with `Counter`.
4. `group_by_length`: words grouped by length, with `defaultdict`.
5. `all_pairs`: every pair of items, with `itertools.combinations`.
6. `roll_dice`: repeatable dice rolls from a seed.

Run the tests:

```
python -m pytest part-2-intermediate-python/08-modules-and-project-structure/08-03-standard-library-tour
```

## Summary

- `math` has `sqrt`, `log`, `exp`, `dist` and `isclose` for comparing floats.
- `random.Random(seed)` gives a repeatable random number generator; always seed experiments.
- `date`, `datetime` and `timedelta` handle calendar arithmetic; `fromisoformat`, `strptime` and `strftime` convert to and from text.
- `Counter` counts in one line; `defaultdict(list)` groups without key checks.
- `itertools` provides `combinations`, `permutations`, `product`, `chain` and `accumulate`.
