# 14-06 Combining tables

## What you will learn

- Join two tables on a shared key with `merge`, and choose between inner, left, right and outer joins.
- Merge on key columns that have different names.
- Check a merge for lost or duplicated rows, with `indicator` and `validate`.
- Stack tables with the same columns using `concat`.

## Why it matters

Information is usually spread over several tables: sales in one, store details in another, customer records in a third. To ask "which region earns most?", you must combine sales with stores. Joins are also where data quietly goes wrong: a key that does not match drops rows, and a duplicated key multiplies them. Checking every merge is a habit that will save you from wrong conclusions.

## Concepts

The examples use the sales data (with duplicates and missing rows dropped, 460 rows) and the store table:

```python
stores = pd.read_csv(DATA / "stores.csv")
print(stores)
```

```
  store        city    region
0    S1      London     South
1    S2  Manchester     North
2    S3       Leeds     North
3    S4     Bristol     South
4    S5     Glasgow  Scotland
```

Note there is no row for store S6, although S6 appears in the sales data.

### merge

**`merge`** combines two tables by matching values in a **key** column. Each sales row gets the city and region of its store. The `how` argument decides what happens to rows without a match:

| `how` | Keeps |
|-------|-------|
| `"inner"` (the default) | only rows whose key appears in both tables |
| `"left"` | every row of the left table; unmatched ones get `NaN` |
| `"right"` | every row of the right table |
| `"outer"` | every row of both |

### Inner merge

```python
inner = sales.merge(stores, on="store", how="inner")
print(len(sales), len(inner))
print(inner.head(3))
```

```
460 382
         date store     category  units  unit_price        city region
0  2026-01-01    S1  Electronics    3.0      137.28      London  South
1  2026-01-01    S3         Toys    2.0       17.16       Leeds  North
2  2026-01-02    S2  Electronics    3.0      131.68  Manchester  North
```

78 sales rows **disappeared**: every S6 sale, because S6 has no row in `stores`. An inner join drops unmatched rows without any warning.

### Left merge

A left merge keeps every row of the left table, and fills in `NaN` where there was no match, so nothing is lost:

```python
left = sales.merge(stores, on="store", how="left")
print(len(left))
print(left[left["city"].isna()]["store"].unique().tolist())
```

```
460
['S6']
```

When enriching a main table with extra details, **left** is usually what you want: it keeps all your data and makes gaps visible.

### Seeing where rows came from

`indicator=True` adds a column `_merge` saying whether each row matched in `both` tables or only one. An outer merge with an indicator is the best way to audit two keys:

```python
check = sales.merge(stores, on="store", how="outer", indicator=True)
print(check["_merge"].value_counts())
```

```
_merge
both          382
left_only      78
right_only      0
Name: count, dtype: int64
```

78 sales rows have no store, and every store has at least one sale.

### Checking for duplicated rows

The other danger is a key that appears **more than once** in the right table. Each matching left row is then repeated, once per match, and totals are silently inflated. Here we accidentally give S1 two rows in the store table:

```python
print(len(left) == len(sales))
duplicated_stores = pd.concat([stores, stores.iloc[[0]]])
bad = sales.merge(duplicated_stores, on="store", how="left")
print(len(sales), len(bad))
try:
    sales.merge(duplicated_stores, on="store", how="left", validate="many_to_one")
except pd.errors.MergeError as error:
    print("MergeError:", str(error).splitlines()[0])
```

```
True
460 541
MergeError: Merge keys are not unique in right dataset; not a many-to-one merge
```

The merged table grew from 460 to 541 rows: every S1 sale now appears twice. Two cheap checks catch this:

1. **Compare row counts** before and after a left merge. They should be equal.
2. **Pass `validate=`**. `"many_to_one"` says "many sales rows may share a store, but each store must appear once in the right table"; pandas raises a `MergeError` if that is not true. Other options are `"one_to_one"` and `"one_to_many"`.

### Keys with different names

If the key column is called something different in each table, use `left_on` and `right_on`:

```python
targets = pd.DataFrame({"shop_id": ["S1", "S2"], "monthly_target": [9000, 7000]})
with_targets = stores.merge(targets, left_on="store", right_on="shop_id", how="left")
print(with_targets)
```

```
  store        city    region shop_id  monthly_target
0    S1      London     South      S1          9000.0
1    S2  Manchester     North      S2          7000.0
2    S3       Leeds     North     NaN             NaN
3    S4     Bristol     South     NaN             NaN
4    S5     Glasgow  Scotland     NaN             NaN
```

Both key columns are kept; drop the extra one with `.drop(columns="shop_id")` if you do not need it.

### concat

**`concat`** stacks tables that have the same columns on top of each other, such as monthly files. `ignore_index=True` renumbers the rows:

```python
january = sales[sales["date"] < "2026-02-01"]
february = sales[(sales["date"] >= "2026-02-01") & (sales["date"] < "2026-03-01")]
both = pd.concat([january, february], ignore_index=True)
print(len(january), len(february), len(both))
```

```
187 135 322
```

(Comparing the text dates with `<` works here because ISO dates sort correctly as text.) Use `merge` to add **columns** from another table by key; use `concat` to add **rows**.

### Putting it together

Once merged, the store details can be grouped like any other column (14-05). `dropna=False` keeps the group of sales with no region:

```python
region_revenue = (
    left.assign(revenue=left["units"] * left["unit_price"])
        .groupby("region", dropna=False)["revenue"].sum()
        .round(2)
)
print(region_revenue)
```

```
region
North       37729.45
Scotland    16646.50
South       47714.30
NaN         11223.60
Name: revenue, dtype: float64
```

Over 11,000 of revenue has no region. With an inner join, it would have vanished from the total without anyone noticing.

## Common mistakes

- **Using an inner join by accident.** `merge` defaults to `how="inner"`, which silently drops unmatched rows. Say `how=` explicitly, and compare row counts.
- **Duplicate keys in the lookup table.** They multiply rows. Use `validate="many_to_one"` when merging details onto a main table.
- **Misspelt or missing key columns.** `sales.merge(other, on="store")` where `other` has no `store` column gives `KeyError: 'store'`.
- **Keys of different types.** Merging a key stored as text (`"1"`) with one stored as numbers (`1`) matches nothing, or raises an error. Check `dtypes` on both sides.

## Try it

Merge the sales with the stores using `how="right"`. How many rows do you get, and why? Then fix the gap properly: add a row for S6 (say Cardiff, region "Wales") to a copy of `stores` with `concat`, merge again, and check that no regions are missing.

## Exercises

Open `ex_14_06.py`:

1. `add_store_details`: a left merge that refuses duplicate store rows.
2. `unmatched_keys`: the keys in one table that have no match in the other.
3. `revenue_by_region`: total revenue per region after merging.
4. `stack_tables`: combine several tables with the same columns.

Run the tests:

```
python -m pytest part-3-data-toolkit/14-pandas/14-06-combining-tables
```

## Summary

- `left.merge(right, on="key", how=...)` joins tables; `how` is `"inner"`, `"left"`, `"right"` or `"outer"`.
- Inner joins drop unmatched rows silently; left joins keep them with `NaN`.
- Audit merges: compare row counts, use `indicator=True`, and pass `validate="many_to_one"`.
- Use `left_on`/`right_on` when the key names differ.
- `pd.concat([a, b], ignore_index=True)` stacks rows; `merge` adds columns.
