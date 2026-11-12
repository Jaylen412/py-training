"""Exercises for 22-05 Naive Bayes."""
import numpy as np
from sklearn.naive_bayes import GaussianNB


def class_priors(labels):
    """`labels` holds whole-number classes 0, 1, 2, ... Return a NumPy array
    with the fraction of samples in each class, in class order.

    Example: class_priors(np.array([0, 0, 1, 2])) returns array([0.5, 0.25, 0.25])
    """
    raise NotImplementedError


def gaussian_likelihood(x, mean, std):
    """Return the normal density: exp(-0.5 * ((x - mean) / std) ** 2) /
    (std * sqrt(2 * pi)). Works on numbers and arrays."""
    raise NotImplementedError


def one_feature_posteriors(values, labels, new_value):
    """Naive Bayes with ONE feature, by hand. For each class (0, 1, 2, ...),
    estimate the prior, and the mean and POPULATION standard deviation
    (np.std) of `values` within the class. Multiply each class's likelihood
    at `new_value` by its prior, and divide by the total so the results add
    up to 1. Return the array of posteriors.
    """
    raise NotImplementedError


def naive_bayes_accuracy(X_train, X_test, y_train, y_test):
    """Fit GaussianNB and return its test accuracy rounded to 3 places."""
    raise NotImplementedError
