# Module 12: Performance and Complexity

Learn to reason about speed. You will measure code properly, predict how it scales with Big-O notation, turn slow algorithms into fast ones, and see why plain Python loops are too slow for large-scale number crunching: the motivation for NumPy in Part 3.

**Prerequisites:** Part 1 and Modules 08 to 11.

## Lessons

1. [12-01 Measuring code](12-01-measuring-code/lesson.md)
2. [12-02 Big-O intuition](12-02-big-o-intuition/lesson.md)
3. [12-03 Why loops are slow for numbers](12-03-why-loops-are-slow-for-numbers/lesson.md)

## Checkpoint quiz

1. Why should you report the minimum of several timings rather than a single run?
2. A function is O(n²). Roughly how much longer does it take if the input is 10 times bigger?
3. Why is `x in my_set` fast but `x in my_list` slow for large collections?
4. How can you rewrite "for each item in A, check if it is in list B" to be O(n + m)?
5. Name two reasons a Python loop over a million floats is slow.

<details>
<summary>Answers</summary>

1. Timings are noisy because other programs interrupt; the minimum is the most stable estimate of the code's own cost.
2. About 100 times longer (10 squared).
3. Sets use hashing to jump straight to where an item would be stored (O(1)); lists must be checked item by item (O(n)).
4. Convert B to a set once, before the loop, then check membership in the set.
5. Every float is a separate object that must be looked up, type-checked and created anew for each result; and each step of the loop is run by the interpreter rather than compiled code.

</details>
