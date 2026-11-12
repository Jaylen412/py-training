import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_23_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_23_03"
)

CANCER = load_breast_cancer()
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(
    CANCER.data, CANCER.target, test_size=0.25, random_state=42, stratify=CANCER.target
)

rng = np.random.default_rng(42)
X_WAVE = np.sort(rng.uniform(0, 1, 100)).reshape(-1, 1)
Y_WAVE = np.sin(2 * np.pi * X_WAVE[:, 0]) + rng.normal(0, 0.2, 100)


def test_boost_by_hand_matches_lesson():
    for trees, expected in [(1, 0.3130), (5, 0.0609), (50, 0.0093)]:
        predictions = mod.boost_by_hand(X_WAVE, Y_WAVE, trees, 0.3)
        assert np.mean((Y_WAVE - predictions) ** 2) == pytest.approx(expected, abs=1e-4)


def test_boost_by_hand_zero_trees_is_the_mean():
    predictions = mod.boost_by_hand(X_WAVE, Y_WAVE, 0, 0.3)
    np.testing.assert_allclose(predictions, np.full(100, Y_WAVE.mean()))


def test_best_tree_count():
    model = GradientBoostingClassifier(learning_rate=0.1, n_estimators=300, random_state=42).fit(X_TRAIN, Y_TRAIN)
    assert mod.best_tree_count(model, X_TEST, Y_TEST) == (74, 0.958)


def test_early_stopping_trees():
    assert mod.early_stopping_trees(X_TRAIN, Y_TRAIN) == 130


def test_compare_models():
    models = [
        GradientBoostingClassifier(random_state=42),
        RandomForestClassifier(n_estimators=200, random_state=42),
        HistGradientBoostingClassifier(random_state=42),
    ]
    assert mod.compare_models(models, X_TRAIN, X_TEST, Y_TRAIN, Y_TEST) == {
        "GradientBoostingClassifier": 0.958,
        "RandomForestClassifier": 0.958,
        "HistGradientBoostingClassifier": 0.972,
    }
