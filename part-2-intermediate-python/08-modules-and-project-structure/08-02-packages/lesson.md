# 08-02 Packages

## What you will learn

- Group related modules into a package: a folder with an `__init__.py` file.
- Import modules and names from inside a package.
- Use relative imports between modules of the same package, and know when absolute imports are better.
- Lay out a small project as a package plus tests.

## Why it matters

Large libraries are packages of packages: `sklearn.linear_model` is the `linear_model` package inside `sklearn`, and `from sklearn.model_selection import train_test_split` reaches two levels in. Your Part 2 project is an installable package of its own. Knowing how packages are laid out lets you read other people's projects and organise yours.

## Concepts

### What a package is

A **package** is a folder of modules that belong together, containing a file called **`__init__.py`**. The folder name is the package name. This lesson's folder contains a small package called `shop`:

```
08-02-packages/
├── examples.py
└── shop/
    ├── __init__.py    runs when the package is imported
    ├── pricing.py     a module inside the package
    └── cart.py        another module, which imports from pricing
```

`shop/pricing.py`:

```python
"""Price calculations for the shop package."""

TAX_RATE = 0.2


def with_tax(price):
    """Return the price with tax added."""
    return round(price * (1 + TAX_RATE), 2)


def apply_discount(price, rate):
    """Return the price with `rate` (0.1 means 10%) taken off."""
    return round(price * (1 - rate), 2)
```

The module's full name is `shop.pricing`: package name, dot, module name.

### Importing from a package

There are three common forms, all used in `examples.py`:

```python
import shop.pricing

print(shop.pricing.with_tax(10))

from shop.pricing import apply_discount

print(apply_discount(50, 0.1))

from shop import cart

print(cart.cart_total([10, 20]))
```

```
12.0
45.0
36.0
```

1. `import package.module` gives the full dotted path, which is long but unambiguous.
2. `from package.module import name` brings in a single name.
3. `from package import module` brings in a module, used as `module.name`.

### `__init__.py`

`__init__.py` runs the first time any part of the package is imported. It can be empty, but it is often used to make the most useful names available directly on the package, so users do not need to know which module they live in:

```python
"""A tiny shop package for lesson 08-02.

Names imported here can be used as `shop.name` by anyone who imports the package.
"""
from .cart import cart_total

VERSION = "1.0"
```

```python
import shop

print(shop.cart_total([5]))
print(shop.VERSION)
```

```
6.0
1.0
```

This is why you can write `pandas.DataFrame` even though `DataFrame` is defined deep inside pandas.

A package is itself a module, with a `__name__` and a file (its `__init__.py`):

```python
print(shop.__name__, shop.pricing.__name__)
print(shop.__file__.endswith("__init__.py"))
```

```
shop shop.pricing
True
```

### Relative and absolute imports

Inside a package, one module often needs another. `shop/cart.py` does this:

```python
"""Shopping cart totals. Uses a relative import to reach a sibling module."""
from .pricing import with_tax


def cart_total(prices):
    """Return the total of a list of prices, including tax."""
    return round(sum([with_tax(price) for price in prices]), 2)
```

The leading dot in `.pricing` makes it a **relative import**: "the module `pricing` in the **same package** as me". Two dots, `..module`, means "in the package one level up". The alternative is an **absolute import**, which spells out the full path from the top: `from shop.pricing import with_tax`.

- **Absolute imports** are clearer to read and work anywhere. Prefer them in general, and always in scripts.
- **Relative imports** are handy inside a package, because they keep working if the package is renamed. They only work in modules that are part of a package.

### Laying out a small project

A typical small project separates the package from its tests and from data:

```
log-tools/
├── README.md
├── pyproject.toml      project details, for installing (Part 2 project)
├── src/
│   └── logtools/
│       ├── __init__.py
│       ├── parsing.py
│       └── reports.py
└── tests/
    ├── test_parsing.py
    └── test_reports.py
```

Each module holds one area of the work (parsing, reporting), the tests mirror the modules, and the `src/` folder keeps the package from being importable by accident without being installed. You will build exactly this shape in the Part 2 project.

## Common mistakes

- **Running a package module directly.** `python shop/cart.py` gives `ImportError: attempted relative import with no known parent package`, because run as a script it is not "inside" a package. Import it from a script outside the package instead, as `examples.py` does.
- **Forgetting `__init__.py`.** Without it, Python may still import the folder in some cases, but tools and tests behave inconsistently. Always include one, even if it is empty.
- **Circular imports.** If `cart.py` imports `pricing.py` and `pricing.py` imports `cart.py`, one of them sees the other only half-loaded, often giving `ImportError: cannot import name ... (most likely due to a circular import)`. Move the shared code into a third module that both import.
- **Putting heavy work in `__init__.py`.** It runs on every import of the package, so keep it to imports and constants.

## Try it

Add a module `shop/receipts.py` with a function `receipt_line(item, price)` that returns a line such as `"pen      $1.80"`, using `with_tax` through a relative import. Import it from a new script in this folder and print a receipt for three items.

## Exercises

Open `ex_08_02.py`:

1. `module_name_from_path`: turn a file path such as `"shop/pricing.py"` into a module name.
2. `resolve_relative`: work out the absolute name of a relative import.
3. `is_valid_module_name`: whether a dotted name could be imported.
4. `discounted_cart_total`: a cart total built with the `shop` package's functions.

Run the tests:

```
python -m pytest part-2-intermediate-python/08-modules-and-project-structure/08-02-packages
```

## Summary

- A package is a folder of modules with an `__init__.py`; modules inside are named `package.module`.
- `import package.module`, `from package.module import name` and `from package import module` all work.
- `__init__.py` runs on first import and can re-export useful names.
- `.module` is a relative import (same package); prefer absolute imports outside packages.
- Keep a project's package, tests and data in separate folders.
