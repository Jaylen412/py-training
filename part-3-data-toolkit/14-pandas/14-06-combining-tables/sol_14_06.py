"""Solutions for 14-06 Combining tables."""
import pandas as pd


def add_store_details(sales, stores):
    """Left-merge store details onto sales, refusing duplicate stores."""
    return sales.merge(stores, on="store", how="left", validate="many_to_one")


def unmatched_keys(left, right, key):
    """Return the sorted keys in `left` with no match in `right`."""
    return sorted(set(left[key]) - set(right[key]))


def revenue_by_region(sales, stores):
    """Return {region: total revenue}, with unmatched stores as "Unknown"."""
    merged = add_store_details(sales, stores)
    merged["region"] = merged["region"].fillna("Unknown")
    revenue = merged["units"] * merged["unit_price"]
    totals = revenue.groupby(merged["region"]).sum()
    return {region: round(float(total), 2) for region, total in totals.items()}


def stack_tables(tables):
    """Stack tables with the same columns."""
    return pd.concat(tables, ignore_index=True)
