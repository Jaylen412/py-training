# Module 02: Values, Variables and Types

The building blocks of every program: numbers, text, true-or-false values, and the variables that hold them. You will learn how Python does arithmetic, how to slice and clean text, and how to convert between types.

**Prerequisites:** Module 01.

## Lessons

1. [02-01 Numbers and arithmetic](02-01-numbers-and-arithmetic/lesson.md)
2. [02-02 Variables and assignment](02-02-variables-and-assignment/lesson.md)
3. [02-03 Strings](02-03-strings/lesson.md)
4. [02-04 String methods and f-strings](02-04-string-methods-and-f-strings/lesson.md)
5. [02-05 Booleans, None and type conversion](02-05-booleans-none-conversion/lesson.md)

## Checkpoint quiz

1. What are the values of `17 // 5`, `17 % 5` and `17 / 5`?
2. After `count = 4` then `count *= 3` then `count -= 2`, what is `count`?
3. For `word = "learning"`, what are `word[0]`, `word[-1]` and `word[1:4]`?
4. What does `f"{0.8241:.1%}"` produce?
5. Why does `input("Age? ") + 1` fail, and how do you fix it?

<details>
<summary>Answers</summary>

1. `3`, `2` and `3.4`.
2. `10` (4 times 3 is 12, minus 2 is 10).
3. `"l"`, `"g"` and `"ear"`.
4. `"82.4%"`.
5. `input` always returns a string, and you cannot add a string and an int. Convert first: `int(input("Age? ")) + 1`.

</details>
