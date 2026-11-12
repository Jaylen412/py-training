"""Solutions for 21-01 Linear regression."""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def fit_line(x, y):
    """Return (slope, intercept) of a one-feature linear regression."""
    model = LinearRegression().fit(np.asarray(x).reshape(-1, 1), y)
    return float(model.coef_[0]), float(model.intercept_)


def coefficient_table(model, feature_names):
    """Return the coefficients labelled by feature, largest in size first."""
    table = pd.Series(model.coef_, index=feature_names)
    return table[table.abs().sort_values(ascending=False).index]


def predict_from_dict(model, features, columns):
    """Predict one sample given as a dictionary."""
    row = pd.DataFrame([[features[name] for name in columns]], columns=columns)
    return float(model.predict(row)[0])


def residuals(model, X, y):
    """Return actual minus predicted."""
    return np.asarray(y) - model.predict(X)
