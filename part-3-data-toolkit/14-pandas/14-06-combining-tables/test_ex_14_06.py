import importlib
import os
from pathlib import Path

import pandas as pd
import pytest

mod = importlib.import_module(
    "sol_14_06" if os.environ.get("COURSE_SOLUTIONS") else "ex_14_06"
)

DATA = Path(__file__).resolve().parents[3] / "data"


@pytest.fixture
def stores():
    return pd.DataFrame({
        "store": ["S1", "S2"],
        "city": ["London", "Leeds"],
        "region": ["South", "North"],
    })


@pytest.fixture
def sales():
    return pd.DataFrame({
        "store": ["S1", "S2", "S1", "S9"],
        "units": [2, 1, 3, 4],
        "unit_price": [10.0, 5.0, 10.0, 2.5],
    })


def test_add_store_details_keeps_every_row(sales, stores):
    result = mod.add_store_details(sales, stores)
    assert len(result) == 4
    assert result["city"].tolist()[:3] == ["London", "Leeds", "London"]
    assert pd.isna(result["city"].iloc[3])


def test_add_store_details_rejects_duplicate_stores(sales, stores):
    duplicated = pd.concat([stores, stores.iloc[[0]]])
    with pytest.raises(pd.errors.MergeError):
        mod.add_store_details(sales, duplicated)


def test_unmatched_keys(sales, stores):
    assert mod.unmatched_keys(sales, stores, "store") == ["S9"]
    assert mod.unmatched_keys(stores, sales, "store") == []


def test_unmatched_keys_course_data():
    sales = pd.read_csv(DATA / "store_sales.csv")
    stores = pd.read_csv(DATA / "stores.csv")
    assert mod.unmatched_keys(sales, stores, "store") == ["S6"]


def test_revenue_by_region(sales, stores):
    assert mod.revenue_by_region(sales, stores) == {"North": 5.0, "South": 50.0, "Unknown": 10.0}


def test_revenue_by_region_all_matched(stores):
    sales = pd.DataFrame({"store": ["S2"], "units": [3], "unit_price": [1.111]})
    assert mod.revenue_by_region(sales, stores) == {"North": 3.33}


def test_stack_tables():
    first = pd.DataFrame({"a": [1, 2]})
    second = pd.DataFrame({"a": [3]})
    result = mod.stack_tables([first, second])
    assert result["a"].tolist() == [1, 2, 3]
    assert result.index.tolist() == [0, 1, 2]


def test_stack_tables_single():
    assert len(mod.stack_tables([pd.DataFrame({"a": [1]})])) == 1
