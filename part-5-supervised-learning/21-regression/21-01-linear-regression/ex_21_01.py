"""Exercises for 21-01 Linear regression."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def fit_line(x, y):
    """Fit LinearRegression on a single feature. `x` is a 1-D array or Series.
    Return (slope, intercept) as floats.

    Example: fit_line(np.array([1, 2, 3]), np.array([5, 7, 9])) returns (2.0, 3.0)
    """
    raise NotImplementedError


def coefficient_table(model, feature_names):
    """Return a pandas Series of the fitted model's coefficients, indexed by
    feature name, sorted by ABSOLUTE size from largest to smallest (keeping
    their signs)."""
    raise NotImplementedError


def predict_from_dict(model, features, columns):
    """`features` is a dictionary of feature values for ONE sample, and
    `columns` is the list of feature names in the order the model was
    trained on. Return the model's prediction as a float.

    Example: predict_from_dict(model, {"bp": 90, "bmi": 30}, ["bmi", "bp"])
    """
    raise NotImplementedError


def residuals(model, X, y):
    """Return actual minus predicted, as a NumPy array."""
    raise NotImplementedError
