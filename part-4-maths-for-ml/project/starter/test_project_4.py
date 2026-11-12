"""Tests for the Part 4 project. Run from the repository root with:

    python -m pytest part-4-maths-for-ml/project/starter

Set COURSE_SOLUTIONS=1 to run the same tests against the reference solution.
"""
import os
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import numpy as np  # noqa: E402
import pytest  # noqa: E402
from sklearn.datasets import load_diabetes, make_regression  # noqa: E402

FOLDER = Path(__file__).resolve().parent.parent / (
    "solution" if os.environ.get("COURSE_SOLUTIONS") else "starter"
)
sys.path.insert(0, str(FOLDER))

import linear_regression_gd as project  # noqa: E402

Model = project.LinearRegressionGD


@pytest.fixture(scope="module")
def regression_data():
    X, y, coef = make_regression(n_samples=200, n_features=3, noise=10, coef=True, random_state=42)
    return X, y, coef


# Requirement 1: hyperparameters

def test_init_stores_hyperparameters():
    model = Model(learning_rate=0.05, epochs=20)
    assert (model.learning_rate, model.epochs) == (0.05, 20)
    assert not hasattr(model, "weights_")


def test_init_defaults():
    model = Model()
    assert (model.learning_rate, model.epochs) == (0.01, 1000)


# Requirement 2: fit

def test_fit_returns_self_and_learns(regression_data):
    X, y, _ = regression_data
    model = Model(learning_rate=0.1, epochs=500)
    assert model.fit(X, y) is model
    assert model.weights_.shape == (3,)
    assert isinstance(model.bias_, float)


def test_fit_matches_least_squares(regression_data):
    X, y, _ = regression_data
    model = Model(learning_rate=0.1, epochs=500).fit(X, y)
    bias, weights = project.fit_least_squares(X, y)
    np.testing.assert_allclose(model.weights_, weights, atol=1e-6)
    assert model.bias_ == pytest.approx(bias, abs=1e-6)


def test_fit_records_falling_loss(regression_data):
    X, y, _ = regression_data
    model = Model(learning_rate=0.1, epochs=300).fit(X, y)
    history = model.loss_history_
    assert len(history) == 300
    assert history[-1] < history[0]
    assert all(later <= earlier + 1e-9 for earlier, later in zip(history, history[1:]))


def test_fit_one_epoch_first_loss():
    X = np.array([[1.0], [2.0], [3.0]])
    y = np.array([2.0, 4.0, 6.0])
    model = Model(learning_rate=0.1, epochs=1).fit(X, y)
    # After one step from zero: w = 0.1 * 2 * mean(y * x) = 0.1 * 2 * 28/3, b = 0.1 * 2 * mean(y) = 0.8
    assert model.weights_[0] == pytest.approx(0.1 * 2 * 28 / 3)
    assert model.bias_ == pytest.approx(0.8)


@pytest.mark.parametrize("X, y", [
    (np.array([1.0, 2.0, 3.0]), np.array([1.0, 2.0, 3.0])),
    (np.ones((3, 2)), np.ones(4)),
    (np.ones((3, 2)), np.ones((3, 1))),
])
def test_fit_rejects_bad_shapes(X, y):
    with pytest.raises(ValueError):
        Model().fit(X, y)


# Requirement 3: predict

def test_predict(regression_data):
    X, y, _ = regression_data
    model = Model(learning_rate=0.1, epochs=500).fit(X, y)
    predictions = model.predict(X[:5])
    np.testing.assert_allclose(predictions, X[:5] @ model.weights_ + model.bias_)


def test_predict_before_fit():
    with pytest.raises(RuntimeError, match="fit"):
        Model().predict(np.ones((2, 3)))


def test_predict_wrong_number_of_columns(regression_data):
    X, y, _ = regression_data
    model = Model(learning_rate=0.1, epochs=10).fit(X, y)
    with pytest.raises(ValueError):
        model.predict(np.ones((2, 5)))


# Requirement 4: score

def test_score_make_regression(regression_data):
    X, y, _ = regression_data
    assert Model(learning_rate=0.1, epochs=500).fit(X, y).score(X, y) == pytest.approx(0.9893, abs=1e-4)


def test_score_perfect_fit():
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = 3 * X[:, 0] + 1
    assert Model(learning_rate=0.05, epochs=5000).fit(X, y).score(X, y) == pytest.approx(1.0, abs=1e-6)


# Requirement 5: helpers

def test_standardise():
    X = np.array([[1.0, 100.0], [3.0, 300.0]])
    scaled, means, stds = project.standardise(X)
    np.testing.assert_allclose(scaled, [[-1, -1], [1, 1]])
    np.testing.assert_allclose(means, [2, 200])
    np.testing.assert_allclose(stds, [1, 100])


def test_fit_least_squares_recovers_line():
    X = np.array([[0.0], [1.0], [2.0]])
    bias, weights = project.fit_least_squares(X, 2 * X[:, 0] + 5)
    assert bias == pytest.approx(5.0)
    np.testing.assert_allclose(weights, [2.0])


def test_diabetes_matches_least_squares():
    diabetes = load_diabetes()
    X, _, _ = project.standardise(diabetes.data)
    model = Model(learning_rate=0.1, epochs=5000).fit(X, diabetes.target)
    _, weights = project.fit_least_squares(X, diabetes.target)
    np.testing.assert_allclose(model.weights_, weights, atol=0.05)
    assert model.score(X, diabetes.target) == pytest.approx(0.5177, abs=1e-3)


# Requirement 6: the loss plot

def test_plot_loss(tmp_path):
    path = project.plot_loss([10.0, 5.0, 1.0], "Loss", tmp_path / "plots" / "loss.png")
    assert path.exists() and path.stat().st_size > 5_000
