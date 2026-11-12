"""Solutions for 19-02 Probability basics."""
import numpy as np


def probability(event):
    """Return the fraction of True values."""
    return float(np.mean(event))


def conditional_probability(event, given):
    """Return P(event | given)."""
    event, given = np.asarray(event, dtype=bool), np.asarray(given, dtype=bool)
    if not given.any():
        raise ValueError("the conditioning event never happens")
    return float(event[given].mean())


def are_independent(event_a, event_b, tolerance=0.01):
    """Return True if P(A and B) is close to P(A) * P(B)."""
    event_a, event_b = np.asarray(event_a, dtype=bool), np.asarray(event_b, dtype=bool)
    joint = probability(event_a & event_b)
    return bool(abs(joint - probability(event_a) * probability(event_b)) <= tolerance)


def bayes_posterior(prevalence, sensitivity, false_positive_rate):
    """Return P(disease | positive)."""
    # Two ways to test positive: ill and detected, or healthy and wrongly flagged.
    p_positive = sensitivity * prevalence + false_positive_rate * (1 - prevalence)
    return sensitivity * prevalence / p_positive


def simulate_two_dice(total, trials, seed):
    """Estimate P(two dice sum to `total`) by simulation."""
    rng = np.random.default_rng(seed)
    first = rng.integers(1, 7, size=trials)
    second = rng.integers(1, 7, size=trials)
    return float(np.mean(first + second == total))
