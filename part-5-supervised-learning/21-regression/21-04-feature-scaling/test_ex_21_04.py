import importlib
import os

import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

mod = importlib.import_module(
    "sol_21_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_21_04"
)

WINE = load_wine(as_frame=True)
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(
    WINE.data, WINE.target, test_size=0.25, random_state=42, stratify=WINE.target
)


def test_standardise_training_statistics():
    train, test, scaler = mod.standardise(X_TRAIN, X_TEST)
    np.testing.assert_allclose(train.mean(axis=0), 0, atol=1e-10)
    np.testing.assert_allclose(train.std(axis=0), 1)
    np.testing.assert_allclose(scaler.mean_, X_TRAIN.mean().to_numpy())


def test_standardise_test_uses_training_stats():
    train, test, _ = mod.standardise(np.array([[0.0], [2.0]]), np.array([[4.0]]))
    np.testing.assert_allclose(test, [[3.0]])


def test_min_max_scale():
    train, test, _ = mod.min_max_scale(np.array([[0.0], [10.0]]), np.array([[5.0], [20.0]]))
    np.testing.assert_allclose(train, [[0.0], [1.0]])
    np.testing.assert_allclose(test, [[0.5], [2.0]])


def test_min_max_scale_wine_range():
    train, _, _ = mod.min_max_scale(X_TRAIN, X_TEST)
    assert train.min() == 0 and train.max() == 1


def test_knn_accuracy_unscaled_and_scaled():
    assert mod.knn_accuracy(X_TRAIN, X_TEST, Y_TRAIN, Y_TEST) == 0.778
    assert mod.knn_accuracy(X_TRAIN, X_TEST, Y_TRAIN, Y_TEST, StandardScaler()) == 0.933
    assert mod.knn_accuracy(X_TRAIN, X_TEST, Y_TRAIN, Y_TEST, MinMaxScaler()) == 0.978


def test_widest_feature():
    assert mod.widest_feature(X_TRAIN) == "proline"


def test_widest_feature_simple():
    frame = pd.DataFrame({"a": [0, 100], "b": [-500, 500], "c": [1, 2]})
    assert mod.widest_feature(frame) == "b"
