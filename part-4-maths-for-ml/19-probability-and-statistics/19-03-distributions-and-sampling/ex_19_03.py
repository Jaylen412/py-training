"""Exercises for 19-03 Distributions and sampling."""
import numpy as np


def fraction_within(values, k):
    """Return the fraction of `values` within k standard deviations of their
    mean (inclusive), using the population standard deviation (np.std).

    Example: for 100,000 normal draws, fraction_within(values, 2) is about 0.95
    """
    raise NotImplementedError


def binomial_probability(trials, p, successes, simulations, seed):
    """Estimate the probability of exactly `successes` successes in `trials`
    yes/no trials with success probability `p`, by drawing `simulations`
    values with np.random.default_rng(seed).binomial(trials, p, size=simulations).

    Example: binomial_probability(20, 0.3, 6, 200_000, 1) is about 0.19
    """
    raise NotImplementedError


def sample_means(population, sample_size, repeats, seed):
    """Return a NumPy array of `repeats` sample means. For each repeat, draw
    `sample_size` values from `population` WITH replacement using
    rng.choice(population, size=sample_size) and take the mean. Create rng
    once with np.random.default_rng(seed).
    """
    raise NotImplementedError


def standard_error(values):
    """Return the estimated standard error of the mean: the SAMPLE standard
    deviation (ddof=1) divided by the square root of the number of values.

    Example: standard_error(np.array([2, 4, 4, 4, 5, 5, 7, 9])) returns about 0.756
    """
    raise NotImplementedError
