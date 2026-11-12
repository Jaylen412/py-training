# 13-03 Vectorised operations and broadcasting

## What you will learn

- Do arithmetic and comparisons on whole arrays at once.
- Apply universal functions such as `np.sqrt`, `np.log` and `np.maximum`.
- Predict when two arrays of different shapes can be combined, using the broadcasting rules.
- Replace a Python loop with a vectorised expression, and measure the speed-up.

## Why it matters

**Vectorisation** means writing one operation on whole arrays instead of a loop over elements. It is how all serious numerical Python is written: shorter, clearer and, as you will see, around 60 times faster than the list comprehension from 12-03. Broadcasting is what lets you standardise every column of a dataset in a single line, one of the most common preprocessing steps in machine learning.

## Concepts

### Element-wise arithmetic

Arithmetic between two arrays of the **same shape** pairs up the elements by position:

```python
first = np.array([1, 2, 3, 4])
second = np.array([10, 20, 30, 40])
print(first + second)
print(second - first)
print(first * second)
print(second / first)
print(first ** 2)
```

```
[11 22 33 44]
[ 9 18 27 36]
[ 10  40  90 160]
[10. 10. 10. 10.]
[ 1  4  9 16]
```

Note that `*` is element-wise multiplication, not the dot product (that is `@`, in 13-05). Comparisons work the same way and give boolean arrays:

```python
print(first > 2)
print(first == second / 10)
```

```
[False False  True  True]
[ True  True  True  True]
```

### Universal functions

NumPy's **universal functions** (**ufuncs**) apply a mathematical function to every element. Use them instead of the `math` module, whose functions only accept single numbers:

```python
values = np.array([1.0, 4.0, 9.0, 16.0])
print(np.sqrt(values))
print(np.log(values))
print(np.round(np.exp([0, 1, 2]), 3))
print(np.abs(np.array([-3, 0, 2])))
print(np.maximum(np.array([1, 5, 2]), np.array([3, 3, 3])))
```

```
[1. 2. 3. 4.]
[0.         1.38629436 2.19722458 2.77258872]
[1.    2.718 7.389]
[3 0 2]
[3 5 3]
```

`np.log` is the natural logarithm. `np.maximum` compares two arrays element by element and keeps the larger of each pair (unlike `np.max`, which finds the single largest value; see 13-04).

### Broadcasting a single number

When one side is a single number, it is used with every element. This is the simplest case of **broadcasting**, NumPy's rule for combining arrays of different shapes:

```python
celsius = np.array([0, 15, 30, 100])
print(celsius * 9 / 5 + 32)
```

```
[ 32.  59.  86. 212.]
```

### Broadcasting a row

A 1-D array can be combined with every **row** of a 2-D array, as long as its length matches the number of columns. Here each column has its own tax rate:

```python
prices = np.array([
    [10.0, 20.0, 30.0],
    [12.0, 18.0, 33.0],
])
tax_rates = np.array([0.2, 0.05, 0.0])     # one rate per column
print(prices.shape, tax_rates.shape)
print(prices * (1 + tax_rates))
```

```
(2, 3) (3,)
[[12.  21.  30. ]
 [14.4 18.9 33. ]]
```

Picture the row of rates being stretched (without actually being copied) down to cover every row:

```
prices            rates (3,) stretched to (2, 3)
[[10 20 30]   *   [[1.2 1.05 1.0]
 [12 18 33]]       [1.2 1.05 1.0]]
```

### Broadcasting a column

To apply one value per **row** instead, the array must have shape `(rows, 1)`: a column. `np.array([[0.1], [0.5]])` is two rows of one value each:

```python
discounts = np.array([[0.1], [0.5]])       # one discount per row
print(discounts.shape)
print(prices * (1 - discounts))
```

```
(2, 1)
[[ 9.  18.  27. ]
 [ 6.   9.  16.5]]
```

```
prices          discounts (2, 1) stretched to (2, 3)
[[10 20 30]  *  [[0.9 0.9 0.9]
 [12 18 33]]     [0.5 0.5 0.5]]
```

### The broadcasting rules

NumPy compares the two shapes **from the right**, one axis at a time. Two axis lengths are compatible if they are **equal**, or if **one of them is 1** (that axis gets stretched). A missing axis on the left counts as 1.

