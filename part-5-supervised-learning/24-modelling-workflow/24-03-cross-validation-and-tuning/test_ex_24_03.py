import importlib
import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from sklearn.compose import ColumnTransformer
from sklearn.datasets import load_iris
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler
from sklearn.tree import DecisionTreeClassifier

mod = importlib.import_module(
    "sol_24_03" if os.environ.get("COURSE_SOLUTIONS") else "ex_24_03"
)

DATA = Path(__file__).resolve().parents[3] / "data"
CHURN = pd.read_csv(DATA / "customer_churn.csv")
X = CHURN.drop(columns=["customer_id", "churned"])
Y = CHURN["churned"]
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)


def churn_pipeline(model):
    preprocess = ColumnTransformer([
        ("numeric", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()),
         ["tenure_months", "monthly_charges", "total_charges", "support_calls"]),
        ("nominal", make_pipeline(SimpleImputer(strategy="most_frequent"), OneHotEncoder(handle_unknown="ignore")),
         ["contract", "payment_method", "internet_service", "region"]),
        ("ordered", make_pipeline(SimpleImputer(strategy="most_frequent"),
                                  OrdinalEncoder(categories=[["low", "medium", "high"]])), ["satisfaction"]),
    ])
    return Pipeline([("preprocess", preprocess), ("model", model)])


def test_kfold_scores_matches_lesson():
    scores = mod.kfold_scores(churn_pipeline(LogisticRegression(max_iter=1000)), X_TRAIN, Y_TRAIN)
    np.testing.assert_allclose(scores, [0.762, 0.816, 0.772, 0.819, 0.778], atol=1e-3)


def test_kfold_scores_numpy_and_unfitted_original():
    iris = load_iris()
    model = DecisionTreeClassifier(random_state=42)
    scores = mod.kfold_scores(model, iris.data, iris.target, n_splits=3)
    assert len(scores) == 3 and all(type(s) is float for s in scores)
    assert not hasattr(model, "tree_")


def test_compare_with_cv():
    models = {
        "logistic": churn_pipeline(LogisticRegression(max_iter=1000)),
        "boosting": churn_pipeline(HistGradientBoostingClassifier(random_state=42)),
    }
    assert mod.compare_with_cv(models, X_TRAIN, Y_TRAIN, scoring="roc_auc") == {"logistic": 0.814, "boosting": 0.76}


def test_compare_with_cv_default_accuracy():
    result = mod.compare_with_cv({"logistic": churn_pipeline(LogisticRegression(max_iter=1000))}, X_TRAIN, Y_TRAIN)
    assert result == {"logistic": 0.791}


def test_tune_c():
    best_c, best_score, best_model = mod.tune_c(churn_pipeline(LogisticRegression(max_iter=1000)),
                                                X_TRAIN, Y_TRAIN, [0.01, 0.1, 1, 10])
    assert (best_c, best_score) == (0.1, 0.815)
    assert best_model.named_steps["model"].C == 0.1


def test_tune_c_single_value():
    best_c, _, _ = mod.tune_c(churn_pipeline(LogisticRegression(max_iter=1000)), X_TRAIN, Y_TRAIN, [5])
    assert best_c == 5


def test_final_test_auc():
    _, _, best_model = mod.tune_c(churn_pipeline(LogisticRegression(max_iter=1000)),
                                  X_TRAIN, Y_TRAIN, [0.01, 0.1, 1, 10])
    assert mod.final_test_auc(best_model, X_TEST, Y_TEST) == 0.837


def test_final_test_auc_perfect():
    class Perfect:
        def predict_proba(self, X):
            return np.column_stack([1 - X, X])

    assert mod.final_test_auc(Perfect(), np.array([0.1, 0.9]), np.array([0, 1])) == 1.0
