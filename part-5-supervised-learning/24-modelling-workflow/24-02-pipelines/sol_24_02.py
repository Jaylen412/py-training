"""Solutions for 24-02 Pipelines."""
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
    """Scaling followed by logistic regression."""
    return Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(C=C, max_iter=1000))])


def churn_pipeline(model):
    """Churn preprocessing followed by `model`."""
    preprocess = ColumnTransformer([
        ("numeric", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), NUMERIC),
        ("nominal", make_pipeline(SimpleImputer(strategy="most_frequent"),
                                  OneHotEncoder(handle_unknown="ignore")), NOMINAL),
        ("ordered", make_pipeline(SimpleImputer(strategy="most_frequent"),
                                  OrdinalEncoder(categories=[SATISFACTION_ORDER])), ORDERED),
    ])
    return Pipeline([("preprocess", preprocess), ("model", model)])


def save_and_reload(pipeline, path):
    """Round-trip a pipeline through a joblib file."""
    joblib.dump(pipeline, path)
    return joblib.load(path)


def leaky_and_honest_scores(X, y, k=20):
    """Feature selection outside versus inside cross-validation."""
    selected = SelectKBest(f_classif, k=k).fit_transform(X, y)
    leaky = cross_val_score(LogisticRegression(), selected, y, cv=5).mean()
    honest = cross_val_score(make_pipeline(SelectKBest(f_classif, k=k), LogisticRegression()), X, y, cv=5).mean()
    return round(float(leaky), 3), round(float(honest), 3)
