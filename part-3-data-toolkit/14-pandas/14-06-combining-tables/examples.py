# 14-06 Combining tables
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)
sales = pd.read_csv(DATA / "store_sales.csv").drop_duplicates().dropna().reset_index(drop=True)
stores = pd.read_csv(DATA / "stores.csv")
print(stores)

# Example 1: an inner merge keeps only rows with a match in both tables
inner = sales.merge(stores, on="store", how="inner")
print(len(sales), len(inner))
print(inner.head(3))

# Example 2: a left merge keeps every sales row; missing matches become NaN
left = sales.merge(stores, on="store", how="left")
print(len(left))
print(left[left["city"].isna()]["store"].unique().tolist())

# Example 3: indicator=True shows where each row came from
check = sales.merge(stores, on="store", how="outer", indicator=True)
print(check["_merge"].value_counts())

# Example 4: checking a merge for lost or duplicated rows
print(len(left) == len(sales))
duplicated_stores = pd.concat([stores, stores.iloc[[0]]])
bad = sales.merge(duplicated_stores, on="store", how="left")
print(len(sales), len(bad))
try:
    sales.merge(duplicated_stores, on="store", how="left", validate="many_to_one")
except pd.errors.MergeError as error:
    print("MergeError:", str(error).splitlines()[0])

# Example 5: merging when the key columns have different names
targets = pd.DataFrame({"shop_id": ["S1", "S2"], "monthly_target": [9000, 7000]})
with_targets = stores.merge(targets, left_on="store", right_on="shop_id", how="left")
print(with_targets)

# Example 6: concat stacks tables with the same columns
january = sales[sales["date"] < "2026-02-01"]
february = sales[(sales["date"] >= "2026-02-01") & (sales["date"] < "2026-03-01")]
both = pd.concat([january, february], ignore_index=True)
print(len(january), len(february), len(both))

# Example 7: region totals after a merge
region_revenue = (
    left.assign(revenue=left["units"] * left["unit_price"])
        .groupby("region", dropna=False)["revenue"].sum()
        .round(2)
)
print(region_revenue)
