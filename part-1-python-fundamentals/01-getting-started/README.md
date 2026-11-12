# Module 01: Getting Started

Set up Python, learn to run code in the REPL and from files, and get the course's tools working. By the end you can write a short program with `print`, read the error Python gives you when something goes wrong, and run the exercise tests.

**Prerequisites:** none.

## Lessons

1. [01-01 Installing and running Python](01-01-running-python/lesson.md) (concept)
2. [01-02 Your first program](01-02-first-program/lesson.md)
3. [01-03 Virtual environments and pip](01-03-virtual-environments/lesson.md) (concept)

## Checkpoint quiz

1. What is the REPL, and how does it differ from running a file?
2. What does `print("a", "b", "c", sep="")` print?
3. A traceback ends with `NameError: name 'pirnt' is not defined`. What should you look for, and where?
4. Why does this course use a virtual environment?
5. What command checks your answers to the exercises in lesson 01-02?

<details>
<summary>Answers</summary>

1. The REPL runs one line at a time and prints every value automatically. A file runs all its lines from top to bottom and only shows what you `print`.
2. `abc`, because the separator between the values is the empty string.
3. A misspelt name, `pirnt` instead of `print`. The lines just above the error give the file name and line number.
4. To give the course its own set of packages (NumPy, pandas, scikit-learn and so on) without affecting, or being affected by, anything else on the computer.
5. `python -m pytest part-1-python-fundamentals/01-getting-started/01-02-first-program`, run from the repository root with the virtual environment active.

</details>
