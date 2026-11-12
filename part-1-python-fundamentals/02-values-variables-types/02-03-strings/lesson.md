# 02-03 Strings

## What you will learn

- Write strings with single, double and triple quotes, including quotes and special characters inside them.
- Join and repeat strings with `+` and `*`, and measure them with `len`.
- Pick out single characters by index and pieces by slicing.
- Explain why strings cannot be changed in place, and build new ones instead.

## Why it matters

Much real-world data arrives as text: names, dates, product codes, lines of a log file. Before you can turn text into numbers a model can use, you need to take it apart and put it back together. Indexing and slicing also work the same way on lists (Module 05) and on NumPy arrays (Module 13), so you will use these ideas for the rest of the course.

## Concepts

### Writing strings

A **string** (type `str`) is a sequence of characters: letters, digits, spaces, punctuation. You can use single or double quotes; they mean exactly the same thing.

```python
greeting = "Hello"
name = 'Ada'
print(greeting, name)
```

```
Hello Ada
```

Choose the kind that does not appear inside the text. If you must use the same kind, put a backslash in front of it:

```python
print("It's raining")
print('She said "hi"')
print('It\'s raining')
```

```
It's raining
She said "hi"
It's raining
```

### Escape sequences

A backslash starts an **escape sequence**: a two-character code for a character that is hard to type. `\n` is a new line, `\t` is a tab, and `\\` is a single backslash.

```python
print("Line one\nLine two")
print("Name:\tAda")
print("A backslash: \\")
```

```
Line one
Line two
Name:	Ada
A backslash: \
```

Triple quotes (`"""` or `'''`) let a string run over several lines, keeping the line breaks:

```python
poem = """Roses are red,
Violets are blue."""
print(poem)
```

```
Roses are red,
Violets are blue.
```

### Joining, repeating and length

`+` joins (or **concatenates**) two strings. `*` repeats a string a whole number of times. `len` gives the number of characters.

```python
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("-" * 20)
print(len(full_name))
print(len(""))
```

```
Ada Lovelace
--------------------
12
0
```

`+` adds no space by itself, so we added `" "` in the middle. The space counts as a character, which is why the length is 12. `""` is the **empty string**, with length 0.

### Indexing

Each character has a position, called its **index**. Indexes start at **0**, not 1. Square brackets after a string pick out the character at an index. Negative indexes count from the end: `-1` is the last character.

```
 P   y   t   h   o   n
 0   1   2   3   4   5
-6  -5  -4  -3  -2  -1
```

```python
word = "Python"
print(word[0])
print(word[1])
print(word[5])
print(word[-1])
print(word[-2])
```

```
P
y
n
n
o
```

The last index is always `len(word) - 1`, here 5.

### Slicing

A **slice** picks out a piece of a string. `word[start:stop]` gives the characters from index `start` up to **but not including** `stop`. Leave out `start` to begin at the start, leave out `stop` to go to the end. A third number, the **step**, takes every n-th character; a step of `-1` goes backwards.

```python
print(word[0:2])
print(word[2:5])
print(word[:3])
print(word[3:])
print(word[::2])
print(word[::-1])
```

```
Py
tho
Pyt
hon
Pto
nohtyP
```

A handy property: `word[:3] + word[3:]` always gives back the whole word, because the first slice stops exactly where the second begins. The number of characters in `word[start:stop]` is `stop - start`.

### Strings are immutable

**Immutable** means "cannot be changed". Once a string exists, you cannot replace one of its characters. Instead, you build a new string from pieces of the old one:

```python
fixed = "J" + word[1:]
print(fixed)
print(word)
```

```
Jython
Python
```

`word` is untouched. If you want the name `word` to refer to the new string, reassign it: `word = "J" + word[1:]`.

## Common mistakes

- **Index out of range.** `"Python"[6]` gives `IndexError: string index out of range`. The last index is `len - 1`. (Slices never raise this error: `"Python"[10:20]` quietly gives an empty string.)
- **Trying to change a character.** `word[0] = "J"` gives `TypeError: 'str' object does not support item assignment`. Build a new string instead.
- **Joining a string and a number.** `"Total: " + 5` gives `TypeError: can only concatenate str (not "int") to str`. Convert the number with `str(5)` (more on this in 02-05), or pass both to `print` separated by a comma.
- **Off-by-one slices.** `word[1:3]` is `"yt"`, two characters, not three. The stop index is not included.

## Try it

Set `date = "2026-11-11"`. Using only slicing, print the year, the month and the day separately. Then print the date in the form `11/11/2026` using slices and `+`.

## Exercises

Open `ex_02_03.py`:

1. `first_and_last`: the first and last characters joined together.
2. `initials`: initials with full stops, from a first and last name.
3. `reverse_text`: the text backwards.
4. `without_ends`: the text with its first and last characters removed.
5. `make_tag`: wrap a name in angle brackets, as in `<div>`.

Run the tests:

```
python -m pytest part-1-python-fundamentals/02-values-variables-types/02-03-strings
```

## Summary

- Strings can use single, double or triple quotes; `\n`, `\t` and `\\` are escape sequences.
- `+` joins strings, `*` repeats them, `len` counts characters.
- Indexes start at 0; negative indexes count from the end.
- `text[start:stop:step]` slices, excluding `stop`; `text[::-1]` reverses.
- Strings are immutable: build new strings rather than changing old ones.
