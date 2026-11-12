import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer, make_moons
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_22_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_22_04"
)

POINTS = np.array([[1, 1], [2, 1], [1, 2], [5, 5], [6, 5], [5, 6]])
LABELS = np.array(["red", "red", "red", "blue", "blue", "blue"])


def test_knn_predict_one():
    assert mod.knn_predict_one(POINTS, LABELS, np.array([2, 2]), 3) == "red"
    assert mod.knn_predict_one(POINTS, LABELS, np.array([5.5, 5.5]), 3) == "blue"


def test_knn_predict_one_majority_beats_nearest():
    X = np.array([[0.0], [1.5], [1.6]])
    y = np.array(["a", "b", "b"])
    assert mod.knn_predict_one(X, y, np.array([0.1]), 1) == "a"
    assert mod.knn_predict_one(X, y, np.array([0.1]), 3) == "b"


def test_knn_predict_one_tie_goes_to_nearest():
    X = np.array([[0.0], [2.0]])
    y = np.array(["near", "far"])
    assert mod.knn_predict_one(X, y, np.array([0.5]), 2) == "near"


def test_best_k():
    X, y = make_moons(n_samples=300, noise=0.3, random_state=42)
    parts = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    assert mod.best_k(*parts, [1, 5, 15, 151]) == 5


def test_best_k_single_option():
    X, y = make_moons(n_samples=100, noise=0.3, random_state=0)
    parts = train_test_split(X, y, test_size=0.3, random_state=0)
    assert mod.best_k(*parts, [7]) == 7


def test_scaled_knn_accuracy():
    data = load_breast_cancer()
    parts = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
    assert mod.scaled_knn_accuracy(*parts) == 0.979


def test_distance_ratio():
    assert mod.distance_ratio(np.array([0, 0]), np.array([[3, 4], [6, 8]])) == pytest.approx(0.5)


def test_distance_ratio_grows_with_dimensions():
    rng = np.random.default_rng(42)
    low = rng.random((300, 2))
    high = rng.random((300, 500))
    assert mod.distance_ratio(low[0], low[1:]) < mod.distance_ratio(high[0], high[1:])
