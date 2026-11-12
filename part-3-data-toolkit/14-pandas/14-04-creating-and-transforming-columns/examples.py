# 14-04 Creating and transforming columns
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)
sales = pd.read_csv(DATA / "store_sales.csv").drop_duplicates().dropna().reset_index(drop=True)
sales["category"] = sales["category"].str.strip().str.title()

# Example 1: vectorised column maths
sales["revenue"] = sales["units"] * sales["unit_price"]
print(sales[["units", "unit_price", "revenue"]].head(3))

# Example 2: new columns from conditions
sales["big_day"] = sales["units"] >= 20
print(sales["big_day"].mean().round(3))

# Example 3: map - replace values using a dictionary
store_names = {"S1": "London", "S2": "Manchester", "S3": "Leeds", "S4": "Bristol", "S5": "Glasgow"}
sales["city"] = sales["store"].map(store_names)
print(sales[["store", "city"]].drop_duplicates().sort_values("store"))


# Example 4: apply - run any function on every value
def price_band(price):
    if price < 10:
        return "budget"
    if price < 50:
        return "mid"
    return "premium"


sales["band"] = sales["unit_price"].apply(price_band)
print(sales["band"].value_counts())

# Example 5: astype
print(sales["units"].dtype)
sales["units"] = sales["units"].astype(int)
print(sales["units"].dtype)

# Example 6: binning numbers into ranges with cut
sales["size"] = pd.cut(sales["units"], bins=[-1, 5, 20, 100], labels=["small", "medium", "large"])
print(sales["size"].value_counts().sort_index())

# Example 7: dates with to_datetime and the .dt accessor
sales["date"] = pd.to_datetime(sales["date"])
sales["month"] = sales["date"].dt.month
sales["weekday"] = sales["date"].dt.day_name()
sales["is_weekend"] = sales["date"].dt.day_of_week >= 5
print(sales[["date", "month", "weekday", "is_weekend"]].head(3))
weekend_units = sales.loc[sales["is_weekend"], "units"].mean()
weekday_units = sales.loc[~sales["is_weekend"], "units"].mean()
print(f"average units: weekend {weekend_units:.2f}, weekday {weekday_units:.2f}")

# Example 8: assign builds several columns in one chained expression
summary = (
    sales.assign(revenue_k=lambda df: (df["revenue"] / 1000).round(3))
         .loc[:, ["date", "store", "revenue_k"]]
         .head(3)
)
print(summary)
