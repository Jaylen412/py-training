# 13-01 Arrays

## What you will learn

- Create NumPy arrays from lists and explain how they differ from lists.
- Read an array's `dtype`, `shape`, `ndim` and `size`.
- Generate arrays with `arange`, `linspace`, `zeros`, `ones` and `full`.
- Convert between arrays and Python lists.

## Why it matters

Module 12 showed that Python loops are slow for numbers. **NumPy** (Numerical Python) is the library that fixes this, and nearly every data-science tool is built on it: pandas columns are NumPy arrays underneath, Matplotlib plots them, and scikit-learn models take them as input and return them as output. From now on, datasets are arrays.

## Concepts

### Importing NumPy

NumPy was installed with the course requirements in Module 01. It is always imported with the alias `np`:

```python
import numpy as np
```

### Arrays

The central object is the **array** (type `ndarray`, for n-dimensional array): a grid of values, all of the same type, stored packed together in memory (12-03). Create one from a list with `np.array`:

```python
prices = np.array([4.99, 12.50, 3.25, 8.00])
print(prices)
print(type(prices).__name__)
```

```
[ 4.99 12.5   3.25  8.  ]
ndarray
```

Arrays print without commas, which is a quick way to tell them from lists.

### Arrays do maths element by element

The biggest difference from lists: arithmetic on an array applies to **every element**.

```python
price_list = [4.99, 12.50, 3.25, 8.00]
print(price_list * 2)
print(prices * 2)
```

```
[4.99, 12.5, 3.25, 8.0, 4.99, 12.5, 3.25, 8.0]
[ 9.98 25.    6.5  16.  ]
```

`* 2` on a list repeats it; on an array it doubles each number. No loop is needed, and the work runs in fast compiled code (13-03 measures how fast).

### dtype

Every array has a single **dtype** (data type) shared by all its elements. NumPy picks one from the values you give it:

```python
print(prices.dtype)
counts = np.array([3, 1, 4])
print(counts.dtype)
mixed = np.array([1, 2.5, 3])
print(mixed, mixed.dtype)
as_int = np.array([1.9, 2.1, -3.7]).astype(int)
print(as_int)
```

```
float64
int64
[1.  2.5 3. ] float64
[ 1  2 -3]
```

- `float64` is a 64-bit (8-byte) float, the same precision as a Python float. `int64` is a 64-bit whole number. (On Windows, integer arrays may show as `int32`.)
- When you mix ints and floats, NumPy **upcasts** everything to float, so the array has one type.
- `astype(type)` converts to a new array of another dtype. Converting floats to ints chops off the decimal part, as `int()` does.

### shape, ndim and size

Arrays can have more than one dimension. A list of equal-length lists makes a **2-D array**, like a table:

```python
table = np.array([
    [1, 2, 3],
    [4, 5, 6],
])
print(table)
print("shape:", table.shape, "ndim:", table.ndim, "size:", table.size)
print("shape:", prices.shape, "ndim:", prices.ndim)
```

```
[[1 2 3]
 [4 5 6]]
shape: (2, 3) ndim: 2 size: 6
shape: (4,) ndim: 1
```

- **`shape`** is a tuple giving the length along each dimension: 2 rows and 3 columns. A 1-D array's shape has one number: `(4,)`.
- **`ndim`** is the number of dimensions; **`size`** is the total number of elements.

Each dimension is called an **axis**: in a 2-D array, axis 0 runs down the rows and axis 1 runs across the columns. In machine learning, a dataset is usually a 2-D array with one row per example and one column per feature, so `X.shape` is `(number of examples, number of features)`.

### Generating arrays

You often need arrays of a pattern rather than typed-in values:

```python
print(np.arange(5))
print(np.arange(2, 10, 3))
print(np.arange(0, 1, 0.25))
print(np.linspace(0, 1, 5))
```

```
[0 1 2 3 4]
[2 5 8]
[0.   0.25 0.5  0.75]
[0.   0.25 0.5  0.75 1.  ]
```

- **`np.arange(start, stop, step)`** works like `range` (stop excluded) but returns an array and allows float steps.
- **`np.linspace(start, stop, count)`** gives `count` evenly spaced values **including** both ends. Prefer it for floats, where rounding can make `arange` give one value more or fewer than you expect. You will use it constantly to make x values for plots.

Arrays filled with one value:

```python
print(np.zeros(3))
print(np.ones((2, 4)))
print(np.full((2, 2), 7))
print(np.zeros(3, dtype=int))
```

```
[0. 0. 0.]
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
[[7 7]
 [7 7]]
[0 0 0]
```

For more than one dimension, pass the shape as a tuple: `np.ones((2, 4))`. `zeros` and `ones` make floats unless you pass `dtype`.

### Back to lists

`tolist()` converts an array back into ordinary Python lists, which is useful for printing, JSON, or code that expects lists. Indexing a single element gives a NumPy scalar, which behaves like a Python number:

```python
print(table.tolist())
print(prices.tolist()[0], type(prices[0]).__name__)
```

```
[[1, 2, 3], [4, 5, 6]]
4.99 float64
```

## Common mistakes

- **Forgetting the tuple for a shape.** `np.zeros(2, 3)` gives `TypeError: Cannot interpret '3' as a data type`, because the second argument is the dtype. Write `np.zeros((2, 3))`.
- **Rows of different lengths.** `np.array([[1, 2], [3]])` gives `ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions...`. Every row of a 2-D array must have the same length.
- **Expecting list behaviour.** `+` on two arrays adds element by element; it does not join them. Use `np.concatenate([a, b])` to join.
- **Silent integer types.** Assigning `2.7` into an `int64` array stores `2`. Check `dtype` when results look truncated.

## Try it

Make an array of the numbers 1 to 12 with `np.arange`, then try `* 10`, `** 2` and `/ 4`. Check the `dtype` after each. Which operation changed the dtype, and why?

## Exercises

Open `ex_13_01.py`:

1. `to_array`: convert a list of numbers to a float array.
2. `describe`: the shape, number of dimensions and dtype name of an array.
3. `evenly_spaced`: evenly spaced points including both ends.
4. `multiples`: multiples of a number up to a limit.
5. `filled_grid`: a 2-D grid filled with one value.

Run the tests:

```
python -m pytest part-3-data-toolkit/13-numpy/13-01-arrays
```

## Summary

- `import numpy as np`; `np.array(list)` makes an array, and arithmetic applies to every element.
- All elements share one `dtype`; mixing ints and floats gives floats; `astype` converts.
- `shape` gives the length along each axis, `ndim` the number of axes, `size` the element count.
- `arange` (stop excluded), `linspace` (both ends included), `zeros`, `ones` and `full` generate arrays.
- `tolist()` converts back to Python lists.
