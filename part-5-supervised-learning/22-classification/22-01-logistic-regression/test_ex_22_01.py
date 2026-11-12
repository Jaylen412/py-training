import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

mod = importlib.import_module(
    "sol_22_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_22_01"
)

CANCER = load_breast_cancer()


def test_sigmoid_values():
    assert mod.sigmoid(0) == pytest.approx(0.5)
    np.testing.assert_allclose(mod.sigmoid(np.array([-5, -1, 1, 5])), [0.0067, 0.2689, 0.7311, 0.9933], atol=1e-4)


def test_sigmoid_symmetry_and_range():
    z = np.linspace(-20, 20, 41)
    values = mod.sigmoid(z)
    assert ((values > 0) & (values < 1)).all()
    np.testing.assert_allclose(values + mod.sigmoid(-z), 1)


def test_classify():
    np.testing.assert_array_equal(mod.classify(np.array([0.1, 0.5, 0.9])), [0, 1, 1])


def test_classify_custom_threshold():
    np.testing.assert_array_equal(mod.classify(np.array([0.1, 0.5, 0.9]), threshold=0.95), [0, 0, 0])
    assert mod.classify(np.array([0.3]), threshold=0.2).dtype.kind == "i"


def test_boundary_value():
    is_malignant = (CANCER.target == 0).astype(int)
    model = LogisticRegression().fit(CANCER.data[:, [0]], is_malignant)
    boundary = mod.boundary_value(model)
    assert boundary == pytest.approx(14.76, abs=0.01)
    assert model.predict_proba([[boundary]])[0, 1] == pytest.approx(0.5)


def test_fit_scaled_logistic():
    X_train, X_test, y_train, y_test = train_test_split(
        CANCER.data, CANCER.target, test_size=0.25, random_state=42, stratify=CANCER.target
    )
    scaler, model = mod.fit_scaled_logistic(X_train, y_train)
    assert model.score(scaler.transform(X_test), y_test) == pytest.approx(0.986, abs=1e-3)
    np.testing.assert_allclose(scaler.mean_, X_train.mean(axis=0))


def test_fit_scaled_logistic_small_c_shrinks_coefficients():
    X_train, _, y_train, _ = train_test_split(CANCER.data, CANCER.target, test_size=0.25, random_state=42)
    _, strong = mod.fit_scaled_logistic(X_train, y_train, C=0.001)
    _, weak = mod.fit_scaled_logistic(X_train, y_train, C=100)
    assert np.abs(strong.coef_).max() < np.abs(weak.coef_).max()


def test_most_likely_names():
    probabilities = np.array([[0.2, 0.8], [0.6, 0.4]])
    assert mod.most_likely_names(probabilities, ["no", "yes"]) == ["yes", "no"]


def test_most_likely_names_three_classes():
    probabilities = np.array([[0.1, 0.2, 0.7]])
    assert mod.most_likely_names(probabilities, ["setosa", "versicolor", "virginica"]) == ["virginica"]
