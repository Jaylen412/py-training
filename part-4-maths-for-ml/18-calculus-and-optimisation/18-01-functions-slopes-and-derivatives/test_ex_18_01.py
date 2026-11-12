import importlib
import math
import os

import pytest

mod = importlib.import_module(
    "sol_18_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_18_01"
)


def test_slope_between():
    assert mod.slope_between((1, 3), (4, 9)) == pytest.approx(2.0)
    assert mod.slope_between((0, 5), (2, 1)) == pytest.approx(-2.0)


def test_slope_between_flat_and_vertical():
    assert mod.slope_between((0, 4), (10, 4)) == 0
    with pytest.raises(ValueError):
        mod.slope_between((2, 1), (2, 5))


def test_numerical_derivative_square():
    for x in [-2, 0, 1, 3]:
        assert mod.numerical_derivative(lambda v: v ** 2, x) == pytest.approx(2 * x, abs=1e-6)


def test_numerical_derivative_sin():
    assert mod.numerical_derivative(math.sin, 0.0) == pytest.approx(1.0, abs=1e-8)
    assert mod.numerical_derivative(math.sin, math.pi / 2) == pytest.approx(0.0, abs=1e-6)


def test_numerical_derivative_uses_step():
    # With a big step, the estimate for x**3 at 0 is (h**3 - (-h)**3) / (2h) = h**2.
    assert mod.numerical_derivative(lambda v: v ** 3, 0.0, step=1.0) == pytest.approx(1.0)


def test_tangent_line():
    slope, intercept = mod.tangent_line(lambda x: x ** 2, 1)
    assert slope == pytest.approx(2.0, abs=1e-6)
    assert intercept == pytest.approx(-1.0, abs=1e-6)


def test_tangent_line_of_a_line_is_itself():
    slope, intercept = mod.tangent_line(lambda x: 3 * x + 4, 10)
    assert (slope, intercept) == (pytest.approx(3.0), pytest.approx(4.0, abs=1e-6))


def test_downhill_direction():
    bowl = lambda x: (x - 3) ** 2
    assert mod.downhill_direction(bowl, 0) == "right"
    assert mod.downhill_direction(bowl, 5) == "left"


def test_downhill_direction_flat():
    assert mod.downhill_direction(lambda x: (x - 3) ** 2, 3) == "flat"
