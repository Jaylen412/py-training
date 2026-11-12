"""Exercises for 20-05 Baselines."""
import numpy as np
from sklearn.dummy import DummyClassifier, DummyRegressor


def majority_baseline_accuracy(y_train, y_test):
    """Return the test accuracy (a float) of always predicting the most
    common class in y_train. You may use DummyClassifier or compute it
    directly."""
    raise NotImplementedError


def mean_baseline_mae(y_train, y_test):
    """Return the mean absolute error on y_test (a float) of always
    predicting the mean of y_train."""
    raise NotImplementedError


def beats_baseline(model, X_train, X_test, y_train, y_test, margin=0.05):
    """Fit `model` and a DummyClassifier(strategy="most_frequent") on the
    training data. Return True if the model's test score is higher than the
    dummy's by MORE than `margin`."""
    raise NotImplementedError


def improvement(baseline_error, model_error):
    """Return the fractional reduction in error: 1 - model_error / baseline_error.
    Raise ValueError if baseline_error is not positive.

    Example: improvement(65.5, 41.5) returns about 0.366
    """
    raise NotImplementedError
