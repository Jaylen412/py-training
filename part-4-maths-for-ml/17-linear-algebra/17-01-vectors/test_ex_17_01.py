import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_17_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_17_01"
)


def test_norm():
    assert mod.norm(np.array([3.0, 4.0])) == pytest.approx(5.0)
    assert mod.norm(np.array([1.0, 2.0, 2.0])) == pytest.approx(3.0)


def test_norm_zero_and_negative():
    assert mod.norm(np.array([0.0, 0.0])) == 0
    assert mod.norm(np.array([-3.0, -4.0])) == pytest.approx(5.0)


def test_unit_vector():
    np.testing.assert_allclose(mod.unit_vector(np.array([3.0, 4.0])), [0.6, 0.8])


def test_unit_vector_has_length_one():
    result = mod.unit_vector(np.array([2.0, -7.0, 1.5, 9.0]))
    assert np.sqrt((result ** 2).sum()) == pytest.approx(1.0)


def test_unit_vector_zero():
    with pytest.raises(ValueError):
        mod.unit_vector(np.array([0.0, 0.0]))


def test_distance():
    assert mod.distance(np.array([1, 2]), np.array([4, 6])) == pytest.approx(5.0)


def test_distance_symmetric_and_zero():
    a, b = np.array([1.0, -2.0, 3.0]), np.array([0.0, 5.0, 1.0])
    assert mod.distance(a, b) == pytest.approx(mod.distance(b, a))
    assert mod.distance(a, a) == 0


def test_nearest_index():
    points = np.array([[5, 5], [1, 1], [2, 0]])
    assert mod.nearest_index(np.array([0, 0]), points) == 1


def test_nearest_index_tie_and_type():
    points = np.array([[1, 0], [0, 1], [3, 3]])
    result = mod.nearest_index(np.array([0, 0]), points)
    assert result == 0
    assert type(result) is int
