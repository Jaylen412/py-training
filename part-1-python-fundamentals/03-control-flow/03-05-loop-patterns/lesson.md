# 03-05 Loop patterns

## What you will learn

- Recognise and write the standard loop patterns: count, sum, search, minimum and maximum.
- Get each item's position as well as its value with `enumerate`.
- Use `else` on a loop to act only when no `break` happened.
- Answer "is there any?" and "are they all?" questions with a flag.

## Why it matters

Almost every loop you will ever write is one of a handful of patterns. Recognising them means you stop inventing loops from scratch and start choosing the right one. Later, NumPy and pandas give you a one-word function for each pattern (`sum`, `max`, `argmax`, `any`, `all`), and you will know exactly what they do under the hood.

## Concepts

All the examples below use this sentence:

```python
sentence = "the cat sat on the mat"
```

### Counting

Start a counter at zero and add one when an item matches:

```python
t_count = 0
for letter in sentence:
    if letter == "t":
        t_count += 1
print("Number of t's:", t_count)
```

```
Number of t's: 5
```

### Summing

The same shape, but add the item's value instead of one. Here, `isdigit()` is a string method that is `True` when every character is a digit:

```python
order_code = "A7B3C9"
digit_sum = 0
for character in order_code:
    if character.isdigit():
        digit_sum += int(character)
print("Sum of digits:", digit_sum)
```

```
Sum of digits: 19
```

### Searching

To find the first match, loop and `break` as soon as you find it. Set a default first, so you can tell afterwards whether anything was found. `-1` is a common "not found" value, as with `find` in 02-04.

```python
found_at = -1
for index in range(len(sentence)):
    if sentence[index] == "s":
        found_at = index
        break
print("First 's' at index:", found_at)
```

```
First 's' at index: 8
```

`range(len(sentence))` gives every valid index: 0 up to the length minus one.

### enumerate

Looping over indexes and then looking up `sentence[index]` works, but it is clumsy. **`enumerate`** gives you both at once: on each iteration it hands over a pair, the index and the item. Writing two names separated by a comma after `for` puts the first part of the pair in one and the second in the other. (Module 05 explains this "unpacking" in detail.)

```python
for index, letter in enumerate("abc"):
    print(index, letter)
```

```
0 a
1 b
2 c
```

The search, rewritten with `enumerate`:

```python
found_at = -1
for index, letter in enumerate(sentence):
    if letter == "o":
        found_at = index
        break
print("First 'o' at index:", found_at)
```

```
First 'o' at index: 12
```

### Maximum and minimum by hand

To find the largest item, start with the first item as "the largest so far", then look at each item and replace your answer whenever you find something bigger. The minimum works the same way with `<`.

```python
digits = "4719362"
largest = int(digits[0])
smallest = int(digits[0])
for character in digits:
    value = int(character)
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value
print("Largest:", largest, "Smallest:", smallest)
```

```
Largest: 9 Smallest: 1
```

Starting from the first item, rather than from 0, matters: if every value were negative, a starting value of 0 would wrongly "win".

### else on a loop

A `for` or `while` loop can have an `else` block. It runs only if the loop finished **without** hitting `break`. That is exactly the "searched everything and found nothing" case:

```python
number = 29
for divisor in range(2, number):
    if number % divisor == 0:
        print(number, "is divisible by", divisor)
        break
else:
    print(number, "is prime")
```

```
29 is prime
```

Note the `else` is lined up with `for`, not with `if`. Change `number` to `27` and the loop breaks at 3, so the `else` block is skipped. Loop `else` is unusual, so many programmers prefer a flag (next section) for clarity. Use whichever reads better.

### Any and all with a flag

A **flag** is a boolean variable that records whether something has happened. To ask "does **any** character match?", start the flag at `False` and set it to `True` on the first match:

```python
password = "secret42"
has_digit = False
for character in password:
    if character.isdigit():
        has_digit = True
        break
print("Password has a digit:", has_digit)
```

```
Password has a digit: True
```

To ask "do **all** characters match?", flip it: start at `True` and set it to `False` on the first character that fails.

## Common mistakes

- **Initialising the maximum to 0.** For the values `-5, -2, -9` this reports a maximum of `0`, which is not even in the data. Start from the first item.
- **Indenting `else` under `if` instead of `for`.** The `else` then belongs to the `if` and runs on every non-matching item. Line it up with `for`.
- **Setting the "found" flag back to `False` inside the loop.** `has_digit = False` inside the loop wipes out an earlier match. Set it once, before the loop.
- **Indexing past the end.** `for index in range(len(text) + 1)` makes `text[index]` raise `IndexError: string index out of range` on the last pass. Use `range(len(text))`, or better, `enumerate`.

## Try it

Modify Example 6 to also record **where** the largest digit is, using `enumerate`. What happens if the largest digit appears twice? Make your code report the first position.

## Exercises

Open `ex_03_05.py`:

1. `count_char`: how many times a character appears in a text.
2. `index_of`: the index of the first occurrence of a character, or -1.
3. `largest_digit`: the largest digit in a string of digits.
4. `is_prime`: whether a whole number is prime.
5. `all_digits`: whether every character in a text is a digit.
6. `last_index_of`: the index of the last occurrence of a character, or -1.

Run the tests:

```
python -m pytest part-1-python-fundamentals/03-control-flow/03-05-loop-patterns
```

## Summary

- Count: start at 0 and add 1 on a match. Sum: start at 0 and add the value.
- Search: set a "not found" default, then `break` on the first match.
- Max and min: start from the first item and replace it when you find a better one.
- `enumerate` gives the index and the item together.
- A loop's `else` runs only if there was no `break`; a boolean flag does the same job more visibly.
