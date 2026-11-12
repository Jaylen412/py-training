"""Solutions for 24-03 Cross-validation and hyperparameter tuning."""
import numpy as np
from sklearn.base import clone
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold, cross_val_score


def _rows(data, positions):
    return data.iloc[positions] if hasattr(data, "iloc") else data[positions]


def kfold_scores(model, X, y, n_splits=5):
    """Return the validation score of each fold."""
    scores = []
    for train_rows, valid_rows in KFold(n_splits=n_splits, shuffle=True, random_state=42).split(X):
        fitted = clone(model).fit(_rows(X, train_rows), _rows(y, train_rows))
        scores.append(float(fitted.score(_rows(X, valid_rows), _rows(y, valid_rows))))
    return scores


def compare_with_cv(models, X, y, scoring="accuracy"):
    """Return {name: mean cross-validated score}."""
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    return {
        name: round(float(cross_val_score(model, X, y, cv=folds, scoring=scoring).mean()), 3)
        for name, model in models.items()
    }


def tune_c(pipeline, X, y, values):
    """Return (best C, best score, best estimator)."""
    folds = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    grid = GridSearchCV(pipeline, {"model__C": values}, cv=folds, scoring="roc_auc").fit(X, y)
    return grid.best_params_["model__C"], round(float(grid.best_score_), 3), grid.best_estimator_


def final_test_auc(model, X_test, y_test):
    """Return the test ROC AUC."""
    return round(float(roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])), 3)
