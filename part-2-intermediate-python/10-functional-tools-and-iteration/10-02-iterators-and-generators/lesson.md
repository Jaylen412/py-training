# 10-02 Iterators and generators

## What you will learn

- Explain the iteration protocol: `iter`, `next` and `StopIteration`.
- Write generator functions with `yield`.
- Write generator expressions, and pass them straight to functions like `sum`.
- Use laziness to process large or endless data with little memory.

## Why it matters

A log file can have millions of lines; a dataset might not fit in memory at all. Generators let you process data **one item at a time**, never holding more than you need. Your Part 2 project reads its log file with generators. Data-loading code in machine learning works the same way, feeding a model batches of data one after another.

## Concepts

### The iteration protocol

An **iterable** is anything a `for` loop can go over: lists, strings, dictionaries, files, `range`. An **iterator** is an object that hands out the items of an iterable **one at a time**. Two built-ins drive it:

- `iter(iterable)` gets an iterator.
- `next(iterator)` returns the next item, and raises `StopIteration` when there are none left.

```python
letters = ["a", "b", "c"]
iterator = iter(letters)
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    next(iterator)
except StopIteration:
    print("StopIteration: no more items")
```

```
a
b
c
StopIteration: no more items
```

This is exactly what a `for` loop does behind the scenes: it calls `iter` once, then `next` repeatedly, and stops quietly at `StopIteration`.

An iterator remembers its position and **cannot be rewound**. Once used up, it stays empty. Results from `map`, `filter`, `zip` and `enumerate` are iterators:

```python
squares = map(lambda number: number ** 2, [1, 2, 3])
print(list(squares))
print(list(squares))
```

```
[1, 4, 9]
[]
```

### Generator functions

A **generator function** is a function containing **`yield`**. Calling it does not run the body; it returns a **generator**, which is an iterator. Each `next` runs the body until the next `yield`, hands out that value, and **pauses** there, keeping all its local variables, until the next `next`.

```python
def countdown(start):
    print("  (starting)")
    while start > 0:
        yield start
        start -= 1
    print("  (finished)")


generator = countdown(3)
print(type(generator).__name__)
for number in generator:
    print(number)
```

```
generator
  (starting)
3
2
1
  (finished)
```

Notice that `(starting)` was printed only when the loop asked for the first value, not when `countdown(3)` was called. Driving it by hand shows the pausing clearly:

```python
generator = countdown(2)
print(next(generator))
print("doing something else")
print(next(generator))
```

```
  (starting)
2
doing something else
1
```

The generator stopped after yielding 1, waiting. It never printed `(finished)`, because nobody asked for another value.

### Endless sequences

Because values are only produced on request, a generator can describe a sequence that never ends. The caller decides how many to take:

```python
def even_numbers():
    number = 0
    while True:
        yield number
        number += 2


evens = even_numbers()
print([next(evens) for _ in range(5)])
```

```
[0, 2, 4, 6, 8]
```

### Generator expressions

A **generator expression** looks like a list comprehension but with round brackets. It produces values lazily instead of building a list. (Underscores in a number like `1_000_000` are just for readability.)

```python
lazy_squares = (number ** 2 for number in range(1_000_000))
print(next(lazy_squares), next(lazy_squares), next(lazy_squares))
print(sum(number ** 2 for number in range(10)))
```

```
0 1 4
285
```

When a generator expression is the only argument to a function, you can drop its own brackets, as in `sum(number ** 2 for number in range(10))`. This is the idiomatic way to write totals: no temporary list is built.

### Laziness saves memory

A list holds all its items at once; a generator holds only its current state. `sys.getsizeof` shows the size of an object in bytes:

```python
as_list = [number for number in range(1_000_000)]
as_generator = (number for number in range(1_000_000))
print(sys.getsizeof(as_list) > 1_000_000, sys.getsizeof(as_generator) < 1_000)
```

```
True True
```

The list takes over a megabyte; the generator a couple of hundred bytes, whatever its length. Use a list when you need to keep the items, index them or loop over them more than once. Use a generator when you only pass through them once.

### Pipelines

Generators can feed each other, forming a **pipeline** in which each item flows through every step before the next item is read:

```python
def read_lines(text):
    for line in text.splitlines():
        yield line


def non_blank(lines):
    for line in lines:
        if line.strip():
            yield line.strip()


def as_numbers(lines):
    for line in lines:
        yield float(line)


raw = "3.5\n\n 4.5\n2\n"
print(sum(as_numbers(non_blank(read_lines(raw)))))
```

```
10.0
```

Each step is small and testable, and the whole pipeline uses the same small amount of memory whether the input has four lines or four million. Looping over an open file is already lazy, so `read_lines` could equally loop over a file object.

## Common mistakes

- **Reusing a used-up iterator.** The second loop over a generator does nothing. Create a fresh generator, or convert to a list if you need several passes.
- **Calling `next` past the end.** Gives `StopIteration`. Use a `for` loop, or `next(iterator, default)`, which returns `default` instead of raising.
- **Expecting a generator function to run immediately.** `countdown(3)` on its own does nothing visible. Loop over it, or pass it to `list`, `sum` and so on.
- **Taking `len()` of a generator.** `len(x for x in range(3))` gives `TypeError: object of type 'generator' has no len()`. Generators do not know their length in advance.

## Try it

Write a generator `fibonacci()` that yields 0, 1, 1, 2, 3, 5, 8, ... forever. Use it with a `for` loop and `break` to print the first Fibonacci number greater than 1,000.

## Exercises

Open `ex_10_02.py`. Use `yield` in the first four.

1. `countdown`: yield from a number down to 1.
2. `parse_numbers`: yield a float for each non-blank line, skipping comments.
3. `chunked`: yield lists of a fixed size from a sequence.
4. `running_average`: yield the average so far after each number.
5. `take`: return the first few items of any iterable, even an endless one.

Run the tests:

```
python -m pytest part-2-intermediate-python/10-functional-tools-and-iteration/10-02-iterators-and-generators
```

## Summary

- `iter` gets an iterator; `next` gets the next item; `StopIteration` signals the end. `for` loops do this for you.
- Iterators are single-use; results of `map`, `filter`, `zip` and generators are iterators.
- A function with `yield` returns a generator that runs lazily, pausing at each `yield`.
- `(expression for item in items)` is a generator expression; `sum(x for x in items)` needs no extra brackets.
- Generators use little memory and chain into pipelines; use lists when you need to keep or reuse the items.
