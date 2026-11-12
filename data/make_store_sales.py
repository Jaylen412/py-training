"""Generate data/store_sales.csv and data/stores.csv for Module 14 onwards.

Run from the repository root:
    python data/make_store_sales.py

store_sales.csv has about 500 rows of daily sales with the columns
date, store, category, units, unit_price. It is deliberately messy:
- some missing units and unit prices,
- a few exact duplicate rows,
- inconsistent spacing and capitals in the category column.
stores.csv lists each store's city and region. One store in the sales data
(S6) is missing from stores.csv, so merges have something to find.
"""
from pathlib import Path

import numpy as np
import pandas as pd

SEED = 42
FOLDER = Path(__file__).parent

STORES = pd.DataFrame({
    "store": ["S1", "S2", "S3", "S4", "S5"],
    "city": ["London", "Manchester", "Leeds", "Bristol", "Glasgow"],
    "region": ["South", "North", "North", "South", "Scotland"],
})

CATEGORIES = {
    # name: (typical price, typical units per day)
    "Electronics": (120.0, 3),
    "Clothing": (35.0, 8),
    "Groceries": (6.5, 30),
    "Toys": (18.0, 6),
}
MESSY_SPELLINGS = {"Electronics": " electronics", "Clothing": "CLOTHING", "Groceries": "groceries ", "Toys": "Toys"}


def main():
    rng = np.random.default_rng(SEED)
    dates = pd.date_range("2026-01-01", "2026-03-31", freq="D")
    stores = ["S1", "S2", "S3", "S4", "S5", "S6"]
    store_size = {"S1": 1.6, "S2": 1.2, "S3": 0.8, "S4": 1.0, "S5": 0.7, "S6": 0.5}

    rows = []
    for _ in range(480):
        date = dates[rng.integers(len(dates))]
        store = stores[rng.integers(len(stores))]
        category = list(CATEGORIES)[rng.integers(len(CATEGORIES))]
        base_price, base_units = CATEGORIES[category]
        weekend_boost = 1.4 if date.day_of_week >= 5 else 1.0
        units = rng.poisson(base_units * store_size[store] * weekend_boost)
        price = round(base_price * rng.uniform(0.85, 1.15), 2)
        rows.append({
            "date": date.strftime("%Y-%m-%d"),
            "store": store,
            "category": category,
            "units": int(units),
            "unit_price": price,
        })
    sales = pd.DataFrame(rows).sort_values(["date", "store"]).reset_index(drop=True)

    # Make it messy.
    messy_rows = rng.choice(len(sales), size=40, replace=False)
    sales.loc[messy_rows, "category"] = sales.loc[messy_rows, "category"].map(MESSY_SPELLINGS)
    sales["units"] = sales["units"].astype("Int64")
    sales.loc[rng.choice(len(sales), size=12, replace=False), "units"] = pd.NA
    sales.loc[rng.choice(len(sales), size=8, replace=False), "unit_price"] = np.nan
    duplicates = sales.iloc[rng.choice(len(sales), size=6, replace=False)]
    sales = pd.concat([sales, duplicates]).sort_values(["date", "store"]).reset_index(drop=True)

    sales.to_csv(FOLDER / "store_sales.csv", index=False)
    STORES.to_csv(FOLDER / "stores.csv", index=False)
    print(f"Wrote {len(sales)} rows to store_sales.csv and {len(STORES)} rows to stores.csv")


if __name__ == "__main__":
    main()
