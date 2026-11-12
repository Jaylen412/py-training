"""Exercises for 14-03 Cleaning data.

None of these functions may modify the DataFrame or Series passed in.
"""
import pandas as pd


def clean_categories(categories):
    """Return the Series with surrounding spaces removed and each value in
    title case.

    Example: pd.Series([" electronics", "CLOTHING"]) becomes ["Electronics", "Clothing"]
    """
    raise NotImplementedError


def drop_missing(frame, columns):
    """Return the rows that have no missing value in any of `columns`."""
    raise NotImplementedError


def fill_with_median(frame, column):
    """Return a copy of `frame` where missing values in `column` are replaced
    by the median of that column."""
    raise NotImplementedError


def remove_duplicates(frame):
    """Return `frame` without duplicate rows, with the index renumbered
    from 0."""
    raise NotImplementedError


def clean_sales(raw):
    """Return the cleaned sales data. In this order:
    1. remove duplicate rows,
    2. tidy the category column with clean_categories,
    3. convert the date column with pd.to_datetime,
    4. drop rows with missing units,
    5. fill missing unit_price values with the median unit_price,
    6. renumber the index from 0.
    For data/store_sales.csv the result has 468 rows and no missing values.
    """
    raise NotImplementedError
