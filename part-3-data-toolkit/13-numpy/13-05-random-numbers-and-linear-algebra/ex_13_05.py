"""Exercises for 13-05 Random numbers and linear algebra basics."""
import numpy as np


def dice_rolls(count, seed):
    """Return an int array of `count` dice rolls (1 to 6 inclusive) from
    np.random.default_rng(seed). The same seed must give the same rolls.

    Example: dice_rolls(5, 42) returns array([1, 5, 4, 3, 3])
    """
    raise NotImplementedError


def shuffle_together(features, labels, seed):
    """Shuffle the rows of `features` and the items of `labels` with ONE
    permutation from np.random.default_rng(seed), so they stay matched.
    Return (shuffled_features, shuffled_labels). Do not change the inputs.
    """
    raise NotImplementedError


def predict_linear(features, weights, bias):
    """Return features @ weights + bias: one prediction per row.

    Example: predict_linear(np.array([[1, 2], [3, 4]]), np.array([10, 1]), 0.5)
    returns array([12.5, 34.5])
    """
    raise NotImplementedError


def can_multiply(shape_a, shape_b):
    """Both shapes are 2-tuples. Return True if a matrix of shape_a can be
    multiplied by a matrix of shape_b with @, otherwise False.

    Example: can_multiply((3, 2), (2, 5)) returns True
    """
    raise NotImplementedError


def gram_matrix(features):
    """Return features.T @ features.

    Example: gram_matrix(np.array([[1, 2], [3, 4]])) returns array([[10, 14], [14, 20]])
    """
    raise NotImplementedError
