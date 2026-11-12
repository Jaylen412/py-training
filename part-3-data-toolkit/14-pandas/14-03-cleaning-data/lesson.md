# 14-03 Cleaning data

## What you will learn

- Find, drop and fill missing values with `isna`, `dropna` and `fillna`.
- Find and remove duplicate rows.
- Tidy messy text with the `.str` accessor, and fix column types.
- Rename columns, and collect cleaning steps into one reusable function.

## Why it matters

Real data is never clean. Our sales file has missing quantities, missing prices, duplicated rows and the same category spelled four different ways. A model trained on that would treat `"CLOTHING"` and `"Clothing"` as different products, and double-count the duplicates. Data scientists often say that cleaning is most of the job, and the decisions you make here directly change your results.

## Concepts

### Finding missing values

pandas marks missing values as `NaN` (for numbers) or `None`/`NaN` (for text). `isna()` gives `True` where a value is missing, and `.sum()` counts per column:

```python
print(sales.isna().sum())
print(sales[sales["unit_price"].isna()].head(3))
```

```
date           0
store          0
category       0
units         12
unit_price     8
dtype: int64
           date store    category  units  unit_price
71   2026-01-14    S2  groceries    38.0         NaN
166  2026-01-28    S2    Clothing    6.0         NaN
195  2026-01-31    S6   Groceries   20.0         NaN
```

### Dropping missing values

`dropna()` removes rows with **any** missing value; `subset=` limits the check to some columns:

```python
print(len(sales), len(sales.dropna()), len(sales.dropna(subset=["units"])))
```

```
486 466 474
```

Dropping is simple but throws information away: 20 rows here, about 4% of the data. If the missing values are not random (say, one store never records prices), dropping can also **bias** what is left.

### Filling missing values

`fillna` replaces missing values. A dictionary gives a different fill for each column:

```python
filled = sales.fillna({"units": 0})
print(filled["units"].isna().sum())
median_price = sales["unit_price"].median()
print(round(median_price, 2))
```

```
0
30.62
```

Choosing a fill value is a judgement call:

- **0** is right only when missing truly means "none". For units sold, we do not know that.
- The **median** (or mean) of the column is a common neutral guess for numbers. The median is less affected by extreme values.
- Sometimes the honest choice is to drop the rows, or to keep a column recording that the value was missing.

In Part 5, filling missing values is called **imputation**, and scikit-learn has tools for it.

### Duplicates

`duplicated()` marks each row that is an exact copy of an earlier one; `keep=False` marks every copy, which is handy for looking at them. `drop_duplicates()` removes the copies:

```python
print(sales.duplicated().sum())
print(sales[sales.duplicated(keep=False)].head(4))
deduplicated = sales.drop_duplicates()
print(len(deduplicated))
```

```
6
          date store  category  units  unit_price
50  2026-01-11    S2  Clothing   21.0       32.11
51  2026-01-11    S2  Clothing   21.0       32.11
91  2026-01-16    S6      Toys    2.0       18.84
93  2026-01-16    S6      Toys    2.0       18.84
480
```

Duplicate rows usually come from a data export or a join going wrong. Here, two identical sales records for the same store, category and day are almost certainly one sale recorded twice.

### Messy text with .str

The `.str` accessor applies string methods (02-04) to every value in a text column:

```python
print(sales["category"].unique().tolist())
clean_category = sales["category"].str.strip().str.title()
print(clean_category.unique().tolist())
print(sales["store"].str.replace("S", "Store ").head(3).tolist())
```

```
['Electronics', 'Toys', 'Groceries', 'Clothing', 'CLOTHING', 'groceries ', ' electronics']
['Electronics', 'Toys', 'Groceries', 'Clothing']
['Store 1', 'Store 3', 'Store 6']
```

Seven spellings collapse to the four real categories. Always check `unique()` on text columns; stray spaces are invisible when you print the table.

### Fixing types

The `date` column was read as text. **`pd.to_datetime`** converts it to proper dates, which can be compared, sorted and taken apart (14-04):