| Shapes | Result | Why |
|--------|--------|-----|
| `(2, 3)` and `(3,)` | `(2, 3)` | 3 matches 3; the missing axis is treated as 1 |
| `(2, 3)` and `(2, 1)` | `(2, 3)` | 1 stretches to 3; 2 matches 2 |
| `(2, 3)` and `(2,)` | error | 3 and 2 differ and neither is 1 |

```python
try:
    prices + np.array([1, 2])
except ValueError as error:
    print("ValueError:", error)
```

```
ValueError: operands could not be broadcast together with shapes (2,3) (2,) 
```

To apply a 1-D array of length 2 to the rows, turn it into a column first with `values.reshape(-1, 1)` (13-04 explains `reshape`).

### Replacing a loop: standardising columns

**Standardising** a column means subtracting its mean and dividing by its standard deviation, so that it ends up with mean 0 and spread 1. Machine learning models often need every feature standardised (Module 21). With broadcasting, it is one line for every column at once:

```python
data = np.array([
    [150.0, 50.0],
    [160.0, 60.0],
    [170.0, 65.0],
    [180.0, 85.0],
])
column_means = data.mean(axis=0)
column_stds = data.std(axis=0)
standardised = (data - column_means) / column_stds
print(np.round(standardised, 3))
```

```
[[-1.342 -1.177]
 [-0.447 -0.392]
 [ 0.447  0.   ]
 [ 1.342  1.569]]
```

`mean(axis=0)` gives one mean per column, shape `(2,)`, which broadcasts across the four rows. (13-04 explains `axis`.) Compare this with the nested loops you would need in plain Python.

### How much faster?

```python
rng = np.random.default_rng(42)
big = rng.random(1_000_000)
as_list = big.tolist()
loop_time = timeit.timeit(lambda: [value * 2 + 1 for value in as_list], number=5) / 5
numpy_time = timeit.timeit(lambda: big * 2 + 1, number=5) / 5
print(f"list comprehension: {loop_time * 1000:.1f} ms, NumPy: {numpy_time * 1000:.2f} ms")
print(f"NumPy was about {loop_time / numpy_time:.0f}x faster")
```

```
list comprehension: 27.7 ms, NumPy: 0.46 ms
NumPy was about 60x faster
```

Your numbers will differ, but the gap will be large. (`np.random.default_rng(42)` makes seeded random numbers; 13-05 covers it.)

## Common mistakes

- **Using `math` functions on arrays.** `math.sqrt(values)` raises a `TypeError` about converting an array to a single number (the wording varies by NumPy version). Use `np.sqrt`.
- **Shapes that do not broadcast.** `(2, 3)` with `(2,)` fails. Make the 1-D array a column with `.reshape(-1, 1)` to apply it per row.
- **Accidental broadcasting.** `(3,)` minus `(3, 1)` silently gives a `(3, 3)` array instead of an error. Check `.shape` when a result is bigger than you expected.
- **Integer truncation.** `/` always gives floats, but assigning float results into an existing int array truncates them.

## Try it

Make `heights = np.array([1.50, 1.65, 1.80])` (metres) and `weights = np.array([50, 68, 90])`. Compute everyone's BMI (weight divided by height squared) in one line, without a loop. Then make a `(3, 3)` table of every weight divided by every height squared, using `heights.reshape(-1, 1)` and broadcasting.

## Exercises

Open `ex_13_03.py`. Do not use loops.

1. `celsius_to_fahrenheit`: convert an array of temperatures.
2. `apply_column_rates`: multiply each column of a table by its own rate.
3. `subtract_row_means`: subtract each row's mean from that row.
4. `standardise_columns`: give every column mean 0 and standard deviation 1.
5. `distances_from`: the distance from one point to each of many points.

Run the tests:

```
python -m pytest part-3-data-toolkit/13-numpy/13-03-vectorised-operations-and-broadcasting
```

## Summary

- Arithmetic and comparisons on same-shaped arrays work element by element; `*` is not the dot product.
- Ufuncs such as `np.sqrt`, `np.log`, `np.exp`, `np.abs` and `np.maximum` apply to every element.
- Broadcasting compares shapes from the right; lengths must be equal, or one of them 1.
- A `(columns,)` array applies per column; a `(rows, 1)` array applies per row.
- Vectorised code is shorter and typically tens of times faster than Python loops.
