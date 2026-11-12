import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_21_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_21_01"
)

DIABETES = load_diabetes(as_frame=True, scaled=False).frame
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(
    DIABETES.drop(columns="target"), DIABETES["target"], test_size=0.25, random_state=42
)


def test_fit_line_exact():
    slope, intercept = mod.fit_line(np.array([1, 2, 3]), np.array([5, 7, 9]))
    assert (slope, intercept) == (pytest.approx(2.0), pytest.approx(3.0))


def test_fit_line_diabetes_bmi():
    slope, intercept = mod.fit_line(X_TRAIN["bmi"], Y_TRAIN)
    assert slope == pytest.approx(10.512, abs=1e-3)
    assert intercept == pytest.approx(-125.177, abs=1e-3)


def test_coefficient_table():
    model = LinearRegression().fit(X_TRAIN, Y_TRAIN)
    table = mod.coefficient_table(model, X_TRAIN.columns)
    assert table.index[:3].tolist() == ["s5", "sex", "s4"]
    assert table["sex"] == pytest.approx(-23.067, abs=1e-3)


def test_coefficient_table_keeps_signs_and_length():
    model = LinearRegression().fit(np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]), np.array([-5.0, 1.0, -4.0]))
    table = mod.coefficient_table(model, ["a", "b"])
    assert table.index.tolist() == ["a", "b"]
    assert table["a"] == pytest.approx(-5.0)


def test_predict_from_dict():
    model = LinearRegression().fit(X_TRAIN[["bmi", "bp"]], Y_TRAIN)
    prediction = mod.predict_from_dict(model, {"bp": 90.0, "bmi": 30.0}, ["bmi", "bp"])
    assert prediction == pytest.approx(8.806 * 30 + 1.432 * 90 - 215.896, abs=0.1)
    assert isinstance(prediction, float)


def test_residuals():
    model = LinearRegression().fit(X_TRAIN, Y_TRAIN)
    result = mod.residuals(model, X_TEST, Y_TEST)
    assert result.shape == (len(Y_TEST),)
    assert result[0] == pytest.approx(81.1, abs=0.05)


def test_residuals_perfect_model():
    X = np.array([[1.0], [2.0]])
    model = LinearRegression().fit(X, np.array([3.0, 5.0]))
    np.testing.assert_allclose(mod.residuals(model, X, np.array([3.0, 5.0])), [0, 0], atol=1e-12)