```python
print(sales["date"].dtype)
sales["date"] = pd.to_datetime(sales["date"])
print(sales["date"].dtype, sales["date"].min(), sales["date"].max())
print(pd.to_numeric(pd.Series(["1.5", "2", "oops"]), errors="coerce").tolist())
```

```
str
datetime64[us] 2026-01-01 00:00:00 2026-03-31 00:00:00
[1.5, 2.0, nan]
```

`pd.to_numeric` converts text to numbers; `errors="coerce"` turns anything unconvertible into `NaN` instead of raising an error, so you can find and deal with the bad values afterwards.

### Renaming columns

`rename(columns={old: new})` returns a DataFrame with new column names:

```python
renamed = sales.rename(columns={"unit_price": "price", "units": "quantity"})
print(renamed.columns.tolist())
```

```
['date', 'store', 'category', 'quantity', 'price']
```

### A cleaning function

Collect the steps into one function, so the same cleaning is applied every time and can be tested (Module 11):

```python
def clean_sales(raw):
    cleaned = raw.drop_duplicates().copy()
    cleaned["category"] = cleaned["category"].str.strip().str.title()
    cleaned["date"] = pd.to_datetime(cleaned["date"])
    cleaned = cleaned.dropna(subset=["units"])
    cleaned["unit_price"] = cleaned["unit_price"].fillna(cleaned["unit_price"].median())
    return cleaned.reset_index(drop=True)


clean = clean_sales(pd.read_csv(DATA / "store_sales.csv"))
print(clean.shape)
print(clean.isna().sum().sum(), clean.duplicated().sum())
print(sorted(clean["category"].unique()))
```

```
(468, 5)
0 0
['Clothing', 'Electronics', 'Groceries', 'Toys']
```

A few details:

- `.copy()` makes sure we work on our own table and never modify the caller's DataFrame.
- The order matters: duplicates are removed **before** filling, so a filled copy cannot accidentally stop matching its twin.
- `reset_index(drop=True)` renumbers the rows 0, 1, 2, ... after rows were removed; `drop=True` throws the old labels away rather than keeping them as a column.

Filling every missing price with one overall median is crude: a missing Electronics price (around 120) is filled with 30.62. You will learn to fill per category in 14-05.

## Common mistakes

- **Chained assignment.** `sales[sales["store"] == "S1"]["units"] = 0` does nothing to `sales`; pandas 3 warns `ChainedAssignmentError: A value is being set on a copy of a DataFrame or Series through chained assignment.`. Use one `loc`: `sales.loc[sales["store"] == "S1", "units"] = 0`.
- **Converting a column with missing values to int.** `sales["units"].astype(int)` gives `IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer...`. Deal with the missing values first, or use pandas' nullable `"Int64"` type.
- **Invalid dates.** `pd.to_datetime` on `"2026-13-01"` raises `DateParseError: month must be in 1..12`. Add `errors="coerce"` to turn bad dates into `NaT` ("not a time") and inspect them.
- **Cleaning in place without keeping the raw data.** Always keep the original file unchanged and write cleaning as a function from raw to clean, so you can rerun and change it.

## Try it

The `clean_sales` function fills missing prices with the overall median. How many prices did it fill? Compare the mean revenue per row before and after cleaning. Would dropping rows with missing prices have given a very different answer?

## Exercises

Open `ex_14_03.py`. None of these functions may modify the DataFrame passed in.

1. `clean_categories`: tidy a Series of category names.
2. `drop_missing`: remove rows missing a value in given columns.
3. `fill_with_median`: fill missing values in one column with that column's median.
4. `remove_duplicates`: remove duplicate rows and renumber the index.
5. `clean_sales`: the full cleaning pipeline.

Run the tests:

```
python -m pytest part-3-data-toolkit/14-pandas/14-03-cleaning-data
```

## Summary

- `isna().sum()` counts missing values; `dropna(subset=...)` drops rows; `fillna(...)` fills them.
- Choosing between dropping and filling (and what to fill with) is a judgement that affects results.
- `duplicated()` finds and `drop_duplicates()` removes repeated rows.
- `.str` applies string methods to a column; `pd.to_datetime` and `pd.to_numeric` fix types.
- Put cleaning steps in a function that copies its input, so cleaning is repeatable and testable.
