"""Exercises for 20-04 Overfitting and underfitting."""
import numpy as np
from sklearn.tree import DecisionTreeClassifier


def polynomial_errors(x, y, x_test, y_test, degree):
    """Fit np.polyfit(x, y, degree) and return (training MSE, test MSE)
    as floats."""
    raise NotImplementedError


def best_degree(x, y, x_test, y_test, degrees):
    """Return the degree from the list `degrees` with the lowest test MSE
    (the first one on a tie)."""
    raise NotImplementedError


def depth_scores(X_train, X_test, y_train, y_test, depths):
    """For each depth, fit DecisionTreeClassifier(max_depth=depth,
    random_state=42) and return a dictionary mapping the depth to a tuple
    (training accuracy, test accuracy), each rounded to 3 places."""
    raise NotImplementedError


def diagnose(train_score, test_score, good_score=0.9, max_gap=0.05):
    """Return a diagnosis from accuracy-like scores (higher is better):
    - "underfitting" if the training score is below good_score,
    - otherwise "overfitting" if train_score - test_score is more than max_gap,
    - otherwise "good fit".

    Example: diagnose(1.0, 0.8) returns "overfitting"
    """
    raise NotImplementedError
