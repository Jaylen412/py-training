"""Solutions for 20-04 Overfitting and underfitting."""
import numpy as np
from sklearn.tree import DecisionTreeClassifier


def polynomial_errors(x, y, x_test, y_test, degree):
    """Return (training MSE, test MSE) for a polynomial fit."""
    coefficients = np.polyfit(x, y, degree)
    train = np.mean((np.polyval(coefficients, x) - y) ** 2)
    test = np.mean((np.polyval(coefficients, x_test) - y_test) ** 2)
    return float(train), float(test)


def best_degree(x, y, x_test, y_test, degrees):
    """Return the degree with the lowest test MSE."""
    test_errors = [polynomial_errors(x, y, x_test, y_test, degree)[1] for degree in degrees]
    return degrees[int(np.argmin(test_errors))]


def depth_scores(X_train, X_test, y_train, y_test, depths):
    """Return {depth: (training accuracy, test accuracy)}."""
    scores = {}
    for depth in depths:
        tree = DecisionTreeClassifier(max_depth=depth, random_state=42).fit(X_train, y_train)
        scores[depth] = (round(tree.score(X_train, y_train), 3), round(tree.score(X_test, y_test), 3))
    return scores


def diagnose(train_score, test_score, good_score=0.9, max_gap=0.05):
    """Label a model from its training and test scores."""
    if train_score < good_score:
        return "underfitting"
    if train_score - test_score > max_gap:
        return "overfitting"
    return "good fit"
