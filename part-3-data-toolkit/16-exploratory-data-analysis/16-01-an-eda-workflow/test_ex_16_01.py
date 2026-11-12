import importlib
import os

import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import load_breast_cancer

mod = importlib.import_module(
    "sol_16_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_16_01"
)


@pytest.fixture
def messy():
    return pd.DataFrame({
        "a": [1, 1, np.nan, 4],
        "b": ["x", "x", None, None],
        "c": [1, 1, 2, 3],
    })


def test_overview(messy):
    assert mod.overview(messy) == {"rows": 4, "columns": 3, "missing": 3, "duplicates": 1}


def test_overview_breast_cancer():
    frame = load_breast_cancer(as_frame=True).frame
    assert mod.overview(frame) == {"rows": 569, "columns": 31, "missing": 0, "duplicates": 0}


def test_missing_report(messy):
    report = mod.missing_report(messy)
    assert report.index.tolist() == ["b", "a"]
    assert report["count"].tolist() == [2, 1]
    assert report["percent"].tolist() == [50.0, 25.0]


def test_missing_report_nothing_missing():
    assert len(mod.missing_report(pd.DataFrame({"a": [1, 2]}))) == 0


def test_class_balance():
    labels = pd.Series(["benign"] * 5 + ["malignant"] * 3)
    assert mod.class_balance(labels) == {"benign": 0.625, "malignant": 0.375}


def test_class_balance_breast_cancer():
    target = load_breast_cancer(as_frame=True).frame["target"]
    assert mod.class_balance(target) == {1: 0.627, 0: 0.373}


def test_median_by_group():
    frame = pd.DataFrame({"g": ["a", "a", "b"], "x": [1, 3, 10], "y": [0, 4, 5]})
    result = mod.median_by_group(frame, "g", ["x", "y"])
    assert result.loc["a", "x"] == 2 and result.loc["a", "y"] == 2 and result.loc["b", "x"] == 10


def test_numbered_findings():
    assert mod.numbered_findings(["a", "b"]) == "1. a\n2. b"


def test_numbered_findings_empty():
    assert mod.numbered_findings([]) == ""
