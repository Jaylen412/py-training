import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer, load_diabetes, make_classification
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

mod = importlib.import_module(
    "sol_20_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_20_05"
)


def test_majority_baseline_accuracy():
    assert mod.majority_baseline_accuracy(np.array([1, 1, 0]), np.array([1, 0, 0, 0])) == 0.25


def test_majority_baseline_accuracy_breast_cancer():
    data = load_breast_cancer()
    _, _, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
    assert mod.majority_baseline_accuracy(y_train, y_test) == pytest.approx(0.629, abs=1e-3)


def test_mean_baseline_mae():
    assert mod.mean_baseline_mae(np.array([10.0, 20.0]), np.array([15.0, 25.0])) == pytest.approx(5.0)


def test_mean_baseline_mae_diabetes():
    data = load_diabetes()
    _, _, y_train, y_test = train_test_split(data.data, data.target, test_size=0.25, random_state=42)
    assert mod.mean_baseline_mae(y_train, y_test) == pytest.approx(65.5, abs=0.1)


def test_beats_baseline_true():
    data = load_breast_cancer()
    parts = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
    assert mod.beats_baseline(DecisionTreeClassifier(max_depth=3, random_state=42), *parts) is True


def test_beats_baseline_false_on_imbalanced_noise():
    rng = np.random.default_rng(0)
    X = rng.normal(size=(600, 3))           # features carry no information
    y = (rng.random(600) < 0.1).astype(int)
    parts = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
    assert mod.beats_baseline(KNeighborsClassifier(), *parts) is False


def test_improvement():
    assert mod.improvement(65.5, 41.5) == pytest.approx(0.366, abs=1e-3)
    assert mod.improvement(10, 10) == 0


def test_improvement_worse_model_and_bad_baseline():
    assert mod.improvement(10, 15) == pytest.approx(-0.5)
    with pytest.raises(ValueError):
        mod.improvement(0, 1)
