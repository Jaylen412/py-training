import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_18_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_18_02"
)


def bowl(point):
    return point[0] ** 2 + 3 * point[1] ** 2


def shifted(point):
    return (point[0] - 1) ** 2 + (point[1] + 2) ** 2 + (point[2] - 3) ** 2


def test_partial_derivative():
    point = np.array([1.0, 1.0])
    assert mod.partial_derivative(bowl, point, 0) == pytest.approx(2.0, abs=1e-6)
    assert mod.partial_derivative(bowl, point, 1) == pytest.approx(6.0, abs=1e-6)


def test_partial_derivative_does_not_change_point():
    point = np.array([1.0, 1.0])
    mod.partial_derivative(bowl, point, 0)
    np.testing.assert_array_equal(point, [1.0, 1.0])


def test_partial_derivative_integer_point():
    assert mod.partial_derivative(bowl, np.array([2, 0]), 0) == pytest.approx(4.0, abs=1e-6)


def test_numerical_gradient():
    np.testing.assert_allclose(mod.numerical_gradient(bowl, np.array([2.0, -1.0])), [4, -6], atol=1e-6)


def test_numerical_gradient_three_inputs():
    result = mod.numerical_gradient(shifted, np.array([0.0, 0.0, 0.0]))
    np.testing.assert_allclose(result, [-2, 4, -6], atol=1e-6)


def test_steepest_descent_direction():
    circle = lambda p: p[0] ** 2 + p[1] ** 2
    np.testing.assert_allclose(mod.steepest_descent_direction(circle, np.array([3.0, 4.0])), [-0.6, -0.8], atol=1e-6)


def test_steepest_descent_direction_is_unit_and_goes_down():
    point = np.array([1.0, 1.0])
    direction = mod.steepest_descent_direction(bowl, point)
    assert np.linalg.norm(direction) == pytest.approx(1.0)
    assert bowl(point + 0.01 * direction) < bowl(point)


def test_steepest_descent_direction_at_minimum():
    with pytest.raises(ValueError):
        mod.steepest_descent_direction(bowl, np.array([0.0, 0.0]))


def test_is_near_minimum():
    assert mod.is_near_minimum(shifted, np.array([1.0, -2.0, 3.0])) is True
    assert mod.is_near_minimum(shifted, np.array([1.0, -2.0, 3.1])) is False
