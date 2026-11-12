import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_23_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_23_01"
)


def test_gini():
    assert mod.gini(["a", "a", "b", "b"]) == pytest.approx(0.5)
    assert mod.gini(["a"] * 9 + ["b"]) == pytest.approx(0.18)


def test_gini_pure_and_three_classes():
    assert mod.gini(["x", "x"]) == 0
    assert mod.gini([0, 1, 2]) == pytest.approx(2 / 3)


def test_entropy():
    assert mod.entropy(["a", "b"]) == pytest.approx(1.0)
    assert mod.entropy(["a"] * 9 + ["b"]) == pytest.approx(0.469, abs=1e-3)


def test_entropy_pure_is_positive_zero():
    result = mod.entropy(["a", "a", "a"])
    assert result == 0
    assert str(result) == "0.0"


def test_best_threshold_simple():
    assert mod.best_threshold([1, 2, 10, 11], ["a", "a", "b", "b"]) == (2, 0.0)


def test_best_threshold_iris():
    iris = load_iris()
    threshold, weighted = mod.best_threshold(iris.data[:, 2], iris.target)
    assert threshold == pytest.approx(1.9)
    assert weighted == pytest.approx(1 / 3)


def test_best_threshold_single_value_has_no_split():
    assert mod.best_threshold([5, 5, 5], ["a", "b", "a"]) is None


def test_depth_scores():
    data = load_breast_cancer()
    parts = train_test_split(data.data, data.target, test_size=0.25, random_state=42, stratify=data.target)
    scores = mod.depth_scores(*parts, [1, 3, None])
    assert scores == {1: (0.923, 0.923), 3: (0.977, 0.944), None: (1.0, 0.923)}
