# 02-04 String methods and f-strings

## What you will learn

- Clean and transform text with string methods such as `strip`, `lower` and `replace`.
- Break text apart with `split` and put it back together with `join`.
- Search text with `find`, `count` and `in`.
- Build readable output with f-strings, including formatted numbers.

## Why it matters

Raw data is messy: names in random capitals, stray spaces, commas inside numbers. Cleaning text is one of the first steps of every data project, and in Part 3 pandas gives you these same methods for whole columns at once. f-strings are how you will report results, such as `Accuracy: 94.3%`, throughout the course.

## Concepts

### Methods

A **method** is a function that belongs to a value. You call it by writing the value, a dot, the method name and brackets: `title.lower()`. String methods never change the original string (strings are immutable); they **return** a new one.

```python
title = "Machine Learning"
print(title.lower())
print(title.upper())
print("ada lovelace".title())
print(title)
```

```
machine learning
MACHINE LEARNING
Ada Lovelace
Machine Learning
```

The last line shows that `title` itself is unchanged.

### Removing whitespace

**Whitespace** means spaces, tabs and new lines. `strip` removes it from both ends of a string, `lstrip` from the left only and `rstrip` from the right only. Whitespace in the middle is left alone. (The square brackets below just make the edges visible.)

```python
raw_input = "   hello world  \n"
print("[" + raw_input.strip() + "]")
print("[" + raw_input.lstrip() + "]")
print("[" + raw_input.rstrip() + "]")
```

```
[hello world]
[hello world  
]
[   hello world]
```

### replace

`replace(old, new)` swaps every occurrence of `old` for `new`. It is case-sensitive. Because each method returns a string, you can **chain** methods, calling the next one on the result of the last:

```python
sentence = "I like cats. Cats are great."
print(sentence.replace("cats", "dogs"))
print(sentence.replace("Cats", "Dogs").replace("cats", "dogs"))
```

```
I like dogs. Cats are great.
I like dogs. Dogs are great.
```

### split and join

`split(separator)` cuts a string into pieces wherever the separator appears. With no separator, it splits on any run of whitespace. The result is a **list** of strings, shown in square brackets. You will study lists in Module 05; for now, think of a list as an ordered collection of values.

`separator.join(pieces)` does the reverse: it glues a list of strings together with the separator between them.

```python
csv_line = "Ada,36,London"
parts = csv_line.split(",")
print(parts)
print("one two  three".split())
print(" - ".join(parts))
```

```
['Ada', '36', 'London']
['one', 'two', 'three']
Ada - 36 - London
```

Note that `"36"` is still a string after splitting. Lesson 02-05 shows how to turn it into a number.

### Searching

`find(text)` gives the index where `text` first appears, or `-1` if it does not appear at all. `count(text)` gives the number of times it appears. The `in` operator answers yes or no, giving `True` or `False`:

```python
email = "ada@example.com"
print(email.find("@"))
print(email.find("#"))
print("@" in email)
print("example" in email)
print(email.count("a"))
```

```
3
-1
True
True
3
```

### Chaining for cleaning

A common cleaning recipe is to strip, then change case:

```python
messy = "  PyThOn  "
print(messy.strip().lower())
```

```
python
```

### f-strings

An **f-string** is a string with an `f` before the opening quote. Anything inside curly brackets `{}` is worked out as Python and its value is inserted into the text.

```python
name = "Ada"
age = 36
print(f"{name} is {age} years old")
print(f"Next year {name} will be {age + 1}")
```

```
Ada is 36 years old
Next year Ada will be 37
```

This is much easier to read than joining pieces with `+`, and numbers are converted to text for you.

### Formatting numbers

After the expression in an f-string, a colon starts a **format specification** that controls how the value looks:

```python
price = 1234.5
print(f"{price:.2f}")
print(f"{price:,.2f}")
print(f"{0.4567:.1%}")
print(f"{7:03d}")
print(f"[{name:>6}]")
print(f"[{name:<6}]")
```

```
1234.50
1,234.50
45.7%
007
[   Ada]
[Ada   ]
```

| Format | Meaning |
|--------|---------|
| `.2f` | Fixed point with 2 decimal places |
| `,.2f` | Same, with commas between thousands |
| `.1%` | Multiply by 100 and show as a percentage, 1 decimal place |
| `03d` | Whole number, padded with zeros to width 3 |
| `>6` / `<6` | Right-align / left-align in a space 6 characters wide |

## Common mistakes

- **Forgetting the brackets on a method.** `"hello".upper` (no brackets) does not call the method; printing it shows something like `<built-in method upper of str object at 0x...>`. Write `"hello".upper()`.
- **Expecting a method to change the string.** `name.strip()` on its own line does nothing useful, because the cleaned string is thrown away. Write `name = name.strip()`.
- **Forgetting the `f`.** `print("Hello {name}")` prints `Hello {name}` literally. Put `f` before the quote.
- **Splitting on the wrong separator.** `"a b".split(",")` gives `['a b']`, a single piece, because there is no comma. Check what actually separates the parts.

## Try it

Take `raw = "  ALAN turing , 41 , london  "`. Using `split`, `strip` and `title`, print `Alan Turing (41) lives in London` with an f-string.

## Exercises

Open `ex_02_04.py`:

1. `clean_name`: tidy up a name with stray spaces and random capitals.
2. `count_words`: the number of words in a sentence.
3. `slugify`: turn a title into a URL-friendly slug.
4. `format_price`: show an amount as money with two decimal places and commas.
5. `format_percentage`: show a fraction as a percentage with one decimal place.
6. `is_mentioned`: whether a word appears in a text, ignoring case.

Run the tests:

```
python -m pytest part-1-python-fundamentals/02-values-variables-types/02-04-string-methods-and-f-strings
```

## Summary

- String methods return new strings; assign the result if you want to keep it.
- `strip`, `lower`, `upper`, `title` and `replace` clean and transform text.
- `split` breaks text into a list; `separator.join(list)` puts it back together.
- `find`, `count` and `in` search text.
- f-strings insert values with `{}`; format specifications like `:.2f` and `:.1%` control how numbers look.
