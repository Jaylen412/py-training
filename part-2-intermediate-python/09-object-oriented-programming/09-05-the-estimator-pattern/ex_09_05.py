"""Exercises for 09-05 The estimator pattern.

Follow the rules from the lesson: hyperparameters in __init__, learned
attributes ending in "_" set in fit, fit returns self, and using the object
before fit raises RuntimeError.
"""


class MedianPredictor:
    """Predicts the median of the training targets for every row."""

    def fit(self, features, targets):
        """Store the median of `targets` as self.median_ and return self.
        Raise ValueError if `targets` is empty.
        (The median is the middle value after sorting; with an even number
        of values it is the mean of the two middle values.)
        """
        raise NotImplementedError

    def predict(self, features):
        """Return a list with self.median_ once per row of `features`.
        Raise RuntimeError with a message mentioning fit() if fit has not been called.

        Example: after fit([[1], [2], [3]], [10, 30, 20]),
        predict([[5], [6]]) returns [20, 20]
        """
        raise NotImplementedError


class MajorityClassifier:
    """Predicts the most common training label for every row."""

    def fit(self, features, labels):
        """Store the most common label as self.majority_ (on a tie, the label
        that appears first in `labels`), store the sorted list of distinct
        labels as self.classes_, and return self.
        """
        raise NotImplementedError

    def predict(self, features):
        """Return self.majority_ once per row. Raise RuntimeError with a message mentioning fit() if not fitted."""
        raise NotImplementedError

    def score(self, features, labels):
        """Return the accuracy: the fraction of rows whose prediction equals
        the true label.

        Example: if 3 of 4 predictions are right, returns 0.75
        """
        raise NotImplementedError


class RangeScaler:
    """Rescales numbers to between 0 and 1, using the training minimum and maximum.

    `values` here is a plain list of numbers (one feature).
    """

    def fit(self, values):
        """Store self.min_ and self.max_ and return self.
        Raise ValueError if `values` is empty."""
        raise NotImplementedError

    def transform(self, values):
        """Return [(value - min_) / (max_ - min_) for each value].
        If max_ equals min_, return 0.0 for every value.
        Raise RuntimeError with a message mentioning fit() if not fitted.

        Example: after fit([10, 20, 30]), transform([20, 40]) returns [0.5, 1.5]
        """
        raise NotImplementedError

    def fit_transform(self, values):
        """Fit on `values`, then transform them."""
        raise NotImplementedError
