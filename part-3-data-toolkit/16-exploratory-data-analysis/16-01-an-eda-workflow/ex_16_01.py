"""Exercises for 16-01 An EDA workflow: reusable helpers for any dataset."""
import pandas as pd


def overview(frame):
    """Return a dictionary with these keys and plain int values:
    "rows", "columns", "missing" (total missing values), "duplicates"
    (number of duplicate rows).

    Example: {"rows": 569, "columns": 32, "missing": 0, "duplicates": 0}
    """
    raise NotImplementedError


def missing_report(frame):
    """Return a DataFrame indexed by column name with two columns:
    "count" (number of missing values) and "percent" (percentage of rows
    missing, rounded to 1 decimal place). Include only columns with at
    least one missing value, sorted by count from most to least.
    """
    raise NotImplementedError


def class_balance(labels):
    """`labels` is a Series. Return a dictionary mapping each class to the
    proportion of rows in it, rounded to 3 decimal places.

    Example: {"benign": 0.627, "malignant": 0.373}
    """
    raise NotImplementedError


def median_by_group(frame, group_column, columns):
    """Return a DataFrame with one row per group (indexed by group) and the
    median of each of `columns` for that group."""
    raise NotImplementedError


def numbered_findings(findings):
    """Return the findings as one string, one per line, numbered from 1, in
    the form "1. first finding". No trailing newline. Return "" for an empty
    list.

    Example: numbered_findings(["a", "b"]) returns "1. a\\n2. b"
    """
    raise NotImplementedError
