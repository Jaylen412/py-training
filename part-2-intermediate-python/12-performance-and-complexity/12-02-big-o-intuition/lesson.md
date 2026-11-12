# 12-02 Big-O intuition

## What you will learn

- Describe how an algorithm's running time grows with its input, using Big-O notation.
- Recognise constant, logarithmic, linear and quadratic growth.
- Explain why `in` is fast for sets and dictionaries but slow for lists.
- Rewrite a quadratic algorithm as a linear one.

## Why it matters

Measuring (12-01) tells you how fast code is today, on today's data. Big-O tells you what will happen when the data gets bigger, which it always does. Code that takes a second on 1,000 rows can take 17 minutes on 1,000,000 rows if it is quadratic. In machine learning, an algorithm's complexity decides whether it is usable at all on a large dataset: you will see this with k-nearest neighbours and hierarchical clustering in Parts 5 and 6.

## Concepts

### Counting steps

Instead of timing code, count how many basic steps it takes as the input size, written **n**, grows. Three ways of working with a list of n items:

```python
def linear_search_steps(items, target):
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            break
    return steps


def binary_search_steps(sorted_items, target):
    low, high = 0, len(sorted_items) - 1
    steps = 0
    while low <= high:
        steps += 1
        middle = (low + high) // 2
        if sorted_items[middle] == target:
            break
        if sorted_items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return steps


def all_pairs_steps(items):
    steps = 0
    for first in items:
        for second in items:
            steps += 1
    return steps
```

**Linear search** checks items one by one. **Binary search** only works on a sorted list: it looks at the middle item and throws away whichever half cannot contain the target, then repeats. Comparing **all pairs** uses nested loops. Searching for the last item (the worst case):

```
        n    linear  binary          pairs
       10        10       4            100
      100       100       7          10000
     1000      1000      10        1000000
     3000      3000      12        9000000
```

As n goes from 10 to 1,000 (100 times bigger), linear search does 100 times more work, binary search goes from 4 steps to 10, and all-pairs does 10,000 times more.

### Big-O notation

**Big-O notation** describes this growth rate, ignoring constant factors and small details. It answers: "if n doubles, what happens to the work?"

| Big-O | Name | If n doubles... | Example |
|-------|------|-----------------|---------|
| O(1) | constant | no change | `my_dict[key]`, `my_list[5]`, `x in my_set` |
| O(log n) | logarithmic | one extra step | binary search |
| O(n) | linear | work doubles | linear search, `sum`, `x in my_list` |
| O(n log n) | "n log n" | a bit more than doubles | `sorted` |
| O(n²) | quadratic | work quadruples | comparing all pairs |

In words: O(n) means "the work grows in proportion to the size of the input". O(n²) means "in proportion to the square of the size". O(log n) means the work grows with the number of times you can halve n, which is very slowly: about 20 steps for a million items, 30 for a billion.

### Membership: list versus set versus dict

`x in my_list` has to compare `x` with the items one by one: O(n). Sets and dictionaries store their items using a **hash**, a number computed from each item that says where it is stored, so `x in my_set` jumps straight to the right place: O(1) on average. Timing a search for a value that is not there:

```python
for size in [1_000, 100_000]:
    as_list = list(range(size))
    as_set = set(as_list)
    as_dict = dict.fromkeys(as_list)
    missing = -1
    list_time = timeit.timeit(lambda: missing in as_list, number=200) / 200
    set_time = timeit.timeit(lambda: missing in as_set, number=200) / 200
    dict_time = timeit.timeit(lambda: missing in as_dict, number=200) / 200
    print(f"n={size:>7}: list {list_time * 1e6:9.2f} us   set {set_time * 1e6:6.3f} us   dict {dict_time * 1e6:6.3f} us")
```

```
n=   1000: list      2.67 us   set  0.025 us   dict  0.023 us
n= 100000: list    356.86 us   set  0.028 us   dict  0.025 us
```

A list 100 times longer took about 100 times longer to search. The set and dictionary did not slow down at all. (`dict.fromkeys(items)` builds a dictionary with those keys, all with the value `None`.) This is why 05-04 said "use a set whenever you mainly ask whether something is in a collection".

### From O(n²) to O(n)

A common pattern is a loop that does a linear operation inside it, giving O(n²) without it being obvious. Checking a list for duplicates by comparing every pair:

```python
def has_duplicates_slow(items):
    for index, first in enumerate(items):
        for second in items[index + 1:]:
            if first == second:
                return True
    return False


def has_duplicates_fast(items):
    return len(set(items)) < len(items)


numbers = list(range(2_000))
slow = timeit.timeit(lambda: has_duplicates_slow(numbers), number=3) / 3
fast = timeit.timeit(lambda: has_duplicates_fast(numbers), number=3) / 3
print(f"slow: {slow * 1000:.1f} ms, fast: {fast * 1000:.3f} ms, ratio: {slow / fast:.0f}x")
```

```
slow: 19.7 ms, fast: 0.011 ms, ratio: 1834x
```

For 2,000 items the set version is already about 1,800 times faster, and the gap grows with n: double the list and the slow version takes four times as long while the fast one takes twice as long. Building a set or dictionary first, then doing O(1) lookups, is the most common way to turn O(n²) code into O(n).

### Watch for hidden loops

Some innocent-looking operations are O(n) themselves, so putting them inside a loop makes the loop O(n²): `x in my_list`, `my_list.index(x)`, `my_list.remove(x)`, `my_list.insert(0, x)`, `my_list.count(x)`, and slicing such as `items[index + 1:]`, which copies part of the list.

## Common mistakes

- **Membership tests on a list inside a loop.** `for word in text: if word in stop_words_list:` is O(n × m). Convert `stop_words_list` to a set once, before the loop.
- **Thinking Big-O gives the speed.** It gives the growth rate. An O(n) algorithm with a large constant factor can be slower than an O(n²) one for small inputs; for large inputs, the lower growth rate always wins.
- **Binary searching an unsorted list.** Binary search only works if the list is sorted; on unsorted data it silently gives wrong answers.
- **Sorting inside a loop.** `sorted` is O(n log n); calling it every time round a loop over the same data multiplies that by n. Sort once.

## Try it

Write a function that finds every word that appears in both of two long texts. Write it first with `if word in other_words_list`, then with a set. Time both on texts of 1,000 and 10,000 words. Do the timings grow as Big-O predicts?

## Exercises

Open `ex_12_02.py`. The tests check correctness, and for the searches they also check how many comparisons you made.

1. `linear_search`: find an item, counting comparisons.
2. `binary_search`: find an item in a sorted list in O(log n) comparisons.
3. `common_elements`: the items two lists share, in O(n + m).
4. `two_sum`: find two numbers adding up to a target, in O(n) with a dictionary.

Run the tests:

```
python -m pytest part-2-intermediate-python/12-performance-and-complexity/12-02-big-o-intuition
```

## Summary

- Big-O describes how work grows with input size n, ignoring constant factors.
- O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) for sorting, O(n²) quadratic.
- `in` is O(n) on lists but O(1) on sets and dictionaries.
- Building a set or dictionary first is the usual way to turn O(n²) into O(n).
- Look out for O(n) operations hiding inside loops.
