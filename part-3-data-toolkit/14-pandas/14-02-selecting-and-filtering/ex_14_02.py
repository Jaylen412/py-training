"""Exercises for 14-02 Selecting and filtering.

Each `sales` argument is a DataFrame with the columns of data/store_sales.csv:
date, store, category, units, unit_price.
"""
import pandas as pd


def select_columns(sales, columns):
    """Return a DataFrame containing only the given list of columns, in that order."""
    raise NotImplementedError


def rows_for_store(sales, store):
    """Return the rows where the store column equals `store`."""
    raise NotImplementedError


def big_days(sales, minimum_units):
    """Return the rows with units >= minimum_units, sorted by units from
    largest to smallest."""
    raise NotImplementedError


def in_categories(sales, categories):
    """Return the rows whose category is in the list `categories`."""
    raise NotImplementedError


def first_row_value(frame, column):
    """Return the value in `column` of the FIRST row by position, whatever its
    index label is.

    Example: if frame was filtered and its first row has label 6, this still
    returns that row's value
    """
    raise NotImplementedError
