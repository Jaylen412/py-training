# 07-02 Debugging

## What you will learn

- Find a bug by printing values as the code runs.
- Pause a program with `breakpoint()` and inspect it with basic `pdb` commands.
- Follow a stack trace through several functions to the line that failed.
- Narrow down where a bug is by bisecting.

## Why it matters

Every programmer writes bugs; good programmers find them quickly. A **bug** is any difference between what code does and what you meant it to do. Some bugs crash the program with a traceback; the worst ones quietly give a wrong answer. In machine learning, a quiet bug such as using the wrong column can make a model look great while being useless, so a calm, systematic approach to debugging matters even more later.

## Concepts

### Reproduce, then investigate

Step one is always to **reproduce** the bug: find a small input that shows it, and know what the right answer would be. This function should average numbers:

```python
def average_buggy(numbers):
    total = 0
    for index in range(1, len(numbers)):
        total += numbers[index]
    return total / len(numbers)


print(average_buggy([10, 20, 30]))   # expected 20.0
```

```
16.666666666666668
```

No crash, just a wrong answer. Now you need to see what is happening inside.

### Print debugging

The simplest tool is a temporary `print` showing the values you care about at each step:

```python
def average_traced(numbers):
    total = 0
    for index in range(1, len(numbers)):
        total += numbers[index]
        print(f"  index={index} value={numbers[index]} total={total}")
    return total / len(numbers)


print(average_traced([10, 20, 30]))
```

```
  index=1 value=20 total=20
  index=2 value=30 total=50
16.666666666666668
```

The trace shows that index 0 is never visited, so 10 is never added: `range(1, ...)` should start at 0. Looping over the items directly avoids index mistakes altogether:

```python
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average([10, 20, 30]))
```

```
20.0
```

Label your prints (`index=`, `total=`) so you can tell them apart, and remove them once the bug is fixed.

### The debugger: breakpoint() and pdb

Python includes a **debugger** called **`pdb`**, which lets you pause a running program and look around. Put `breakpoint()` on the line where you want to stop and run the program normally. When it reaches that line, it pauses and shows a `(Pdb)` prompt. (`examples.py` has its `breakpoint()` commented out so the file runs straight through.)

The commands you need first:

| Command | Meaning |
|---------|---------|
| `p expression` | print the value of an expression |
| `n` | next: run the current line and stop at the next one |
| `s` | step into the function called on this line |
| `c` | continue until the next breakpoint (or the end) |
| `l` | list the code around the current line |
| `q` | quit the program |

With a `breakpoint()` placed inside the loop of `average_buggy`, a session looks like this (what you type follows each `(Pdb)` prompt; the path is shortened):

```
> buggy.py(4)average_buggy()
-> breakpoint()
(Pdb) p index
1
(Pdb) p numbers[index]
20
(Pdb) p total
0
```

The very first pass of the loop already has `index` equal to 1, which reveals the bug immediately, without editing the code to add prints. Type `c` to carry on or `q` to stop.

VS Code has the same features with buttons: click to the left of a line number to set a red-dot breakpoint, then choose **Run > Start Debugging**. The variables panel shows every value at once.

### Reading a stack trace

When an error happens deep inside several function calls, the traceback lists **every** call that was in progress, outermost first. This list of calls is the **stack trace**. Given:

```python
def parse_price(text):
    return float(text)


def total_price(rows):
    total = 0
    for row in rows:
        total += parse_price(row["price"])
    return total


rows = [{"price": "1.50"}, {"price": "2,25"}]
print(total_price(rows))
```

the traceback is:

```
Traceback (most recent call last):
  File "deep.py", line 13, in <module>
    print(total_price(rows))
          ~~~~~~~~~~~^^^^^^
  File "deep.py", line 8, in total_price
    total += parse_price(row["price"])
             ~~~~~~~~~~~^^^^^^^^^^^^^^
  File "deep.py", line 2, in parse_price
    return float(text)
ValueError: could not convert string to float: '2,25'
```

Read it from the bottom:

1. **What**: `ValueError`, because `'2,25'` has a comma instead of a decimal point.
2. **Where it failed**: line 2, in `parse_price`.
3. **How it got there**: `parse_price` was called from line 8 in `total_price`, which was called from line 13 at the top level (`<module>`).

The failing line is not always where the mistake is. `parse_price` is fine; the bad data came from `rows`. Walk up the stack to find where the bad value came from.

### Bisecting

When a result passes through several steps, **bisecting** means checking the value halfway along to find out which half contains the bug, then repeating on that half. This word counter gives the wrong answer:

```python
def clean(text):
    return text.strip().lower()


def to_words(text):
    return text.split(" ")


def count_words(text):
    return len(to_words(clean(text)))


sentence = "  The  quick fox "
print(count_words(sentence))            # expected 3
print(repr(clean(sentence)))            # is the cleaning step right?
print(to_words(clean(sentence)))        # is the splitting step right?
```

```
4
'the  quick fox'
['the', '', 'quick', 'fox']
```

The cleaning step looks right. The splitting step produced an empty string between the two spaces, so the bug is in `to_words`. `split(" ")` splits on every single space, while `split()` with no argument splits on runs of whitespace:

```python
def to_words_fixed(text):
    return text.split()


print(len(to_words_fixed(clean(sentence))))
```

```
3
```

The same idea works on data: if a function fails on a list of 1,000 rows, try it on the first 500, then the first 250, and so on, until you find the row that breaks it.

### A debugging checklist

1. Reproduce the bug with the smallest input you can find, and write down the expected answer.
2. Read the traceback, if there is one, from the bottom up.
3. Form a guess about the cause, then check it with a print, the debugger or bisecting.
4. Fix one thing, then rerun the failing example **and** all the tests.
5. Add a test for the bug, so it can never come back unnoticed.

## Common mistakes

- **Changing code at random.** Editing things until the output looks right usually adds new bugs. Find the cause first.
- **Assuming the line in the traceback is the culprit.** It is where the error showed up; the bad value may have been created earlier. Walk up the stack.
- **Leaving debugging prints and `breakpoint()` calls behind.** A forgotten `breakpoint()` freezes the program at the `(Pdb)` prompt later. Search for them before you finish.
- **Not re-running the tests after a fix.** A fix in one place can break another. Run the whole test file.

## Try it

Put `breakpoint()` inside the loop of `longest_run` in `07-01/examples.py`, run the file, and use `p character`, `p current` and `n` to watch the run lengths change on `"aaabbc"`. Type `q` to quit when you are done.

## Exercises

Open `ex_07_02.py`. Each docstring shows a buggy version of the function. Find the bug (run it, print, or use the debugger), then write a correct version.

1. `average`: skips a number and crashes on an empty list.
2. `find_max`: wrong when every number is negative.
3. `count_words`: miscounts when there are extra spaces.
4. `is_sorted`: crashes with `IndexError`.
5. `capitalise_words`: changes nothing at all.

Run the tests:

```
python -m pytest part-1-python-fundamentals/07-problem-solving-and-debugging/07-02-debugging
```

## Summary

- Reproduce the bug with a small input and a known expected answer first.
- Labelled `print` calls show values as the code runs; remove them afterwards.
- `breakpoint()` pauses the program; `p`, `n`, `s`, `c` and `q` inspect and control it.
- A stack trace lists every active call; read from the bottom, then walk up to find where bad data came from.
- Bisect by checking intermediate results until you find the step that goes wrong, then add a test for the bug.
