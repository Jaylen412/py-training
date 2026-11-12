"""Solutions for 18-03 Loss functions."""
import numpy as np


def mean_squared_error(actual, predicted):
    """Mean of squared residuals."""
    return float(np.mean((np.asarray(actual) - np.asarray(predicted)) ** 2))


def root_mean_squared_error(actual, predicted):
    """Square root of the MSE."""
    return float(np.sqrt(mean_squared_error(actual, predicted)))


def mean_absolute_error(actual, predicted):
    """Mean of absolute residuals."""
    return float(np.mean(np.abs(np.asarray(actual) - np.asarray(predicted))))


def loss_curve(x, y, intercept, slopes):
    """Return the MSE for each candidate slope."""
    return np.array([mean_squared_error(y, intercept + slope * x) for slope in slopes])


def best_parameter(candidates, losses):
    """Return the candidate with the smallest loss."""
    return float(np.asarray(candidates)[np.argmin(losses)])
