# 14-03 Cleaning data
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)
sales = pd.read_csv(DATA / "store_sales.csv")

# Example 1: finding missing values
print(sales.isna().sum())
print(sales[sales["unit_price"].isna()].head(3))

# Example 2: dropping rows with missing values
print(len(sales), len(sales.dropna()), len(sales.dropna(subset=["units"])))

# Example 3: filling missing values
filled = sales.fillna({"units": 0})
print(filled["units"].isna().sum())
median_price = sales["unit_price"].median()
print(round(median_price, 2))

# Example 4: duplicates
print(sales.duplicated().sum())
print(sales[sales.duplicated(keep=False)].head(4))
deduplicated = sales.drop_duplicates()
print(len(deduplicated))

# Example 5: messy text - the .str accessor
print(sales["category"].unique().tolist())
clean_category = sales["category"].str.strip().str.title()
print(clean_category.unique().tolist())
print(sales["store"].str.replace("S", "Store ").head(3).tolist())

# Example 6: fixing types
print(sales["date"].dtype)
sales["date"] = pd.to_datetime(sales["date"])
print(sales["date"].dtype, sales["date"].min(), sales["date"].max())
print(pd.to_numeric(pd.Series(["1.5", "2", "oops"]), errors="coerce").tolist())

# Example 7: renaming columns
renamed = sales.rename(columns={"unit_price": "price", "units": "quantity"})
print(renamed.columns.tolist())


# Example 8: a cleaning function that puts it all together
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
