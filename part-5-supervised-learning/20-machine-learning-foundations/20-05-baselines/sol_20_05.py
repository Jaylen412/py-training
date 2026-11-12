"""Solutions for 20-05 Baselines."""
import numpy as np
from sklearn.dummy import DummyClassifier, DummyRegressor


def majority_baseline_accuracy(y_train, y_test):
    """Accuracy of always predicting the training majority class."""
    dummy = DummyClassifier(strategy="most_frequent").fit(np.zeros((len(y_train), 1)), y_train)
    return float(dummy.score(np.zeros((len(y_test), 1)), y_test))


def mean_baseline_mae(y_train, y_test):
    """MAE of always predicting the training mean."""
    return float(np.mean(np.abs(np.asarray(y_test) - np.mean(y_train))))


def beats_baseline(model, X_train, X_test, y_train, y_test, margin=0.05):
    """Return True if the model clearly beats the majority baseline."""
    dummy = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
    model.fit(X_train, y_train)
    return bool(model.score(X_test, y_test) - dummy.score(X_test, y_test) > margin)


def improvement(baseline_error, model_error):
    """Return the fractional error reduction over the baseline."""
    if baseline_error <= 0:
        raise ValueError("the baseline error must be positive")
    return 1 - model_error / baseline_error
