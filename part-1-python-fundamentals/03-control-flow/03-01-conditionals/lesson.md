# 03-01 Conditionals

## What you will learn

- Run code only when a condition is true, using `if`.
- Choose between two or more paths with `else` and `elif`.
- Nest one decision inside another.
- Pick between two values in one line with a conditional expression.

## Why it matters

Until now, every line of your programs ran every time. Real programs react: approve a payment or reject it, label an email as spam or not. A trained decision tree in Part 5 is, underneath, nothing more than a large set of nested `if` statements that the computer wrote for itself.

## Concepts

### if

An **`if` statement** runs a block of code only when its **condition**, an expression that is true or false, is true.

```python
temperature = 31
if temperature > 30:
    print("It's hot today.")
    print("Drink plenty of water.")
print("Have a nice day.")
```

```
It's hot today.
Drink plenty of water.
Have a nice day.
```

Three details matter:

- The `if` line ends with a **colon** (`:`).
- The lines that belong to the `if` are **indented**: pushed right by four spaces. This group of lines is called a **block**. Python uses indentation, not brackets, to know which lines are inside.
- The first line that is not indented (`print("Have a nice day.")`) is outside the `if`, so it always runs.

Change `temperature` to `20` and only "Have a nice day." is printed.

### else

`else` gives a second block to run when the condition is false. Exactly one of the two blocks runs.

```python
balance = 40
price = 55
if balance >= price:
    print("Purchase approved")
else:
    print("Not enough money")
```

```
Not enough money
```

### elif

`elif` (short for "else if") adds more conditions. Python checks them **from top to bottom** and runs the block of the **first** one that is true, then skips the rest. `else` at the end catches everything that matched nothing.

```python
score = 72
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)
```

```
Grade: B
```

72 is not 90 or more, but it is 70 or more, so `grade` becomes `"B"`. The `score >= 50` check is never made, even though it is also true.

Because the first true branch wins, order matters. Here the special case can never be reached:

```python
score = 95
if score >= 50:
    print("Passed")
elif score >= 90:
    print("Passed with distinction")  # never reached
```

```
Passed
```

Put the most specific (strictest) conditions first.

### Nested conditionals

A block can contain another `if`. Each level is indented four more spaces.

```python
age = 16
has_ticket = True
if has_ticket:
    if age >= 18:
        print("Enjoy the film.")
    else:
        print("Enjoy the film. No alcohol, please.")
else:
    print("Please buy a ticket.")
```

```
Enjoy the film. No alcohol, please.
```

Nesting is fine for two levels. Deeper than that becomes hard to read; the next lesson shows how `and` and `or` can flatten it.

### Truthiness in conditions

A condition does not have to be a comparison. Any value works, using the truthiness rules from 02-05. A common idiom is `if name:` for "if the name is not empty":

```python
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")
```

```
Hello, stranger!
```

### Conditional expressions

When you just need to pick one of two values, a **conditional expression** does it in one line: `value_if_true if condition else value_if_false`.

```python
items_in_basket = 1
label = "item" if items_in_basket == 1 else "items"
print(f"You have {items_in_basket} {label}.")
```

```
You have 1 item.
```

Use it only for short, simple choices. If either side needs more than a value, use a full `if` statement.

### return inside if

In the exercises, a function can `return` from inside any branch. As soon as Python reaches a `return`, the function ends and hands back that value:

```python
def sign_of(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
```

(This function is exercise 1, so it is not in `examples.py`; check your version with the tests.)

## Common mistakes

- **Using `=` in a condition.** `if x = 5:` gives `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?`. Comparison needs `==`.
- **Forgetting the colon.** `if x == 5` gives `SyntaxError: expected ':'`.
- **Forgetting to indent.** An unindented line after `if x == 5:` gives `IndentationError: expected an indented block after 'if' statement on line 2`. Indent the block by four spaces.
- **Inconsistent indentation.** Indenting one line of a block by four spaces and the next by five gives `IndentationError: unexpected indent`. Let your editor insert four spaces when you press Tab.

## Try it

In `examples.py`, change `score` in Example 3 to `90`, `89`, `50` and `49`. Predict the grade each time before running. These boundary values are exactly where bugs hide.

## Exercises

Open `ex_03_01.py`:

1. `sign_of`: whether a number is positive, negative or zero.
2. `letter_grade`: turn a score into A, B, C or F.
3. `ticket_price`: a cinema price that depends on age.
4. `larger_of`: the larger of two numbers, using a conditional expression.
5. `describe_temperature`: a word that describes a temperature.

Run the tests:

```
python -m pytest part-1-python-fundamentals/03-control-flow/03-01-conditionals
```

## Summary

- `if condition:` runs the indented block only when the condition is true.
- `elif` and `else` add alternatives; only the first true branch runs.
- Order your conditions from most to least specific.
- Indentation (four spaces) defines blocks, and every `if`, `elif` and `else` line ends with a colon.
- `a if condition else b` picks between two values in one line.
