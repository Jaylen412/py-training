import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier

mod = importlib.import_module(
    "sol_20_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_20_03"
)

DATA = load_breast_cancer()
X, y = DATA.data, DATA.target


def test_split_data_shapes_and_order():
    X_train, X_test, y_train, y_test = mod.split_data(X, y)
    assert X_train.shape == (426, 30) and X_test.shape == (143, 30)
    assert y_train.shape == (426,) and y_test.shape == (143,)


def test_split_data_is_stratified_and_repeatable():
    _, X_test, y_train, y_test = mod.split_data(X, y, test_size=0.1, seed=3)
    assert abs(y_test.mean() - y.mean()) < 0.01
    np.testing.assert_array_equal(X_test, mod.split_data(X, y, test_size=0.1, seed=3)[1])


def test_train_and_test_scores():
    train, test = mod.train_and_test_scores(DecisionTreeClassifier(random_state=42), X, y)
    assert train == 1.0
    assert 0.85 < test < 1.0


def test_train_and_test_scores_shallow_tree_gap_is_smaller():
    train, test = mod.train_and_test_scores(DecisionTreeClassifier(max_depth=1, random_state=42), X, y)
    assert abs(train - test) < 0.05


def test_scale_without_leakage():
    X_train = np.array([[1.0, 10.0], [3.0, 30.0]])
    X_test = np.array([[5.0, 50.0]])
    scaled_train, scaled_test = mod.scale_without_leakage(X_train, X_test)
    np.testing.assert_allclose(scaled_train, [[-1, -1], [1, 1]])
    np.testing.assert_allclose(scaled_test, [[3, 3]])


def test_scale_without_leakage_uses_training_stats_only():
    X_train, X_test, _, _ = mod.split_data(X, y)
    scaled_train, scaled_test = mod.scale_without_leakage(X_train, X_test)
    np.testing.assert_allclose(scaled_train.mean(axis=0), 0, atol=1e-10)
    assert np.abs(scaled_test.mean(axis=0)).max() > 0.01


def test_score_range_over_splits():
    low, high = mod.score_range_over_splits(DecisionTreeClassifier(random_state=42), X, y, [0, 1, 2, 3, 4])
    assert 0.8 < low < high <= 1.0


def test_score_range_over_splits_single_seed():
    low, high = mod.score_range_over_splits(DecisionTreeClassifier(random_state=42), X, y, [7])
    assert low == high
