import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_19_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_19_01"
)

SCORES = np.array([62, 71, 71, 75, 78, 80, 84, 88, 95, 41])


def test_median_odd_and_even():
    assert mod.median(np.array([3, 1, 2])) == 2.0
    assert mod.median(SCORES) == pytest.approx(76.5)


def test_median_matches_numpy():
    values = np.random.default_rng(0).normal(size=101)
    assert mod.median(values) == pytest.approx(np.median(values))


def test_median_empty():
    with pytest.raises(ValueError):
        mod.median(np.array([]))


def test_mode():
    assert mod.mode(SCORES) == 71


def test_mode_tie_returns_smallest():
    assert mod.mode(np.array([4, 1, 4, 2, 1])) == 1


def test_variance():
    assert mod.variance(np.array([2, 4, 4, 4, 5, 5, 7, 9])) == pytest.approx(4.0)
    assert mod.variance(SCORES) == pytest.approx(203.85)


def test_variance_sample():
    assert mod.variance(SCORES, sample=True) == pytest.approx(226.5)


def test_z_scores():
    z = mod.z_scores(SCORES)
    assert z[-1] == pytest.approx(-2.346, abs=1e-3)
    assert z.mean() == pytest.approx(0.0, abs=1e-12)
    assert z.std() == pytest.approx(1.0)


def test_percentile_rank():
    assert mod.percentile_rank(np.array([10, 20, 30, 40]), 30) == 50.0


def test_percentile_rank_extremes():
    assert mod.percentile_rank(SCORES, 0) == 0.0
    assert mod.percentile_rank(SCORES, 1000) == 100.0
