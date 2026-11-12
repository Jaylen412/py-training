"""Solutions for 20-02 The scikit-learn interface."""
import numpy as np


def fit_and_predict(model, X, y, new_X):
    """Fit the model, then predict new samples."""
    return model.fit(X, y).predict(new_X)


def as_one_sample(features):
    """Return a one-row 2-D array."""
    return np.asarray(features).reshape(1, -1)


def learned_attributes(model):
    """Return the sorted names of the learned attributes."""
    return sorted(name for name in vars(model) if name.endswith("_") and not name.startswith("_"))


def training_scores(models, X, y):
    """Return {class name: training score} for each model."""
    return {type(model).__name__: round(model.fit(X, y).score(X, y), 3) for model in models}
