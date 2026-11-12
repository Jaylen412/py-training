import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_20_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_20_04"
)

rng = np.random.default_rng(42)
X_POINTS = np.sort(rng.uniform(0, 1, 30))
Y_POINTS = np.sin(2 * np.pi * X_POINTS) + rng.normal(0, 0.25, size=30)
X_TEST = np.sort(rng.uniform(0, 1, 30))
Y_TEST = np.sin(2 * np.pi * X_TEST) + rng.normal(0, 0.25, size=30)


def test_polynomial_errors():
    train, test = mod.polynomial_errors(X_POINTS, Y_POINTS, X_TEST, Y_TEST, 3)
    assert train == pytest.approx(0.039, abs=1e-3)
    assert test == pytest.approx(0.066, abs=1e-3)


def test_polynomial_errors_overfit():
    train, test = mod.polynomial_errors(X_POINTS, Y_POINTS, X_TEST, Y_TEST, 15)
    assert train < 0.02 and test > 0.5


def test_best_degree():
    assert mod.best_degree(X_POINTS, Y_POINTS, X_TEST, Y_TEST, list(range(1, 16))) == 5


def test_best_degree_restricted_choice():
    assert mod.best_degree(X_POINTS, Y_POINTS, X_TEST, Y_TEST, [1, 15]) == 1


def test_depth_scores():
    data = load_breast_cancer()
    parts = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
    scores = mod.depth_scores(*parts, [1, 3, None])
    assert scores[1] == (0.923, 0.923)
    assert scores[3] == (0.977, 0.944)
    assert scores[None][0] == 1.0


@pytest.mark.parametrize("train, test, expected", [
    (0.80, 0.78, "underfitting"),
    (1.00, 0.80, "overfitting"),
    (0.95, 0.93, "good fit"),
    (0.95, 0.90, "good fit"),
])
def test_diagnose(train, test, expected):
    assert mod.diagnose(train, test) == expected


def test_diagnose_custom_thresholds():
    assert mod.diagnose(0.85, 0.84, good_score=0.8) == "good fit"
    assert mod.diagnose(0.95, 0.92, max_gap=0.01) == "overfitting"
