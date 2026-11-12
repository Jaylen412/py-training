import importlib
import os

import pytest

mod = importlib.import_module(
    "sol_09_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_09_05"
)


def test_median_predictor_odd():
    model = mod.MedianPredictor().fit([[1], [2], [3]], [10, 30, 20])
    assert model.median_ == 20
    assert model.predict([[5], [6]]) == [20, 20]


def test_median_predictor_even_and_chaining():
    predictions = mod.MedianPredictor().fit([[1]] * 4, [1, 2, 3, 10]).predict([[0]])
    assert predictions == [2.5]


def test_median_predictor_errors():
    with pytest.raises(RuntimeError, match="fit"):
        mod.MedianPredictor().predict([[1]])
    with pytest.raises(ValueError):
        mod.MedianPredictor().fit([], [])


def test_majority_classifier():
    model = mod.MajorityClassifier().fit([[0]] * 5, ["cat", "dog", "dog", "cat", "dog"])
    assert model.majority_ == "dog"
    assert model.classes_ == ["cat", "dog"]
    assert model.predict([[1], [2]]) == ["dog", "dog"]


def test_majority_classifier_tie_goes_to_first_seen():
    model = mod.MajorityClassifier().fit([[0]] * 4, ["b", "a", "a", "b"])
    assert model.majority_ == "b"


def test_majority_classifier_score():
    model = mod.MajorityClassifier().fit([[0]] * 3, ["yes", "yes", "no"])
    assert model.score([[0]] * 4, ["yes", "no", "yes", "yes"]) == pytest.approx(0.75)


def test_majority_classifier_not_fitted():
    with pytest.raises(RuntimeError, match="fit"):
        mod.MajorityClassifier().predict([[1]])


def test_range_scaler():
    scaler = mod.RangeScaler().fit([10, 20, 30])
    assert (scaler.min_, scaler.max_) == (10, 30)
    assert scaler.transform([20, 40]) == pytest.approx([0.5, 1.5])


def test_range_scaler_fit_transform():
    assert mod.RangeScaler().fit_transform([0, 5, 10]) == pytest.approx([0.0, 0.5, 1.0])


def test_range_scaler_constant_values():
    assert mod.RangeScaler().fit_transform([7, 7]) == [0.0, 0.0]


def test_range_scaler_errors():
    with pytest.raises(RuntimeError, match="fit"):
        mod.RangeScaler().transform([1])
    with pytest.raises(ValueError):
        mod.RangeScaler().fit([])
