# 14-01 Series and DataFrames

## What you will learn

- Create a pandas Series and DataFrame, and explain how they relate.
- Load a CSV file with `read_csv`.
- Take a first look at a dataset with `head`, `tail`, `shape`, `info` and `describe`.
- Read a DataFrame's columns, index and dtypes.

## Why it matters

Real data comes as tables with named columns of different types: dates, shop codes, quantities, prices. NumPy arrays hold one type and have no column names. **pandas** adds both, plus tools for loading, cleaning, grouping and joining tables. It is the workhorse of data analysis in Python, and the starting point of every project from here to the capstone.

## Concepts

### Importing pandas

pandas is always imported as `pd`. The examples also build the path to the course's `data` folder from the script's own location (06-01), and widen the printed output:

```python
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)
```

### Series

A **Series** is a 1-D array of values with a **label** for each one. The labels form the **index**. A Series can also have a name.

```python
temperatures = pd.Series([12.5, 15.0, 9.5], index=["Mon", "Tue", "Wed"], name="temp_c")
print(temperatures)
print(temperatures["Tue"], temperatures.mean())
```

```
Mon    12.5
Tue    15.0
Wed     9.5
Name: temp_c, dtype: float64
15.0 12.333333333333334
```

You can look values up by label, and it has all the NumPy-style methods (`mean`, `max` and so on). Underneath, the values are a NumPy array.

### DataFrames

A **DataFrame** is a table: a set of named columns, each one a Series, all sharing the same index. The easiest way to build one by hand is from a dictionary of column name to values:

```python
people = pd.DataFrame({
    "name": ["Ada", "Alan", "Grace"],
    "age": [36, 41, 85],
    "city": ["London", "Manchester", "New York"],
})
print(people)
print(people.shape)
print(people.columns.tolist())
print(people.index.tolist())
```

```
    name  age        city
0    Ada   36      London
1   Alan   41  Manchester
2  Grace   85    New York
(3, 3)
['name', 'age', 'city']
[0, 1, 2]
```

When you do not give an index, pandas numbers the rows from 0; this is a **RangeIndex**. `shape` is (rows, columns), as in NumPy.

Selecting one column gives a Series:

```python
print(type(people["age"]).__name__)
print(people["age"].max())
```

```
Series
85
```

### Reading a CSV

**`pd.read_csv(path)`** reads a CSV file into a DataFrame, using the first line as column names and guessing a type for each column. This course's sales data lives in `data/store_sales.csv`: one row per shop, per product category, per day.

```python
sales = pd.read_csv(DATA / "store_sales.csv")
print(sales.shape)
print(sales.head())
```

```
(486, 5)
         date store     category  units  unit_price
0  2026-01-01    S1  Electronics    3.0      137.28
1  2026-01-01    S3         Toys    2.0       17.16
2  2026-01-01    S6  Electronics    4.0      105.93
3  2026-01-01    S6    Groceries   27.0        6.51
4  2026-01-02    S2  Electronics    3.0      131.68
```

`head(n)` shows the first `n` rows (5 by default) and `tail(n)` the last. Always look at the data before doing anything with it.

### info

**`info()`** prints a compact summary of the columns: how many non-missing values each has, and its dtype.

```python
sales.info()
```

```
<class 'pandas.DataFrame'>
RangeIndex: 486 entries, 0 to 485
Data columns (total 5 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   date        486 non-null    str    
 1   store       486 non-null    str    
 2   category    486 non-null    str    
 3   units       474 non-null    float64
 4   unit_price  478 non-null    float64
dtypes: float64(2), str(3)
memory usage: 19.1 KB
```

Already this tells us a lot:

- There are 486 rows, but `units` has only 474 values and `unit_price` 478: some are **missing**.
- `units` is `float64` even though it counts whole items. pandas reads missing numbers as `NaN` (13-04), which is a float, so the whole column becomes float.
- `date` was read as text (`str`), not as a date. Lesson 14-03 fixes that.

(`str` is the text dtype in pandas 3. Older versions call it `object`.)

### describe

**`describe()`** gives summary statistics of every numeric column:

```python
print(sales.describe().round(2))
```

```
        units  unit_price
count  474.00      478.00
mean    12.34       45.18
std     13.44       45.04
min      0.00        5.55
25%      4.00       15.46
50%      7.00       30.62
75%     14.75       40.15
max     73.00      137.89
```

`count` is the number of non-missing values. `25%`, `50%` and `75%` are **percentiles**: a quarter of the days sold 4 units or fewer, half sold 7 or fewer (the 50% value is the **median**). The mean (12.34) is well above the median (7), a sign that a few very large values pull it up. Module 16 shows how to spot this.

### dtypes and tail

```python
print(sales.dtypes)
print(sales.tail(3))
```

```
date              str
store             str
category          str
units         float64
unit_price    float64
dtype: object
           date store     category  units  unit_price
483  2026-03-31    S5         Toys    6.0       18.28
484  2026-03-31    S6  Electronics    0.0      117.66
485  2026-03-31    S6    Groceries   11.0        5.90
```

The data runs from 1 January to 31 March 2026.

## Common mistakes

- **Misspelling a column name.** `sales["Units"]` gives `KeyError: 'Units'`. Column names are case-sensitive; check `sales.columns`.
- **Selecting several columns with one pair of brackets.** `sales["store", "units"]` gives `KeyError: ('store', 'units')`. Use a list inside the brackets: `sales[["store", "units"]]`.
- **A wrong relative path.** `pd.read_csv("store_sales.csv")` gives `FileNotFoundError` unless you run Python from the `data` folder. Build paths from `Path(__file__)` as above.
- **Trusting the data without looking.** Skipping `info()` and `describe()` means missing values and wrong types surprise you later.

## Try it

Load `data/stores.csv` and run `head`, `info` and `describe`. Why does `describe()` complain or show something different? (Hint: does the table have any numeric columns? Try `describe(include="all")`.)

## Exercises

Open `ex_14_01.py`:

1. `make_people`: build a DataFrame from two lists.
2. `load_csv`: read a CSV file into a DataFrame.
3. `shape_summary`: the number of rows and columns and the column names.
4. `missing_counts`: how many values are missing in each column.
5. `numeric_columns`: the names of the numeric columns.

Run the tests:

```
python -m pytest part-3-data-toolkit/14-pandas/14-01-series-and-dataframes
```

## Summary

- `import pandas as pd`; a Series is a labelled 1-D array, a DataFrame a table of Series sharing an index.
- `pd.DataFrame({"column": values, ...})` builds a table; `pd.read_csv(path)` loads one.
- `df["column"]` gives a Series; `df.shape`, `df.columns`, `df.index` and `df.dtypes` describe the table.
- `head`, `tail`, `info` and `describe` are your first look at any dataset.
- Missing numbers become `NaN`, which turns whole-number columns into floats.
