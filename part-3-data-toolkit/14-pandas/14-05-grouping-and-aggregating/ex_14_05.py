"""Exercises for 14-05 Grouping and aggregating.

Each `sales` argument has the columns store, category, units, unit_price
and revenue.
"""
import pandas as pd


def rows_per_category(sales):
    """Return a dictionary mapping each category to its number of rows.

    Example: {"Toys": 2, "Clothing": 1}
    """
    raise NotImplementedError


def revenue_by_store(sales):
    """Return a Series of total revenue per store (indexed by store),
    sorted from largest to smallest."""
    raise NotImplementedError


def category_summary(sales):
    """Return a DataFrame indexed by category with these columns, in order:
    rows (number of rows), total_units (sum of units),
    average_price (mean unit_price), revenue (sum of revenue).
    """
    raise NotImplementedError


def store_category_table(sales):
    """Return a pivot table with one row per store, one column per category,
    and the total revenue in each cell. Combinations with no sales should
    be 0, not NaN (pivot_table has a fill_value argument)."""
    raise NotImplementedError


def fill_price_by_category(sales):
    """Return a copy of `sales` where each missing unit_price is replaced by
    the median unit_price of the same category. Use groupby and transform."""
    raise NotImplementedError
