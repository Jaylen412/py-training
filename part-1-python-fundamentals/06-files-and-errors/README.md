# Module 06: Files and Errors

Make programs that remember things between runs and cope with bad input. You will read and write text, CSV and JSON files, catch the exceptions that real-world data causes, and raise your own exceptions when a function receives something it cannot use.

**Prerequisites:** Modules 01 to 05.

## Lessons

1. [06-01 Reading and writing text files](06-01-text-files/lesson.md)
2. [06-02 CSV and JSON](06-02-csv-and-json/lesson.md)
3. [06-03 Exceptions](06-03-exceptions/lesson.md)
4. [06-04 Raising errors and validating input](06-04-raising-errors/lesson.md)

## Checkpoint quiz

1. What is the difference between opening a file with `"w"` and with `"a"`?
2. You read a CSV with `DictReader` and `row["price"] * 2` gives `"9.999.99"`. What happened?
3. Why is `except:` with no exception type a bad idea?
4. When does an `else` block after `try`/`except` run? And `finally`?
5. A function receives `quantity=-3`. Should it raise `ValueError` or `TypeError`, and what should the message say?

<details>
<summary>Answers</summary>

1. `"w"` empties the file (or creates it) before writing; `"a"` keeps the contents and writes at the end.
2. CSV values are strings, so `*` repeated the text `"9.99"`. Convert with `float(row["price"])` first.
3. It catches every exception, including bugs like `NameError`, so mistakes are hidden and the program carries on with wrong results.
4. `else` runs only if the `try` block raised no exception. `finally` always runs.
5. `ValueError`, because the type (int) is right but the value is not. The message should say what is wrong and show the value, for example `quantity must be positive, got -3`.

</details>
