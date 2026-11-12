import importlib
import os

import numpy as np

mod = importlib.import_module(
    "sol_13_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_13_02"
)

SCORES = np.array([
    [72, 88, 95],
    [64, 70, 81],
    [91, 85, 78],
    [55, 62, 90],
])


def test_column():
    np.testing.assert_array_equal(mod.column(SCORES, 0), [72, 64, 91, 55])


def test_column_is_one_dimensional():
    assert mod.column(SCORES, 2).shape == (4,)


def test_last_rows():
    np.testing.assert_array_equal(mod.last_rows(SCORES, 2), [[91, 85, 78], [55, 62, 90]])


def test_last_rows_zero():
    assert mod.last_rows(SCORES, 0).shape == (0, 3)


def test_values_between():
    np.testing.assert_array_equal(mod.values_between(np.array([5, 12, 8, 20]), 6, 15), [12, 8])


def test_values_between_inclusive_and_empty():
    np.testing.assert_array_equal(mod.values_between(np.array([6, 15, 16]), 6, 15), [6, 15])
    assert mod.values_between(np.array([1, 2]), 5, 9).size == 0


def test_replace_below():
    np.testing.assert_array_equal(mod.replace_below(np.array([3, 9, 1]), 5), [5, 9, 5])


def test_replace_below_leaves_original():
    original = np.array([3, 9, 1])
    mod.replace_below(original, 5)
    np.testing.assert_array_equal(original, [3, 9, 1])


def test_rows_where():
    np.testing.assert_array_equal(mod.rows_where(SCORES, 2, 85), [[72, 88, 95], [55, 62, 90]])


def test_rows_where_none_match():
    assert mod.rows_where(SCORES, 0, 100).shape == (0, 3)


def test_pick_rows():
    np.testing.assert_array_equal(mod.pick_rows(SCORES, [3, 0]), [[55, 62, 90], [72, 88, 95]])


def test_pick_rows_repeats():
    assert mod.pick_rows(SCORES, [1, 1, 1]).shape == (3, 3)
