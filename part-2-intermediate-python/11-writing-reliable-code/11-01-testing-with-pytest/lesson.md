# 11-01 Testing with pytest

## What you will learn

- Organise tests into a test file with clear, focused test functions.
- Check that code raises the right exception with `pytest.raises`.
- Run one test over many inputs with `@pytest.mark.parametrize`.
- Share set-up between tests with fixtures.

## Why it matters

In 04-05 you wrote your first tests. Real projects have hundreds, and they need structure: no repeated set-up code, many cases per function, and checks that errors happen when they should. Your Part 2 project ships with a pytest suite, and the capstone asks you to test your data-preparation code. In data work, tests catch the silent bugs that would otherwise make a model look better than it really is.

## Concepts

### The code under test

This lesson tests a small `Basket` class, in `basket.py` next to the lesson:

```python
class Basket:
    """Holds items and their prices, and applies discount codes."""

    DISCOUNTS = {"SAVE10": 0.10, "HALF": 0.50}

    def __init__(self):
        self.items = {}
        self.discount = 0.0

    def add(self, name, price, quantity=1):
        if price < 0:
            raise ValueError(f"price cannot be negative: {price}")
        if quantity < 1:
            raise ValueError(f"quantity must be at least 1: {quantity}")
        old_price, old_quantity = self.items.get(name, (price, 0))
        self.items[name] = (price, old_quantity + quantity)

    def apply_code(self, code):
        if code not in self.DISCOUNTS:
            raise KeyError(f"unknown discount code: {code}")
        self.discount = self.DISCOUNTS[code]

    def total(self):
        subtotal = sum(price * quantity for price, quantity in self.items.values())
        return round(subtotal * (1 - self.discount), 2)
```

Used directly:

```python
basket = Basket()
basket.add("pen", 1.50, quantity=2)
basket.add("pad", 4.00)
print(basket.total())
basket.apply_code("SAVE10")
print(basket.total())
```

```
7.0
6.3
```

### Test file structure

pytest **discovers** tests automatically: it looks for files named `test_*.py`, and inside them for functions named `test_*`. A typical layout puts tests in a `tests/` folder, one test file per module, for example `tests/test_basket.py` for `basket.py`. (This lesson's tests are in `basket_checks.py`, a name pytest does not pick up automatically, so they are not mixed into the course's own test runs. `examples.py` runs them explicitly.)

Each test should check **one behaviour**, and its name should say which: `test_unknown_code_raises` tells you what broke without reading the code. A common shape for a test body is **arrange, act, assert**: set things up, do the one thing being tested, then check the result.

### pytest.raises

To check that code raises an exception, wrap it in **`with pytest.raises(ExceptionType):`**. The test passes only if that exception is raised inside the block. `match=` also checks the message, using a pattern that must appear in it:

```python
def test_unknown_code_raises(basket):
    with pytest.raises(KeyError, match="unknown discount code"):
        basket.apply_code("FREE")
```

`pytest.raises` works in ordinary code too, which is handy for experimenting. The `as` name gives access to the exception afterwards:

```python
with pytest.raises(ValueError) as error_info:
    basket.add("pen", -1)
print("Raised:", error_info.value)
```

```
Raised: price cannot be negative: -1
```

Match the specific exception type, not `Exception`. Checking for a too-general type can let a test pass for the wrong reason, such as an unrelated bug that raises a different error.

### pytest.approx

`pytest.approx` compares floats with a small tolerance (04-05):

```python
print(0.1 + 0.2 == pytest.approx(0.3))
```

```
True
```

### Fixtures

Many tests need the same starting point. A **fixture** is a function marked `@pytest.fixture` that builds it. Any test that names the fixture as a parameter receives a **fresh** copy of its result:

```python
@pytest.fixture
def basket():
    new_basket = Basket()
    new_basket.add("pen", 1.50, quantity=2)
    new_basket.add("pad", 4.00)
    return new_basket


def test_total(basket):
    assert basket.total() == 7.00


def test_adding_same_item_increases_quantity(basket):
    basket.add("pen", 1.50)
    assert basket.items["pen"] == (1.50, 3)
```

