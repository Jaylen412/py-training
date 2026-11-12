import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_diabetes

mod = importlib.import_module(
    "sol_19_04" if os.environ.get("COURSE_SOLUTIONS") else "ex_19_04"
)

DIABETES = load_diabetes(as_frame=True, scaled=False).frame
BMI = DIABETES["bmi"].to_numpy()
PROGRESSION = DIABETES["target"].to_numpy()


def test_covariance():
    assert mod.covariance(np.array([1, 2, 3]), np.array([2, 4, 6])) == pytest.approx(4 / 3)


def test_covariance_diabetes_and_units():
    assert mod.covariance(BMI, PROGRESSION) == pytest.approx(199.3, abs=0.05)
    assert mod.covariance(BMI * 10, PROGRESSION) == pytest.approx(10 * mod.covariance(BMI, PROGRESSION))


def test_pearson_correlation():
    assert mod.pearson_correlation(np.array([1, 2, 3]), np.array([6, 4, 2])) == pytest.approx(-1.0)
    assert mod.pearson_correlation(BMI, PROGRESSION) == pytest.approx(np.corrcoef(BMI, PROGRESSION)[0, 1])


def test_pearson_correlation_ignores_units():
    assert mod.pearson_correlation(BMI * 10 + 3, PROGRESSION) == pytest.approx(0.586, abs=1e-3)


def test_pearson_correlation_constant():
    with pytest.raises(ValueError):
        mod.pearson_correlation(np.array([1, 1, 1]), np.array([1, 2, 3]))


def test_bootstrap_statistic_shape_and_seed():
    values = np.arange(20.0)
    first = mod.bootstrap_statistic(values, np.mean, 100, 1)
    assert first.shape == (100,)
    np.testing.assert_array_equal(first, mod.bootstrap_statistic(values, np.mean, 100, 1))


def test_bootstrap_statistic_uses_replacement():
    values = np.arange(20.0)
    results = mod.bootstrap_statistic(values, np.mean, 200, 2)
    assert results.std() > 0.5   # without replacement every mean would be 9.5


def test_bootstrap_statistic_matches_standard_error():
    sample = np.random.default_rng(42).normal(50, 10, size=100)
    results = mod.bootstrap_statistic(sample, np.mean, 4000, 3)
    assert results.std() == pytest.approx(np.std(sample, ddof=1) / 10, rel=0.08)


def test_confidence_interval_contains_estimate():
    sample = np.random.default_rng(42).normal(50, 10, size=100)
    low, high = mod.confidence_interval(sample, np.mean)
    assert low < sample.mean() < high
    assert 2 < high - low < 6


def test_confidence_interval_level_changes_width():
    sample = np.random.default_rng(42).normal(50, 10, size=100)
    narrow = mod.confidence_interval(sample, np.mean, level=0.5)
    wide = mod.confidence_interval(sample, np.mean, level=0.99)
    assert (narrow[1] - narrow[0]) < (wide[1] - wide[0])
