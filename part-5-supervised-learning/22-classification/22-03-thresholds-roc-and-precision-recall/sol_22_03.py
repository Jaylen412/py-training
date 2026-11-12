"""Solutions for 22-03 Thresholds, ROC and precision-recall curves."""
import numpy as np
from sklearn.metrics import precision_score, recall_score, roc_auc_score


def precision_recall_at(y_true, probabilities, threshold):
    """Return (precision, recall) at a threshold."""
    predictions = (np.asarray(probabilities) >= threshold).astype(int)
    return (
        float(precision_score(y_true, predictions, zero_division=0)),
        float(recall_score(y_true, predictions)),
    )


def lowest_cost_threshold(y_true, probabilities, miss_cost, false_alarm_cost, thresholds):
    """Return the threshold with the smallest total cost."""
    y_true = np.asarray(y_true)
    costs = []
    for threshold in thresholds:
        flagged = np.asarray(probabilities) >= threshold
        misses = np.sum(~flagged & (y_true == 1))
        false_alarms = np.sum(flagged & (y_true == 0))
        costs.append(miss_cost * misses + false_alarm_cost * false_alarms)
    return float(thresholds[int(np.argmin(costs))])


def threshold_for_recall(y_true, probabilities, required_recall, thresholds):
    """Return the highest threshold that still achieves the required recall."""
    good = [t for t in thresholds if precision_recall_at(y_true, probabilities, t)[1] >= required_recall]
    return float(max(good)) if good else None


def auc(y_true, probabilities):
    """Return the ROC AUC."""
    return float(roc_auc_score(y_true, probabilities))
