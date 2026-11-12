import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_13_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_13_01"
)


def test_to_array():
    result = mod.to_array([1, 2, 3])
    assert isinstance(result, np.ndarray)
    assert result.dtype == np.float64
    np.testing.assert_array_equal(result, [1.0, 2.0, 3.0])


def test_to_array_empty():
    result = mod.to_array([])
    assert result.shape == (0,)
    assert result.dtype == np.float64


def test_describe():
    assert mod.describe(np.zeros((2, 3))) == ((2, 3), 2, "float64")


def test_describe_one_dimension():
    assert mod.describe(np.array([1, 2, 3], dtype=np.int64)) == ((3,), 1, "int64")


def test_evenly_spaced():
    np.testing.assert_allclose(mod.evenly_spaced(0, 1, 5), [0, 0.25, 0.5, 0.75, 1])


def test_evenly_spaced_includes_both_ends():
    result = mod.evenly_spaced(-2, 2, 3)
    np.testing.assert_allclose(result, [-2, 0, 2])
    assert len(mod.evenly_spaced(0, 10, 11)) == 11


def test_multiples():
    np.testing.assert_array_equal(mod.multiples(3, 10), [3, 6, 9])


def test_multiples_includes_limit():
    np.testing.assert_array_equal(mod.multiples(5, 20), [5, 10, 15, 20])
    assert len(mod.multiples(7, 3)) == 0


def test_filled_grid():
    result = mod.filled_grid(2, 3, 7)
    assert result.shape == (2, 3)
    assert (result == 7).all()


def test_filled_grid_float_value():
    result = mod.filled_grid(1, 1, 0.5)
    assert result[0, 0] == pytest.approx(0.5)
