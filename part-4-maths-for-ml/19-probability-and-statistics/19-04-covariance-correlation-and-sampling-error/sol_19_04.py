"""Solutions for 19-04 Covariance, correlation and sampling error."""
import numpy as np


def covariance(x, y):
    """Return the population covariance."""
    return float(np.mean((x - x.mean()) * (y - y.mean())))


def pearson_correlation(x, y):
    """Return the Pearson correlation coefficient."""
    spread = np.std(x) * np.std(y)
    if spread == 0:
        raise ValueError("correlation is undefined when a variable is constant")
    return covariance(x, y) / spread


def bootstrap_statistic(values, statistic, repeats, seed):
    """Return `repeats` bootstrap values of `statistic`."""
    rng = np.random.default_rng(seed)
    return np.array([
        statistic(rng.choice(values, size=len(values), replace=True)) for _ in range(repeats)
    ])


def confidence_interval(values, statistic, level=0.95, repeats=5000, seed=42):
    """Return a percentile bootstrap confidence interval."""
    results = bootstrap_statistic(values, statistic, repeats, seed)
    tail = (1 - level) / 2 * 100     # 2.5 for a 95% interval
    low, high = np.percentile(results, [tail, 100 - tail])
    return float(low), float(high)
