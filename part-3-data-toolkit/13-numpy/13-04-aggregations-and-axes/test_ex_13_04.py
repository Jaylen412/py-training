import importlib
import os

import numpy as np

mod = importlib.import_module(
    "sol_13_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_13_04"
)

SALES = np.array([
    [120, 95, 140],
    [130, 80, 150],
    [110, 105, 160],
    [125, 90, 155],
])


def test_column_means():
    np.testing.assert_allclose(mod.column_means(SALES), [121.25, 92.5, 151.25])


def test_column_means_single_row():
    np.testing.assert_allclose(mod.column_means(np.array([[1, 2, 3]])), [1, 2, 3])


def test_row_totals():
    np.testing.assert_array_equal(mod.row_totals(SALES), [355, 360, 375, 370])


def test_row_totals_shape():
    assert mod.row_totals(np.ones((7, 2))).shape == (7,)


def test_best_column():
    assert mod.best_column(SALES) == 2
    assert mod.best_column(np.array([[1, 10], [3, 20]])) == 1


def test_best_column_returns_int():
    assert type(mod.best_column(SALES)) is int


def test_row_shares():
    np.testing.assert_allclose(mod.row_shares(np.array([[1, 3], [2, 2]])), [[0.25, 0.75], [0.5, 0.5]])


def test_row_shares_rows_sum_to_one():
    np.testing.assert_allclose(mod.row_shares(SALES).sum(axis=1), np.ones(4))


def test_count_above():
    np.testing.assert_array_equal(mod.count_above(SALES, 100), [4, 1, 4])


def test_count_above_none():
    np.testing.assert_array_equal(mod.count_above(SALES, 1000), [0, 0, 0])


def test_to_column():
    result = mod.to_column(np.array([1, 2, 3]))
    assert result.shape == (3, 1)
    np.testing.assert_array_equal(result.ravel(), [1, 2, 3])


def test_to_column_empty():
    assert mod.to_column(np.array([])).shape == (0, 1)
