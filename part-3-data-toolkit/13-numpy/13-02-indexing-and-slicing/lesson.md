# 13-02 Indexing and slicing

## What you will learn

- Index and slice 1-D and 2-D arrays, including whole rows and columns.
- Explain why a slice is a view, and when to use `copy()`.
- Select elements by a condition with boolean masks, combining conditions with `&` and `|`.
- Pick out specific positions with fancy indexing.

## Why it matters

Selecting data is half of data work: the rows for one customer group, the column for one feature, the values above a threshold. In machine learning you will constantly split a dataset into its feature columns and its target column, and boolean masks are how you filter rows. pandas, in Module 14, uses the same ideas with friendlier labels.

## Concepts

### 1-D: like lists

Indexing and slicing a 1-D array works exactly as for lists (02-03, 05-01):

```python
temperatures = np.array([12, 15, 9, 21, 18, 7, 14])
print(temperatures[0], temperatures[-1])
print(temperatures[2:5])
print(temperatures[::2])
```

```
12 14
[ 9 21 18]
[12  9 18 14]
```

### 2-D: [row, column]

For a 2-D array, give a row index and a column index **inside one pair of brackets**, separated by a comma. A colon on its own means "all of this axis".

```python
scores = np.array([
    [72, 88, 95],   # student 0: maths, science, art
    [64, 70, 81],   # student 1
    [91, 85, 78],   # student 2
    [55, 62, 90],   # student 3
])
print(scores[1, 2])
print(scores[0])
print(scores[:, 0])
print(scores[1:3, :2])
```

```
81
[72 88 95]
[72 64 91 55]
[[64 70]
 [91 85]]
```

- `scores[1, 2]` is row 1, column 2: student 1's art score.
- `scores[0]` is the whole first row; `scores[:, 0]` is the whole first column (every student's maths score).
- `scores[1:3, :2]` slices both axes: rows 1 and 2, columns 0 and 1.

Selecting a column with `[:, column]` is how you will pull a single feature out of a dataset.

### Slices are views

A slice of a list is a new list (05-05). A slice of a NumPy array is **not** a copy: it is a **view**, a new array object that looks at the **same memory**. Changing the view changes the original:

```python
first_row = scores[0]
first_row[0] = 100
print(scores[0])
safe_copy = scores[0].copy()
safe_copy[0] = 0
print(scores[0], safe_copy)
```

```
[100  88  95]
[100  88  95] [ 0 88 95]
```

NumPy does this to avoid copying large amounts of data. When you want an independent array to change, call `.copy()`. (Student 0's maths score is now 100, which shows up in later examples.)

### Boolean masks

Comparing an array with a value gives an array of `True`/`False`, one per element, called a **boolean mask**. Using a mask as an index keeps the elements where it is `True`:

```python
warm = temperatures > 13
print(warm)
print(temperatures[warm])
```

```
[False  True False  True  True False  True]
[15 21 18 14]
```

To combine conditions, use **`&`** (and), **`|`** (or) and **`~`** (not), with **brackets around each condition**. Python's `and`/`or` do not work element by element.

```python
print(temperatures[(temperatures > 10) & (temperatures < 20)])
print(temperatures[(temperatures < 8) | (temperatures > 20)])
```

```
[12 15 18 14]
[21  7]
```

Because `True` counts as 1, `.sum()` of a mask counts the matches. Assigning through a mask changes just those elements:

```python
print((temperatures > 13).sum())
adjusted = temperatures.copy()
adjusted[adjusted < 10] = 10
print(adjusted)
```

```
4
[12 15 10 21 18 10 14]
```

### Masks on rows

A 1-D mask with one entry per row selects whole rows of a 2-D array. This is how you filter a dataset:

```python
passed_art = scores[:, 2] >= 80
print(passed_art)
print(scores[passed_art])
```

```
[ True  True False  True]
[[100  88  95]
 [ 64  70  81]
 [ 55  62  90]]
```

Read it as: build a mask from the art column, then keep the rows where it is `True`.

### Fancy indexing

Indexing with a **list of positions** picks out exactly those elements, in that order. This is called **fancy indexing**. With 2-D arrays it can select rows or (after `:,`) columns:

```python
print(temperatures[[0, 3, 6]])
print(scores[[3, 0]])
print(scores[:, [2, 0]])
```

```
[12 21 14]
[[ 55  62  90]
 [100  88  95]]
[[ 95 100]
 [ 81  64]
 [ 78  91]
 [ 90  55]]
```

Unlike slices, boolean masks and fancy indexing always return **copies**.

## Common mistakes

- **Using `and`/`or` with arrays.** `temperatures[(temperatures > 10) and (temperatures < 20)]` gives `ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()`. Use `&` and `|`.
- **Leaving out the brackets.** `temperatures > 10 & temperatures < 20` is evaluated as `temperatures > (10 & temperatures) < 20` and fails with the same error. Bracket each condition.
- **Changing a slice by accident.** Modifying a slice changes the original array. Call `.copy()` when you need an independent array.
- **Out-of-range indexes.** `scores[4, 0]` gives `IndexError: index 4 is out of bounds for axis 0 with size 4`. The message tells you which axis is wrong.

## Try it

Using `scores`, find the students (row numbers) whose science score is higher than their maths score. Hint: compare two columns to get a mask, then use `np.where(mask)` or `np.arange(4)[mask]` to turn it into row numbers.

## Exercises

Open `ex_13_02.py`:

1. `column`: one column of a 2-D array.
2. `last_rows`: the last few rows.
3. `values_between`: the values within a range, using a mask.
4. `replace_below`: a copy with small values raised to a floor, leaving the original alone.
5. `rows_where`: the rows whose value in one column passes a threshold.
6. `pick_rows`: specific rows in a given order.

Run the tests:

```
python -m pytest part-3-data-toolkit/13-numpy/13-02-indexing-and-slicing
```

## Summary

- 2-D arrays are indexed `[row, column]`; `:` means the whole axis, so `[:, j]` is column j.
- Slices are views that share memory with the original; use `.copy()` for independence.
- A comparison gives a boolean mask; `array[mask]` keeps the `True` elements or rows.
- Combine masks with `&`, `|` and `~`, bracketing each condition; `mask.sum()` counts matches.
- Fancy indexing with a list of positions selects specific elements, rows or columns.
