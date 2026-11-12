import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_18_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_18_03"
)

HOURS = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
SCORES = np.array([52.0, 55.0, 61.0, 64.0, 70.0, 72.0])


def test_mean_squared_error():
    assert mod.mean_squared_error(np.array([1, 2]), np.array([1, 4])) == pytest.approx(2.0)
    assert mod.mean_squared_error(SCORES, 50 + 4 * HOURS) == pytest.approx(3.6667, abs=1e-4)


def test_mean_squared_error_perfect():
    assert mod.mean_squared_error(SCORES, SCORES) == 0


def test_root_mean_squared_error():
    assert mod.root_mean_squared_error(SCORES, 50 + 4 * HOURS) == pytest.approx(1.915, abs=1e-3)


def test_mean_absolute_error():
    assert mod.mean_absolute_error(np.array([1, 2]), np.array([1, 4])) == pytest.approx(1.0)
    assert mod.mean_absolute_error(SCORES, 50 + 4 * HOURS) == pytest.approx(1.6667, abs=1e-4)


def test_mse_punishes_big_errors_more_than_mae():
    zeros = np.zeros(4)
    spread = np.array([2.0, 2.0, 2.0, 2.0])
    single = np.array([0.0, 0.0, 0.0, 8.0])
    assert mod.mean_absolute_error(zeros, spread) == mod.mean_absolute_error(zeros, single)
    assert mod.mean_squared_error(zeros, single) == 4 * mod.mean_squared_error(zeros, spread)


def test_loss_curve():
    losses = mod.loss_curve(HOURS, SCORES, 47, [4.0, 4.3])
    assert losses.shape == (2,)
    assert losses[1] == pytest.approx(0.8317, abs=1e-3)


def test_loss_curve_is_a_bowl():
    slopes = np.linspace(2, 7, 101)
    losses = mod.loss_curve(HOURS, SCORES, 47, slopes)
    best = losses.argmin()
    assert 0 < best < 100
    assert (np.diff(losses[:best]) < 0).all() and (np.diff(losses[best:]) > 0).all()


def test_best_parameter():
    assert mod.best_parameter([1, 2, 3], [5.0, 0.5, 2.0]) == 2.0


def test_best_parameter_tie_and_real_curve():
    assert mod.best_parameter([1, 2], [1.0, 1.0]) == 1.0
    slopes = np.linspace(2, 7, 101)
    assert mod.best_parameter(slopes, mod.loss_curve(HOURS, SCORES, 47, slopes)) == pytest.approx(4.35)
