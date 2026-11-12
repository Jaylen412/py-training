import importlib
import os
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

mod = importlib.import_module(
    "sol_24_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_24_02"
)

DATA = Path(__file__).resolve().parents[3] / "data"
CHURN = pd.read_csv(DATA / "customer_churn.csv")
X = CHURN.drop(columns=["customer_id", "churned"])
Y = CHURN["churned"]
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = train_test_split(X, Y, test_size=0.2, random_state=42, stratify=Y)


def test_scaled_logistic_pipeline():
    cancer = load_breast_cancer()
    Xc_train, Xc_test, yc_train, yc_test = train_test_split(
        cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
    )
    pipe = mod.scaled_logistic_pipeline()
    assert list(pipe.named_steps) == ["scale", "model"]
    assert round(pipe.fit(Xc_train, yc_train).score(Xc_test, yc_test), 3) == 0.986


def test_scaled_logistic_pipeline_passes_c():
    assert mod.scaled_logistic_pipeline(C=0.1).named_steps["model"].C == 0.1


def test_churn_pipeline_logistic():
    pipe = mod.churn_pipeline(LogisticRegression(max_iter=1000))
    assert isinstance(pipe, Pipeline) and list(pipe.named_steps) == ["preprocess", "model"]
    assert round(pipe.fit(X_TRAIN, Y_TRAIN).score(X_TEST, Y_TEST), 3) == 0.797


def test_churn_pipeline_other_model_and_unknown_category():
    pipe = mod.churn_pipeline(HistGradientBoostingClassifier(random_state=42)).fit(X_TRAIN, Y_TRAIN)
    assert round(pipe.score(X_TEST, Y_TEST), 3) == 0.76
    odd = X_TEST.head(2).copy()
    odd["region"] = "Moon"
    assert pipe.predict(odd).shape == (2,)


def test_save_and_reload(tmp_path):
    pipe = mod.churn_pipeline(LogisticRegression(max_iter=1000)).fit(X_TRAIN, Y_TRAIN)
    path = tmp_path / "model.joblib"
    loaded = mod.save_and_reload(pipe, path)
    assert path.exists()
    np.testing.assert_array_equal(loaded.predict_proba(X_TEST), pipe.predict_proba(X_TEST))


def test_save_and_reload_is_a_copy(tmp_path):
    pipe = mod.scaled_logistic_pipeline()
    assert mod.save_and_reload(pipe, tmp_path / "p.joblib") is not pipe


def test_leaky_and_honest_scores():
    rng = np.random.default_rng(42)
    noise = rng.normal(size=(100, 5000))
    labels = rng.integers(0, 2, size=100)
    assert mod.leaky_and_honest_scores(noise, labels) == (0.89, 0.52)


def test_leaky_and_honest_scores_types():
    rng = np.random.default_rng(0)
    leaky, honest = mod.leaky_and_honest_scores(rng.normal(size=(60, 200)), rng.integers(0, 2, size=60), k=5)
    assert type(leaky) is float and type(honest) is float
    assert leaky > honest
