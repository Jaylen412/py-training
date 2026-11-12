# 11-03 Style and readability

## What you will learn

- Apply the essentials of PEP 8, Python's style guide.
- Choose names that make code explain itself, and replace magic numbers with constants.
- Keep functions short and focused, with docstrings.
- Refactor a messy script step by step without changing what it does.

## Why it matters

Code is read far more often than it is written, by colleagues, by reviewers, and by you in six months. Data-science code has a reputation for being written once in a hurry and then never understood again. Clean, consistent code makes bugs easier to spot, and makes your projects something you can show to an employer.

## Concepts

### PEP 8 essentials

**PEP 8** is the official style guide for Python code. The rules that matter most:

- **Indentation**: 4 spaces, never tabs.
- **Line length**: keep lines under about 79 to 99 characters; break long expressions inside brackets.
- **Blank lines**: two around top-level functions and classes, one between methods.
- **Spaces**: around `=` and operators (`total = price * 2`), after commas, but not inside brackets (`f(x)` not `f( x )`) and not around `=` in keyword arguments (`f(sep="-")`).
- **Imports**: at the top of the file, one per line, grouped as standard library, then third-party packages, then your own modules.
- **Naming**: `snake_case` for functions and variables, `CamelCase` for classes, `UPPER_CASE` for constants.
- **Comparisons**: `x is None` rather than `x == None`; `if items:` rather than `if len(items) > 0:`.

Tools can check and fix most of this for you. **ruff** and **black** are popular choices (`pip install ruff`, then `ruff check your_file.py`). Many editors run them every time you save.

### A messy example

This function works. Try to work out what it does before reading on:

```python
def f(d):
    r = {}
    for x in d:
        if x[1] != None and x[1] >= 0 and x[1] <= 100:
            if x[0].strip().lower() in r:
                r[x[0].strip().lower()].append(x[1])
            else:
                r[x[0].strip().lower()] = [x[1]]
    o = {}
    for k in r:
        a = sum(r[k]) / len(r[k])
        if a >= 70:
            g = "pass"
        else:
            g = "fail"
        o[k] = (round(a, 1), g)
    return o


raw_scores = [("Ada ", 91), ("alan", 64), ("ADA", 85), ("Grace", None), ("alan", 120), ("Grace", 72)]
print(f(raw_scores))
```

```
{'ada': (88.0, 'pass'), 'alan': (64.0, 'fail'), 'grace': (72.0, 'pass')}
```

It builds a class report: for each student, the average of their valid scores and whether they passed. The problems:

- **Meaningless names**: `f`, `d`, `r`, `x`, `o`, `k`, `a`, `g`.
- **Magic numbers**: `0`, `100` and `70` have meanings ("lowest score", "highest score", "pass mark") that the code does not state.
- **Repetition**: `x[0].strip().lower()` appears three times.
- **One function doing three jobs**: filtering, grouping and summarising.
- **Index access** (`x[0]`, `x[1]`) where unpacking would name the parts.
- `!= None` instead of `is not None`.

### Refactoring

**Refactoring** means improving the structure of code **without changing its behaviour**. The safe way to do it is in small steps, checking after each one that the output is still the same. Ideally, write a test for the current behaviour first. Here is the result:

```python
PASS_MARK = 70
MIN_SCORE = 0
MAX_SCORE = 100


def normalise_name(name: str) -> str:
    """Return the name stripped and lower-cased, so variants match."""
    return name.strip().lower()


def is_valid_score(score) -> bool:
    """Return True if score is present and within the allowed range."""
    return score is not None and MIN_SCORE <= score <= MAX_SCORE


def group_scores(records):
    """Group valid scores by normalised student name."""
    scores_by_student = {}
    for name, score in records:
        if is_valid_score(score):
            scores_by_student.setdefault(normalise_name(name), []).append(score)
    return scores_by_student


def summarise_student(scores):
    """Return (average rounded to 1 place, "pass" or "fail")."""
    average = sum(scores) / len(scores)
    result = "pass" if average >= PASS_MARK else "fail"
    return round(average, 1), result


def class_report(records):
    """Return a summary for each student with at least one valid score."""
    return {
        student: summarise_student(scores)
        for student, scores in group_scores(records).items()
    }
```

`dictionary.setdefault(key, default)` returns the value for `key`, first storing `default` if the key is missing; it is another way to write the grouping pattern from 05-05.

The behaviour is unchanged, which we check directly:

```python
print(class_report(raw_scores))
print(class_report(raw_scores) == f(raw_scores))
```

```
{'ada': (88.0, 'pass'), 'alan': (64.0, 'fail'), 'grace': (72.0, 'pass')}
True
```

The new version is longer, but each function can be read and understood in seconds, the rules are named, and every piece can be tested on its own:

```python
print(normalise_name("  ADA "), is_valid_score(120), summarise_student([60, 90]))
```

```
ada False (75.0, 'pass')
```

### Guidelines for functions

- **One job per function.** If its description needs the word "and", consider splitting it.
- **Short.** Most functions fit on one screen; many are under 15 lines.
- **A docstring** saying what it does (and returns), starting with a verb.
- **Few parameters.** More than about four suggests the function does too much, or the parameters belong together in a dataclass.
- **Comments explain why, not what.** `# 1.5 because overtime is paid at time and a half` is useful; `# multiply by 1.5` is not.

## Common mistakes

- **Refactoring and changing behaviour at the same time.** If the output changes, you cannot tell whether it was the clean-up or the "improvement". Refactor first, check, then change behaviour separately.
- **Abbreviations.** `calc_avg_scr` saves a few keystrokes and costs every future reader. Write `calculate_average_score`.
- **Names that lie.** A function called `get_total` that also saves to a file will surprise everyone. Names must describe everything a function does.
- **Commenting out old code and leaving it.** Version control (git) remembers old versions; delete dead code.

## Try it

Take your expense tracker from the Part 1 project. Find the longest function, and refactor it into smaller ones without changing its behaviour. Run the project tests after each step.

## Exercises

Open `ex_11_03.py`. Each docstring shows a messy but working version. Write a clean version that behaves identically, with good names, constants instead of magic numbers, and helper functions where they help.

1. `shipping_cost`: price a parcel by weight and speed.
2. `order_summary`: summarise a list of order lines.
3. `format_receipt`: turn order lines into receipt text.

Run the tests:

```
python -m pytest part-2-intermediate-python/11-writing-reliable-code/11-03-style-and-readability
```

## Summary

- Follow PEP 8: 4-space indents, sensible line length, `snake_case`, `CamelCase` classes, `UPPER_CASE` constants, imports at the top.
- Use descriptive names and named constants instead of magic numbers.
- Keep functions short, single-purpose and documented.
- Refactor in small steps, checking that behaviour is unchanged after each one.
- Let tools such as ruff and black handle formatting for you.
