import importlib
import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

mod = importlib.import_module(
    "sol_14_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_14_03"
)

SALES_CSV = Path(__file__).resolve().parents[3] / "data" / "store_sales.csv"


@pytest.fixture
def messy():
    return pd.DataFrame({
        "store": ["S1", "S1", "S2", "S3"],
        "units": [5.0, 5.0, np.nan, 8.0],
        "unit_price": [10.0, 10.0, 30.0, np.nan],
    })


def test_clean_categories():
    result = mod.clean_categories(pd.Series([" electronics", "CLOTHING", "groceries "]))
    assert result.tolist() == ["Electronics", "Clothing", "Groceries"]


def test_clean_categories_leaves_input():
    original = pd.Series([" toys"])
    mod.clean_categories(original)
    assert original.tolist() == [" toys"]


def test_drop_missing(messy):
    assert mod.drop_missing(messy, ["units"])["store"].tolist() == ["S1", "S1", "S3"]
    assert len(mod.drop_missing(messy, ["units", "unit_price"])) == 2


def test_drop_missing_leaves_input(messy):
    mod.drop_missing(messy, ["units"])
    assert len(messy) == 4


def test_fill_with_median(messy):
    result = mod.fill_with_median(messy, "unit_price")
    assert result["unit_price"].tolist() == [10.0, 10.0, 30.0, 10.0]
    assert result["units"].isna().sum() == 1


def test_fill_with_median_leaves_input(messy):
    mod.fill_with_median(messy, "units")
    assert messy["units"].isna().sum() == 1


def test_remove_duplicates(messy):
    result = mod.remove_duplicates(messy)
    assert len(result) == 3
    assert result.index.tolist() == [0, 1, 2]


def test_clean_sales_real_data():
    result = mod.clean_sales(pd.read_csv(SALES_CSV))
    assert result.shape == (468, 5)
    assert result.isna().sum().sum() == 0
    assert result.duplicated().sum() == 0
    assert sorted(result["category"].unique()) == ["Clothing", "Electronics", "Groceries", "Toys"]
    assert pd.api.types.is_datetime64_any_dtype(result["date"])
    assert result.index.tolist() == list(range(468))


def test_clean_sales_leaves_input():
    raw = pd.read_csv(SALES_CSV)
    mod.clean_sales(raw)
    assert raw.shape == (486, 5)
    assert raw["date"].dtype != "datetime64[us]"
