"""Solutions for 14-02 Selecting and filtering."""
import pandas as pd


def select_columns(sales, columns):
    """Return only the given columns."""
    return sales[columns]


def rows_for_store(sales, store):
    """Return the rows for one store."""
    return sales[sales["store"] == store]


def big_days(sales, minimum_units):
    """Return rows with at least `minimum_units`, largest first."""
    return sales[sales["units"] >= minimum_units].sort_values("units", ascending=False)


def in_categories(sales, categories):
    """Return rows whose category is in `categories`."""
    return sales[sales["category"].isin(categories)]


def first_row_value(frame, column):
    """Return `column` from the first row by position."""
    # iloc works by position; get_loc turns the column name into a position.
    return frame.iloc[0, frame.columns.get_loc(column)]
