import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

mod = importlib.import_module(
    "sol_22_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_22_03"
)


@pytest.fixture(scope="module")
def scored():
    cancer = load_breast_cancer()
    y = (cancer.target == 0).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler().fit(X_train)
    model = LogisticRegression(C=0.05, max_iter=1000).fit(scaler.transform(X_train), y_train)
    return y_test, model.predict_proba(scaler.transform(X_test))[:, 1]


THRESHOLDS = np.linspace(0.01, 0.99, 99)


def test_precision_recall_at(scored):
    precision, recall = mod.precision_recall_at(*scored, 0.5)
    assert (round(precision, 3), round(recall, 3)) == (1.0, 0.943)
    precision, recall = mod.precision_recall_at(*scored, 0.1)
    assert (round(precision, 3), round(recall, 3)) == (0.768, 1.0)


def test_precision_recall_at_nothing_flagged():
    assert mod.precision_recall_at(np.array([0, 1]), np.array([0.1, 0.2]), 0.9) == (0.0, 0.0)


def test_lowest_cost_threshold(scored):
    assert mod.lowest_cost_threshold(*scored, 20, 1, THRESHOLDS) == pytest.approx(0.2)


def test_lowest_cost_threshold_simple():
    y = np.array([0, 0, 1])
    probabilities = np.array([0.1, 0.6, 0.7])
    assert mod.lowest_cost_threshold(y, probabilities, 1, 1, np.array([0.5, 0.65, 0.9])) == 0.65


def test_threshold_for_recall(scored):
    result = mod.threshold_for_recall(*scored, 1.0, THRESHOLDS)
    assert mod.precision_recall_at(*scored, result)[1] == 1.0
    assert mod.precision_recall_at(*scored, result + 0.01)[1] < 1.0


def test_threshold_for_recall_impossible():
    assert mod.threshold_for_recall(np.array([1]), np.array([0.2]), 1.0, np.array([0.5, 0.9])) is None


def test_auc(scored):
    assert mod.auc(*scored) == pytest.approx(0.9985, abs=1e-4)


def test_auc_perfect_and_reversed():
    y = np.array([0, 0, 1, 1])
    assert mod.auc(y, np.array([0.1, 0.2, 0.8, 0.9])) == 1.0
    assert mod.auc(y, np.array([0.9, 0.8, 0.2, 0.1])) == 0.0
