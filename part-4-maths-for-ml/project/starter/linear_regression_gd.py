"""Part 4 project: linear regression trained by gradient descent, in NumPy.

Run from the repository root, once everything is written, to train on two
datasets, compare with least squares and save the loss curves:
    python part-4-maths-for-ml/project/starter/linear_regression_gd.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes, make_regression

FIGURES = Path(__file__).parent / "figures"


class LinearRegressionGD:
    """Linear regression, prediction = X @ weights_ + bias_, fitted by
    gradient descent on the mean squared error. Follows the estimator
    pattern from 09-05."""

    def __init__(self, learning_rate=0.01, epochs=1000):
        """Requirement 1. Store the two hyperparameters. Learn nothing here."""
        raise NotImplementedError

    def fit(self, X, y):
        """Requirement 2. Learn from training data and return self.

        - Convert X and y to float arrays. Raise ValueError unless X is 2-D
          and y is 1-D with one value per row of X.
        - Start with weights_ = zeros (one per feature) and bias_ = 0.0.
        - For each epoch: compute errors = X @ weights_ + bias_ - y; compute
          the gradients (2 / n) * X.T @ errors and 2 * mean(errors) from the
          same old parameters; update both; then append the new MSE (a float)
          to loss_history_.
        """
        raise NotImplementedError

    def predict(self, X):
        """Requirement 3. Return X @ weights_ + bias_.
        Raise RuntimeError mentioning fit() if not fitted, and ValueError if X
        does not have one column per weight."""
        raise NotImplementedError

    def score(self, X, y):
        """Requirement 4. Return R squared as a float:
        1 - (MSE of the predictions on X) / (variance of y).
        1.0 is perfect; 0.0 is no better than always predicting the mean."""
        raise NotImplementedError


def standardise(X):
    """Requirement 5. Return (X_standardised, column means, column standard
    deviations), where X_standardised = (X - means) / stds."""
    raise NotImplementedError


def fit_least_squares(X, y):
    """Requirement 5. Return (bias, weights) found by np.linalg.lstsq on X
    with a column of ones in front (17-04). bias is a float."""
    raise NotImplementedError


def plot_loss(history, title, path):
    """Requirement 6. Save a titled, labelled, log-scale line plot of the loss
    history to `path`, creating its folder if needed. Return the path."""
    raise NotImplementedError


def compare(name, X, y, learning_rate, epochs):
    """Train both ways on one dataset, print the comparison and plot the loss."""
    model = LinearRegressionGD(learning_rate=learning_rate, epochs=epochs).fit(X, y)
    bias, weights = fit_least_squares(X, y)
    print(f"--- {name} ---")
    print("gradient descent weights:", np.round(model.weights_, 3), "bias:", round(model.bias_, 3))
    print("least squares weights:   ", np.round(weights, 3), "bias:", round(bias, 3))
    print("largest weight difference:", f"{np.abs(model.weights_ - weights).max():.2e}")
    print("R squared:", round(model.score(X, y), 4))
    plot_loss(model.loss_history_, f"{name}: training loss", FIGURES / f"loss_{name}.png")
    return model


def main():
    X, y, true_coef = make_regression(
        n_samples=200, n_features=3, noise=10, coef=True, random_state=42
    )
    print("make_regression true weights:", np.round(true_coef, 3))
    compare("make_regression", X, y, learning_rate=0.1, epochs=500)

    diabetes = load_diabetes()
    X_scaled, _, _ = standardise(diabetes.data)
    compare("diabetes", X_scaled, diabetes.target, learning_rate=0.1, epochs=5000)


if __name__ == "__main__":
    main()
