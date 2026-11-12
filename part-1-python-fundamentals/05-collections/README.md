# Module 05: Collections

Python's built-in containers for many values at once: lists, tuples, dictionaries and sets. You will learn when to use each, how to nest them to represent real records, why copying is subtler than it looks, and how to build new collections in one line with comprehensions.

**Prerequisites:** Modules 01 to 04.

## Lessons

1. [05-01 Lists](05-01-lists/lesson.md)
2. [05-02 Tuples and unpacking](05-02-tuples-and-unpacking/lesson.md)
3. [05-03 Dictionaries](05-03-dictionaries/lesson.md)
4. [05-04 Sets](05-04-sets/lesson.md)
5. [05-05 Nested data and references](05-05-nested-data-and-references/lesson.md)
6. [05-06 Comprehensions](05-06-comprehensions/lesson.md)

## Checkpoint quiz

1. What is the difference between `scores.sort()` and `sorted(scores)`?
2. Which collection would you use for (a) the x and y of a single point, (b) counting how often each word occurs, (c) the distinct cities in a list of addresses?
3. After `a = [1, 2]`, `b = a`, `b.append(3)`, what is `a`?
4. Why does `grid.copy()` not protect the inner lists of a list of lists?
5. Rewrite as a comprehension: `result = []` / `for w in words:` / `if len(w) > 3: result.append(w.upper())`.

<details>
<summary>Answers</summary>

1. `scores.sort()` sorts the list in place and returns `None`. `sorted(scores)` returns a new sorted list and leaves `scores` unchanged.
2. (a) a tuple, (b) a dictionary, (c) a set.
3. `[1, 2, 3]`. `b` is another name for the same list, not a copy.
4. It is a shallow copy: the outer list is new, but its items are references to the same inner lists. Use `copy.deepcopy`.
5. `result = [w.upper() for w in words if len(w) > 3]`.

</details>
