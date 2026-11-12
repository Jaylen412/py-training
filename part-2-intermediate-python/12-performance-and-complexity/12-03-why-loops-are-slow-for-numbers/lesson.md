# 12-03 Why loops are slow for numbers

## What you will learn

- Measure the cost of a Python loop over a million numbers.
- Explain why pure-Python number crunching is slow: every number is an object.
- Prefer built-ins such as `sum`, and comprehensions, over hand-written loops.
- Write the core numerical operations of data science (mean, dot product, element-wise maths) in plain Python, ready to compare with NumPy in Part 3.

## Why it matters

Machine learning is arithmetic on large tables of numbers: a dataset might have a million rows and fifty columns, and training repeats calculations over all of them many times. Plain Python loops are too slow for that. This lesson shows why, and sets up the solution: **vectorised** libraries such as NumPy, which you start in the very next module and which do the same work tens to hundreds of times faster.

## Concepts

All timings come from one laptop. Your numbers will differ, but the comparisons should be similar.

### A million numbers

We make a list of a million random floats, seeded so you get the same values:

```python
import math
import random
import timeit

rng = random.Random(42)
values = [rng.random() for _ in range(1_000_000)]


def loop_sum(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total


loop_time = timeit.timeit(lambda: loop_sum(values), number=5) / 5
sum_time = timeit.timeit(lambda: sum(values), number=5) / 5
fsum_time = timeit.timeit(lambda: math.fsum(values), number=5) / 5
print(f"loop:      {loop_time * 1000:6.1f} ms  -> {loop_sum(values):.4f}")
print(f"sum():     {sum_time * 1000:6.1f} ms  -> {sum(values):.4f}")
print(f"math.fsum: {fsum_time * 1000:6.1f} ms  -> {math.fsum(values):.4f}")
print(f"the loop is {loop_time / sum_time:.1f}x slower than sum()")
```

```
loop:        10.2 ms  -> 500014.5439
sum():        2.4 ms  -> 500014.5439
math.fsum:    9.0 ms  -> 500014.5439
the loop is 4.3x slower than sum()
```

All three give the same answer. The built-in `sum` is about four times faster than the loop, because its loop runs inside Python's own C code rather than in Python. `math.fsum` is slower but more accurate, because it carefully avoids the float rounding errors from 02-01. (For these values the difference does not show at 4 decimal places.)

Ten milliseconds sounds fast. But training a model can mean doing this kind of pass over the data thousands of times, on many columns.

### Element-wise operations

A typical data-science operation combines two columns item by item, such as "scale this column and add that one":

```python
def scale_and_add_loop(first, second, factor):
    result = []
    for index in range(len(first)):
        result.append(first[index] * factor + second[index])
    return result


def scale_and_add_comprehension(first, second, factor):
    return [a * factor + b for a, b in zip(first, second)]


other = [rng.random() for _ in range(1_000_000)]
loop_time = timeit.timeit(lambda: scale_and_add_loop(values, other, 2.0), number=3) / 3
comp_time = timeit.timeit(lambda: scale_and_add_comprehension(values, other, 2.0), number=3) / 3
print(f"index loop:    {loop_time * 1000:6.1f} ms")
print(f"comprehension: {comp_time * 1000:6.1f} ms")
```

```
index loop:    30.7 ms
comprehension: 24.3 ms
```

The comprehension with `zip` is a little faster and clearer than indexing, but both are still tens of milliseconds for one simple operation.

### Why Python is slow at this

In Python, **every number is a full object**. A float is not just its 8 bytes of value; it carries a type, a reference count and more:

```python
print(type(values[0]).__name__, values[0].__sizeof__(), "bytes for one float object")
print("a list of 1,000,000 floats points to 1,000,000 separate objects")
```

```
float 24 bytes for one float object
a list of 1,000,000 floats points to 1,000,000 separate objects
```

A list does not hold the numbers themselves; it holds a million **references** to number objects scattered around memory. For each step of a loop, the Python interpreter must:

1. fetch the next reference and follow it to the object,
2. check the object's type to work out what `*` or `+` means for it,
3. create a brand-new object for the result,
4. update reference counts, and eventually free the old objects.

The actual multiplication is a tiny fraction of this work. All the rest is overhead, paid a million times.

### What vectorised libraries do differently

A library like **NumPy** stores numbers in a **packed array**: one block of memory holding raw 8-byte values side by side, all of the same type, with no per-number objects. An operation such as "multiply every element by 2" is written once and runs as a single tight loop in compiled C code: no type checks per element, no new objects, and it can use the processor's ability to work on several numbers at once. This style, writing one operation on a whole array instead of a loop over items, is called **vectorisation**.

The result is typically 10 to 100 times faster than Python loops, and the code is shorter. In Module 13 you will rerun these exact examples with NumPy and compare.

### The operations you will vectorise

Here are two operations you will meet constantly, written in plain Python. A **mean** is the sum divided by the count; a **dot product** multiplies two lists item by item and adds up the results (Module 17 explains why it matters so much in machine learning):

```python
def mean(numbers):
    return sum(numbers) / len(numbers)


def dot_product(first, second):
    return sum(a * b for a, b in zip(first, second))


print(f"mean: {mean(values):.4f}")
print(f"dot product: {dot_product(values, other):.1f}")
dot_time = timeit.timeit(lambda: dot_product(values, other), number=3) / 3
print(f"dot product of two 1,000,000-long lists: {dot_time * 1000:.1f} ms")
```

```
mean: 0.5000
dot product: 249910.6
dot product of two 1,000,000-long lists: 26.4 ms
```

The mean of random numbers between 0 and 1 is close to 0.5, as it should be.

## Common mistakes

- **Writing a loop when a built-in exists.** `sum`, `min`, `max`, `len`, `sorted`, `any` and `all` all run their loops in C. Use them.
- **Indexing in loops.** `for index in range(len(items)): items[index]` is slower and harder to read than `for item in items`, or `zip` for several lists.
- **Building with `+` in a loop.** `result = result + [value]` copies the whole list each time, which is O(n²). Use `append` or a comprehension.
- **Expecting pure Python to scale.** Code that is fine for a thousand numbers is often too slow for a million. That is the signal to reach for NumPy, not to micro-optimise loops.

## Try it

Time `mean(values)` against `statistics.mean(values)` from the standard library. Which is faster, and why might the library version be slower? (Hint: read the first paragraph of `help(statistics.mean)`.)

## Exercises

Open `ex_12_03.py`. These are the basic operations of numerical computing, written in plain Python. In Module 13 you will do each of them in one line of NumPy.

1. `mean`: the average of a list.
2. `dot_product`: multiply two lists item by item and sum.
3. `elementwise_add`: add two lists item by item.
4. `standardise`: turn values into z-scores.
5. `matrix_vector_multiply`: multiply a list of rows by a vector.

Run the tests:

```
python -m pytest part-2-intermediate-python/12-performance-and-complexity/12-03-why-loops-are-slow-for-numbers
```

## Summary

- Pure-Python loops over a million numbers take tens of milliseconds per pass.
- Built-ins like `sum` are faster than hand-written loops because their loops run in C.
- Every Python number is an object, so loops spend most of their time on overhead, not arithmetic.
- Vectorised libraries store raw numbers in packed arrays and run whole-array operations in compiled code.
- Next: NumPy, which makes these operations short and fast.
