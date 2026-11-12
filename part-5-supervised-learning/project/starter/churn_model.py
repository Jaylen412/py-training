"""Part 5 project: predict customer churn (starter).

Run from the repository root:
    python part-5-supervised-learning/project/starter/churn_model.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier, RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (ConfusionMatrixDisplay, RocCurveDisplay, accuracy_score, precision_score,
                             recall_score, roc_auc_score)
from sklearn.model_selection import (GridSearchCV, StratifiedKFold, cross_val_predict, cross_val_score,
                                     train_test_split)
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

HERE = Path(__file__).resolve().parent
DATA = HERE.parents[2] / "data"
FIGURES = HERE / "figures"

NUMERIC = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
NOMINAL = ["contract", "payment_method", "internet_service", "region"]
ORDERED = ["satisfaction"]
SATISFACTION_ORDER = ["low", "medium", "high"]


def load_churn(path=None):
    """Read customer_churn.csv (default: data/customer_churn.csv)."""
    return pd.read_csv(path or DATA / "customer_churn.csv")


def churn_summary(df):
    """Return a dict with the facts for the EDA section of the report:
    rows, churn_rate (rounded to 3 places), missing (counts for columns with
    gaps) and churn_by_contract (churn rate per contract, rounded to 3)."""
    raise NotImplementedError


def split_data(df, test_size=0.2):
    """Drop customer_id, split into X_train, X_test, y_train, y_test (stratified,
    random_state=42)."""
    raise NotImplementedError


def build_pipeline(model):
    """Return an unfitted Pipeline: "preprocess" (ColumnTransformer) then "model"."""
    raise NotImplementedError


def candidate_models():
    """Return {name: unfitted pipeline} for four candidates: "baseline"
    (DummyClassifier most_frequent), "logistic regression", "random forest"
    (200 trees, min_samples_leaf=5) and "gradient boosting"
    (HistGradientBoostingClassifier). All with random_state=42 where it exists."""
    raise NotImplementedError


def folds():
    """The cross-validation folds used everywhere."""
    return StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


def compare_models(models, X_train, y_train):
    """Return a DataFrame with one row per model and columns mean_auc and
    std_auc (5-fold ROC AUC, rounded to 3 places), sorted by mean_auc, best first."""
    raise NotImplementedError


def tune_logistic(X_train, y_train, values=(0.01, 0.1, 1, 10)):
    """Grid-search model__C for the logistic regression pipeline by ROC AUC.
    Return the fitted GridSearchCV."""
    raise NotImplementedError


def evaluate(model, X_test, y_test, threshold=0.5):
    """Return a dict with accuracy, precision, recall and roc_auc on the test
    set (each rounded to 3 places) plus the confusion counts tn, fp, fn, tp
    as ints. Predict churn when the probability is at least `threshold`."""
    raise NotImplementedError


def best_threshold(y_true, probabilities, miss_cost, false_alarm_cost):
    """Return the threshold in 0.05, 0.10, ..., 0.95 with the lowest total
    cost, miss_cost * false negatives + false_alarm_cost * false positives
    (the first on a tie), as a float rounded to 2 places. Pass validation or
    out-of-fold probabilities, never the test set's."""
    raise NotImplementedError


def top_coefficients(fitted_pipeline, count=5):
    """For a fitted logistic regression pipeline, return a Series of the
    `count` coefficients with the largest absolute value, indexed by feature
    name (with the "numeric__" style prefixes removed), keeping their signs
    and ordered by absolute size, largest first. Values rounded to 3 places."""
    raise NotImplementedError


def plot_evaluation(model, X_test, y_test, path):
    """Save a figure with the confusion matrix (left) and the ROC curve (right)."""
    raise NotImplementedError


def main():
    churn = load_churn()
    print(churn_summary(churn))
    X_train, X_test, y_train, y_test = split_data(churn)

    print("\nCross-validated ROC AUC (training data only):")
    print(compare_models(candidate_models(), X_train, y_train).to_string())

    grid = tune_logistic(X_train, y_train)
    print("\nBest C:", grid.best_params_["model__C"], "cross-validated AUC:", round(grid.best_score_, 3))
    final = grid.best_estimator_

    # A missed churner costs 5 times a wasted retention offer. Choose the
    # threshold from out-of-fold training predictions, not from the test set.
    out_of_fold = cross_val_predict(final, X_train, y_train, cv=folds(), method="predict_proba")[:, 1]
    threshold = best_threshold(y_train, out_of_fold, miss_cost=5, false_alarm_cost=1)
    print("\nChosen threshold:", threshold)

    print("\nTest set (used once), threshold 0.5:")
    print(evaluate(final, X_test, y_test))
    print(f"Test set, threshold {threshold}:")
    print(evaluate(final, X_test, y_test, threshold))
    print("\nStrongest coefficients:")
    print(top_coefficients(final, 6).to_string())

    plot_evaluation(final, X_test, y_test, FIGURES / "evaluation.png")
    print("\nSaved", FIGURES / "evaluation.png")


if __name__ == "__main__":
    main()
