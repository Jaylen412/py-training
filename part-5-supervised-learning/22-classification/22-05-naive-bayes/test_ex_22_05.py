import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

mod = importlib.import_module(
    "sol_22_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_22_05"
)

IRIS = load_iris()


def test_class_priors():
    np.testing.assert_allclose(mod.class_priors(np.array([0, 0, 1, 2])), [0.5, 0.25, 0.25])


def test_class_priors_iris():
    np.testing.assert_allclose(mod.class_priors(IRIS.target), [1 / 3] * 3)


def test_gaussian_likelihood():
    assert mod.gaussian_likelihood(0.0, 0.0, 1.0) == pytest.approx(0.398942, abs=1e-6)
    assert mod.gaussian_likelihood(1.0, 0.0, 1.0) == pytest.approx(0.241971, abs=1e-6)


def test_gaussian_likelihood_array_and_symmetry():
    values = mod.gaussian_likelihood(np.array([4.0, 6.0]), 5.0, 2.0)
    assert values[0] == pytest.approx(values[1])


def test_one_feature_posteriors_matches_hand_example():
    posteriors = mod.one_feature_posteriors(IRIS.data[:, 2], IRIS.target, 4.9)
    np.testing.assert_allclose(posteriors, [0.0, 0.482, 0.518], atol=1e-3)


def test_one_feature_posteriors_matches_gaussiannb():
    values = IRIS.data[:, 3]
    model = GaussianNB(var_smoothing=0).fit(values.reshape(-1, 1), IRIS.target)
    for new_value in [0.3, 1.4, 1.8]:
        np.testing.assert_allclose(
            mod.one_feature_posteriors(values, IRIS.target, new_value),
            model.predict_proba([[new_value]])[0],
            atol=1e-6,
        )


def test_naive_bayes_accuracy_iris():
    parts = train_test_split(IRIS.data, IRIS.target, test_size=0.3, random_state=42, stratify=IRIS.target)
    assert mod.naive_bayes_accuracy(*parts) == 0.911


def test_naive_bayes_accuracy_wine():
    wine = load_wine()
    parts = train_test_split(wine.data, wine.target, test_size=0.3, random_state=42, stratify=wine.target)
    assert mod.naive_bayes_accuracy(*parts) == 1.0
