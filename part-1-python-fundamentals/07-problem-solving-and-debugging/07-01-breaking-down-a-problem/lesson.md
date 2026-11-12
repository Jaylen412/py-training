# 07-01 Breaking down a problem

## What you will learn

- Restate a problem precisely before writing any code.
- Work examples by hand, including edge cases, and keep them as checks.
- Plan a solution in pseudocode.
- Solve a simpler version of a problem first, then extend it.

## Why it matters

Knowing Python's syntax is not the hard part of programming; knowing what to write is. When you face a blank file, a reliable process gets you moving. You will use this process in the Part 1 project, which is the first program in this course where nobody tells you which functions to write, and again in every project after it.

## Concepts

We will work through one problem from start to finish:

> Given a string, find the longest run of the same character repeated in a row, and report the character and the length of the run.

### Step 1: Restate the problem

Rewrite the problem in your own words, and make every vague part precise. Ask:

- **What goes in?** A string. Could it be empty? Yes, any string.
- **What comes out?** Two things: a character and a number. A tuple `(character, length)` fits.
- **What are the rules?** A "run" is consecutive identical characters. Is `"A"` the same as `"a"`? Let us say no: compare exactly.
- **What about ties?** If two runs are equally long, report the first.
- **What about nothing?** For the empty string there is no character: return `(None, 0)`.

Most bugs come from questions like these that were never asked. If you were given the problem by someone else, this is the time to ask them.

### Step 2: Work examples by hand

Before writing code, solve a few examples yourself, on paper. Include a typical case, a case where the answer is not at the start, and edge cases:

| Input | Expected | Why |
|-------|----------|-----|
| `"aaabbc"` | `("a", 3)` | typical |
| `"abbbbc"` | `("b", 4)` | the longest run is in the middle |
| `"abc"` | `("a", 1)` | every run has length 1, so the first wins |
| `""` | `(None, 0)` | empty input |

Pay attention to **how** you found the answers. For `"abbbbc"` you probably scanned left to right, counting, and remembered the best count so far. That is your algorithm.

Keep the examples. They become your tests:

```python
examples = [
    ("aaabbc", ("a", 3)),
    ("abbbbc", ("b", 4)),
    ("abc", ("a", 1)),
    ("", (None, 0)),
]
```

### Step 3: Write pseudocode

**Pseudocode** is a plain-language description of the steps, written in the shape of code but without worrying about syntax. It lets you check the logic before fighting with details.

```
best = nothing, longest = 0
current run length = 0, previous character = nothing
for each character:
    if it equals the previous character:
        current run length goes up by 1
    otherwise:
        a new run starts: current run length = 1
    remember this character as previous
    if current run length beats longest:
        longest = current run length, best = this character
answer is (best, longest)
```

Trace the pseudocode by hand on one example (`"abbbbc"` is a good choice) before you translate it.

### Step 4: Solve a simpler version first

If the full problem feels like too much, solve a smaller one. Here: just find the **length** of the longest run, ignoring which character it is.

```python
def longest_run_length(text):
    longest = 0
    current = 0
    previous = None
    for character in text:
        if character == previous:
            current += 1
        else:
            current = 1
        previous = character
        if current > longest:
            longest = current
    return longest


print(longest_run_length("aaabbc"), longest_run_length("abbbbc"), longest_run_length(""))
```

```
3 4 0
```

It works, so the counting logic is right. Starting `previous` at `None` means the first character never matches, so the first run correctly starts at 1.

### Step 5: Extend to the full problem

Now add the one missing piece: remember **which** character gave the longest run.

```python
def longest_run(text):
    """Return (character, length) of the longest run in `text`."""
    best_character = None
    longest = 0
    current = 0
    previous = None
    for character in text:
        if character == previous:
            current += 1
        else:
            current = 1
        previous = character
        if current > longest:
            longest = current
            best_character = character
    return best_character, longest
```

Using `>` rather than `>=` means a later run of the same length does not replace an earlier one, which is exactly the tie rule from Step 1.

### Step 6: Check against your examples

```python
for text, expected in examples:
    result = longest_run(text)
    status = "ok" if result == expected else "WRONG"
    print(f"{text!r:10} -> {result}  expected {expected}  {status}")
```

```
'aaabbc'   -> ('a', 3)  expected ('a', 3)  ok
'abbbbc'   -> ('b', 4)  expected ('b', 4)  ok
'abc'      -> ('a', 1)  expected ('a', 1)  ok
''         -> (None, 0)  expected (None, 0)  ok
```

All four pass. (`!r:10` shows the string with quotes and pads it to 10 characters.) In a real project these checks would go in a pytest file, as in 04-05.

### When you are stuck

- **Shrink the input.** What is the answer for a one-character string? Two characters?
- **Do it by hand, slowly,** and write down every step you take. Those steps are the program.
- **Solve a simpler problem.** Drop one requirement, solve that, then add it back.
- **Split the problem.** Can it be two smaller problems, each its own function, as in 04-04?

## Common mistakes

- **Coding before understanding.** Writing code first and working out the rules later leads to rewriting. Spend the first few minutes on Steps 1 and 2.
- **Only trying the obvious example.** A solution tested only on `"aaabbc"` might fail when the longest run is in the middle, or on an empty string. Choose examples that probe the edges.
- **Throwing the examples away.** The hand-worked examples are free tests. Keep them in a test file.
- **Trying to solve everything at once.** If a function is not working and you cannot see why, go back to the simpler version and add one feature at a time.

## Try it

Use the same steps for this problem: "Given a list of daily temperatures, find the length of the longest streak of days on which the temperature went up compared with the day before." Write your restatement, four examples (including an empty list and a list that only goes down), pseudocode, and then the code.

## Summary

- Restate the problem: inputs, outputs, rules, ties and empty cases.
- Work examples by hand, including edge cases, and keep them as tests.
- Write pseudocode and trace it by hand before writing Python.
- Solve a simpler version first, then add the missing pieces one at a time.
- When stuck: shrink the input, go slowly by hand, or split the problem.

## Review questions

1. Why should you restate a problem before writing code?
2. Name two kinds of example you should always work by hand, besides a typical case.
3. What is pseudocode, and why write it?
4. In `longest_run`, why does using `>` rather than `>=` matter?
5. You have a function that almost works but fails on some inputs, and you cannot see why. What can you do?

<details>
<summary>Answers</summary>

1. To make vague parts precise (inputs, outputs, ties, empty input) before they turn into bugs, and to discover questions you need to ask.
2. Edge cases, such as empty input or a single item, and cases where the answer is somewhere unexpected, such as in the middle or at the end.
3. A plain-language outline of the steps in the shape of code. It lets you check the logic without worrying about syntax.
4. With `>`, a later run of the same length does not replace the first one, so ties go to the first run as the problem requires.
5. Go back to a simpler version that works and add features one at a time, test it on the smallest failing input, or trace it by hand step by step (and see 07-02 for debugging tools).

</details>
