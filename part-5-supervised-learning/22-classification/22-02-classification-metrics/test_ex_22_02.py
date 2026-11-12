import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

mod = importlib.import_module(
    "sol_22_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_22_02"
)


@pytest.fixture(scope="module")
def predictions():
    cancer = load_breast_cancer()
    y = (cancer.target == 0).astype(int)
    X_train, X_test, y_train, y_test = train_test_split(cancer.data, y, test_size=0.25, random_state=42, stratify=y)
    scaler = StandardScaler().fit(X_train)
    model = LogisticRegression(max_iter=1000).fit(scaler.transform(X_train), y_train)
    return y_test, model.predict(scaler.transform(X_test))


def test_confusion_counts_small():
    assert mod.confusion_counts([0, 1, 1, 0], [0, 1, 0, 1]) == {"tn": 1, "fp": 1, "fn": 1, "tp": 1}


def test_confusion_counts_breast_cancer(predictions):
    assert mod.confusion_counts(*predictions) == {"tn": 89, "fp": 1, "fn": 4, "tp": 49}


def test_precision_recall_f1_match_sklearn(predictions):
    counts = mod.confusion_counts(*predictions)
    assert mod.precision(counts) == pytest.approx(precision_score(*predictions))
    assert mod.recall(counts) == pytest.approx(recall_score(*predictions))
    assert mod.f1(counts) == pytest.approx(f1_score(*predictions))


def test_metrics_with_no_positive_predictions():
    counts = mod.confusion_counts([0, 0, 1], [0, 0, 0])
    assert mod.precision(counts) == 0.0
    assert mod.recall(counts) == 0.0
    assert mod.f1(counts) == 0.0


def test_recall_with_no_actual_positives():
    assert mod.recall(mod.confusion_counts([0, 0], [0, 1])) == 0.0


def test_metric_summary(predictions):
    assert mod.metric_summary(*predictions) == {"accuracy": 0.965, "precision": 0.98, "recall": 0.925, "f1": 0.951}


def test_metric_summary_accuracy_matches(predictions):
    assert mod.metric_summary(*predictions)["accuracy"] == round(accuracy_score(*predictions), 3)
