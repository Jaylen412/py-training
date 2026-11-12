# 06-01 Reading and writing text files

## What you will learn

- Build file paths that work on every operating system with `pathlib.Path`.
- Open files safely with `with`, in read, write and append modes.
- Read a whole file, or go through it line by line.
- Write text to a file, including several lines at once.

## Why it matters

Programs that forget everything when they stop are of limited use. Files let you keep data between runs, read data that someone else produced, and save your results. Your Part 1 project stores expenses in a file, and every dataset in Parts 3 to 7 is loaded from one.

## Concepts

### Paths

A **path** says where a file lives, such as `data/store_sales.csv`. Windows writes paths with backslashes and macOS and Linux with forward slashes, so building them by joining strings is fragile. The standard library's **`pathlib`** module gives you `Path` objects that handle this for you. The `/` operator joins parts of a path.

```python
from pathlib import Path

lesson_folder = Path(__file__).parent
notes_path = lesson_folder / "notes.txt"
print(notes_path.name, notes_path.suffix, notes_path.stem)
```

```
notes.txt .txt notes
```

The first line makes `Path` available; Module 08 explains `from ... import`. `__file__` is a special variable holding the path of the script that is running, and `.parent` is the folder containing it. Building paths from `Path(__file__).parent` means the script finds its files no matter which folder you run it from.

### Opening a file with with

To use a file you **open** it, which gives you a **file object**, and when you are done you must **close** it so that everything is saved and the operating system can release it. The `with` statement does the closing for you, even if something goes wrong inside the block:

```python
with open(notes_path, "w") as file:
    file.write("first line\n")
    file.write("second line\n")
print(notes_path.exists())
```

```
True
```

The second argument to `open` is the **mode**:

| Mode | Meaning |
|------|---------|
| `"r"` | read (the default); the file must exist |
| `"w"` | write; creates the file, or **empties it** if it already exists |
| `"a"` | append; creates the file, or adds to the end of it |

`write` does not add a newline for you, so each line ends with `"\n"`. Indented code under `with` can use `file`; after the block, the file is closed.

### Reading

`read()` returns the entire file as one string. `repr()` shows a string the way you would type it in code, which makes the hidden `\n` characters visible:

```python
with open(notes_path) as file:
    content = file.read()
print(repr(content))
```

```
'first line\nsecond line\n'
```

### Appending

Mode `"a"` adds to the end without touching what is already there:

```python
with open(notes_path, "a") as file:
    file.write("third line\n")
```

### Reading line by line

A file object can be looped over directly, giving one line at a time. This works even for files far too large to fit in memory. Each line still ends with `"\n"`, so remove it with `rstrip("\n")` (or `strip()` to remove spaces too):

```python
with open(notes_path) as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, line.rstrip("\n"))
```

```
1 first line
2 second line
3 third line
```

`enumerate(file, start=1)` numbers the lines from 1 instead of 0.

To get a list of lines without the newlines, read everything and use the string method `splitlines()`:

```python
with open(notes_path) as file:
    lines = file.read().splitlines()
print(lines)
```

```
['first line', 'second line', 'third line']
```

### Writing several lines

`join` (02-04) turns a list of strings into one string with newlines between them:

```python
shopping = ["eggs", "flour", "milk"]
shopping_path = lesson_folder / "shopping.txt"
with open(shopping_path, "w") as file:
    file.write("\n".join(shopping) + "\n")
print(shopping_path.read_text())
```

```
eggs
flour
milk

```

(The blank line at the end is `print`'s own newline after the file's final `"\n"`.)

### Path shortcuts

For small files, `Path` objects have shortcuts that open, read or write, and close in one step:

```python
summary_path = lesson_folder / "summary.txt"
summary_path.write_text("3 items\n")
print(summary_path.read_text().strip())
```

```
3 items
```

`glob` lists files matching a pattern, where `*` means "anything". `exists()` checks for a file and `unlink()` deletes one:

```python
for path in sorted(lesson_folder.glob("*.txt")):
    print("Found:", path.name)

for path in [notes_path, shopping_path, summary_path]:
    path.unlink()
print(notes_path.exists())
```

```
Found: notes.txt
Found: shopping.txt
Found: summary.txt
False
```

## Common mistakes

- **Opening a file that is not there.** `open("missing.txt")` gives `FileNotFoundError: [Errno 2] No such file or directory: 'missing.txt'`. Check the path, and remember that a relative path is relative to the folder you ran Python **from**, not the folder of the script. Build paths from `Path(__file__).parent`.
- **Wiping a file with `"w"`.** Opening an existing file in `"w"` mode empties it immediately. Use `"a"` to add to it.
- **Writing a number.** `file.write(5)` gives `TypeError: write() argument must be str, not int`. Convert with `str()` or use an f-string.
- **Using the file after the `with` block.** `file.read()` after the block gives `ValueError: I/O operation on closed file.`. Do all the reading inside the block.

## Try it

Write a script that asks for nothing, but appends the current line count of a file `log.txt` to the end of that same file each time it runs. Run it three times and look at the file. (Hint: handle the first run, when the file does not exist yet, with `exists()`.)

## Exercises

Open `ex_06_01.py`. Every function receives a `Path`. The tests create temporary files for you.

1. `count_lines`: how many lines a file has.
2. `write_lines`: write a list of strings to a file, one per line.
3. `append_line`: add one line to the end of a file.
4. `longest_line`: the longest line in a file, without its newline.
5. `file_stats`: the number of lines, words and characters, as a tuple.

Run the tests:

```
python -m pytest part-1-python-fundamentals/06-files-and-errors/06-01-text-files
```

## Summary

- Build paths with `pathlib.Path` and `/`; `Path(__file__).parent` is the script's folder.
- `with open(path, mode) as file:` opens a file and closes it automatically.
- Modes: `"r"` read, `"w"` write (empties the file first), `"a"` append.
- `read()` gives one string; looping over the file gives one line at a time, each ending in `"\n"`.
- `write` needs strings and adds no newlines; `Path.read_text` and `write_text` are shortcuts for small files.
