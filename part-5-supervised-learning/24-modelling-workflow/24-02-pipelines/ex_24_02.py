"""Exercises for 24-02 Pipelines."""
import joblib
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

NUMERIC = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
NOMINAL = ["contract", "payment_method", "internet_service", "region"]
ORDERED = ["satisfaction"]
SATISFACTION_ORDER = ["low", "medium", "high"]


def scaled_logistic_pipeline(C=1.0):
    """Return an unfitted Pipeline with steps named "scale" (StandardScaler)
    and "model" (LogisticRegression(C=C, max_iter=1000))."""
    raise NotImplementedError


def churn_pipeline(model):
    """Return an unfitted Pipeline with two steps:
    - "preprocess": a ColumnTransformer with parts "numeric" (median
      imputation, then scaling) for NUMERIC, "nominal" (most-frequent
      imputation, then OneHotEncoder(handle_unknown="ignore")) for NOMINAL,
      and "ordered" (most-frequent imputation, then
      OrdinalEncoder(categories=[SATISFACTION_ORDER])) for ORDERED;
    - "model": the `model` passed in.
    """
    raise NotImplementedError


def save_and_reload(pipeline, path):
    """Save `pipeline` to `path` with joblib, load it back, and return the
    loaded object."""
    raise NotImplementedError


def leaky_and_honest_scores(X, y, k=20):
    """Return (leaky, honest) mean 5-fold cross_val_score accuracies:
    - leaky: run SelectKBest(f_classif, k=k) on ALL of X and y first, then
      cross-validate LogisticRegression() on the selected features;
    - honest: cross-validate make_pipeline(SelectKBest(f_classif, k=k),
      LogisticRegression()) on X.
    Both as floats rounded to 3 places.
    """
    raise NotImplementedError
