# 08-04 Command-line programs

## What you will learn

- Read command-line arguments from `sys.argv`.
- Describe and parse arguments, options and flags with `argparse`.
- Return exit codes that tell the terminal whether a program succeeded.
- Structure a command-line program so its logic is easy to test.

## Why it matters

Your expense tracker asked questions with `input()`. Most real tools instead take everything on the command line, like `pip install -r requirements.txt` or `pytest -q`. That makes them scriptable: you can run them in a loop, from another program, or on a schedule. Your Part 2 project is a command-line tool, and many machine learning scripts are run as `python train.py --epochs 20 --seed 42`.

## Concepts

### sys.argv

When you run `python greet.py Ada --times 2`, the words after `python` are stored in the list **`sys.argv`**. `sys.argv[0]` is the script's path, and the arguments follow: here, `["greet.py", "Ada", "--times", "2"]`. Every item is a string.

```python
import argparse
import sys

print(sys.argv[0].endswith("examples.py"), len(sys.argv))
```

```
True 1
```

`examples.py` was run with no arguments, so the list holds only the script name. You can process `sys.argv[1:]` by hand:

```python
def add_numbers(arguments):
    return sum([float(argument) for argument in arguments])


print(add_numbers(["3", "4.5"]))
```

```
7.5
```

That is fine for one or two plain arguments, but options such as `--times 2`, defaults, type checking and help messages quickly get complicated. That is what `argparse` is for.

### argparse

The standard library's **`argparse`** module lets you **describe** the arguments you expect and then does the parsing, the type conversion, the error messages and the help text for you.

```python
def build_parser():
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--times", type=int, default=1, help="how many greetings")
    parser.add_argument("--shout", action="store_true", help="use capitals")
    return parser
```

There are three kinds of argument here:

- A **positional argument** (`name`) is required and identified by position.
- An **option** (`--times`) starts with `--`, takes a value, and is optional. `type=int` converts the text, and `default=1` is used when it is left out.
- A **flag** (`--shout`) takes no value; `action="store_true"` makes it `True` when present and `False` otherwise.

`parse_args` takes a list of strings (by default `sys.argv[1:]`) and returns an object whose attributes hold the values. Passing a list explicitly is how you test a parser without a terminal:

```python
parser = build_parser()
args = parser.parse_args(["Ada", "--times", "2", "--shout"])
print(args)
print(args.name, args.times, args.shout)
print(parser.parse_args(["Grace"]))
```

```
Namespace(name='Ada', times=2, shout=True)
Ada 2 True
Namespace(name='Grace', times=1, shout=False)
```

`times` is already an `int`. Options can come in any order, before or after the positional argument.

### Help for free

argparse builds a help message from your descriptions. Users see it with `--help` (or `-h`):

```python
parser.print_help()
```

```
usage: examples.py [-h] [--times TIMES] [--shout] name

Greet someone.

positional arguments:
  name           who to greet

options:
  -h, --help     show this help message and exit
  --times TIMES  how many greetings
  --shout        use capitals
```

### Exit codes

When a program finishes, it returns a whole number to the terminal called the **exit code**. By convention, **0 means success** and anything else means failure. Scripts and tools such as CI systems check it to decide whether to carry on. A clean design is a `main(argv)` function that returns the exit code, with error messages sent to **standard error** (`file=sys.stderr`), the separate output stream for problems:

```python
def main(argv):
    args = build_parser().parse_args(argv)
    if args.times < 1:
        print("error: --times must be at least 1", file=sys.stderr)
        return 1
    greeting = f"Hello, {args.name}!"
    if args.shout:
        greeting = greeting.upper()
    for _ in range(args.times):
        print(greeting)
    return 0


print("exit code:", main(["Linus", "--times", "2"]))
print("exit code:", main(["Linus", "--times", "0"]))
```

```
Hello, Linus!
Hello, Linus!
exit code: 0
error: --times must be at least 1
exit code: 1
```

When argparse itself finds a problem, it prints a usage message and exits with code 2 by raising `SystemExit`:

```python
try:
    build_parser().parse_args(["Ada", "--times", "lots"])
except SystemExit as error:
    print("argparse exited with code", error.code)
```

```
usage: examples.py [-h] [--times TIMES] [--shout] name
examples.py: error: argument --times: invalid int value: 'lots'
argparse exited with code 2
```

### A complete program

`greet.py` in this folder puts it all together. The last lines connect `main` to the terminal: `main()` with no argument makes argparse read `sys.argv`, and `sys.exit` hands the exit code to the terminal.

```python
if __name__ == "__main__":
    sys.exit(main())
```

Try it from the repository root:

```
$ python part-2-intermediate-python/08-modules-and-project-structure/08-04-command-line-programs/greet.py Ada --times 2 --shout
HELLO, ADA!
HELLO, ADA!
$ echo $?
0
```

`echo $?` shows the exit code of the last command (on Windows PowerShell, `echo $LASTEXITCODE`). Leaving out `name` gives `greet.py: error: the following arguments are required: name` and exit code 2.

The design rule: keep `main(argv)` thin. It parses arguments, calls ordinary functions that do the real work and return values, prints results, and returns an exit code. The real work is then easy to test without any terminal.

## Common mistakes

- **Forgetting that `sys.argv` items are strings.** `sys.argv[1] + 1` gives a `TypeError`. Use `type=int` in argparse, or convert yourself.
- **Indexing `sys.argv` without checking its length.** `sys.argv[1]` with no arguments gives `IndexError: list index out of range`. argparse reports missing arguments properly.
- **Writing `action="store_true"` options with a value.** `--shout yes` gives `error: unrecognized arguments: yes`. Flags take no value.
- **Calling `sys.exit` deep inside functions.** It makes them impossible to test. Return values and exit codes from `main`, and call `sys.exit` only in the main guard.

## Try it

Add a `--greeting` option to `greet.py` with a default of `"Hello"`, so `greet.py Ada --greeting Hi` prints `Hi, Ada!`. Check that `--help` describes it.

## Exercises

Open `ex_08_04.py`. You will build a small temperature conversion tool.

1. `parse_key_values`: turn `["name=Ada", "age=36"]` into a dictionary, as you might for `sys.argv[1:]`.
2. `convert`: convert a temperature to Celsius or Fahrenheit.
3. `build_parser`: an argparse parser for the tool.
4. `main`: parse, check, convert, print and return an exit code.

Run the tests:

```
python -m pytest part-2-intermediate-python/08-modules-and-project-structure/08-04-command-line-programs
```

## Summary

- `sys.argv` lists the command-line words as strings; `sys.argv[0]` is the script.
- `argparse` handles positional arguments, `--options` with types and defaults, and `store_true` flags.
- `parse_args(list)` lets you test a parser directly; argparse generates `--help` and exits with code 2 on bad input.
- Exit code 0 means success; send error messages to `sys.stderr`.
- Keep `main(argv)` thin, return the exit code, and call `sys.exit(main())` only in the main guard.
