"""Exercises for 22-03 Thresholds, ROC and precision-recall curves.

`y_true` is an array of 0/1 labels; `probabilities` is an array of
predicted P(class 1).
"""
import numpy as np
from sklearn.metrics import precision_score, recall_score, roc_auc_score


def precision_recall_at(y_true, probabilities, threshold):
    """Predict 1 where probability >= threshold. Return (precision, recall)
    as floats, using zero_division=0 for precision."""
    raise NotImplementedError


def lowest_cost_threshold(y_true, probabilities, miss_cost, false_alarm_cost, thresholds):
    """For each threshold, total cost = miss_cost * (false negatives) +
    false_alarm_cost * (false positives). Return the threshold with the
    lowest total cost (the first on a tie), as a float."""
    raise NotImplementedError


def threshold_for_recall(y_true, probabilities, required_recall, thresholds):
    """Return the HIGHEST threshold in `thresholds` whose recall is at least
    `required_recall`, or None if no threshold achieves it."""
    raise NotImplementedError


def auc(y_true, probabilities):
    """Return the area under the ROC curve, as a float."""
    raise NotImplementedError
