"""Solutions for 21-02 Regression metrics."""
import numpy as np


def mae(actual, predicted):
    """Mean absolute error."""
    return float(np.mean(np.abs(np.asarray(actual) - np.asarray(predicted))))


def rmse(actual, predicted):
    """Root mean squared error."""
    return float(np.sqrt(np.mean((np.asarray(actual) - np.asarray(predicted)) ** 2)))


def r_squared(actual, predicted):
    """Coefficient of determination."""
    actual, predicted = np.asarray(actual, dtype=float), np.asarray(predicted, dtype=float)
    ss_residual = np.sum((actual - predicted) ** 2)
    ss_total = np.sum((actual - actual.mean()) ** 2)
    return float(1 - ss_residual / ss_total)


def evaluate(model, X_test, y_test):
    """Return MAE, RMSE and R squared for a fitted model."""
    predictions = model.predict(X_test)
    return {
        "mae": round(mae(y_test, predictions), 3),
        "rmse": round(rmse(y_test, predictions), 3),
        "r2": round(r_squared(y_test, predictions), 3),
    }


def pick_metric(large_errors_much_worse):
    """Choose RMSE when big errors are disproportionately bad, else MAE."""
    return "rmse" if large_errors_much_worse else "mae"
