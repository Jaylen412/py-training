"""Exercises for 14-01 Series and DataFrames."""
import pandas as pd


def make_people(names, ages):
    """Return a DataFrame with two columns, "name" and "age", from two lists.

    Example: make_people(["Ada"], [36]) has one row: name "Ada", age 36
    """
    raise NotImplementedError


def load_csv(path):
    """Read the CSV file at `path` and return it as a DataFrame."""
    raise NotImplementedError


def shape_summary(frame):
    """Return a tuple (number of rows, number of columns, list of column names).

    Example: for make_people(["Ada"], [36]) returns (1, 2, ["name", "age"])
    """
    raise NotImplementedError


def missing_counts(frame):
    """Return a dictionary mapping each column name to its number of missing
    values (as a plain int).
    Hint: frame.isna().sum() gives a Series of counts; .to_dict() converts it.

    Example: {"date": 0, "store": 0, "units": 12}
    """
    raise NotImplementedError


def numeric_columns(frame):
    """Return a list of the names of the numeric columns, in column order.
    Hint: frame.select_dtypes(include="number") keeps only numeric columns.

    Example: for the sales data returns ["units", "unit_price"]
    """
    raise NotImplementedError
