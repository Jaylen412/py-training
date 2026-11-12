import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_21_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_21_02"
)

DATA = load_diabetes()
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(DATA.data, DATA.target, test_size=0.25, random_state=42)
MODEL = LinearRegression().fit(X_TRAIN, Y_TRAIN)
PREDICTIONS = MODEL.predict(X_TEST)


def test_mae_matches_sklearn():
    assert mod.mae(Y_TEST, PREDICTIONS) == pytest.approx(mean_absolute_error(Y_TEST, PREDICTIONS))


def test_mae_simple():
    assert mod.mae(np.array([100.0] * 4), np.array([100, 100, 100, 140.0])) == 10.0


def test_rmse_matches_sklearn():
    assert mod.rmse(Y_TEST, PREDICTIONS) == pytest.approx(root_mean_squared_error(Y_TEST, PREDICTIONS))


def test_rmse_punishes_one_big_error():
    assert mod.rmse(np.array([100.0] * 4), np.array([100, 100, 100, 140.0])) == pytest.approx(20.0)


def test_r_squared_matches_sklearn():
    assert mod.r_squared(Y_TEST, PREDICTIONS) == pytest.approx(r2_score(Y_TEST, PREDICTIONS))


def test_r_squared_edge_cases():
    actual = np.array([1.0, 2.0, 3.0])
    assert mod.r_squared(actual, actual) == pytest.approx(1.0)
    assert mod.r_squared(actual, np.full(3, 2.0)) == pytest.approx(0.0)
    assert mod.r_squared(actual, np.array([3.0, 2.0, 1.0])) < 0


def test_evaluate():
    assert mod.evaluate(MODEL, X_TEST, Y_TEST) == {"mae": 41.549, "rmse": 53.37, "r2": 0.485}


def test_pick_metric():
    assert mod.pick_metric(True) == "rmse"
    assert mod.pick_metric(False) == "mae"
