# Module 04: Functions

Write your own functions: define them, pass arguments in, return results, and keep their variables private. You will learn to break a problem into small, pure functions that are easy to test, and finish by reading and writing pytest tests yourself.

**Prerequisites:** Modules 01 to 03.

## Lessons

1. [04-01 Defining and calling functions](04-01-defining-functions/lesson.md)
2. [04-02 Arguments in depth](04-02-arguments-in-depth/lesson.md)
3. [04-03 Scope](04-03-scope/lesson.md)
4. [04-04 Functions as building blocks](04-04-functions-as-building-blocks/lesson.md)
5. [04-05 Reading and writing tests](04-05-reading-and-writing-tests/lesson.md)

## Checkpoint quiz

1. A function prints its answer but has no `return`. What does `result = f()` store?
2. Why is `def add(item, items=[]):` a bug waiting to happen?
3. Inside a function you write `total += 1`, where `total` is a global. What error do you get, and why?
4. What makes a function "pure"?
5. Name three kinds of test case you should write for a function.

<details>
<summary>Answers</summary>

1. `None`. Printing shows a value but does not hand it back.
2. The default list is created once, when the function is defined, so every call that relies on it shares and grows the same list. Use `items=None` and create the list inside.
3. `UnboundLocalError`. Assigning to `total` inside the function makes it local, and `+=` tries to read the local before it has a value.
4. Its result depends only on its arguments, and it has no side effects such as printing or changing globals.
5. Typical values, edge cases (boundaries, empty input, zero) and unusual values (negative, very large, unexpected types).

</details>
