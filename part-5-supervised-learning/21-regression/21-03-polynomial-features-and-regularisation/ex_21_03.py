"""Exercises for 21-03 Polynomial features and regularisation."""
import numpy as np
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures


def polynomial_feature_count(n_features, degree):
    """Return the number of columns PolynomialFeatures(degree,
    include_bias=False) creates from `n_features` features.
    Hint: fit it on np.zeros((1, n_features)) and look at the output shape.

    Example: polynomial_feature_count(2, 2) returns 5
    """
    raise NotImplementedError


def fit_polynomial(x, y, degree):
    """`x` is 1-D. Make polynomial features of x up to `degree` (no bias
    column), fit LinearRegression, and return (fitted model, fitted
    PolynomialFeatures) so the caller can transform new x values."""
    raise NotImplementedError


def ridge_test_scores(X_train, X_test, y_train, y_test, alphas):
    """Return a dictionary mapping each alpha to the test R squared of
    Ridge(alpha=alpha) fitted on the training data, rounded to 3 places."""
    raise NotImplementedError


def lasso_kept_features(X_train, y_train, feature_names, alpha):
    """Fit Lasso(alpha=alpha) and return the list of feature names whose
    coefficient is not exactly zero, in their original order."""
    raise NotImplementedError
