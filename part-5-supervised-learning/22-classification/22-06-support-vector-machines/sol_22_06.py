"""Solutions for 22-06 Support vector machines."""
import numpy as np
from sklearn.svm import SVC


def svm_test_accuracy(X_train, X_test, y_train, y_test, kernel="rbf", C=1.0, gamma="scale"):
    """Return the test accuracy of an SVC."""
    model = SVC(kernel=kernel, C=C, gamma=gamma).fit(X_train, y_train)
    return round(model.score(X_test, y_test), 3)


def support_vector_count(model):
    """Return the number of support vectors."""
    return int(len(model.support_vectors_))


def best_gamma(X_train, X_test, y_train, y_test, gammas):
    """Return the gamma with the highest test accuracy."""
    scores = [svm_test_accuracy(X_train, X_test, y_train, y_test, gamma=gamma) for gamma in gammas]
    return gammas[int(np.argmax(scores))]


def add_squared_distance(X):
    """Append each row's squared distance from the origin."""
    X = np.asarray(X, dtype=float)
    return np.hstack([X, (X ** 2).sum(axis=1, keepdims=True)])
