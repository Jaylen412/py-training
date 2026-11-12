# Module 08: Modules and Project Structure

Move beyond single files. You will split code into modules and packages, import them correctly, tour the most useful parts of the standard library, and turn scripts into proper command-line programs with arguments and exit codes.

**Prerequisites:** Part 1 (Modules 01 to 07).

## Lessons

1. [08-01 Imports and modules](08-01-imports-and-modules/lesson.md)
2. [08-02 Packages](08-02-packages/lesson.md)
3. [08-03 Standard library tour](08-03-standard-library-tour/lesson.md)
4. [08-04 Command-line programs](08-04-command-line-programs/lesson.md)

## Checkpoint quiz

1. What is the value of `__name__` in a file that is run directly, and in one that is imported?
2. What is the difference between `from .pricing import with_tax` and `from shop.pricing import with_tax`?
3. Why should you create random numbers with `random.Random(42)` in an experiment?
4. What does `Counter(words).most_common(3)` return?
5. What exit code means success, and how does a `main(argv)` function report failure?

<details>
<summary>Answers</summary>

1. `"__main__"` when run directly; the module's name (for example `"temperatures"`) when imported.
2. The first is a relative import (the `pricing` module in the same package as the current module); the second is an absolute import that spells out the full path.
3. A fixed seed makes the sequence of random numbers the same on every run, so results can be reproduced and tested.
4. A list of the three most frequent words as `(word, count)` tuples, most frequent first.
5. 0. It prints an error to `sys.stderr` and returns a non-zero code (such as 1), which the main guard passes to `sys.exit`.

</details>
