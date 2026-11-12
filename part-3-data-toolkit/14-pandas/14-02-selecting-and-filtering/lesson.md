# 14-02 Selecting and filtering

## What you will learn

- Select one or more columns.
- Select rows and columns by label with `loc` and by position with `iloc`.
- Filter rows with boolean conditions, `isin` and `query`.
- Sort a DataFrame by one or more columns.

## Why it matters

Answering any question about data starts with selecting the right part of it: the sales for one store, the days with unusually large orders, the ten most expensive items. In machine learning you will select the feature columns and the target column out of a DataFrame before training every model.

## Concepts

All examples use the sales data from 14-01, loaded as `sales`.

### Selecting columns

One column name in square brackets gives a Series; a **list** of names gives a DataFrame:

```python
print(sales["units"].head(3))
print(sales[["store", "units"]].head(3))
```

```
0    3.0
1    2.0
2    4.0
Name: units, dtype: float64
  store  units
0    S1    3.0
1    S3    2.0
2    S6    4.0
```

Note the double brackets in `sales[["store", "units"]]`: the outer pair selects, the inner pair is the list.

### loc and iloc

pandas has two ways to pick rows and columns:

- **`loc[rows, columns]`** selects by **label**: index labels and column names.
- **`iloc[rows, columns]`** selects by **integer position**, like NumPy.

```python
print(sales.loc[0, "store"])
print(sales.loc[0:2, ["date", "units"]])
print(sales.iloc[0:2, 0:2])
print(sales.iloc[-1])
```

```
S1
         date  units
0  2026-01-01    3.0
1  2026-01-01    2.0
2  2026-01-01    4.0
         date store
0  2026-01-01    S1
1  2026-01-01    S3
date          2026-03-31
store                 S6
category       Groceries
units               11.0
unit_price           5.9
Name: 485, dtype: object
```

Watch out: **`loc` slices include the end label** (`0:2` gives rows 0, 1 and 2), while **`iloc` slices exclude the end position**, like Python (`0:2` gives rows 0 and 1). Here the labels and positions happen to be the same numbers, but after filtering or sorting they are not, and that is when the difference matters.

A single row comes back as a Series whose index is the column names.

### Boolean filters

Filtering works exactly like NumPy masks (13-02): a comparison on a column gives a Series of `True`/`False`, and indexing with it keeps the `True` rows. The row labels are kept, so you can see where each row came from:

```python
big_orders = sales[sales["units"] > 40]
print(len(big_orders))
print(big_orders.head(3))
```

```
25
           date store   category  units  unit_price
6    2026-01-03    S1  Groceries   67.0        7.22
12   2026-01-04    S2  Groceries   46.0        5.74
137  2026-01-23    S1  Groceries   61.0        6.89
```

Combine conditions with `&` (and), `|` (or) and `~` (not), **with brackets around each condition**:

```python
s1_electronics = sales[(sales["store"] == "S1") & (sales["category"] == "Electronics")]
print(len(s1_electronics))
print(len(sales[(sales["units"] == 0) | (sales["unit_price"] > 135)]))
```

```
19
20
```

### isin

To keep rows where a column has **any one of several values**, use `isin` rather than a chain of `|`:

```python
north = sales[sales["store"].isin(["S2", "S3"])]
print(north["store"].unique().tolist())
```

```
['S3', 'S2']
```

`unique()` lists the distinct values in the order they first appear.

### query

**`query`** writes the same filter as a string, which can be easier to read for long conditions. Inside the string, use `and`, `or` and column names directly:

```python
print(len(sales.query("store == 'S1' and units > 20")))
```

```
22
```

### Filtering rows and choosing columns together

`loc` accepts a boolean mask for the rows and a list of column names, so you can filter and select in one step:

```python
print(sales.loc[sales["units"] > 50, ["date", "store", "units"]])
```

```
           date store  units
6    2026-01-03    S1   67.0
137  2026-01-23    S1   61.0
185  2026-01-31    S1   54.0
196  2026-02-01    S1   63.0
197  2026-02-01    S2   73.0
207  2026-02-04    S1   52.0
269  2026-02-15    S1   64.0
303  2026-02-21    S1   55.0
307  2026-02-22    S2   51.0
344  2026-03-01    S1   65.0
357  2026-03-03    S1   55.0
445  2026-03-21    S1   60.0
472  2026-03-29    S1   56.0
476  2026-03-30    S1   55.0
```

Store S1 dominates the biggest days. That is the kind of pattern that filtering reveals.

### Sorting

**`sort_values`** sorts by one or more columns. `ascending=False` puts the largest first; with several columns, give one `ascending` value per column:

```python
print(sales.sort_values("unit_price", ascending=False).head(3))
print(sales.sort_values(["store", "units"], ascending=[True, False]).head(3))
```

```
           date store     category  units  unit_price
172  2026-01-29    S3  Electronics    2.0      137.89
47   2026-01-10    S3  Electronics    4.0      137.89
337  2026-02-27    S5  Electronics    2.0      137.67
           date store   category  units  unit_price
6    2026-01-03    S1  Groceries   67.0        7.22
344  2026-03-01    S1  Groceries   65.0        6.37
269  2026-02-15    S1  Groceries   64.0        5.86
```

Like most pandas methods, `sort_values` returns a **new** DataFrame and leaves `sales` unchanged. Assign the result if you want to keep it.

## Common mistakes

- **Using `and`/`or` in a filter.** `sales[sales["units"] > 40 and sales["store"] == "S1"]` gives `ValueError: The truth value of a Series is ambiguous. Use a.empty, a.item(), a.any() or a.all().`. Use `&` and `|` with brackets, or `query`.
- **Mixing up `loc` and `iloc` slices.** `sales.loc[0:2]` has 3 rows; `sales.iloc[0:2]` has 2.
- **Using positions with `loc` after filtering.** After `big_orders = sales[sales["units"] > 40]`, the first row's label is 6, so `big_orders.loc[0]` raises `KeyError`. Use `big_orders.iloc[0]` for "the first row".
- **Expecting methods to change the DataFrame.** `sales.sort_values("units")` on its own line does nothing visible to `sales`. Assign the result.

## Try it

Find the five days with the highest revenue (units times unit price) for Groceries in store S2. You can compute revenue on the fly: `(rows["units"] * rows["unit_price"])`, then use `nlargest(5)` on that Series.

## Exercises

Open `ex_14_02.py`:

1. `select_columns`: a DataFrame with only some columns.
2. `rows_for_store`: the rows for one store.
3. `big_days`: rows with at least a given number of units, largest first.
4. `in_categories`: rows whose category is one of several.
5. `first_row_value`: one value from the first row, by position.

Run the tests:

```
python -m pytest part-3-data-toolkit/14-pandas/14-02-selecting-and-filtering
```

## Summary

- `df["col"]` gives a Series; `df[["a", "b"]]` gives a DataFrame.
- `loc` selects by label (slices include the end); `iloc` selects by position (slices exclude the end).
- Filter with boolean conditions combined by `&`, `|` and `~`, each condition in brackets; `isin` matches a list of values; `query` takes a string.
- `df.loc[mask, columns]` filters and selects at once.
- `sort_values(columns, ascending=...)` returns a new, sorted DataFrame.
