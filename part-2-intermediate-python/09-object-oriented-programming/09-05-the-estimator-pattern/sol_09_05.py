"""Solutions for 09-05 The estimator pattern."""
from collections import Counter


class MedianPredictor:
    def fit(self, features, targets):
        if len(targets) == 0:
            raise ValueError("cannot fit on empty data")
        ordered = sorted(targets)
        middle = len(ordered) // 2
        if len(ordered) % 2 == 1:
            self.median_ = ordered[middle]
        else:
            self.median_ = (ordered[middle - 1] + ordered[middle]) / 2
        return self

    def predict(self, features):
        if not hasattr(self, "median_"):
            raise RuntimeError("call fit() before predict()")
        return [self.median_ for _ in features]


class MajorityClassifier:
    def fit(self, features, labels):
        if len(labels) == 0:
            raise ValueError("cannot fit on empty data")
        # Counter.most_common keeps first-seen order for ties.
        self.majority_ = Counter(labels).most_common(1)[0][0]
        self.classes_ = sorted(set(labels))
        return self

    def predict(self, features):
        if not hasattr(self, "majority_"):
            raise RuntimeError("call fit() before predict()")
        return [self.majority_ for _ in features]

    def score(self, features, labels):
        predictions = self.predict(features)
        correct = sum([prediction == label for prediction, label in zip(predictions, labels)])
        return correct / len(labels)


class RangeScaler:
    def fit(self, values):
        if len(values) == 0:
            raise ValueError("cannot fit on empty data")
        self.min_ = min(values)
        self.max_ = max(values)
        return self

    def transform(self, values):
        if not hasattr(self, "min_"):
            raise RuntimeError("call fit() before transform()")
        spread = self.max_ - self.min_
        if spread == 0:
            return [0.0 for _ in values]
        return [(value - self.min_) / spread for value in values]

    def fit_transform(self, values):
        return self.fit(values).transform(values)
