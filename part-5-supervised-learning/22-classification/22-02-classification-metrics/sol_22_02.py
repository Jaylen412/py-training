"""Solutions for 22-02 Classification metrics."""
import numpy as np


def confusion_counts(y_true, y_pred):
    """Count TN, FP, FN and TP."""
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    return {
        "tn": int(np.sum((y_true == 0) & (y_pred == 0))),
        "fp": int(np.sum((y_true == 0) & (y_pred == 1))),
        "fn": int(np.sum((y_true == 1) & (y_pred == 0))),
        "tp": int(np.sum((y_true == 1) & (y_pred == 1))),
    }


def precision(counts):
    """Fraction of predicted positives that are correct."""
    predicted_positive = counts["tp"] + counts["fp"]
    return counts["tp"] / predicted_positive if predicted_positive else 0.0


def recall(counts):
    """Fraction of actual positives that were found."""
    actual_positive = counts["tp"] + counts["fn"]
    return counts["tp"] / actual_positive if actual_positive else 0.0


def f1(counts):
    """Harmonic mean of precision and recall."""
    p, r = precision(counts), recall(counts)
    return 2 * p * r / (p + r) if p + r else 0.0


def metric_summary(y_true, y_pred):
    """Return accuracy, precision, recall and F1."""
    counts = confusion_counts(y_true, y_pred)
    accuracy = (counts["tp"] + counts["tn"]) / len(np.asarray(y_true))
    return {
        "accuracy": round(accuracy, 3),
        "precision": round(precision(counts), 3),
        "recall": round(recall(counts), 3),
        "f1": round(f1(counts), 3),
    }
