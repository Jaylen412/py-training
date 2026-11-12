"""Exercises for 24-03 Cross-validation and hyperparameter tuning."""
import numpy as np
from sklearn.base import clone
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV, KFold, StratifiedKFold, cross_val_score


def kfold_scores(model, X, y, n_splits=5):
    """k-fold cross-validation by hand. Use KFold(n_splits=n_splits,
    shuffle=True, random_state=42). For each fold, fit a fresh copy of the
    model (clone(model)) on the training rows and score it on the validation
    rows. X and y may be NumPy arrays or pandas objects: select rows with
    X[rows] for arrays, X.iloc[rows] for pandas (hasattr(X, "iloc") tells
    you which). Return the list of scores as floats.
    """
    raise NotImplementedError


def compare_with_cv(models, X, y, scoring="accuracy"):
    """`models` is a dict {name: estimator}. Return {name: mean score}
    using cross_val_score with StratifiedKFold(n_splits=5, shuffle=True,
    random_state=42) and the given scoring, each rounded to 3 places."""
    raise NotImplementedError


def tune_c(pipeline, X, y, values):
    """Grid-search the pipeline's "model__C" over `values` with
    StratifiedKFold(n_splits=5, shuffle=True, random_state=42) and
    scoring="roc_auc". Return (best C, best score rounded to 3 places,
    the fitted best estimator)."""
    raise NotImplementedError


def final_test_auc(model, X_test, y_test):
    """Return the test-set ROC AUC of a fitted classifier, rounded to 3
    places, using the probabilities of class 1."""
    raise NotImplementedError
