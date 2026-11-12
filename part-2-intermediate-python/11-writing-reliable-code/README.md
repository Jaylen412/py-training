# Module 11: Writing Reliable Code

Write code that you and others can trust and maintain. You will organise pytest suites with fixtures and parametrised cases, document types with hints, refactor messy code into clean, readable functions, and use context managers and logging to keep programs tidy and observable.

**Prerequisites:** Part 1 and Modules 08 to 10.

## Lessons

1. [11-01 Testing with pytest](11-01-testing-with-pytest/lesson.md)
2. [11-02 Type hints](11-02-type-hints/lesson.md)
3. [11-03 Style and readability](11-03-style-and-readability/lesson.md)
4. [11-04 Context managers and logging](11-04-context-managers-and-logging/lesson.md)

## Checkpoint quiz

1. Why should tests use a fixture rather than a shared module-level object?
2. What does `@pytest.mark.parametrize("value", [1, 2, 3])` do to a test?
3. Will Python stop you calling `def f(x: int) -> int` with a string? What are hints for, then?
4. What is refactoring, and how do you make sure you have not broken anything?
5. What advantage does `logger.warning(...)` have over `print(...)` for diagnostic messages?

<details>
<summary>Answers</summary>

1. A fixture gives each test a fresh object, so tests cannot affect each other or depend on the order they run in.
2. It runs the test three times, once with each value, and reports each case separately.
3. No; hints are not enforced at runtime. They document intent and let editors and checkers such as mypy find mistakes before the code runs.
4. Improving code's structure without changing its behaviour. Work in small steps and run tests (or compare outputs) after each one.
5. Log messages have levels, so you can show or hide detail by changing one setting, and they can be formatted with timestamps and sent to files without changing the code that logs.

</details>
