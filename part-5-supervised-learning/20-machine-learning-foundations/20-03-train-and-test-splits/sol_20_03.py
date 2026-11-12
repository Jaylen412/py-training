"""Solutions for 20-03 Train and test splits."""
import numpy as np
from sklearn.base import clone
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def split_data(X, y, test_size=0.25, seed=42):
    """Return a stratified, repeatable train/test split."""
    return train_test_split(X, y, test_size=test_size, random_state=seed, stratify=y)


def train_and_test_scores(model, X, y, seed=42):
    """Return (training score, test score)."""
    X_train, X_test, y_train, y_test = split_data(X, y, seed=seed)
    model.fit(X_train, y_train)
    return round(model.score(X_train, y_train), 3), round(model.score(X_test, y_test), 3)


def scale_without_leakage(X_train, X_test):
    """Standardise both sets using statistics from the training set only."""
    scaler = StandardScaler().fit(X_train)
    return scaler.transform(X_train), scaler.transform(X_test)


def score_range_over_splits(model, X, y, seeds):
    """Return the lowest and highest test score over several splits."""
    scores = []
    for seed in seeds:
        X_train, X_test, y_train, y_test = split_data(X, y, seed=seed)
        # clone gives an unfitted copy with the same hyperparameters.
        scores.append(clone(model).fit(X_train, y_train).score(X_test, y_test))
    return min(scores), max(scores)
