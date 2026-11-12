# 14-05 Grouping and aggregating

## What you will learn

- Count values with `value_counts`.
- Split data into groups and summarise each with `groupby`.
- Compute several named summaries at once with `agg`.
- Build two-way summary tables with `pivot_table`.

## Why it matters

Most questions about data are questions about groups: which store earns most, which category sells most units, how revenue changes by month. "Split the data into groups, apply a summary to each, combine the results" is the most useful pattern in data analysis. You will also use it to check machine learning results, for example a model's accuracy for each customer group.

## Concepts

The examples use cleaned sales data with a `revenue` column (14-03 and 14-04).

### value_counts

**`value_counts()`** counts how many rows have each value, most common first. `normalize=True` gives proportions instead:

```python
print(sales["category"].value_counts())
print(sales["store"].value_counts(normalize=True).round(3).head(3))
```

```
category
Clothing       126
Electronics    112
Groceries      112
Toys           110
Name: count, dtype: int64
store
S5    0.185
S1    0.176
S6    0.170
Name: proportion, dtype: float64
```

### Split, apply, combine

**`groupby(column)`** splits the rows into one group per distinct value. Selecting a column and calling an aggregation then summarises each group, and pandas combines the results into a Series indexed by the group values:

```python
print(sales.groupby("store")["revenue"].sum().round(2))
```

```
store
S1    31471.01
S2    21829.01
S3    15900.44
S4    16243.29
S5    16646.50
S6    11223.60
Name: revenue, dtype: float64
```

Read it as: "group the sales by store, take the revenue column, and sum it within each group". S1 earns almost three times as much as S6. Any aggregation works: `sum`, `mean`, `median`, `min`, `max`, `count` (non-missing values), `size` (rows), `std`, `nunique` (distinct values).

The result is an ordinary Series, so you can sort it:

```python
by_category = sales.groupby("category")["units"].mean().sort_values(ascending=False)
print(by_category.round(2))
```

```
category
Groceries      31.70
Clothing        8.97
Toys            6.35
Electronics     2.85
Name: units, dtype: float64
```

### Several summaries with agg

**`agg`** computes several summaries at once. **Named aggregation** gives each result column a name and says which column and function it uses, as `new_name=(column, function)`:

```python
summary = sales.groupby("category").agg(
    rows=("units", "size"),
    total_units=("units", "sum"),
    average_price=("unit_price", "mean"),
    revenue=("revenue", "sum"),
)
print(summary.round(2))
```

```
             rows  total_units  average_price   revenue
category                                               
Clothing      126       1130.0          34.81  39300.06
Electronics   112        319.0         121.13  38634.96
Groceries     112       3550.0           6.49  23124.86
Toys          110        698.0          17.63  12253.97
```

This table tells a story: Groceries sell by far the most units but at low prices, while Electronics sell few units at high prices and earn almost as much as Clothing.

### Grouping by several columns

Pass a list to group by combinations. The result has a two-level index:

```python
print(sales.groupby(["store", "category"])["revenue"].sum().round(0).head(6))
```

```
store  category   
S1     Clothing       11753.0
       Electronics     9961.0
       Groceries       7186.0
       Toys            2571.0
S2     Clothing        7582.0
       Electronics     7781.0
Name: revenue, dtype: float64
```

### Grouping by a derived value

You can group by any Series of the same length, not only an existing column, for example the month of each date:

```python
monthly = sales.groupby(sales["date"].dt.month)["revenue"].sum().round(2)
print(monthly)
```

```
date
1    44241.98
2    36589.72
3    32482.15
Name: revenue, dtype: float64
```

Revenue fell each month. Whether that is a real trend or just noise is the kind of question Module 19 helps you answer.

### pivot_table

A **pivot table** lays a two-way summary out as a grid: one variable down the rows, another across the columns, and a summary in each cell:

```python
pivot = sales.pivot_table(index="store", columns="category", values="revenue", aggfunc="sum").round(0)
print(pivot)
```

```
category  Clothing  Electronics  Groceries    Toys
store                                             
S1         11753.0       9961.0     7186.0  2571.0
S2          7582.0       7781.0     3693.0  2773.0
S3          5656.0       4375.0     4063.0  1806.0
S4          6841.0       4164.0     2683.0  2555.0
S5          4483.0       6924.0     3638.0  1601.0
S6          2986.0       5429.0     1861.0   948.0
```

It contains the same numbers as the two-column `groupby`, laid out for reading. S5 is unusual: Electronics is its best category, while every other store except S6 earns most from Clothing.

### Getting the groups back as a column

By default the group values become the index. `as_index=False` (or `.reset_index()` afterwards) keeps them as an ordinary column, which is easier to sort, filter or merge:

```python
top_stores = sales.groupby("store", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
print(top_stores.head(3).round(2))
```

```
  store   revenue
0    S1  31471.01
1    S2  21829.01
4    S5  16646.50
```

### transform: a group summary on every row

One more tool answers the 14-04 "Try it": **`transform`** computes a group summary but returns it **aligned with the original rows**, so you can put it in a new column. For example, `sales.groupby("category")["unit_price"].transform("mean")` gives every row its category's average price, and `.transform("median")` inside `fillna` fills each missing price with its own category's median, a better fill than the overall median used in 14-03.

## Common mistakes

- **Grouping by a column that does not exist.** `sales.groupby("store")["revenue"]` before creating `revenue` gives `KeyError: 'Column not found: revenue'`.
- **Confusing `count` and `size`.** `count` counts non-missing values in a column; `size` counts rows, including those with missing values.
- **Summing text columns.** `sales.groupby("store").sum()` tries to sum every column, including text, which joins the strings together. Select the numeric column first: `groupby("store")["revenue"].sum()`.
- **Forgetting that a groupby result is indexed by group.** To merge or filter it like a normal table, use `as_index=False` or `reset_index()`.

## Try it

Using `transform`, add a column with each store's average daily units, then find the rows where a store sold more than twice its own average. Which categories are those big days in?

## Exercises

Open `ex_14_05.py`. Each `sales` argument has the columns store, category, units, unit_price and revenue.

1. `rows_per_category`: how many rows each category has.
2. `revenue_by_store`: total revenue per store, largest first.
3. `category_summary`: several named summaries per category.
4. `store_category_table`: a pivot table of revenue.
5. `fill_price_by_category`: fill missing prices with their category's median.

Run the tests:

```
python -m pytest part-3-data-toolkit/14-pandas/14-05-grouping-and-aggregating
```

## Summary

- `value_counts()` counts each value; `normalize=True` gives proportions.
- `df.groupby("key")["column"].agg_function()` summarises each group.
- `agg(name=(column, function), ...)` makes several named summaries at once.
- Group by a list for combinations, or by any derived Series such as `df["date"].dt.month`.
- `pivot_table(index=..., columns=..., values=..., aggfunc=...)` builds a two-way grid; `transform` puts group summaries back on each row.
