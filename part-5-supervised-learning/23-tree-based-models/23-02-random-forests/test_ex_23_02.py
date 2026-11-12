import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_23_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_23_02"
)

CANCER = load_breast_cancer()
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(
    CANCER.data, CANCER.target, test_size=0.25, random_state=42, stratify=CANCER.target
)


def test_bagged_vote_matches_lesson():
    predictions = mod.bagged_vote(X_TRAIN, Y_TRAIN, X_TEST, 25, 42)
    assert predictions.shape == (len(Y_TEST),)
    assert np.mean(predictions == Y_TEST) == pytest.approx(0.951, abs=1e-3)


def test_bagged_vote_values_and_repeatable():
    first = mod.bagged_vote(X_TRAIN, Y_TRAIN, X_TEST, 5, 1)
    assert set(np.unique(first)) <= {0, 1}
    np.testing.assert_array_equal(first, mod.bagged_vote(X_TRAIN, Y_TRAIN, X_TEST, 5, 1))


def test_forest_scores():
    assert mod.forest_scores(X_TRAIN, X_TEST, Y_TRAIN, Y_TEST, [1, 25, 100]) == {1: 0.923, 25: 0.951, 100: 0.958}


def test_top_features():
    forest = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_TRAIN, Y_TRAIN)
    assert mod.top_features(forest, CANCER.feature_names, 3) == ["worst perimeter", "worst area", "worst concave points"]


def test_top_features_all():
    forest = RandomForestClassifier(n_estimators=10, random_state=0).fit(X_TRAIN, Y_TRAIN)
    assert len(mod.top_features(forest, CANCER.feature_names, 30)) == 30


def test_oob_accuracy():
    assert mod.oob_accuracy(X_TRAIN, Y_TRAIN) == 0.962
