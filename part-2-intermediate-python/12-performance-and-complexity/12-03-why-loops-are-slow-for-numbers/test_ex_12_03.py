import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_12_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_12_03"
)


def test_mean():
    assert mod.mean([1, 2, 6]) == pytest.approx(3.0)
    assert mod.mean([-1.5]) == pytest.approx(-1.5)


def test_mean_empty():
    with pytest.raises(ValueError):
        mod.mean([])


def test_dot_product():
    assert mod.dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert mod.dot_product([], []) == 0


def test_dot_product_length_mismatch():
    with pytest.raises(ValueError):
        mod.dot_product([1, 2], [1])


def test_elementwise_add():
    assert mod.elementwise_add([1, 2], [10, 20]) == [11, 22]
    assert mod.elementwise_add([], []) == []


def test_elementwise_add_length_mismatch():
    with pytest.raises(ValueError):
        mod.elementwise_add([1], [1, 2])


def test_standardise():
    result = mod.standardise([2, 4, 4, 4, 5, 5, 7, 9])
    assert result == pytest.approx([-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0])


def test_standardise_has_mean_zero_and_spread_one():
    result = mod.standardise([10, 20, 35, 47, 100])
    assert sum(result) / len(result) == pytest.approx(0.0, abs=1e-12)
    assert (sum(z * z for z in result) / len(result)) ** 0.5 == pytest.approx(1.0)


def test_standardise_constant_values():
    assert mod.standardise([5, 5, 5]) == [0.0, 0.0, 0.0]


def test_matrix_vector_multiply():
    assert mod.matrix_vector_multiply([[1, 2], [3, 4]], [10, 1]) == [12, 34]


def test_matrix_vector_multiply_identity_and_mismatch():
    assert mod.matrix_vector_multiply([[1, 0], [0, 1]], [7, 9]) == [7, 9]
    with pytest.raises(ValueError):
        mod.matrix_vector_multiply([[1, 2, 3]], [1, 2])
