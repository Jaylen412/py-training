"""Exercises for 06-02 CSV and JSON.

Each path argument is a pathlib.Path.
"""
import csv
import json


def read_scores(path):
    """The CSV has the columns name and score. Return a list of dictionaries,
    one per row, with "score" converted to an int.

    Example: a file with the rows "name,score" / "Ada,95" returns
    [{"name": "Ada", "score": 95}]
    """
    raise NotImplementedError


def column_average(path, column):
    """Return the average of the numeric `column` of the CSV, as a float.
    Return 0.0 if the file has a header but no data rows.

    Example: a file with "item,price" / "pen,1.5" / "pad,2.5" and
    column="price" returns 2.0
    """
    raise NotImplementedError


def write_records(path, records, fieldnames):
    """Write `records` (a list of dictionaries) to a CSV file with a header
    row, using `fieldnames` as the column order.

    Example: write_records(path, [{"a": 1, "b": 2}], ["a", "b"]) writes
    "a,b" then "1,2"
    """
    raise NotImplementedError


def save_json(path, data):
    """Save `data` to the file as JSON with indent=2."""
    raise NotImplementedError


def load_json(path):
    """Load and return the JSON data stored in the file.

    Example: after save_json(path, {"a": [1, 2]}), load_json(path) returns {"a": [1, 2]}
    """
    raise NotImplementedError


def csv_to_json(csv_path, json_path):
    """Read every row of the CSV with DictReader and save the list of row
    dictionaries to `json_path` as JSON. Values stay as strings.
    Return the number of rows converted.

    Example: a CSV with a header and 3 rows returns 3
    """
    raise NotImplementedError
