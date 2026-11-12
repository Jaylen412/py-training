import importlib
import os

import numpy as np
from sklearn.datasets import load_diabetes, load_iris
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

mod = importlib.import_module(
    "sol_20_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_20_02"
)

IRIS = load_iris()


def test_fit_and_predict():
    new = np.array([[5.0, 3.4, 1.5, 0.2], [6.7, 3.0, 5.2, 2.3]])
    predictions = mod.fit_and_predict(KNeighborsClassifier(), IRIS.data, IRIS.target, new)
    np.testing.assert_array_equal(predictions, [0, 2])


def test_fit_and_predict_regression():
    X = np.array([[1.0], [2.0], [3.0]])
    predictions = mod.fit_and_predict(LinearRegression(), X, 2 * X[:, 0] + 1, np.array([[10.0]]))
    np.testing.assert_allclose(predictions, [21.0])


def test_as_one_sample():
    result = mod.as_one_sample(np.array([5.0, 3.4, 1.5, 0.2]))
    assert result.shape == (1, 4)
    model = KNeighborsClassifier().fit(IRIS.data, IRIS.target)
    assert model.predict(result)[0] == 0


def test_as_one_sample_list():
    assert mod.as_one_sample([1, 2, 3]).shape == (1, 3)


def test_learned_attributes_linear_regression():
    diabetes = load_diabetes()
    names = mod.learned_attributes(LinearRegression().fit(diabetes.data, diabetes.target))
    assert "coef_" in names and "intercept_" in names
    assert names == sorted(names)
    assert "fit_intercept" not in names


def test_learned_attributes_unfitted():
    assert mod.learned_attributes(LinearRegression()) == []


def test_training_scores():
    scores = mod.training_scores(
        [KNeighborsClassifier(), DecisionTreeClassifier(random_state=42)], IRIS.data, IRIS.target
    )
    assert scores == {"KNeighborsClassifier": 0.967, "DecisionTreeClassifier": 1.0}


def test_training_scores_empty():
    assert mod.training_scores([], IRIS.data, IRIS.target) == {}
