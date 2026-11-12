import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

mod = importlib.import_module(
    "sol_21_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_21_03"
)

DATA = load_diabetes()
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(DATA.data, DATA.target, test_size=0.25, random_state=42)
SCALER = StandardScaler().fit(X_TRAIN)
X_TRAIN_S, X_TEST_S = SCALER.transform(X_TRAIN), SCALER.transform(X_TEST)


@pytest.mark.parametrize("n_features, degree, expected", [(2, 2, 5), (1, 3, 3), (10, 3, 285), (3, 1, 3)])
def test_polynomial_feature_count(n_features, degree, expected):
    assert mod.polynomial_feature_count(n_features, degree) == expected


def test_fit_polynomial_recovers_curve():
    rng = np.random.default_rng(42)
    x = rng.uniform(0, 10, 200)
    y = 0.5 * x ** 2 - 2 * x + rng.normal(0, 2, 200)
    model, poly = mod.fit_polynomial(x, y, 2)
    np.testing.assert_allclose(model.coef_, [-1.906, 0.504], atol=1e-3)
    prediction = model.predict(poly.transform(np.array([[4.0]])))[0]
    assert prediction == pytest.approx(0.5 * 16 - 8, abs=1.0)


def test_fit_polynomial_degree_one_is_a_line():
    model, poly = mod.fit_polynomial(np.array([0.0, 1.0, 2.0]), np.array([1.0, 3.0, 5.0]), 1)
    assert model.coef_ == pytest.approx([2.0])


def test_ridge_test_scores_on_polynomial_features():
    poly = PolynomialFeatures(degree=3, include_bias=False).fit(X_TRAIN_S)
    scores = mod.ridge_test_scores(poly.transform(X_TRAIN_S), poly.transform(X_TEST_S), Y_TRAIN, Y_TEST, [0.1, 1000])
    assert scores == {0.1: -2.177, 1000: 0.395}


def test_ridge_test_scores_small_alpha_matches_linear():
    scores = mod.ridge_test_scores(X_TRAIN_S, X_TEST_S, Y_TRAIN, Y_TEST, [1e-8])
    assert scores[1e-8] == pytest.approx(0.485, abs=1e-3)


def test_lasso_kept_features():
    kept = mod.lasso_kept_features(X_TRAIN_S, Y_TRAIN, DATA.feature_names, 1.0)
    assert kept == ["age", "sex", "bmi", "bp", "s1", "s3", "s4", "s5", "s6"]


def test_lasso_kept_features_strong_alpha():
    kept = mod.lasso_kept_features(X_TRAIN_S, Y_TRAIN, DATA.feature_names, 20)
    assert len(kept) == 3
    assert "bmi" in kept
