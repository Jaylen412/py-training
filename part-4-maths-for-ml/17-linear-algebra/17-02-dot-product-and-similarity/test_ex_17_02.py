import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_17_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_17_02"
)


def test_cosine_similarity():
    assert mod.cosine_similarity(np.array([1, 0]), np.array([0, 5])) == pytest.approx(0.0)
    assert mod.cosine_similarity(np.array([3, 4]), np.array([30, 40])) == pytest.approx(1.0)
    assert mod.cosine_similarity(np.array([1, 2]), np.array([-1, -2])) == pytest.approx(-1.0)


def test_cosine_similarity_documents():
    football = np.array([3, 2, 4, 0, 0])
    match_report = np.array([6, 5, 7, 0, 1])
    assert mod.cosine_similarity(football, match_report) == pytest.approx(0.987, abs=0.001)


def test_cosine_similarity_zero_vector():
    with pytest.raises(ValueError):
        mod.cosine_similarity(np.array([0, 0]), np.array([1, 2]))


def test_angle_between():
    assert mod.angle_between(np.array([1, 0]), np.array([1, 1])) == pytest.approx(45.0)
    assert mod.angle_between(np.array([1, 0]), np.array([-3, 0])) == pytest.approx(180.0)


def test_angle_between_same_direction_float_rounding():
    vector = np.array([0.1, 0.2, 0.3])
    assert mod.angle_between(vector, vector * 3) == pytest.approx(0.0, abs=1e-5)


def test_most_similar():
    documents = np.array([[0, 1], [5, 1], [1, 1]])
    assert mod.most_similar(np.array([1, 0]), documents) == 1


def test_most_similar_ignores_length():
    documents = np.array([[100, 100], [1, 0]])
    assert mod.most_similar(np.array([2, 0]), documents) == 1


def test_project():
    np.testing.assert_allclose(mod.project(np.array([3, 4]), np.array([2, 0])), [3, 0])


def test_project_residual_is_orthogonal():
    vector, onto = np.array([2.0, 5.0, -1.0]), np.array([1.0, 1.0, 1.0])
    residual = vector - mod.project(vector, onto)
    assert residual @ onto == pytest.approx(0.0, abs=1e-12)


def test_are_orthogonal():
    assert mod.are_orthogonal(np.array([1, 2]), np.array([-2, 1])) is True
    assert mod.are_orthogonal(np.array([1, 2]), np.array([2, 1])) is False


def test_are_orthogonal_tolerance():
    assert mod.are_orthogonal(np.array([1.0, 0.0]), np.array([1e-12, 1.0])) is True
