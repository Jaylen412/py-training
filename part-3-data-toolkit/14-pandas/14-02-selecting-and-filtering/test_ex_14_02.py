import importlib
import os
from pathlib import Path

import pandas as pd
import pytest

mod = importlib.import_module(
    "sol_14_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_14_02"
)

SALES_CSV = Path(__file__).resolve().parents[3] / "data" / "store_sales.csv"


@pytest.fixture
def sales():
    return pd.read_csv(SALES_CSV)


@pytest.fixture
def small():
    return pd.DataFrame({
        "store": ["S1", "S2", "S1", "S3"],
        "category": ["Toys", "Toys", "Clothing", "Groceries"],
        "units": [5, 40, 12, 40],
        "unit_price": [18.0, 17.5, 35.0, 6.5],
    })


def test_select_columns(small):
    result = mod.select_columns(small, ["units", "store"])
    assert result.columns.tolist() == ["units", "store"]
    assert len(result) == 4


def test_select_columns_single(small):
    assert isinstance(mod.select_columns(small, ["units"]), pd.DataFrame)


def test_rows_for_store(small):
    assert mod.rows_for_store(small, "S1")["units"].tolist() == [5, 12]


def test_rows_for_store_real_data(sales):
    result = mod.rows_for_store(sales, "S6")
    assert len(result) == 85
    assert set(result["store"]) == {"S6"}


def test_rows_for_store_missing(small):
    assert len(mod.rows_for_store(small, "S9")) == 0


def test_big_days(small):
    result = mod.big_days(small, 12)
    assert result["units"].tolist() == [40, 40, 12]


def test_big_days_real_data(sales):
    result = mod.big_days(sales, 60)
    assert result["units"].tolist() == [73, 67, 65, 64, 63, 61, 60]


def test_in_categories(small):
    result = mod.in_categories(small, ["Toys", "Groceries"])
    assert result["store"].tolist() == ["S1", "S2", "S3"]


def test_in_categories_none(small):
    assert len(mod.in_categories(small, [])) == 0


def test_first_row_value_after_filter(small):
    filtered = small[small["units"] > 10]  # first row has label 1
    assert mod.first_row_value(filtered, "store") == "S2"


def test_first_row_value_real_data(sales):
    assert mod.first_row_value(sales, "unit_price") == pytest.approx(137.28)
