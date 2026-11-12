"""Exercises for 23-03 Gradient boosting."""
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeRegressor


def boost_by_hand(x, y, n_trees, learning_rate, max_depth=2):
    """Gradient boosting for regression, by hand. `x` has shape (n, 1).
    Start every prediction at the mean of y. Then n_trees times: compute
    residuals = y - prediction, fit DecisionTreeRegressor(max_depth=max_depth,
    random_state=42) to (x, residuals), and add learning_rate times its
    predictions on x. Return the final predictions (a 1-D array).
    """
    raise NotImplementedError


def best_tree_count(model, X_test, y_test):
    """`model` is a FITTED GradientBoostingClassifier. Use
    model.staged_predict(X_test) to compute the test accuracy after each
    tree. Return (number of trees with the best accuracy, that accuracy
    rounded to 3 places). On a tie, return the smallest number of trees."""
    raise NotImplementedError


def early_stopping_trees(X_train, y_train):
    """Fit GradientBoostingClassifier(n_estimators=1000, validation_fraction=0.2,
    n_iter_no_change=10, random_state=42) and return how many trees it
    actually used (its n_estimators_)."""
    raise NotImplementedError


def compare_models(models, X_train, X_test, y_train, y_test):
    """Fit each model and return {class name: test accuracy rounded to 3 places}."""
    raise NotImplementedError
