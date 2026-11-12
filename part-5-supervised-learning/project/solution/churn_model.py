"""Part 5 project: predict customer churn (reference solution).

Run from the repository root:
    python part-5-supervised-learning/project/solution/churn_model.py
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
    missing = df.isna().sum()
    return {
        "rows": len(df),
        "churn_rate": round(float(df["churned"].mean()), 3),
        "missing": missing[missing > 0].to_dict(),
        "churn_by_contract": df.groupby("contract")["churned"].mean().round(3).to_dict(),
    }


def split_data(df, test_size=0.2):
    """Drop customer_id, split into X_train, X_test, y_train, y_test (stratified,
    random_state=42)."""
    X = df.drop(columns=["customer_id", "churned"])
    y = df["churned"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)


def build_pipeline(model):
    """Return an unfitted Pipeline: "preprocess" (ColumnTransformer) then "model"."""
    preprocess = ColumnTransformer([
        ("numeric", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), NUMERIC),
        ("nominal", make_pipeline(SimpleImputer(strategy="most_frequent"),
                                  OneHotEncoder(handle_unknown="ignore")), NOMINAL),
        ("ordered", make_pipeline(SimpleImputer(strategy="most_frequent"),
                                  OrdinalEncoder(categories=[SATISFACTION_ORDER])), ORDERED),
    ])
    return Pipeline([("preprocess", preprocess), ("model", model)])


def candidate_models():
    """Return {name: unfitted pipeline} for four candidates: "baseline"
    (DummyClassifier most_frequent), "logistic regression", "random forest"
    (200 trees, min_samples_leaf=5) and "gradient boosting"
    (HistGradientBoostingClassifier). All with random_state=42 where it exists."""
    return {
        "baseline": build_pipeline(DummyClassifier(strategy="most_frequent")),
        "logistic regression": build_pipeline(LogisticRegression(max_iter=1000)),
        "random forest": build_pipeline(
            RandomForestClassifier(n_estimators=200, min_samples_leaf=5, random_state=42)),
        "gradient boosting": build_pipeline(HistGradientBoostingClassifier(random_state=42)),
    }


def folds():
    """The cross-validation folds used everywhere."""
    return StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


def compare_models(models, X_train, y_train):
    """Return a DataFrame with one row per model and columns mean_auc and
    std_auc (5-fold ROC AUC, rounded to 3 places), sorted by mean_auc, best first."""
    rows = {}
    for name, model in models.items():
        scores = cross_val_score(model, X_train, y_train, cv=folds(), scoring="roc_auc")
        rows[name] = {"mean_auc": round(float(scores.mean()), 3), "std_auc": round(float(scores.std()), 3)}
    return pd.DataFrame(rows).T.sort_values("mean_auc", ascending=False)


def tune_logistic(X_train, y_train, values=(0.01, 0.1, 1, 10)):
    """Grid-search model__C for the logistic regression pipeline by ROC AUC.
    Return the fitted GridSearchCV."""
    pipeline = build_pipeline(LogisticRegression(max_iter=1000))
    grid = GridSearchCV(pipeline, {"model__C": list(values)}, cv=folds(), scoring="roc_auc")
    return grid.fit(X_train, y_train)


def evaluate(model, X_test, y_test, threshold=0.5):
    """Return a dict with accuracy, precision, recall and roc_auc on the test
    set (each rounded to 3 places) plus the confusion counts tn, fp, fn, tp
    as ints. Predict churn when the probability is at least `threshold`."""
    probabilities = model.predict_proba(X_test)[:, 1]
    predicted = (probabilities >= threshold).astype(int)
    tn = int(np.sum((y_test == 0) & (predicted == 0)))
    fp = int(np.sum((y_test == 0) & (predicted == 1)))
    fn = int(np.sum((y_test == 1) & (predicted == 0)))
    tp = int(np.sum((y_test == 1) & (predicted == 1)))
    return {
        "accuracy": round(float(accuracy_score(y_test, predicted)), 3),
        "precision": round(float(precision_score(y_test, predicted, zero_division=0)), 3),
        "recall": round(float(recall_score(y_test, predicted)), 3),
        "roc_auc": round(float(roc_auc_score(y_test, probabilities)), 3),
        "tn": tn, "fp": fp, "fn": fn, "tp": tp,
    }


def best_threshold(y_true, probabilities, miss_cost, false_alarm_cost):
    """Return the threshold in 0.05, 0.10, ..., 0.95 with the lowest total
    cost, miss_cost * false negatives + false_alarm_cost * false positives
    (the first on a tie), as a float rounded to 2 places. Pass validation or
    out-of-fold probabilities, never the test set's."""
    y_true = np.asarray(y_true)
    best, best_cost = None, None
    for threshold in np.round(np.arange(0.05, 1.0, 0.05), 2):
        flagged = np.asarray(probabilities) >= threshold
        cost = miss_cost * np.sum(~flagged & (y_true == 1)) + false_alarm_cost * np.sum(flagged & (y_true == 0))
        if best_cost is None or cost < best_cost:
            best, best_cost = float(threshold), cost
    return best


def top_coefficients(fitted_pipeline, count=5):
    """For a fitted logistic regression pipeline, return a Series of the
    `count` coefficients with the largest absolute value, indexed by feature
    name (with the "numeric__" style prefixes removed), keeping their signs
    and ordered by absolute size, largest first. Values rounded to 3 places."""
    names = fitted_pipeline.named_steps["preprocess"].get_feature_names_out()
    names = [name.split("__", 1)[1] for name in names]
    coefficients = pd.Series(fitted_pipeline.named_steps["model"].coef_[0], index=names)
    order = coefficients.abs().sort_values(ascending=False).index[:count]
    return coefficients[order].round(3)


def plot_evaluation(model, X_test, y_test, path):
    """Save a figure with the confusion matrix (left) and the ROC curve (right)."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, ax=axes[0], colorbar=False)
    axes[0].set_title("Confusion matrix (threshold 0.5)")
    RocCurveDisplay.from_estimator(model, X_test, y_test, ax=axes[1])
    axes[1].plot([0, 1], [0, 1], linestyle="--", color="grey")
    axes[1].set_title("ROC curve")
    fig.savefig(path, dpi=100, bbox_inches="tight")
    plt.close(fig)


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
