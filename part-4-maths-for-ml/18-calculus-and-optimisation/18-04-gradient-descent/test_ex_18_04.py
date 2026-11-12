import importlib
import os
import warnings

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_18_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_18_04"
)

HOURS = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
SCORES = np.array([52.0, 55.0, 61.0, 64.0, 70.0, 72.0])


def test_gradient_descent_1d_first_step():
    assert mod.gradient_descent_1d(lambda x: 2 * (x - 3), 0.0, 0.1, 1) == pytest.approx([0.0, 0.6])


def test_gradient_descent_1d_converges():
    path = mod.gradient_descent_1d(lambda x: 2 * (x - 3), 0.0, 0.1, 100)
    assert len(path) == 101
    assert path[-1] == pytest.approx(3.0, abs=1e-6)


def test_gradient_descent_1d_zero_steps():
    assert mod.gradient_descent_1d(lambda x: x, 5.0, 0.1, 0) == [5.0]


def test_mse_gradient_at_zero():
    dw, db = mod.mse_gradient(HOURS, SCORES, 0.0, 0.0)
    assert dw == pytest.approx(-2 * np.mean(SCORES * HOURS))
    assert db == pytest.approx(-2 * np.mean(SCORES))


def test_mse_gradient_matches_numerical_derivative():
    w, b, step = 3.0, 40.0, 1e-6
    loss = lambda w_, b_: np.mean((SCORES - (w_ * HOURS + b_)) ** 2)
    dw, db = mod.mse_gradient(HOURS, SCORES, w, b)
    assert dw == pytest.approx((loss(w + step, b) - loss(w - step, b)) / (2 * step), rel=1e-4)
    assert db == pytest.approx((loss(w, b + step) - loss(w, b - step)) / (2 * step), rel=1e-4)


def test_fit_line_matches_least_squares():
    w, b, history = mod.fit_line(HOURS, SCORES, 0.02, 5000)
    assert w == pytest.approx(4.229, abs=1e-3)
    assert b == pytest.approx(47.533, abs=1e-3)
    assert len(history) == 5000
    assert history[-1] < history[0]


def test_fit_line_history_first_value():
    _, _, history = mod.fit_line(HOURS, SCORES, 0.02, 1)
    assert history[0] == pytest.approx(833.508, abs=1e-3)


def test_has_diverged():
    assert mod.has_diverged([10.0, 5.0, 2.0]) is False
    assert mod.has_diverged([10.0, 50.0, 400.0]) is True


def test_has_diverged_not_finite():
    assert mod.has_diverged([10.0, float("inf")]) is True
    assert mod.has_diverged([10.0, float("nan")]) is True


def test_large_learning_rate_diverges():
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        _, _, history = mod.fit_line(HOURS, SCORES, 0.1, 50)
    assert mod.has_diverged(history) is True
