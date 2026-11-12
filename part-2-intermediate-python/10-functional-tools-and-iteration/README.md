# Module 10: Functional Tools and Iteration

Treat functions as values and data as streams. You will pass functions to other functions and sort with `key=`, write lazy generators, accept and pass on any arguments with `*args` and `**kwargs`, and build closures and decorators.

**Prerequisites:** Part 1 and Modules 08 to 09.

## Lessons

1. [10-01 Functions as values](10-01-functions-as-values/lesson.md)
2. [10-02 Iterators and generators](10-02-iterators-and-generators/lesson.md)
3. [10-03 `*args`, `**kwargs` and unpacking](10-03-args-kwargs-and-unpacking/lesson.md)
4. [10-04 Decorators and closures](10-04-decorators-and-closures/lesson.md)

## Checkpoint quiz

1. How do you sort a list of dictionaries by `"score"`, highest first, with ties broken by `"name"` A to Z?
2. Why does a second `list(generator)` give `[]`?
3. What is the difference between `sum([x * x for x in data])` and `sum(x * x for x in data)`?
4. What does `def connect(host, *, port=80):` force callers to do?
5. What three things should every decorator's wrapper do?

<details>
<summary>Answers</summary>

1. `sorted(records, key=lambda record: (-record["score"], record["name"]))`.
2. A generator is an iterator: it can only be used once, and the first `list` used up all its values.
3. Both give the same total. The first builds a full list in memory first; the second is a generator expression that produces one value at a time.
4. Pass `port` by keyword (`port=8080`); passing it by position raises `TypeError`.
5. Accept `*args, **kwargs`, call the original function with them and return its result, and be decorated with `@functools.wraps(function)` to keep the name and docstring.

</details>
