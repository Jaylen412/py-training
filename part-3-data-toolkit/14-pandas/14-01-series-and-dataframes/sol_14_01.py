"""Solutions for 14-01 Series and DataFrames."""
import pandas as pd


def make_people(names, ages):
    """Return a DataFrame with "name" and "age" columns."""
    return pd.DataFrame({"name": names, "age": ages})


def load_csv(path):
    """Read a CSV file into a DataFrame."""
    return pd.read_csv(path)


def shape_summary(frame):
    """Return (rows, columns, column names)."""
    rows, columns = frame.shape
    return rows, columns, frame.columns.tolist()


def missing_counts(frame):
    """Return {column: number of missing values}."""
    return {column: int(count) for column, count in frame.isna().sum().items()}


def numeric_columns(frame):
    """Return the names of the numeric columns."""
    return frame.select_dtypes(include="number").columns.tolist()
