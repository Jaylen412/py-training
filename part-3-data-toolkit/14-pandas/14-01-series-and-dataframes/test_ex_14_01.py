import importlib
import os
from pathlib import Path

import numpy as np
import pandas as pd

mod = importlib.import_module(
    "sol_14_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_14_01"
)

SALES_CSV = Path(__file__).resolve().parents[3] / "data" / "store_sales.csv"


def test_make_people():
    frame = mod.make_people(["Ada", "Alan"], [36, 41])
    assert isinstance(frame, pd.DataFrame)
    assert frame.columns.tolist() == ["name", "age"]
    assert frame["age"].tolist() == [36, 41]


def test_make_people_empty():
    assert len(mod.make_people([], [])) == 0


def test_load_csv_real_file():
    frame = mod.load_csv(SALES_CSV)
    assert frame.shape == (486, 5)


def test_load_csv_temporary_file(tmp_path):
    path = tmp_path / "tiny.csv"
    path.write_text("a,b\n1,2\n3,4\n")
    assert mod.load_csv(path)["b"].tolist() == [2, 4]


def test_shape_summary():
    frame = pd.DataFrame({"name": ["Ada"], "age": [36]})
    assert mod.shape_summary(frame) == (1, 2, ["name", "age"])


def test_shape_summary_real_file():
    rows, columns, names = mod.shape_summary(pd.read_csv(SALES_CSV))
    assert (rows, columns) == (486, 5)
    assert names == ["date", "store", "category", "units", "unit_price"]


def test_missing_counts():
    frame = pd.DataFrame({"a": [1, np.nan, 3], "b": ["x", "y", None]})
    assert mod.missing_counts(frame) == {"a": 1, "b": 1}


def test_missing_counts_real_file():
    counts = mod.missing_counts(pd.read_csv(SALES_CSV))
    assert counts["units"] == 12 and counts["unit_price"] == 8 and counts["date"] == 0
    assert all(type(value) is int for value in counts.values())


def test_numeric_columns():
    assert mod.numeric_columns(pd.read_csv(SALES_CSV)) == ["units", "unit_price"]


def test_numeric_columns_none():
    assert mod.numeric_columns(pd.DataFrame({"text": ["a"]})) == []
