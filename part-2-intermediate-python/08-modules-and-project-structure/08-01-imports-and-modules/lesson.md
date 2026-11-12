# 08-01 Imports and modules

## What you will learn

- Import a module, or specific names from it, and use aliases.
- Split your own code into modules and import them.
- Use `if __name__ == "__main__":` so a file can be both imported and run.
- Explain where Python looks when you import something.

## Why it matters

So far each program has lived in one file. Real projects are spread across many files, and lean heavily on code other people wrote. Every data-science script in Parts 3 to 7 starts with lines like `import numpy as np` and `from sklearn.linear_model import LinearRegression`. This lesson explains exactly what those lines do.

## Concepts

### Modules

A **module** is a file of Python code that other code can use. Every `.py` file is a module; its name is the file name without `.py`. **Importing** a module runs its code once and gives you access to the functions, classes and variables it defines.

### import module

`import math` loads the standard library's `math` module and creates a variable `math` that refers to it. You reach what is inside with a dot:

```python
import math

print(math.pi)
print(math.sqrt(16))
print(math.floor(3.7), math.ceil(3.2))
```

```
3.141592653589793
4.0
3 4
```

The dot keeps it clear where each name comes from: `math.sqrt` is obviously the `math` module's square root.

### from module import name

`from module import name` copies specific names into your file, so you can use them without the module prefix:

```python
from math import pi, sqrt

print(round(pi * 2 ** 2, 2))
print(sqrt(81))
```

```
12.57
9.0
```

This is shorter, but readers must look at the top of the file to see where `sqrt` came from. Avoid `from module import *`, which pulls in every name and makes this impossible.

### Aliases

`as` gives a module (or a name) a different name in your file. Some aliases are universal conventions you will use constantly: `import numpy as np`, `import pandas as pd`, `import matplotlib.pyplot as plt`.

```python
import statistics as stats

print(stats.mean([2, 4, 9]))
print(stats.median([5, 1, 3]))
```

```
5
3
```

### Importing your own modules

Any `.py` file in the same folder as your script can be imported by name. This lesson's folder contains `temperatures.py`:

```python
"""Helper module for lesson 08-01: temperature conversions."""

FREEZING_C = 0.0


def c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def f_to_c(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


print(f"temperatures.py is running, and its __name__ is {__name__!r}")

if __name__ == "__main__":
    # Only runs when this file is run directly, not when it is imported.
    print("Self-test:", c_to_f(100), f_to_c(212))
```

`examples.py` imports it like any other module:

```python
import temperatures

print(temperatures.c_to_f(25))
print(temperatures.FREEZING_C)

import temperatures

print("Imported twice, but the message above appeared once")
```

```
temperatures.py is running, and its __name__ is 'temperatures'
77.0
0.0
Imported twice, but the message above appeared once
```

Importing ran the top-level code of `temperatures.py`, which is why its `print` appeared. The second `import` did nothing: Python remembers modules it has already loaded and never runs them twice. (Normally, imports all go at the top of a file; here they are spread out to show this effect.)

`dir()` lists the names a module contains. Names starting with `_` are internal, so we filter them out:

```python
print([name for name in dir(temperatures) if not name.startswith("_")])
```

```
['FREEZING_C', 'c_to_f', 'f_to_c']
```

### `__name__` and the main guard

Every module has a variable `__name__`. When a file is imported, `__name__` is the module's name. When a file is **run directly**, `__name__` is the string `"__main__"`:

```python
print("In examples.py, __name__ is", repr(__name__))
```

```
In examples.py, __name__ is '__main__'
```

Running `python temperatures.py` directly gives:

```
temperatures.py is running, and its __name__ is '__main__'
Self-test: 212.0 100.0
```

The block under `if __name__ == "__main__":` ran this time, but not when `examples.py` imported the file. This **main guard** lets one file be both a reusable module and a runnable program. The usual pattern, which you saw at the bottom of the expense tracker, is:

```python
def main():
    ...

if __name__ == "__main__":
    main()
```

Code at the top level of a module runs on import, so keep it to definitions (functions, constants, imports) and put actions inside `main()`.

### Where Python looks

When you `import name`, Python searches a list of folders, `sys.path`, in order, and uses the first `name.py` (or package) it finds. The first entry is the folder of the script you ran; after that come the standard library and the packages installed in your virtual environment.

```python
import sys

print(sys.path[0].endswith("08-01-imports-and-modules"))
print(math.__name__, type(math))
```

```
True
math <class 'module'>
```

Because your own folder comes first, a file of yours can accidentally **hide** a standard library module with the same name (see Common mistakes).

## Common mistakes

- **Misspelling a module name.** `import tempratures` gives `ModuleNotFoundError: No module named 'tempratures'`. The same error appears for a package that is not installed (for example `numpy` with the virtual environment not active).
- **Asking for a name the module does not have.** `from math import squareroot` gives `ImportError: cannot import name 'squareroot' from 'math'`, and `math.squareroot(4)` gives `AttributeError: module 'math' has no attribute 'squareroot'`.
- **Naming your file after a standard module.** A file called `random.py` in your folder is imported instead of the real one, and `random.randint` gives `AttributeError: module 'random' has no attribute 'randint' (consider renaming '.../random.py' since it has the same name as the standard library module named 'random' ...)`. Rename your file.
- **Doing work at the top level of a module.** Prints and calculations outside functions run every time the module is imported. Put them in `main()` behind the main guard.

## Try it

Create `geometry.py` in this folder with functions `circle_area(radius)` and `square_area(side)`, plus a main guard that prints a quick self-test. Import it in the REPL (started from this folder) and check that the self-test does not run on import.

## Exercises

Open `ex_08_01.py`. Add the imports you need at the top of the file.

1. `circle_area`: the area of a circle, using `math.pi`.
2. `round_up`: round up to the next whole number, using `math.ceil`.
3. `median_of`: the median of a list, using the `statistics` module.
4. `distance`: the distance between two points, using `math.dist`.
5. `imported_modules`: find the module names imported in a piece of source code.

Run the tests:

```
python -m pytest part-2-intermediate-python/08-modules-and-project-structure/08-01-imports-and-modules
```

## Summary

- A module is a `.py` file; `import module` runs it once and gives access through `module.name`.
- `from module import name` imports specific names; `as` gives an alias.
- Files in the script's folder can be imported by name; Python searches `sys.path` in order.
- `__name__` is `"__main__"` only in the file being run, so `if __name__ == "__main__":` separates "run me" code from "import me" code.
- Do not name your files after standard library modules.
