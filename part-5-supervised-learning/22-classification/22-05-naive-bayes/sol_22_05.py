"""Solutions for 22-05 Naive Bayes."""
import numpy as np
from sklearn.naive_bayes import GaussianNB


def class_priors(labels):
    """Fraction of samples in each class."""
    labels = np.asarray(labels)
    return np.bincount(labels) / len(labels)


def gaussian_likelihood(x, mean, std):
    """Height of the normal curve at x."""
    x = np.asarray(x, dtype=float)
    return np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))


def one_feature_posteriors(values, labels, new_value):
    """Class probabilities for one feature, by Bayes' rule."""
    values, labels = np.asarray(values, dtype=float), np.asarray(labels)
    priors = class_priors(labels)
    classes = range(len(priors))
    likelihoods = np.array([
        gaussian_likelihood(new_value, values[labels == c].mean(), values[labels == c].std())
        for c in classes
    ])
    unnormalised = likelihoods * priors
    return unnormalised / unnormalised.sum()


def naive_bayes_accuracy(X_train, X_test, y_train, y_test):
    """Test accuracy of Gaussian Naive Bayes."""
    return round(GaussianNB().fit(X_train, y_train).score(X_test, y_test), 3)
