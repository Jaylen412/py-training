"""Solutions for 17-04 Linear models as matrix maths."""
import numpy as np


def predict(features, weights, bias):
    """Return the linear model's predictions."""
    return features @ weights + bias


def add_bias_column(features):
    """Put a column of ones in front of the features."""
    return np.column_stack([np.ones(len(features)), features])


def solve_system(coefficients, right_hand_side):
    """Solve a square system of linear equations."""
    try:
        return np.linalg.solve(coefficients, right_hand_side)
    except np.linalg.LinAlgError:
        raise ValueError("the system has no unique solution (the matrix is singular)")


def fit_least_squares(features, targets):
    """Return the least-squares bias and weights."""
    solution, *_ = np.linalg.lstsq(add_bias_column(features), targets, rcond=None)
    return float(solution[0]), solution[1:]
