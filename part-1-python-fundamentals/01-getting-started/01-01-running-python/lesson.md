# 01-01 Installing and running Python

## What you will learn

- Install Python 3.11 or newer and check which version you have.
- Use the Python REPL to try out code one line at a time.
- Run a Python file from the terminal.
- Choose an editor and read what the terminal tells you.

## Why it matters

Every lesson, exercise and project in this course is a Python file that you run from the terminal. Getting comfortable with these few commands now means that, later on, when you train your first machine learning model, the only new thing will be the model.

## Concepts

### What Python is

**Python** is a programming language: a precise way of writing instructions that a computer can follow. The program that reads those instructions and carries them out is called the **Python interpreter**. When people say "install Python", they mean install the interpreter.

### Installing Python

- **macOS:** download the installer from [python.org/downloads](https://www.python.org/downloads/), or use Homebrew with `brew install python`.
- **Windows:** download the installer from python.org. On the first screen of the installer, tick **"Add python.exe to PATH"**.
- **Linux:** Python is usually already installed. Use your package manager (for example `sudo apt install python3`) if it is missing or older than 3.11.

### The terminal

The **terminal** (called Terminal on macOS, PowerShell or Command Prompt on Windows) is a window where you type commands as text. You type a command, press Enter, and the terminal prints the result. Check your Python version like this:

```
$ python3 --version
Python 3.13.7
```

The `$` stands for the terminal's prompt; do not type it. Your version number may be different. Anything 3.11 or higher is fine. On Windows, the command is usually `python` or `py` instead of `python3`. In the rest of this course we write `python`; use whichever name works on your machine.

### The REPL

If you type `python3` on its own, you start the **REPL** (Read, Evaluate, Print, Loop). It reads one line of Python, works out its value, prints it, and waits for the next line. The `>>>` prompt means it is ready.

```
$ python3
>>> 2 + 3
5
>>> 7 * 6
42
>>> print("Hello!")
Hello!
>>> exit()
```

The REPL is ideal for quick experiments. Nothing you type there is saved, so anything longer than a few lines belongs in a file. Type `exit()` (or press Ctrl+D on macOS and Linux, Ctrl+Z then Enter on Windows) to leave.

### Running a Python file

A Python file is a plain text file whose name ends in `.py`. To run it, give its path to Python. This lesson's `examples.py` contains:

```python
print("Hello from a Python file!")

print(2 + 3)
print("Seven times six is", 7 * 6)

print("First line")
print("Second line")
print("Third line")
```

From the root of this repository, run:

```
$ python part-1-python-fundamentals/01-getting-started/01-01-running-python/examples.py
Hello from a Python file!
5
Seven times six is 42
First line
Second line
Third line
```

Notice two differences from the REPL. First, a file only shows what you `print`; writing `2 + 3` on its own line in a file would calculate 5 and then throw it away silently. Second, the lines run from top to bottom, one after another, which is why "First line" appears before "Second line".

### Choosing an editor

You need a **code editor**: a text editor that understands code. We recommend **Visual Studio Code** (free, works on every system) with the official Python extension. It colours your code, warns about mistakes as you type, and has a built-in terminal (View > Terminal), so you can edit and run in one window. Any editor that saves plain text works; word processors such as Microsoft Word do not, because they add hidden formatting.

### Reading the terminal

When you run a command, the terminal shows one of three things:

1. **The program's output**, as above. The program finished normally.
2. **An error message** from Python, which starts with `Traceback` or names an error such as `SyntaxError`. Lesson 01-02 shows how to read one.
3. **A message from the terminal itself**, such as `command not found` or `No such file or directory`. This means the problem is the command, not your Python code.

## Common mistakes

- **`python: command not found`** (or `'python' is not recognized` on Windows). The terminal cannot find Python under that name. Try `python3` or `py`. On Windows, rerun the installer and tick "Add python.exe to PATH".
- **`can't open file '.../examples.py': [Errno 2] No such file or directory`.** You are in a different folder from the one you think. Run `pwd` (macOS/Linux) or `cd` (Windows) to see where you are, and `cd` into the repository root first.
- **Typing Python code at the terminal prompt instead of the REPL.** If you type `print("hi")` at the `$` prompt, the terminal itself tries to run it and complains. Start `python3` first, then type Python at the `>>>` prompt.
- **Typing terminal commands inside the REPL.** `python3 examples.py` typed after `>>>` gives `SyntaxError: invalid syntax`. Leave the REPL with `exit()` first.

## Try it

Start the REPL and type `10 / 4`, then `10 // 4`, then `"ha" * 3`. Predict each answer before pressing Enter. You will learn exactly what these do in Module 02.

## Summary

- The Python interpreter runs your code; check it with `python3 --version`.
- The REPL (`>>>`) runs one line at a time and prints each value automatically.
- `python path/to/file.py` runs a whole file from top to bottom; files only show what you `print`.
- Use a code editor such as VS Code, not a word processor.
- Errors that start with `Traceback` come from Python; `command not found` comes from the terminal.

## Review questions

1. What is the difference between "Python the language" and "the Python interpreter"?
2. You type `5 * 5` in the REPL and see `25`. You put the same line in a file and run it, and see nothing. Why?
3. What does the `>>>` prompt tell you?
4. You run `python examples.py` and get `No such file or directory`. Is the problem in your Python code? What should you check?
5. Why is Microsoft Word a bad choice for writing Python?

<details>
<summary>Answers</summary>

1. The language is the set of rules for writing instructions. The interpreter is the program that reads and carries out code written in that language.
2. The REPL prints the value of every line automatically. A file only shows values that you pass to `print`.
3. That the Python REPL is running and waiting for a line of Python.
4. No. The terminal could not find the file. Check which folder you are in (`pwd` or `cd`) and that the path you typed is correct.
5. Word saves formatting information alongside the text and may change quotes into "smart quotes", so Python cannot read the file correctly. Code must be saved as plain text.

</details>
