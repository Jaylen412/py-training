"""Solutions for 13-05 Random numbers and linear algebra basics."""
import numpy as np


def dice_rolls(count, seed):
    """Return reproducible dice rolls."""
    rng = np.random.default_rng(seed)
    return rng.integers(1, 7, size=count)  # 7 because the upper bound is excluded


def shuffle_together(features, labels, seed):
    """Shuffle features and labels with one shared permutation."""
    order = np.random.default_rng(seed).permutation(len(labels))
    return features[order], labels[order]


def predict_linear(features, weights, bias):
    """Return one linear prediction per row."""
    return features @ weights + bias


def can_multiply(shape_a, shape_b):
    """Return True if the inner dimensions match."""
    return shape_a[1] == shape_b[0]


def gram_matrix(features):
    """Return features.T @ features."""
    return features.T @ features
