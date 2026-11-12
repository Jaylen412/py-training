import importlib
import os

import numpy as np
import pytest

mod = importlib.import_module(
    "sol_19_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_19_03"
)


def test_fraction_within_normal():
    values = np.random.default_rng(0).normal(size=100_000)
    assert mod.fraction_within(values, 1) == pytest.approx(0.683, abs=0.01)
    assert mod.fraction_within(values, 2) == pytest.approx(0.954, abs=0.01)


def test_fraction_within_small_example():
    values = np.array([0.0, 0.0, 10.0, 10.0])   # mean 5, sd 5
    assert mod.fraction_within(values, 1) == 1.0
    assert mod.fraction_within(values, 0.5) == 0.0


def test_binomial_probability():
    assert mod.binomial_probability(20, 0.3, 6, 200_000, 1) == pytest.approx(0.1916, abs=0.005)


def test_binomial_probability_certain_and_repeatable():
    assert mod.binomial_probability(5, 1.0, 5, 1000, 3) == 1.0
    assert mod.binomial_probability(10, 0.5, 5, 1000, 3) == mod.binomial_probability(10, 0.5, 5, 1000, 3)


def test_sample_means_shape_and_centre():
    population = np.random.default_rng(1).exponential(10, size=50_000)
    means = mod.sample_means(population, 30, 2000, 42)
    assert means.shape == (2000,)
    assert means.mean() == pytest.approx(population.mean(), rel=0.03)


def test_sample_means_central_limit_spread():
    population = np.random.default_rng(1).exponential(10, size=50_000)
    means = mod.sample_means(population, 100, 3000, 7)
    assert means.std() == pytest.approx(population.std() / 10, rel=0.08)


def test_sample_means_repeatable():
    population = np.arange(100.0)
    np.testing.assert_array_equal(mod.sample_means(population, 5, 10, 9), mod.sample_means(population, 5, 10, 9))


def test_standard_error():
    assert mod.standard_error(np.array([2, 4, 4, 4, 5, 5, 7, 9])) == pytest.approx(0.7559, abs=1e-4)


def test_standard_error_shrinks_with_n():
    rng = np.random.default_rng(3)
    small = mod.standard_error(rng.normal(size=100))
    large = mod.standard_error(rng.normal(size=10_000))
    assert large < small / 5
