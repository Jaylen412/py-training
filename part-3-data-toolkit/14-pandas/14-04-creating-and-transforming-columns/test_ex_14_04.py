import importlib
import os

import pandas as pd
import pytest

mod = importlib.import_module(
    "sol_14_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_14_04"
)


@pytest.fixture
def sales():
    return pd.DataFrame({
        "date": ["2026-01-01", "2026-01-03", "2026-01-04", "2026-02-09"],
        "store": ["S1", "S2", "S9", "S1"],
        "units": [0, 6, 21, 100],
        "unit_price": [10.0, 2.5, 1.0, 0.5],
    })


def test_add_revenue(sales):
    assert mod.add_revenue(sales)["revenue"].tolist() == [0.0, 15.0, 21.0, 50.0]


def test_add_revenue_leaves_input(sales):
    mod.add_revenue(sales)
    assert "revenue" not in sales.columns


def test_add_city(sales):
    result = mod.add_city(sales, {"S1": "London", "S2": "Leeds"})
    assert result["city"].tolist() == ["London", "Leeds", "Unknown", "London"]


def test_add_city_empty_lookup(sales):
    assert set(mod.add_city(sales, {})["city"]) == {"Unknown"}


def test_add_size_band_edges(sales):
    assert mod.add_size_band(sales)["size"].astype(str).tolist() == ["small", "medium", "large", "large"]


def test_add_size_band_boundaries():
    frame = pd.DataFrame({"units": [5, 20]})
    assert mod.add_size_band(frame)["size"].astype(str).tolist() == ["small", "medium"]


def test_add_date_parts(sales):
    result = mod.add_date_parts(sales)
    assert pd.api.types.is_datetime64_any_dtype(result["date"])
    assert result["month"].tolist() == [1, 1, 1, 2]
    assert result["weekday"].tolist() == ["Thursday", "Saturday", "Sunday", "Monday"]
    assert result["is_weekend"].tolist() == [False, True, True, False]


def test_add_date_parts_leaves_input(sales):
    mod.add_date_parts(sales)
    assert sales.columns.tolist() == ["date", "store", "units", "unit_price"]
    assert sales["date"].iloc[0] == "2026-01-01"
