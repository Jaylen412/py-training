# 14-02 Selecting and filtering
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)
sales = pd.read_csv(DATA / "store_sales.csv")

# Example 1: one column gives a Series; a list of columns gives a DataFrame
print(sales["units"].head(3))
print(sales[["store", "units"]].head(3))

# Example 2: loc selects by label, iloc by position
print(sales.loc[0, "store"])
print(sales.loc[0:2, ["date", "units"]])
print(sales.iloc[0:2, 0:2])
print(sales.iloc[-1])

# Example 3: boolean filters - like NumPy masks
big_orders = sales[sales["units"] > 40]
print(len(big_orders))
print(big_orders.head(3))

# Example 4: combining conditions with & and |
s1_electronics = sales[(sales["store"] == "S1") & (sales["category"] == "Electronics")]
print(len(s1_electronics))
print(len(sales[(sales["units"] == 0) | (sales["unit_price"] > 135)]))

# Example 5: isin for "one of these values"
north = sales[sales["store"].isin(["S2", "S3"])]
print(north["store"].unique().tolist())

# Example 6: query - the same filters written as text
print(len(sales.query("store == 'S1' and units > 20")))

# Example 7: loc with a filter and columns at once
print(sales.loc[sales["units"] > 50, ["date", "store", "units"]])

# Example 8: sorting
print(sales.sort_values("unit_price", ascending=False).head(3))
print(sales.sort_values(["store", "units"], ascending=[True, False]).head(3))
