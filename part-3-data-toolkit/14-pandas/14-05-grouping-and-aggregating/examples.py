# 14-05 Grouping and aggregating
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)
sales = pd.read_csv(DATA / "store_sales.csv").drop_duplicates().dropna().reset_index(drop=True)
sales["category"] = sales["category"].str.strip().str.title()
sales["date"] = pd.to_datetime(sales["date"])
sales["revenue"] = sales["units"] * sales["unit_price"]

# Example 1: value_counts - how many rows per value
print(sales["category"].value_counts())
print(sales["store"].value_counts(normalize=True).round(3).head(3))

# Example 2: groupby + one aggregation
print(sales.groupby("store")["revenue"].sum().round(2))

# Example 3: sorting the result
by_category = sales.groupby("category")["units"].mean().sort_values(ascending=False)
print(by_category.round(2))

# Example 4: several aggregations with agg
summary = sales.groupby("category").agg(
    rows=("units", "size"),
    total_units=("units", "sum"),
    average_price=("unit_price", "mean"),
    revenue=("revenue", "sum"),
)
print(summary.round(2))

# Example 5: grouping by two columns
print(sales.groupby(["store", "category"])["revenue"].sum().round(0).head(6))

# Example 6: grouping by a date part
monthly = sales.groupby(sales["date"].dt.month)["revenue"].sum().round(2)
print(monthly)

# Example 7: pivot_table - a two-way summary table
pivot = sales.pivot_table(index="store", columns="category", values="revenue", aggfunc="sum").round(0)
print(pivot)

# Example 8: reset_index turns the group labels back into a column
top_stores = sales.groupby("store", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False)
print(top_stores.head(3).round(2))
