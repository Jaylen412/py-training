"""Tests for the Part 5 project. Run from the repository root with:

    python -m pytest part-5-supervised-learning/project/starter

Set COURSE_SOLUTIONS=1 to run the same tests against the reference solution.
"""
import os
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import pytest  # noqa: E402
from sklearn.linear_model import LogisticRegression  # noqa: E402
from sklearn.pipeline import Pipeline  # noqa: E402

FOLDER = Path(__file__).resolve().parent.parent / (
    "solution" if os.environ.get("COURSE_SOLUTIONS") else "starter"
)
sys.path.insert(0, str(FOLDER))

import churn_model as project  # noqa: E402


@pytest.fixture(scope="module")
def churn():
    return project.load_churn()


@pytest.fixture(scope="module")
def split(churn):
    return project.split_data(churn)


@pytest.fixture(scope="module")
def fitted(split):
    X_train, _, y_train, _ = split
    return project.build_pipeline(LogisticRegression(max_iter=1000, C=0.1)).fit(X_train, y_train)


# Requirement 1: understand the data

def test_churn_summary(churn):
    summary = project.churn_summary(churn)
    assert summary["rows"] == 2000
    assert summary["churn_rate"] == 0.277
    assert summary["missing"] == {"monthly_charges": 52, "total_charges": 48, "payment_method": 79, "satisfaction": 115}
    assert summary["churn_by_contract"] == {"month-to-month": 0.421, "one-year": 0.144, "two-year": 0.053}


# Requirement 2: split before anything else

def test_split_data_shapes_and_columns(split):
    X_train, X_test, y_train, y_test = split
    assert X_train.shape == (1600, 9) and X_test.shape == (400, 9)
    assert "customer_id" not in X_train.columns and "churned" not in X_train.columns
    assert y_train.mean() == pytest.approx(y_test.mean(), abs=0.005)


def test_split_data_is_repeatable(churn, split):
    again = project.split_data(churn)
    pd.testing.assert_frame_equal(split[0], again[0])


# Requirement 3: preprocessing inside a pipeline

def test_build_pipeline_handles_gaps_and_unknowns(split):
    X_train, X_test, y_train, _ = split
    pipeline = project.build_pipeline(LogisticRegression(max_iter=1000))
    assert isinstance(pipeline, Pipeline) and list(pipeline.named_steps) == ["preprocess", "model"]
    pipeline.fit(X_train, y_train)
    odd = X_test.head(3).copy()
    odd["region"] = "Moon"
    assert pipeline.predict_proba(odd).shape == (3, 2)
    assert pipeline.named_steps["preprocess"].transform(X_test).shape == (400, 19)


# Requirement 4: compare at least three model families

def test_candidate_models_names():
    models = project.candidate_models()
    assert list(models) == ["baseline", "logistic regression", "random forest", "gradient boosting"]
    assert all(isinstance(model, Pipeline) for model in models.values())


def test_compare_models(split):
    X_train, _, y_train, _ = split
    table = project.compare_models(project.candidate_models(), X_train, y_train)
    assert table.index.tolist() == ["logistic regression", "random forest", "gradient boosting", "baseline"]
    assert table.loc["logistic regression", "mean_auc"] == 0.814
    assert table.loc["baseline", "mean_auc"] == 0.5
    assert list(table.columns) == ["mean_auc", "std_auc"]


# Requirement 5: tune with cross-validation

def test_tune_logistic(split):
    X_train, _, y_train, _ = split
    grid = project.tune_logistic(X_train, y_train)
    assert grid.best_params_ == {"model__C": 0.1}
    assert round(grid.best_score_, 3) == 0.815


# Requirement 6: evaluate once on the test set

def test_evaluate(fitted, split):
    _, X_test, _, y_test = split
    result = project.evaluate(fitted, X_test, y_test)
    assert result == {"accuracy": 0.785, "precision": 0.658, "recall": 0.468, "roc_auc": 0.837,
                      "tn": 262, "fp": 27, "fn": 59, "tp": 52}


def test_evaluate_lower_threshold_raises_recall(fitted, split):
    _, X_test, _, y_test = split
    result = project.evaluate(fitted, X_test, y_test, threshold=0.2)
    assert result["recall"] == 0.892 and result["fn"] == 12 and result["fp"] == 105
    assert all(type(result[key]) is int for key in ["tn", "fp", "fn", "tp"])


def test_best_threshold_simple():
    y = np.array([0, 0, 1, 1])
    probabilities = np.array([0.1, 0.4, 0.45, 0.9])
    assert project.best_threshold(y, probabilities, miss_cost=1, false_alarm_cost=1) == 0.45


def test_best_threshold_costly_misses_lower_it():
    y = np.array([0] * 8 + [1] * 2)
    probabilities = np.array([0.1, 0.1, 0.1, 0.2, 0.2, 0.3, 0.45, 0.5, 0.35, 0.8])
    cheap = project.best_threshold(y, probabilities, miss_cost=1, false_alarm_cost=1)
    costly = project.best_threshold(y, probabilities, miss_cost=20, false_alarm_cost=1)
    assert (cheap, costly) == (0.55, 0.35)


def test_best_threshold_on_churn(fitted, split):
    from sklearn.model_selection import cross_val_predict

    X_train, _, y_train, _ = split
    out_of_fold = cross_val_predict(fitted, X_train, y_train, cv=project.folds(), method="predict_proba")[:, 1]
    assert project.best_threshold(y_train, out_of_fold, miss_cost=5, false_alarm_cost=1) == 0.2


# Requirement 7: explain the model

def test_top_coefficients(fitted):
    top = project.top_coefficients(fitted, 3)
    assert top.index.tolist() == ["contract_month-to-month", "satisfaction", "contract_two-year"]
    assert top.iloc[0] > 0 and top.iloc[1] < 0
    assert list(top.abs().sort_values(ascending=False).index) == top.index.tolist()


def test_plot_evaluation_writes_png(fitted, split, tmp_path):
    _, X_test, _, y_test = split
    path = tmp_path / "nested" / "evaluation.png"
    project.plot_evaluation(fitted, X_test, y_test, path)
    assert path.exists() and path.stat().st_size > 5000
