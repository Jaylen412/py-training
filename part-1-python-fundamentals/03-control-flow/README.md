# Module 03: Control Flow

Make programs decide and repeat. You will branch with `if`, `elif` and `else`, combine conditions with `and`, `or` and `not`, and repeat work with `while` and `for` loops, finishing with the handful of loop patterns that cover most real code.

**Prerequisites:** Modules 01 and 02.

## Lessons

1. [03-01 Conditionals](03-01-conditionals/lesson.md)
2. [03-02 Boolean logic](03-02-boolean-logic/lesson.md)
3. [03-03 while loops](03-03-while-loops/lesson.md)
4. [03-04 for loops and range](03-04-for-loops-and-range/lesson.md)
5. [03-05 Loop patterns](03-05-loop-patterns/lesson.md)

## Checkpoint quiz

1. With `score = 85`, what does this print? `if score >= 50: print("C")` / `elif score >= 80: print("B")`
2. Why is `if day == "Sat" or "Sun":` always true?
3. What numbers does `range(10, 0, -3)` produce?
4. Why should a running maximum start from the first item rather than from 0?
5. When does the `else` block of a `for` loop run?

<details>
<summary>Answers</summary>

1. `C`. The first true branch wins, and `85 >= 50` is checked first. Put the stricter condition first.
2. Python reads it as `(day == "Sat") or "Sun"`, and the non-empty string `"Sun"` is truthy. Write `day == "Sat" or day == "Sun"`.
3. `10, 7, 4, 1`.
4. If every value is negative, 0 would be larger than all of them and would be reported as the maximum even though it is not in the data.
5. When the loop finishes without a `break`.

</details>
