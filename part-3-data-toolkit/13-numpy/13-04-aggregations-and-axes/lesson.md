# 13-04 Aggregations and axes

## What you will learn

- Summarise arrays with `sum`, `mean`, `std`, `min` and `max`.
- Choose the `axis` argument to summarise per column or per row.
- Find positions of extreme values with `argmax` and `argmin`.
- Change an array's shape with `reshape`, and handle missing values with `nan` functions.

## Why it matters

An **aggregation** reduces many numbers to a few: a total, an average, a maximum. Almost every analysis starts with them, and every model evaluation ends with them (the average error, the accuracy). With 2-D data you nearly always want one summary **per column** (per feature) or **per row** (per example), and the `axis` argument is how you say which.

## Concepts

The examples use four weeks of sales for three shops:

```python
sales = np.array([
    [120, 95, 140],    # week 1: shop A, shop B, shop C
    [130, 80, 150],    # week 2
    [110, 105, 160],   # week 3
    [125, 90, 155],    # week 4
])
```

### Whole-array aggregations

With no arguments, aggregation methods summarise every element:

```python
print(sales.sum(), sales.mean(), sales.min(), sales.max())
print(round(sales.std(), 2))
```

```
1460 121.66666666666667 80 160
25.28
```

`std` is the **standard deviation**: a measure of how spread out the values are (Module 19 explains it properly). Each method also exists as a function: `np.sum(sales)`, `np.mean(sales)` and so on.

### The axis argument

`axis` says which axis to **collapse**:

- **`axis=0`** collapses the rows, leaving **one result per column**.
- **`axis=1`** collapses the columns, leaving **one result per row**.

```python
print(sales.sum(axis=0))
print(sales.mean(axis=0))
print(sales.sum(axis=1))
print(sales.max(axis=1))
```

```
[485 370 605]
[121.25  92.5  151.25]
[355 360 375 370]
[140 150 160 155]
```

`sales.sum(axis=0)` is each shop's total over the four weeks; `sales.sum(axis=1)` is each week's total over the three shops. A memory aid: the axis you name is the one that **disappears**. The shape `(4, 3)` becomes `(3,)` with `axis=0` and `(4,)` with `axis=1`.

```
axis=0: down the rows            axis=1: across the columns
 120  95 140                      120  95 140  -> 355
 130  80 150                      130  80 150  -> 360
 110 105 160                      110 105 160  -> 375
 125  90 155                      125  90 155  -> 370
  |    |   |
 485  370 605
```

For a dataset with one row per example, `axis=0` gives per-feature summaries, which is what you want almost every time.

### argmax and argmin

`argmax` and `argmin` return the **position** of the largest or smallest value, rather than the value itself:

```python
print(sales.sum(axis=0).argmax())
print(sales.argmax(axis=1))
flat_position = sales.argmax()
row, column = np.unravel_index(flat_position, sales.shape)
print(flat_position, int(row), int(column))
```

```
2
[2 2 2 2]
8 2 2
```

Shop 2 (shop C) sold the most overall, and was the best shop in every week. Without `axis`, `argmax` gives a position in the array flattened into one long row; `np.unravel_index` converts that back into a (row, column) pair. You will use `argmax` in Part 5 to turn a classifier's per-class probabilities into a predicted class.

### keepdims for broadcasting back

Dividing each row by its own total needs the totals as a column, shape `(4, 1)`, so that they broadcast across the row (13-03). `keepdims=True` keeps the collapsed axis with length 1:

```python
row_totals = sales.sum(axis=1, keepdims=True)
print(row_totals.shape)
print(np.round(sales / row_totals, 3))
```

```
(4, 1)
[[0.338 0.268 0.394]
 [0.361 0.222 0.417]
 [0.293 0.28  0.427]
 [0.338 0.243 0.419]]
```

Each row now shows each shop's share of that week's sales, and each row adds up to 1.

### Cumulative sums and boolean aggregations

`cumsum` gives running totals. On boolean arrays, `sum` counts the `True` values, `all` asks "are they all true?" and `any` asks "is at least one true?". All of them accept `axis`:

```python
print(sales[:, 0].cumsum())
print((sales > 100).sum(axis=0))
print((sales > 100).all(axis=1))
print((sales > 150).any())
```

```
[120 250 360 485]
[4 1 4]
[False False  True False]
True
```

Shop B beat 100 in only one week; week 3 was the only week in which every shop beat 100.

### reshape

`reshape` gives the same elements a new shape, as long as the total size matches. One dimension can be `-1`, meaning "work this out from the others":

```python
numbers = np.arange(12)
print(numbers.reshape(3, 4))
print(numbers.reshape(2, -1).shape)
print(sales.reshape(-1))
print(sales.ravel()[:3])
```

```
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
(2, 6)
[120  95 140 130  80 150 110 105 160 125  90 155]
[120  95 140]
```

`reshape(-1)` and `ravel()` both flatten to 1-D, reading row by row. Two reshapes you will see constantly in machine learning: `values.reshape(-1, 1)` turns a 1-D array into a single column (scikit-learn wants features as a 2-D table, even if there is only one feature), and `column.ravel()` turns a column back into a 1-D array.

### Missing values: nan

`np.nan` ("not a number") is a special float used for missing or undefined values. Any arithmetic with `nan` gives `nan`, so one missing value spoils an ordinary aggregation. The `nan` versions skip them:

```python
readings = np.array([3.0, np.nan, 5.0])
print(readings.mean(), np.nanmean(readings))
```

```
nan 4.0
```

There are also `np.nansum`, `np.nanmax` and others. `np.isnan(array)` gives a mask of the missing values. pandas (Module 14) handles missing values much more conveniently.

## Common mistakes

- **Mixing up the axes.** `sales.mean(axis=1)` gives per-row (per-week) means, not per-shop. Remember: the named axis disappears. Check the result's shape.
- **Shape mismatch when dividing by a summary.** `sales / sales.sum(axis=1)` gives `ValueError: operands could not be broadcast together with shapes (4,3) (4,)`. Use `keepdims=True`.
- **Reshaping to an impossible size.** `np.arange(12).reshape(5, -1)` gives `ValueError: cannot reshape array of size 12 into shape (5,newaxis)`. The sizes must divide exactly.
- **A silent `nan`.** A mean of `nan` means at least one value is missing. Use `np.nanmean` or deal with the missing values first.

## Try it

For `sales`, find which week each shop had its best week (one answer per shop). Then find each shop's average week-on-week change using `np.diff(sales, axis=0)`.

## Exercises

Open `ex_13_04.py`. Do not use loops.

1. `column_means`: the mean of each column.
2. `row_totals`: the sum of each row.
3. `best_column`: the index of the column with the highest total.
4. `row_shares`: each value as a fraction of its row total.
5. `count_above`: how many values in each column exceed a threshold.
6. `to_column`: reshape a 1-D array into a single column.

Run the tests:

```
python -m pytest part-3-data-toolkit/13-numpy/13-04-aggregations-and-axes
```

## Summary

- `sum`, `mean`, `std`, `min` and `max` summarise all elements, or one axis with `axis=`.
- `axis=0` gives one result per column; `axis=1` gives one result per row. The named axis disappears.
- `argmax` and `argmin` give positions; `keepdims=True` keeps a summary broadcastable.
- `reshape` changes shape without changing the data; `-1` means "work it out"; `reshape(-1, 1)` makes a column.
- `nan` marks missing values; use `np.nanmean` and friends to skip them.
