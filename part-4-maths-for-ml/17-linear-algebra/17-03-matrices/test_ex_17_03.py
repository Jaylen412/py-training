import importlib
import os

import numpy as np
from sklearn.datasets import load_iris

mod = importlib.import_module(
    "sol_17_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_17_03"
)

X = load_iris().data


def test_result_shape():
    assert mod.result_shape((150, 4), (4, 2)) == (150, 2)
    assert mod.result_shape((3, 2), (2, 3)) == (3, 3)


def test_result_shape_incompatible():
    assert mod.result_shape((150, 4), (2, 4)) is None


def test_weighted_scores():
    np.testing.assert_array_equal(mod.weighted_scores(np.array([[1, 2], [3, 4]]), np.array([10, 1])), [12, 34])


def test_weighted_scores_iris():
    scores = mod.weighted_scores(X, np.array([0.5, -0.2, 1.0, 0.3]))
    assert scores.shape == (150,)
    assert round(float(scores[0]), 2) == 3.31


def test_column_means_by_matmul():
    np.testing.assert_allclose(mod.column_means_by_matmul(np.array([[1, 10], [3, 20]])), [2, 15])


def test_column_means_by_matmul_iris():
    np.testing.assert_allclose(mod.column_means_by_matmul(X), X.mean(axis=0))


def test_gram_matrix():
    np.testing.assert_array_equal(mod.gram_matrix(np.array([[1, 2], [3, 4]])), [[10, 14], [14, 20]])


def test_gram_matrix_iris_shape():
    assert mod.gram_matrix(X).shape == (4, 4)


def test_is_symmetric():
    assert mod.is_symmetric(np.array([[1, 2], [2, 5]])) is True
    assert mod.is_symmetric(np.array([[1, 2], [3, 5]])) is False


def test_is_symmetric_non_square_and_gram():
    assert mod.is_symmetric(np.ones((2, 3))) is False
    assert mod.is_symmetric(X.T @ X) is True
