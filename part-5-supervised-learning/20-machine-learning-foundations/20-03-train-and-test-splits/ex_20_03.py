"""Exercises for 20-03 Train and test splits."""
import numpy as np
from sklearn.base import clone
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def split_data(X, y, test_size=0.25, seed=42):
    """Return train_test_split(X, y, ...) with the given test size and
    random_state=seed, stratified by y. Returns X_train, X_test, y_train, y_test.
    """
    raise NotImplementedError


def train_and_test_scores(model, X, y, seed=42):
    """Split with split_data (default test size), fit `model` on the training
    part, and return (training score, test score), each rounded to 3 places."""
    raise NotImplementedError


def scale_without_leakage(X_train, X_test):
    """Fit a StandardScaler on X_train ONLY, and return
    (scaled X_train, scaled X_test)."""
    raise NotImplementedError


def score_range_over_splits(model, X, y, seeds):
    """For each seed, split with split_data(X, y, seed=seed), fit a fresh copy
    of the model (sklearn.base.clone(model)) on the training part and record
    its test score. Return (lowest score, highest score)."""
    raise NotImplementedError
