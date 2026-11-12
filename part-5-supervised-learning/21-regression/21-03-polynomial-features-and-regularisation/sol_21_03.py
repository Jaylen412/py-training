"""Solutions for 21-03 Polynomial features and regularisation."""
import numpy as np
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures


def polynomial_feature_count(n_features, degree):
    """Return how many features PolynomialFeatures creates."""
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    return poly.fit_transform(np.zeros((1, n_features))).shape[1]


def fit_polynomial(x, y, degree):
    """Fit a polynomial regression on one feature."""
    poly = PolynomialFeatures(degree=degree, include_bias=False)
    features = poly.fit_transform(np.asarray(x).reshape(-1, 1))
    return LinearRegression().fit(features, y), poly


def ridge_test_scores(X_train, X_test, y_train, y_test, alphas):
    """Return {alpha: test R squared}."""
    return {
        alpha: round(Ridge(alpha=alpha).fit(X_train, y_train).score(X_test, y_test), 3)
        for alpha in alphas
    }


def lasso_kept_features(X_train, y_train, feature_names, alpha):
    """Return the names of the features Lasso keeps."""
    coefficients = Lasso(alpha=alpha).fit(X_train, y_train).coef_
    return [name for name, coefficient in zip(feature_names, coefficients) if coefficient != 0]
