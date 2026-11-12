# 03-03 while loops

## What you will learn

- Repeat a block of code for as long as a condition stays true.
- Use a counter to control how many times a loop runs.
- Leave a loop early with `break` and skip ahead with `continue`.
- Spot and avoid infinite loops.

## Why it matters

Computers are useful because they repeat work tirelessly. A `while` loop repeats until something changes, which is exactly how training works in Part 4: gradient descent keeps adjusting a model **while** its error is still going down. You will write that loop yourself in Module 18.

## Concepts

### The while loop

A **`while` loop** checks a condition; if it is true, it runs the indented block (the **body**), then goes back and checks the condition again. Each pass through the body is called an **iteration**. When the condition is false, the loop ends and the program continues after it.

```python
count = 1
while count <= 3:
    print("Count is", count)
    count += 1
print("Finished; count is now", count)
```

```
Count is 1
Count is 2
Count is 3
Finished; count is now 4
```

Trace it by hand: `count` is 1, 2, 3 on the passes that print. After the third pass it becomes 4, the condition `4 <= 3` is false, and the loop stops. A variable like `count` that tracks how many times something has happened is a **counter**.

Every loop needs three parts: **set up** the variable before the loop, **test** it in the condition, and **change** it inside the body.

### Zero iterations

The condition is checked before the first pass, so the body may never run at all:

```python
fuel = 0
while fuel > 0:
    print("Driving...")
    fuel -= 1
print("Out of fuel")
```

```
Out of fuel
```

### Loop until a goal

`while` shines when you do not know in advance how many iterations you need. How many years does it take to double your savings at 7% a year?

```python
savings = 100.0
years = 0
while savings < 200:
    savings *= 1.07
    years += 1
print(f"Savings double after {years} years: {savings:.2f}")
```

```
Savings double after 11 years: 210.49
```

### break

`break` leaves the loop immediately, skipping the rest of the body and the condition check. A common pattern is `while True:`, a loop that would run forever, with a `break` inside that fires when the job is done:

```python
number = 1
while True:
    if number * number > 50:
        break
    number += 1
print("First number whose square is over 50:", number)
```

```
First number whose square is over 50: 8
```

### continue

`continue` skips the rest of the current iteration and jumps back to the condition check:

```python
number = 0
while number < 10:
    number += 1
    if number % 3 != 0:
        continue
    print(number, "is a multiple of 3")
```

```
3 is a multiple of 3
6 is a multiple of 3
9 is a multiple of 3
```

Notice that `number += 1` comes **before** the `continue`. If it came after, `continue` would skip it, `number` would never change, and the loop would never end.

### Taking a number apart

`% 10` gives the last digit of a whole number, and `// 10` removes it. Repeating both while anything is left visits every digit:

```python
remaining = 2026
digit_total = 0
while remaining > 0:
    digit_total += remaining % 10
    remaining //= 10
print("Sum of the digits of 2026:", digit_total)
```

```
Sum of the digits of 2026: 10
```

`remaining` goes 2026, 202, 20, 2, 0, and the digits added are 6, 2, 0, 2.

### Keep asking until the answer is valid

A classic use of `while` is to keep asking the user until they type something acceptable. In a real program:

```python
answer = ""
while answer != "yes" and answer != "no":
    answer = input("Continue? (yes/no) ").strip().lower()
```

`examples.py` cannot wait for typing, so it fakes a user who first types `maybe` and then `yes`:

```python
attempt = 0
answer = ""
while answer != "yes" and answer != "no":
    attempt += 1
    if attempt == 1:
        answer = "maybe"
    else:
        answer = "yes"
    print(f"Attempt {attempt}: got {answer}")
print("Valid answer received:", answer)
```

```
Attempt 1: got maybe
Attempt 2: got yes
Valid answer received: yes
```

### Infinite loops

If the condition never becomes false and nothing calls `break`, the loop runs forever. This is an **infinite loop**. Your program seems to freeze or prints endlessly. Press **Ctrl+C** in the terminal to stop it; Python prints `KeyboardInterrupt`. Then check that something in the body moves the loop towards its end.

## Common mistakes

- **Forgetting to update the counter.** `while count <= 3: print(count)` with no `count += 1` never ends. Every loop must change something its condition depends on.
- **Updating after `continue`.** If the update line is below a `continue`, it is skipped and the loop can get stuck. Update first.
- **Off-by-one conditions.** `while count < 3` starting from 1 runs twice, not three times. Trace the first and last iteration by hand.
- **Using `while` where you know the count.** To run something exactly 10 times, a `for` loop (next lesson) is shorter and cannot become infinite.

## Try it

Change Example 3 to find how many years it takes to **triple** the savings at 5% a year. Then try a rate of 0% and see what happens. (Press Ctrl+C to stop it, then explain why.)

## Exercises

Open `ex_03_03.py`:

1. `countdown_text`: build a countdown string such as `"3 2 1 Go!"`.
2. `sum_of_digits`: add up the digits of a whole number.
3. `count_halvings`: how many times a number can be halved before it drops below 1.
4. `first_power_of_two_over`: the first power of two greater than a limit.
5. `collatz_steps`: the number of steps for a number to reach 1 under the Collatz rule.

Run the tests:

```
python -m pytest part-1-python-fundamentals/03-control-flow/03-03-while-loops
```

## Summary

- `while condition:` repeats its body as long as the condition is true, checking before each pass.
- Set up, test and change: every loop variable needs all three.
- `break` leaves the loop; `continue` skips to the next check.
- `while True:` plus `break` is a common way to loop until a goal is met.
- Press Ctrl+C to stop an infinite loop, then find what is not changing.
