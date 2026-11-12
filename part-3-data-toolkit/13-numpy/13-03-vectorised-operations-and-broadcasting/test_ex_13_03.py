import importlib
import os

import numpy as np

mod = importlib.import_module(
    "sol_13_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_13_03"
)


def test_celsius_to_fahrenheit():
    np.testing.assert_allclose(mod.celsius_to_fahrenheit(np.array([0, 100])), [32, 212])


def test_celsius_to_fahrenheit_two_dimensional():
    result = mod.celsius_to_fahrenheit(np.array([[-40, 0], [37, 100]]))
    np.testing.assert_allclose(result, [[-40, 32], [98.6, 212]])


def test_apply_column_rates():
    result = mod.apply_column_rates(np.array([[1, 2], [3, 4]]), np.array([10, 0.5]))
    np.testing.assert_allclose(result, [[10, 1], [30, 2]])


def test_apply_column_rates_keeps_shape():
    table = np.ones((5, 3))
    assert mod.apply_column_rates(table, np.array([1, 2, 3])).shape == (5, 3)


def test_subtract_row_means():
    result = mod.subtract_row_means(np.array([[1, 3], [10, 20]]))
    np.testing.assert_allclose(result, [[-1, 1], [-5, 5]])


def test_subtract_row_means_rows_average_zero():
    rng = np.random.default_rng(0)
    result = mod.subtract_row_means(rng.random((4, 6)))
    np.testing.assert_allclose(result.mean(axis=1), np.zeros(4), atol=1e-12)


def test_standardise_columns():
    np.testing.assert_allclose(mod.standardise_columns(np.array([[1.0], [3.0]])), [[-1], [1]])


def test_standardise_columns_mean_zero_std_one():
    data = np.array([[150.0, 50.0], [160.0, 60.0], [170.0, 65.0], [180.0, 85.0]])
    result = mod.standardise_columns(data)
    np.testing.assert_allclose(result.mean(axis=0), [0, 0], atol=1e-12)
    np.testing.assert_allclose(result.std(axis=0), [1, 1])


def test_distances_from():
    result = mod.distances_from(np.array([0, 0]), np.array([[3, 4], [6, 8]]))
    np.testing.assert_allclose(result, [5, 10])


def test_distances_from_same_point():
    result = mod.distances_from(np.array([1, 1]), np.array([[1, 1], [4, 5]]))
    np.testing.assert_allclose(result, [0, 5])
