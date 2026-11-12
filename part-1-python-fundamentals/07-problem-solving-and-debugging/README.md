# Module 07: Problem Solving and Debugging

The skills that turn knowing Python into writing programs: a step-by-step way to go from a problem statement to working code, and a systematic way to find and fix bugs with prints, the debugger, stack traces and bisecting.

**Prerequisites:** Modules 01 to 06.

## Lessons

1. [07-01 Breaking down a problem](07-01-breaking-down-a-problem/lesson.md) (concept)
2. [07-02 Debugging](07-02-debugging/lesson.md)

## Checkpoint quiz

1. List the steps for going from a problem statement to working code.
2. Why should hand-worked examples include an empty input?
3. What do the pdb commands `p`, `n` and `c` do?
4. A traceback ends in `parse_price`, but `parse_price` is correct. Where should you look next?
5. What is bisecting, and when is it useful?

<details>
<summary>Answers</summary>

1. Restate the problem, work examples by hand, write pseudocode, solve a simpler version, extend it, and check it against the examples.
2. Empty input is a common edge case that typical examples miss, and it often crashes code (for example, division by `len` of an empty list).
3. `p` prints an expression's value, `n` runs the current line and stops at the next, `c` continues running until the next breakpoint.
4. Up the stack trace, at the function that called `parse_price` and the data it passed in.
5. Checking an intermediate result halfway through a process to see which half contains the bug, then repeating. It is useful when data passes through several steps, or when a large input fails and you need to find the bad part.

</details>
