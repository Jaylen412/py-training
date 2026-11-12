"""Part 4 project: linear regression trained by gradient descent, in NumPy.

Run from the repository root to train on two datasets, compare with least
squares and save the loss curves:
    python part-4-maths-for-ml/project/solution/linear_regression_gd.py
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
    gradient descent on the mean squared error."""

    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs

    def fit(self, X, y):
        """Learn weights_ and bias_ from the training data. Returns self."""
        X, y = _check_inputs(X, y)
        n_samples, n_features = X.shape
        self.weights_ = np.zeros(n_features)
        self.bias_ = 0.0
        self.loss_history_ = []
        for _ in range(self.epochs):
            errors = X @ self.weights_ + self.bias_ - y
            # Gradients of the MSE (18-04), for every weight at once.
            weight_gradient = 2 / n_samples * (X.T @ errors)
            bias_gradient = 2 * errors.mean()
            self.weights_ -= self.learning_rate * weight_gradient
            self.bias_ -= self.learning_rate * bias_gradient
            self.loss_history_.append(float(np.mean((X @ self.weights_ + self.bias_ - y) ** 2)))
        return self

    def predict(self, X):
        """Return one prediction per row of X."""
        if not hasattr(self, "weights_"):
            raise RuntimeError("call fit() before predict()")
        X = np.asarray(X, dtype=float)
        if X.ndim != 2 or X.shape[1] != len(self.weights_):
            raise ValueError(f"expected X with {len(self.weights_)} columns, got shape {X.shape}")
        return X @ self.weights_ + self.bias_

    def score(self, X, y):
        """Return R squared: 1 - (MSE of the predictions / variance of y)."""
        y = np.asarray(y, dtype=float)
        mse = np.mean((y - self.predict(X)) ** 2)
        return float(1 - mse / np.var(y))


def _check_inputs(X, y):
    X = np.asarray(X, dtype=float)
    y = np.asarray(y, dtype=float)
    if X.ndim != 2:
        raise ValueError(f"X must be 2-D (samples, features), got shape {X.shape}")
    if y.ndim != 1 or len(y) != len(X):
        raise ValueError(f"y must be 1-D with {len(X)} values, got shape {y.shape}")
    return X, y


def standardise(X):
    """Return (X_standardised, column means, column standard deviations)."""
    X = np.asarray(X, dtype=float)
    means = X.mean(axis=0)
    stds = X.std(axis=0)
    return (X - means) / stds, means, stds


def fit_least_squares(X, y):
    """Return (bias, weights) from np.linalg.lstsq, for comparison."""
    X_with_ones = np.column_stack([np.ones(len(X)), X])
    solution, *_ = np.linalg.lstsq(X_with_ones, y, rcond=None)
    return float(solution[0]), solution[1:]


def plot_loss(history, title, path):
    """Save a log-scale plot of the loss history to `path`."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(history)
    ax.set_yscale("log")
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Mean squared error (log scale)")
    ax.set_title(title)
    fig.savefig(path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return path


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
