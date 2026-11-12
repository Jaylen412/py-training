import importlib
import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from sklearn.compose import ColumnTransformer

mod = importlib.import_module(
    "sol_24_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_24_01"
)

DATA = Path(__file__).resolve().parents[3] / "data"
CHURN = pd.read_csv(DATA / "customer_churn.csv")
NUMERIC = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
NOMINAL = ["contract", "payment_method", "internet_service", "region"]
ORDERED = ["satisfaction"]


def test_missing_report_churn():
    report = mod.missing_report(CHURN)
    assert report.index.tolist() == ["satisfaction", "payment_method", "monthly_charges", "total_charges"]
    assert report.tolist() == [115, 79, 52, 48]


def test_missing_report_no_gaps():
    assert len(mod.missing_report(pd.DataFrame({"a": [1, 2]}))) == 0


def test_split_churn():
    X_train, X_test, y_train, y_test = mod.split_churn(CHURN)
    assert X_train.shape == (1600, 9) and X_test.shape == (400, 9)
    assert "customer_id" not in X_train.columns and "churned" not in X_train.columns
    assert y_train.mean() == pytest.approx(y_test.mean(), abs=0.01)


def test_split_churn_test_size():
    X_train, X_test, _, _ = mod.split_churn(CHURN, test_size=0.5)
    assert len(X_train) == len(X_test) == 1000


def test_column_groups():
    X = CHURN.drop(columns=["customer_id", "churned"])
    numeric, text = mod.column_groups(X)
    assert numeric == NUMERIC
    assert text == NOMINAL + ORDERED


def test_column_groups_all_text():
    assert mod.column_groups(pd.DataFrame({"a": ["x"], "b": ["y"]})) == ([], ["a", "b"])


def test_build_preprocessor_output():
    X_train, X_test, _, _ = mod.split_churn(CHURN)
    preprocess = mod.build_preprocessor(NUMERIC, NOMINAL, ORDERED, ["low", "medium", "high"])
    assert isinstance(preprocess, ColumnTransformer)
    train_ready = preprocess.fit_transform(X_train)
    test_ready = preprocess.transform(X_test)
    assert train_ready.shape == (1600, 19) and test_ready.shape == (400, 19)
    assert not np.isnan(train_ready).any() and not np.isnan(test_ready).any()
    np.testing.assert_allclose(train_ready[:, :4].mean(axis=0), 0, atol=1e-9)


def test_build_preprocessor_order_and_unknown():
    preprocess = mod.build_preprocessor(NUMERIC, NOMINAL, ORDERED, ["low", "medium", "high"])
    X_train, _, _, _ = mod.split_churn(CHURN)
    preprocess.fit(X_train)
    odd = X_train.head(3).copy()
    odd["satisfaction"] = ["low", "medium", "high"]
    odd["region"] = "Moon"
    result = preprocess.transform(odd)
    np.testing.assert_array_equal(result[:, -1], [0, 1, 2])
    region_columns = [i for i, name in enumerate(preprocess.get_feature_names_out()) if "region" in name]
    assert result[:, region_columns].sum() == 0
