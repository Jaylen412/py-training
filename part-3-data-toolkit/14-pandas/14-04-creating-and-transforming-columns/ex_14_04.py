"""Exercises for 14-04 Creating and transforming columns.

Each function returns a NEW DataFrame and must not modify the one passed in.
"""
import pandas as pd


def add_revenue(sales):
    """Return `sales` with a new column "revenue" = units * unit_price."""
    raise NotImplementedError


def add_city(sales, cities):
    """Return `sales` with a new column "city", found by looking up each store
    in the dictionary `cities`. Stores not in the dictionary get "Unknown".

    Example: cities={"S1": "London"} gives "London" for S1 and "Unknown" for S9
    """
    raise NotImplementedError


def add_size_band(sales):
    """Return `sales` with a new column "size": "small" for 0 to 5 units,
    "medium" for 6 to 20, "large" for 21 to 100. Use pd.cut.
    """
    raise NotImplementedError


def add_date_parts(sales):
    """Return `sales` with the date column converted to datetimes and three
    new columns: "month" (1 to 12), "weekday" (such as "Thursday") and
    "is_weekend" (True on Saturday and Sunday).
    """
    raise NotImplementedError
