"""Exercises for 22-02 Classification metrics.

Labels are 0 (negative) and 1 (positive). Do not use sklearn.metrics.
"""
import numpy as np


def confusion_counts(y_true, y_pred):
    """Return a dictionary {"tn": ..., "fp": ..., "fn": ..., "tp": ...}
    of plain ints.

    Example: confusion_counts([0, 1, 1, 0], [0, 1, 0, 1]) returns
    {"tn": 1, "fp": 1, "fn": 1, "tp": 1}
    """
    raise NotImplementedError


def precision(counts):
    """Return TP / (TP + FP) from a counts dictionary, or 0.0 if nothing
    was predicted positive."""
    raise NotImplementedError


def recall(counts):
    """Return TP / (TP + FN), or 0.0 if there are no actual positives."""
    raise NotImplementedError


def f1(counts):
    """Return 2 * precision * recall / (precision + recall), or 0.0 if both
    are zero."""
    raise NotImplementedError


def metric_summary(y_true, y_pred):
    """Return {"accuracy": ..., "precision": ..., "recall": ..., "f1": ...},
    each rounded to 3 decimal places."""
    raise NotImplementedError
