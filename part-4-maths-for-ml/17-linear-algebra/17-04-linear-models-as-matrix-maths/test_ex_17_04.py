import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_17_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_17_04"
)


def test_predict():
    np.testing.assert_allclose(mod.predict(np.array([[1, 2]]), np.array([3, 4]), 5), [16])


def test_predict_houses():
    X = np.array([[120.0, 3.0, 15.0], [80.0, 2.0, 40.0]])
    np.testing.assert_allclose(mod.predict(X, np.array([2.0, 10.0, -0.5]), 50.0), [312.5, 210.0])


def test_add_bias_column():
    np.testing.assert_array_equal(mod.add_bias_column(np.array([[2, 3]])), [[1, 2, 3]])


def test_add_bias_column_shape():
    result = mod.add_bias_column(np.zeros((5, 3)))
    assert result.shape == (5, 4)
    np.testing.assert_array_equal(result[:, 0], np.ones(5))


def test_solve_system():
    np.testing.assert_allclose(mod.solve_system(np.array([[2, 1], [1, 3]]), np.array([5, 10])), [1, 3])


def test_solve_system_three_unknowns():
    A = np.array([[1.0, 1.0, 1.0], [0.0, 2.0, 5.0], [2.0, 5.0, -1.0]])
    b = np.array([6.0, -4.0, 27.0])
    np.testing.assert_allclose(A @ mod.solve_system(A, b), b)


def test_solve_system_singular():
    with pytest.raises(ValueError):
        mod.solve_system(np.array([[1.0, 2.0], [2.0, 4.0]]), np.array([1.0, 2.0]))


def test_fit_least_squares_exact_data():
    X = np.array([[1.0], [2.0], [3.0], [4.0]])
    y = 3 * X[:, 0] + 7
    bias, weights = mod.fit_least_squares(X, y)
    assert bias == pytest.approx(7.0)
    np.testing.assert_allclose(weights, [3.0])


def test_fit_least_squares_noisy_data():
    rng = np.random.default_rng(42)
    X = rng.uniform(0, 10, size=(500, 2))
    y = X @ np.array([1.5, -2.0]) + 4 + rng.normal(0, 0.5, size=500)
    bias, weights = mod.fit_least_squares(X, y)
    assert isinstance(bias, float)
    assert bias == pytest.approx(4.0, abs=0.2)
    np.testing.assert_allclose(weights, [1.5, -2.0], atol=0.05)
