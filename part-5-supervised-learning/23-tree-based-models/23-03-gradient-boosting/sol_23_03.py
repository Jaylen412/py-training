"""Solutions for 23-03 Gradient boosting."""
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeRegressor


def boost_by_hand(x, y, n_trees, learning_rate, max_depth=2):
    """Return the training predictions after boosting n_trees small trees."""
    y = np.asarray(y, dtype=float)
    prediction = np.full_like(y, y.mean())
    for _ in range(n_trees):
        residuals = y - prediction
        tree = DecisionTreeRegressor(max_depth=max_depth, random_state=42).fit(x, residuals)
        prediction += learning_rate * tree.predict(x)
    return prediction


def best_tree_count(model, X_test, y_test):
    """Return (number of trees, accuracy) at the best stage."""
    accuracies = [np.mean(predictions == y_test) for predictions in model.staged_predict(X_test)]
    best = int(np.argmax(accuracies))       # argmax returns the first maximum
    return best + 1, round(float(accuracies[best]), 3)


def early_stopping_trees(X_train, y_train):
    """Return the number of trees early stopping used."""
    model = GradientBoostingClassifier(
        n_estimators=1000, validation_fraction=0.2, n_iter_no_change=10, random_state=42
    ).fit(X_train, y_train)
    return int(model.n_estimators_)


def compare_models(models, X_train, X_test, y_train, y_test):
    """Return {class name: test accuracy}."""
    return {type(m).__name__: round(m.fit(X_train, y_train).score(X_test, y_test), 3) for m in models}
