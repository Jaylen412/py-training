# 14-04 Creating and transforming columns

## What you will learn

- Create new columns from arithmetic and conditions on existing ones.
- Transform values with `map` (a lookup) and `apply` (any function).
- Convert types with `astype`, and group numbers into ranges with `pd.cut`.
- Take dates apart with the `.dt` accessor.

## Why it matters

Raw columns are rarely exactly what you need. Revenue is units times price; "was it a weekend?" comes from a date; a model may work better with "small, medium, large" than with raw counts. Building new columns from old ones is called **feature engineering** in machine learning, and it often matters more than the choice of model.

## Concepts

The examples start from the sales data with duplicates and missing rows removed and categories tidied (14-03).

### Arithmetic on columns

Columns combine element by element, like NumPy arrays. Assigning to a new column name adds the column:

```python
sales["revenue"] = sales["units"] * sales["unit_price"]
print(sales[["units", "unit_price", "revenue"]].head(3))
```

```
   units  unit_price  revenue
0    3.0      137.28   411.84
1    2.0       17.16    34.32
2    4.0      105.93   423.72
```

No loop is needed, and it is fast for millions of rows.

### Columns from conditions

A comparison gives a boolean column. Because `True` counts as 1, its mean is the fraction of rows that are `True`:

```python
sales["big_day"] = sales["units"] >= 20
print(sales["big_day"].mean().round(3))
```

```
0.207
```

About 21% of rows sold 20 units or more.

### map: look values up

**`map(dictionary)`** replaces each value with the matching value from a dictionary. Values with no match become `NaN`:

```python
store_names = {"S1": "London", "S2": "Manchester", "S3": "Leeds", "S4": "Bristol", "S5": "Glasgow"}
sales["city"] = sales["store"].map(store_names)
print(sales[["store", "city"]].drop_duplicates().sort_values("store"))
```

```
   store        city
0     S1      London
4     S2  Manchester
1     S3       Leeds
14    S4     Bristol
5     S5     Glasgow
2     S6         NaN
```

Store S6 is not in the dictionary, so its city is missing. Always check for `NaN` after a `map`. (For large lookup tables, a merge is usually better; see 14-06.)

### apply: any function

**`apply(function)`** calls a Python function on each value of a Series. It can express any rule you can write as a function:

```python
def price_band(price):
    if price < 10:
        return "budget"
    if price < 50:
        return "mid"
    return "premium"


sales["band"] = sales["unit_price"].apply(price_band)
print(sales["band"].value_counts())
```

```
band
mid        236
premium    112
budget     112
Name: count, dtype: int64
```

`value_counts()` counts each distinct value (more in 14-05). `apply` runs a Python loop under the hood, so it is much slower than vectorised arithmetic on large data. Prefer built-in operations when they exist, such as `pd.cut` below for this exact job.

### astype

`astype` converts a column's type. Now that missing units have been removed, `units` can be whole numbers again:

```python
print(sales["units"].dtype)
sales["units"] = sales["units"].astype(int)
print(sales["units"].dtype)
```

```
float64
int64
```

### Binning with cut

**`pd.cut`** groups numbers into ranges ("bins"). `bins` gives the edges; each bin includes its right edge, so `[-1, 5, 20, 100]` makes the ranges (−1, 5], (5, 20] and (20, 100]. `labels` names them:

```python
sales["size"] = pd.cut(sales["units"], bins=[-1, 5, 20, 100], labels=["small", "medium", "large"])
print(sales["size"].value_counts().sort_index())
```

```
size
small     189
medium    181
large     90
Name: count, dtype: int64
```

The lower edge is −1 so that 0 units falls into "small". The result is a **categorical** column: a fixed set of labels in a defined order, which is why `sort_index()` lists them small to large rather than alphabetically.

### Dates with .dt

Once a column is a proper datetime (14-03), the **`.dt`** accessor gives its parts:

```python
sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month
sales["weekday"] = sales["date"].dt.day_name()
sales["is_weekend"] = sales["date"].dt.day_of_week >= 5
print(sales[["date", "month", "weekday", "is_weekend"]].head(3))
weekend_units = sales.loc[sales["is_weekend"], "units"].mean()
weekday_units = sales.loc[~sales["is_weekend"], "units"].mean()
print(f"average units: weekend {weekend_units:.2f}, weekday {weekday_units:.2f}")
```

```
        date  month   weekday  is_weekend
0 2026-01-01      1  Thursday       False
1 2026-01-01      1  Thursday       False
2 2026-01-01      1  Thursday       False
average units: weekend 17.15, weekday 10.63
```

`day_of_week` counts Monday as 0, so Saturday and Sunday are 5 and 6. Weekends sell about 60% more per row: a useful feature for any model predicting sales. Other parts include `.dt.year`, `.dt.day`, `.dt.hour` and `.dt.quarter`.

### assign for chained transformations

**`assign`** returns a new DataFrame with added columns, so it can be chained with other methods. Each new column is given as a function of the DataFrame:

```python
summary = (
    sales.assign(revenue_k=lambda df: (df["revenue"] / 1000).round(3))
         .loc[:, ["date", "store", "revenue_k"]]
         .head(3)
)
print(summary)
```

```
        date store  revenue_k
0 2026-01-01    S1      0.412
1 2026-01-01    S3      0.034
2 2026-01-01    S6      0.424
```

Wrapping the chain in brackets lets you put one step per line. `assign` never changes the original DataFrame, which makes it a good fit for the "raw in, clean out" functions from 14-03.

## Common mistakes

- **Forgetting the result of `map` can be missing.** Unmatched values become `NaN` silently. Check with `.isna().sum()`.
- **Using `apply` for simple arithmetic.** `sales["units"].apply(lambda u: u * 2)` works but is slow; `sales["units"] * 2` is the vectorised way.
- **Using `.dt` on a text column.** `.dt.month` on dates stored as strings gives `AttributeError: Can only use .dt accessor with datetimelike values`. Convert with `pd.to_datetime` first.
- **Bins that miss values.** A value outside all the bins, such as 0 with `bins=[0, 5, ...]` (0 is not inside (0, 5]), becomes `NaN`. Check the edges.

## Try it

Add a column `price_change` that shows how much each row's unit price differs from the average price of its category. (Hint: compute a dictionary of category averages with a loop or `sales[sales["category"] == name]["unit_price"].mean()`, then use `map`.) In 14-05 you will learn a one-line way.

## Exercises

Open `ex_14_04.py`. Each function returns a new DataFrame and must not modify its input.

1. `add_revenue`: add a revenue column.
2. `add_city`: add a city column by looking stores up in a dictionary.
3. `add_size_band`: bin units into "small", "medium" and "large".
4. `add_date_parts`: add month, weekday name and weekend columns.

Run the tests:

```
python -m pytest part-3-data-toolkit/14-pandas/14-04-creating-and-transforming-columns
```

## Summary

- `df["new"] = expression` adds a column; arithmetic and comparisons work element by element.
- `map(dict)` looks values up (unmatched become `NaN`); `apply(function)` runs any function, but slowly.
- `astype` converts types; `pd.cut(values, bins, labels)` groups numbers into labelled ranges.
- `.dt.month`, `.dt.day_name()`, `.dt.day_of_week` and friends take datetimes apart.
- `assign` adds columns in a chain and never modifies the original.
