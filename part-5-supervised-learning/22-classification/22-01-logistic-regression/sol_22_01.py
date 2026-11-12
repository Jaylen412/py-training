"""Solutions for 22-01 Logistic regression."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def sigmoid(z):
    """The logistic function."""
    return 1 / (1 + np.exp(-np.asarray(z, dtype=float)))


def classify(probabilities, threshold=0.5):
    """Turn probabilities into 0/1 labels."""
    return (np.asarray(probabilities) >= threshold).astype(int)


def boundary_value(model):
    """Return where the score of a one-feature model is zero."""
    return float(-model.intercept_[0] / model.coef_[0, 0])


def fit_scaled_logistic(X_train, y_train, C=1.0):
    """Standardise, then fit logistic regression."""
    scaler = StandardScaler().fit(X_train)
    model = LogisticRegression(C=C, max_iter=5000).fit(scaler.transform(X_train), y_train)
    return scaler, model


def most_likely_names(probabilities, class_names):
    """Return the name of the most probable class for each row."""
    return [class_names[index] for index in np.argmax(probabilities, axis=1)]