Because each test gets a new basket, the second test adding a pen cannot affect the first. Tests must never depend on each other or on the order they run in. You have already used pytest's built-in fixtures: `capsys` (captured output) and `tmp_path` (a temporary folder).

### Parametrised tests

**`@pytest.mark.parametrize`** runs one test function once for each set of values. Give it the parameter names as a string and a list of value tuples:

```python
@pytest.mark.parametrize(
    "code, expected",
    [("SAVE10", 6.30), ("HALF", 3.50)],
)
def test_discount_codes(basket, code, expected):
    basket.apply_code(code)
    assert basket.total() == pytest.approx(expected)


@pytest.mark.parametrize("price, quantity", [(-1, 1), (2.0, 0)])
def test_invalid_items_rejected(basket, price, quantity):
    with pytest.raises(ValueError):
        basket.add("bad", price, quantity)
```

This replaces copy-pasted near-identical tests, and pytest reports each case separately, so you can see exactly which input failed. Fixtures and parameters combine freely.

### Running the tests

`examples.py` runs the file with `pytest.main`, the same as typing `python -m pytest -v basket_checks.py`. The `-v` (verbose) flag lists every test (paths shortened here):

```
collecting ... collected 8 items

basket_checks.py::test_empty_basket_total_is_zero PASSED [ 12%]
basket_checks.py::test_total PASSED [ 25%]
basket_checks.py::test_adding_same_item_increases_quantity PASSED [ 37%]
basket_checks.py::test_discount_codes[SAVE10-6.3] PASSED [ 50%]
basket_checks.py::test_discount_codes[HALF-3.5] PASSED [ 62%]
basket_checks.py::test_unknown_code_raises PASSED [ 75%]
basket_checks.py::test_invalid_items_rejected[-1-1] PASSED [ 87%]
basket_checks.py::test_invalid_items_rejected[2.0-0] PASSED [100%]

============================== 8 passed in 0.01s ===============================
pytest exit code: 0
```

Six test functions produced eight tests, because the parametrised ones ran twice each; the values appear in square brackets. Other useful options: `-k discount` runs only tests whose names contain "discount", `-x` stops at the first failure, and `--lf` reruns only the tests that failed last time.

## Common mistakes

- **Tests that share state.** A module-level `basket = Basket()` used by several tests makes their results depend on the order they run in. Use a fixture.
- **Calling the fixture yourself.** Writing `basket()` inside a test gives an error explaining that fixtures are not meant to be called directly. Just list it as a parameter.
- **Parameter names that do not match.** `@pytest.mark.parametrize("code, expected", ...)` on a test with a parameter `discount_code` gives an error saying the function uses no argument `code`. The names must match exactly.
- **Code after the failing line inside `pytest.raises`.** Once the exception is raised, the rest of the `with` block is skipped. Put only the one call that should raise inside it.

## Try it

Copy `basket_checks.py` to a new file `test_my_basket.py` in this folder and add a parametrised test checking that adding `quantity` pens at 1.50 gives a total of `1.50 * quantity`, for quantities 1, 5 and 10. Run it with `python -m pytest -v` on that file.

## Exercises

Open `ex_11_01.py`, then read `test_ex_11_01.py`. The tests use a fixture, parametrised cases and `pytest.raises`; reading them tells you exactly what each piece must do.

1. `parse_score`: turn text into a whole-number score from 0 to 100.
2. `Inventory`: a class with `add`, `remove` and `quantity` methods.

Before you write `Inventory`, the tests that use the `inventory` fixture are reported as **ERROR** rather than **FAILED**. pytest uses ERROR when something goes wrong while setting a test up (here, the fixture calls your unfinished class) and FAILED when the test itself fails. Both disappear once `Inventory` works.

Run the tests:

```
python -m pytest part-2-intermediate-python/11-writing-reliable-code/11-01-testing-with-pytest
```

## Summary

- pytest finds `test_*` functions in `test_*.py` files; each test checks one behaviour and has a descriptive name.
- `with pytest.raises(Error, match="text"):` checks that the right exception is raised.
- `@pytest.fixture` builds fresh set-up for every test that names it as a parameter.
- `@pytest.mark.parametrize("a, b", [...])` runs one test for many inputs, reporting each separately.
- `-v`, `-k`, `-x` and `--lf` control what pytest runs and shows.
