import importlib
import os

import numpy as np

mod = importlib.import_module(
    "sol_13_05" if os.environ.get("COURSE_SOLUTIONS") else "ex_13_05"
)


def test_dice_rolls_known_seed():
    np.testing.assert_array_equal(mod.dice_rolls(5, 42), np.random.default_rng(42).integers(1, 7, 5))


def test_dice_rolls_range_and_repeatable():
    rolls = mod.dice_rolls(10_000, 7)
    assert rolls.min() == 1 and rolls.max() == 6
    np.testing.assert_array_equal(rolls, mod.dice_rolls(10_000, 7))


def test_shuffle_together_keeps_rows_matched():
    features = np.array([[1, 10], [2, 20], [3, 30], [4, 40], [5, 50]])
    labels = np.array([1, 2, 3, 4, 5])
    shuffled_features, shuffled_labels = mod.shuffle_together(features, labels, 42)
    np.testing.assert_array_equal(shuffled_features[:, 0], shuffled_labels)
    assert sorted(shuffled_labels.tolist()) == [1, 2, 3, 4, 5]


def test_shuffle_together_uses_seed_and_leaves_inputs():
    features = np.arange(20).reshape(10, 2)
    labels = np.arange(10)
    first = mod.shuffle_together(features, labels, 1)
    second = mod.shuffle_together(features, labels, 1)
    np.testing.assert_array_equal(first[1], second[1])
    np.testing.assert_array_equal(labels, np.arange(10))
    assert not np.array_equal(first[1], labels)


def test_predict_linear():
    result = mod.predict_linear(np.array([[1, 2], [3, 4]]), np.array([10, 1]), 0.5)
    np.testing.assert_allclose(result, [12.5, 34.5])


def test_predict_linear_zero_weights():
    result = mod.predict_linear(np.ones((3, 4)), np.zeros(4), 2.0)
    np.testing.assert_allclose(result, [2, 2, 2])


def test_can_multiply():
    assert mod.can_multiply((3, 2), (2, 5)) is True
    assert mod.can_multiply((3, 2), (3, 2)) is False


def test_can_multiply_square():
    assert mod.can_multiply((4, 4), (4, 4)) is True


def test_gram_matrix():
    np.testing.assert_array_equal(mod.gram_matrix(np.array([[1, 2], [3, 4]])), [[10, 14], [14, 20]])


def test_gram_matrix_shape_and_symmetry():
    result = mod.gram_matrix(np.random.default_rng(0).random((10, 3)))
    assert result.shape == (3, 3)
    np.testing.assert_allclose(result, result.T)
