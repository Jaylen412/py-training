"""Solutions for 19-03 Distributions and sampling."""
import numpy as np


def fraction_within(values, k):
    """Return the fraction of values within k SDs of the mean."""
    return float(np.mean(np.abs(values - values.mean()) <= k * values.std()))


def binomial_probability(trials, p, successes, simulations, seed):
    """Estimate P(exactly `successes` successes) by simulation."""
    draws = np.random.default_rng(seed).binomial(trials, p, size=simulations)
    return float(np.mean(draws == successes))


def sample_means(population, sample_size, repeats, seed):
    """Return the means of many random samples."""
    rng = np.random.default_rng(seed)
    return np.array([rng.choice(population, size=sample_size).mean() for _ in range(repeats)])


def standard_error(values):
    """Return the standard error of the mean."""
    return float(np.std(values, ddof=1) / np.sqrt(len(values)))
