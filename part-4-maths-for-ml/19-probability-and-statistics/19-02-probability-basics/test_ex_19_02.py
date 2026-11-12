import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import load_breast_cancer

mod = importlib.import_module(
    "sol_19_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_19_02"
)

DATA = load_breast_cancer(as_frame=True).frame
MALIGNANT = (DATA["target"] == 0).to_numpy()
LARGE = (DATA["mean radius"] > 15).to_numpy()


def test_probability():
    assert mod.probability(np.array([True, False, True, True])) == 0.75
    assert mod.probability(MALIGNANT) == pytest.approx(0.3726, abs=1e-4)


def test_conditional_probability():
    a = np.array([1, 1, 0, 0], dtype=bool)
    b = np.array([1, 0, 1, 0], dtype=bool)
    assert mod.conditional_probability(a, b) == 0.5


def test_conditional_probability_breast_cancer():
    assert mod.conditional_probability(MALIGNANT, LARGE) == pytest.approx(161 / 173)
    assert mod.conditional_probability(MALIGNANT, ~LARGE) == pytest.approx(51 / 396)


def test_conditional_probability_impossible_condition():
    with pytest.raises(ValueError):
        mod.conditional_probability(np.array([True]), np.array([False]))


def test_are_independent():
    rng = np.random.default_rng(0)
    coin = rng.integers(0, 2, size=100_000) == 1
    six = rng.integers(1, 7, size=100_000) == 6
    assert mod.are_independent(coin, six) is True


def test_are_dependent():
    assert mod.are_independent(MALIGNANT, LARGE) is False


def test_bayes_posterior():
    assert mod.bayes_posterior(0.01, 0.95, 0.05) == pytest.approx(0.1610, abs=1e-4)


def test_bayes_posterior_edge_cases():
    assert mod.bayes_posterior(0.5, 0.9, 0.1) == pytest.approx(0.9)
    assert mod.bayes_posterior(0.01, 1.0, 0.0) == pytest.approx(1.0)


def test_simulate_two_dice():
    assert mod.simulate_two_dice(7, 200_000, 1) == pytest.approx(1 / 6, abs=0.005)
    assert mod.simulate_two_dice(2, 200_000, 1) == pytest.approx(1 / 36, abs=0.002)


def test_simulate_two_dice_is_repeatable_and_impossible_totals():
    assert mod.simulate_two_dice(7, 1000, 5) == mod.simulate_two_dice(7, 1000, 5)
    assert mod.simulate_two_dice(13, 1000, 5) == 0.0
