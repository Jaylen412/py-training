"""Exercises for 19-02 Probability basics.

Event arguments are boolean NumPy arrays (or pandas Series) of equal length.
"""
import numpy as np


def probability(event):
    """Return the fraction of True values, as a float.

    Example: probability(np.array([True, False, True, True])) returns 0.75
    """
    raise NotImplementedError


def conditional_probability(event, given):
    """Return P(event | given): the fraction of rows where `given` is True in
    which `event` is also True. Raise ValueError if `given` is never True.

    Example: conditional_probability(np.array([1, 1, 0, 0], bool), np.array([1, 0, 1, 0], bool))
    returns 0.5
    """
    raise NotImplementedError


def are_independent(event_a, event_b, tolerance=0.01):
    """Return True if |P(A and B) - P(A) * P(B)| <= tolerance."""
    raise NotImplementedError


def bayes_posterior(prevalence, sensitivity, false_positive_rate):
    """Return P(disease | positive test) using Bayes' rule.

    Example: bayes_posterior(0.01, 0.95, 0.05) returns about 0.161
    """
    raise NotImplementedError


def simulate_two_dice(total, trials, seed):
    """Roll two fair dice `trials` times using np.random.default_rng(seed)
    (draw all first dice, then all second dice, each with
    rng.integers(1, 7, size=trials)). Return the fraction of rolls whose
    total equals `total`.
    """
    raise NotImplementedError
