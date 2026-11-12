"""Tests for the Part 3 project. Run from the repository root with:

    python -m pytest part-3-data-toolkit/project/starter

Set COURSE_SOLUTIONS=1 to run the same tests against the reference solution.
"""
import os
import re
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import pandas as pd  # noqa: E402
import pytest  # noqa: E402

PROJECT_FOLDER = Path(__file__).resolve().parent.parent / (
    "solution" if os.environ.get("COURSE_SOLUTIONS") else "starter"
)
sys.path.insert(0, str(PROJECT_FOLDER))

import eda  # noqa: E402

DATA = Path(__file__).resolve().parents[3] / "data"


@pytest.fixture(scope="module")
def raw_sales():
    return pd.read_csv(DATA / "store_sales.csv")


@pytest.fixture(scope="module")
def stores():
    return pd.read_csv(DATA / "stores.csv")


@pytest.fixture(scope="module")
def sales(raw_sales):
    return eda.add_features(eda.clean_sales(raw_sales))


# Requirement 1: wine

def test_load_wine_frame():
    wines = eda.load_wine_frame()
    assert wines.shape == (178, 15)
    assert sorted(wines["cultivar"].unique()) == ["class_0", "class_1", "class_2"]


def test_wine_summary():
    summary = eda.wine_summary(eda.load_wine_frame())
    assert summary.loc["class_0", "proline"] == pytest.approx(1095.0)
    assert summary.columns.tolist() == ["alcohol", "flavanoids", "color_intensity", "proline"]


def test_strongest_wine_correlations():
    result = eda.strongest_wine_correlations(eda.load_wine_frame(), count=2)
    assert result.index.tolist() == ["flavanoids", "od280/od315_of_diluted_wines"]


# Requirement 2: cleaning

def test_clean_sales_shape_and_quality(raw_sales):
    clean = eda.clean_sales(raw_sales)
    assert clean.shape == (468, 5)
    assert clean.isna().sum().sum() == 0
    assert clean.duplicated().sum() == 0
    assert sorted(clean["category"].unique()) == ["Clothing", "Electronics", "Groceries", "Toys"]
    assert pd.api.types.is_datetime64_any_dtype(clean["date"])


def test_clean_sales_fills_price_by_category(raw_sales):
    clean = eda.clean_sales(raw_sales)
    electronics = clean[clean["category"] == "Electronics"]["unit_price"]
    assert electronics.min() > 90  # an overall median (about 30) would show up here


def test_clean_sales_leaves_input(raw_sales):
    eda.clean_sales(raw_sales)
    assert raw_sales.shape == (486, 5)


# Requirement 3: features

def test_add_features(sales):
    assert {"revenue", "month", "weekday", "is_weekend"} <= set(sales.columns)
    first = sales.iloc[0]
    assert first["revenue"] == pytest.approx(first["units"] * first["unit_price"])
    assert sales["month"].unique().tolist() == [1, 2, 3]


# Requirement 4: summary numbers

def test_sales_summary(sales, stores):
    summary = eda.sales_summary(sales, stores)
    assert summary["total_revenue"] == pytest.approx(115246.15, abs=0.01)
    assert summary["unmatched_stores"] == ["S6"]
    assert summary["revenue_without_region"] == pytest.approx(11456.79, abs=0.01)
    assert summary["weekend_uplift"] == pytest.approx(0.585, abs=0.001)
    assert list(summary["revenue_by_category"])[0] == "Electronics"
    assert list(summary["revenue_by_store"])[0] == "S1"


# Requirement 5: figures

def test_make_figures(tmp_path, sales):
    paths = eda.make_figures(eda.load_wine_frame(), sales, tmp_path / "figures")
    assert len(paths) >= 6
    for path in paths:
        assert path.exists() and path.suffix == ".png" and path.stat().st_size > 5_000


# Requirement 6: the report

def test_report_has_five_numbered_findings():
    report = (PROJECT_FOLDER / "REPORT.md").read_text()
    findings_section = report.split("## Findings", 1)[1].split("\n## ", 1)[0]
    findings = re.findall(r"^\d+\. .+$", findings_section, flags=re.MULTILINE)
    assert len(findings) >= 5
    for finding in findings:
        assert re.search(r"\d", finding[3:]), f"finding without a number: {finding}"
        assert "TODO" not in finding


def test_report_figures_exist():
    report = (PROJECT_FOLDER / "REPORT.md").read_text()
    images = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", report)
    assert len(images) >= 6
    for image in images:
        assert (PROJECT_FOLDER / image).exists(), f"missing figure: {image}"
