"""Exercises for 14-06 Combining tables.

`sales` has the columns store, units, unit_price (and maybe others).
`stores` has the columns store, city, region.
"""
import pandas as pd


def add_store_details(sales, stores):
    """Return `sales` left-merged with `stores` on "store", keeping every
    sales row. Pass validate="many_to_one" so that duplicate store rows
    raise pd.errors.MergeError."""
    raise NotImplementedError


def unmatched_keys(left, right, key):
    """Return a sorted list of the distinct values of `key` in `left` that
    do not appear in `right`.

    Example: for the course data, unmatched_keys(sales, stores, "store") returns ["S6"]
    """
    raise NotImplementedError


def revenue_by_region(sales, stores):
    """Return a dictionary mapping region to total revenue
    (units * unit_price), rounded to 2 decimal places. Sales whose store has
    no region are grouped under "Unknown".
    """
    raise NotImplementedError


def stack_tables(tables):
    """Return the list of DataFrames stacked into one, with the index
    renumbered from 0."""
    raise NotImplementedError
