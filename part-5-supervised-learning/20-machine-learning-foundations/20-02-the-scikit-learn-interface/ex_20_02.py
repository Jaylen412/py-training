"""Exercises for 20-02 The scikit-learn interface."""
import numpy as np


def fit_and_predict(model, X, y, new_X):
    """Fit `model` on X and y, then return its predictions for new_X."""
    raise NotImplementedError


def as_one_sample(features):
    """Return the 1-D array `features` as a 2-D array with one row.

    Example: as_one_sample(np.array([5.0, 3.4])).shape is (1, 2)
    """
    raise NotImplementedError


def learned_attributes(model):
    """Return a sorted list of the names of the model's learned attributes:
    the names in vars(model) that end with "_" but do not start with "_".

    Example: for a fitted LinearRegression, the list includes "coef_" and "intercept_"
    """
    raise NotImplementedError


def training_scores(models, X, y):
    """Fit each model in the list on X and y, and return a dictionary mapping
    each model's class name (type(model).__name__) to its score on X and y,
    rounded to 3 decimal places."""
    raise NotImplementedError
