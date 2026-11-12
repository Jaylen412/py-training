# 01-03 Virtual environments and pip

## What you will learn

- Explain what a package is and why projects keep their own copies.
- Create and activate a virtual environment with `python -m venv`.
- Install this course's packages with `pip install -r requirements.txt`.
- Run the course tests with `pytest`.

## Why it matters

Parts 3 to 7 of this course depend on packages that do not come with Python: NumPy, pandas, Matplotlib, seaborn and scikit-learn. Setting up a virtual environment now means that every lesson runs the same way on your machine as it did when it was written, and the exercise tests work from day one.

## Concepts

### Packages

A **package** is a bundle of Python code that someone else wrote and shared so that you can use it. Python ships with a large **standard library** of built-in tools, but most data science tools are separate packages. They are published on the **Python Package Index (PyPI)**, a public catalogue at pypi.org.

**pip** is the program that downloads packages from PyPI and installs them. It comes with Python.

### Why a virtual environment?

If you install packages for the whole computer, every project shares one set. Project A might need an old version of a package while project B needs a new one, and they cannot both have their way. A **virtual environment** is a private folder holding its own Python and its own packages for one project. Packages installed into it do not affect anything else on your computer, and you can delete the folder and start again at any time.

### Creating one

From the repository root, run:

```
$ python3 -m venv .venv
```

This means "run the `venv` tool that comes with Python and create an environment in a folder called `.venv`". The name `.venv` is a common convention. The folder is listed in this repository's `.gitignore` file, so it is never saved to version control.

### Activating it

**Activating** an environment tells your terminal to use its Python and pip instead of the system ones.

```
# macOS and Linux
$ source .venv/bin/activate

# Windows PowerShell
> .venv\Scripts\Activate.ps1
```

Your prompt now starts with `(.venv)`. Inside an active environment, plain `python` and `pip` always point at the environment's copies, whatever your system calls them. Activation only lasts for that terminal window: open a new window and you must activate again. To switch it off, type `deactivate`.

VS Code can do this for you: open the Command Palette, choose **Python: Select Interpreter**, and pick the one inside `.venv`.

### Installing the course packages

The file `requirements.txt` at the repository root lists the packages this course uses, one per line:

```
numpy
pandas
matplotlib
seaborn
scikit-learn
pytest
```

With the environment active, install them all at once:

```
(.venv) $ pip install -r requirements.txt
```

The `-r` flag means "read the package names from this file". The download takes a minute or two. You only need to do this once per environment.

### Checking it worked

This lesson's `examples.py` asks Python where it is running from:

```python
import sys

print("Python program:", sys.executable)
print("Python version:", sys.version.split()[0])
print("Inside a virtual environment:", sys.prefix != sys.base_prefix)
```

The first line loads a built-in tool called `sys`; you will learn about `import` in Module 08. Run it with the environment active:

```
(.venv) $ python part-1-python-fundamentals/01-getting-started/01-03-virtual-environments/examples.py
Python program: /Users/you/py-training/.venv/bin/python
Python version: 3.13.7
Inside a virtual environment: True
```

Your path and version will differ. What matters is that the path contains `.venv` and the last line says `True`.

### Running the tests with pytest

**pytest** is a package for running **tests**: small programs that check whether other code gives the right answers. Every exercise in this course comes with a test file, named like `test_ex_01_02.py`. To check your work on a lesson, point pytest at the lesson's folder:

```
(.venv) $ python -m pytest part-1-python-fundamentals/01-getting-started/01-02-first-program
```

pytest prints a dot for each passing test and an `F` for each failing one, followed by details of the failures. Before you start an exercise, every test fails with `NotImplementedError`; that is expected. Your job is to make them pass.

Each lesson also has a reference solution file, such as `sol_01_02.py`. Try the exercises yourself before you look.

## Common mistakes

- **`ModuleNotFoundError: No module named 'pytest'`** (or `'numpy'`). Either the environment is not active in this terminal, or you have not installed the requirements into it. Activate it and run `pip install -r requirements.txt`.
- **Running `pip install` before activating.** The packages go into the system Python instead, and may fail with `error: externally-managed-environment`. Activate first, then install.
- **PowerShell refuses to run `Activate.ps1`** with a message about execution policies. Run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once, then try again.
- **Creating the environment in the wrong folder.** If `.venv` ends up inside a lesson folder, `pip install -r requirements.txt` cannot find the file. Delete that `.venv`, `cd` to the repository root, and create it again.

## Try it

Run `pip list` with the environment active, then again after `deactivate`. Compare the two lists: the environment should contain numpy, pandas and the rest, while your system Python probably does not.

## Summary

- Packages are shared Python code; pip installs them from PyPI.
- A virtual environment gives one project its own Python and packages.
- Create with `python3 -m venv .venv`, activate with `source .venv/bin/activate` (or `.venv\Scripts\Activate.ps1`).
- Install the course packages with `pip install -r requirements.txt`.
- Check exercises with `python -m pytest <lesson folder>`.

## Review questions

1. What is the difference between the standard library and a package from PyPI?
2. Name one problem that virtual environments solve.
3. You open a new terminal window and get `No module named 'pandas'`, although it worked yesterday. What most likely happened?
4. What does the `-r` in `pip install -r requirements.txt` mean?
5. You run pytest on a lesson before writing any code and every test fails. Is something broken?

<details>
<summary>Answers</summary>

1. The standard library comes with Python and is always available. A PyPI package is shared separately and must be installed with pip first.
2. Two projects needing different versions of the same package. Each project gets its own environment with its own versions.
3. The virtual environment is not active in the new window. Activation only lasts for one terminal session; activate it again.
4. Read the list of packages to install from the named file.
5. No. The exercise stubs raise `NotImplementedError` until you write them, so the tests are expected to fail at the start.

</details>
