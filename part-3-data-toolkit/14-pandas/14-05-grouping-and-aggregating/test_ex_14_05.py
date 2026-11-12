import importlib
import os

import numpy as np
import pandas as pd
import pytest

mod = importlib.import_module(
    "sol_14_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_14_05"
)


@pytest.fixture
def sales():
    frame = pd.DataFrame({
        "store": ["S1", "S1", "S2", "S2", "S3"],
        "category": ["Toys", "Clothing", "Toys", "Toys", "Clothing"],
        "units": [2, 1, 4, 3, 5],
        "unit_price": [10.0, 30.0, 12.0, 8.0, 20.0],
    })
    frame["revenue"] = frame["units"] * frame["unit_price"]
    return frame


def test_rows_per_category(sales):
    assert mod.rows_per_category(sales) == {"Toys": 3, "Clothing": 2}


def test_rows_per_category_empty():
    empty = pd.DataFrame({"category": pd.Series([], dtype=str)})
    assert mod.rows_per_category(empty) == {}


def test_revenue_by_store(sales):
    result = mod.revenue_by_store(sales)
    assert result.index.tolist() == ["S3", "S2", "S1"]
    assert result.tolist() == [100.0, 72.0, 50.0]


def test_revenue_by_store_values(sales):
    result = mod.revenue_by_store(sales)
    assert result.to_dict() == {"S1": 50.0, "S2": 72.0, "S3": 100.0}
    assert result.is_monotonic_decreasing


def test_category_summary(sales):
    result = mod.category_summary(sales)
    assert result.columns.tolist() == ["rows", "total_units", "average_price", "revenue"]
    assert result.loc["Toys", "rows"] == 3
    assert result.loc["Toys", "total_units"] == 9
    assert result.loc["Toys", "average_price"] == pytest.approx(10.0)
    assert result.loc["Clothing", "revenue"] == pytest.approx(130.0)


def test_store_category_table(sales):
    table = mod.store_category_table(sales)
    assert table.loc["S2", "Toys"] == pytest.approx(72.0)
    assert table.loc["S3", "Toys"] == 0
    assert table.shape == (3, 2)


def test_fill_price_by_category():
    frame = pd.DataFrame({
        "category": ["Toys", "Toys", "Toys", "Clothing", "Clothing"],
        "unit_price": [10.0, 20.0, np.nan, 50.0, np.nan],
    })
    result = mod.fill_price_by_category(frame)
    assert result["unit_price"].tolist() == [10.0, 20.0, 15.0, 50.0, 50.0]


def test_fill_price_by_category_leaves_input():
    frame = pd.DataFrame({"category": ["Toys", "Toys"], "unit_price": [10.0, np.nan]})
    mod.fill_price_by_category(frame)
    assert frame["unit_price"].isna().sum() == 1
