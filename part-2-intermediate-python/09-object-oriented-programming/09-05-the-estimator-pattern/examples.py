# 09-05 The estimator pattern


# Example 1: the simplest possible "model": always predict the mean
class MeanPredictor:
    """Predicts the mean of the training targets for every input."""

    def fit(self, features, targets):
        """Learn from the training data. Returns self."""
        if len(targets) == 0:
            raise ValueError("cannot fit on empty data")
        self.mean_ = sum(targets) / len(targets)
        return self

    def predict(self, features):
        """Return one prediction per row of `features`."""
        if not hasattr(self, "mean_"):
            raise RuntimeError("call fit() before predict()")
        return [self.mean_ for _ in features]


# Training data: house sizes (square metres) and prices (thousands)
sizes = [[50], [70], [90], [110]]
prices = [150, 210, 260, 330]

model = MeanPredictor()
model.fit(sizes, prices)
print(model.mean_)
print(model.predict([[60], [100]]))

# Example 2: fit returns self, so calls can be chained
print(MeanPredictor().fit(sizes, prices).predict([[80]]))

# Example 3: using a model before fitting fails clearly
try:
    MeanPredictor().predict([[80]])
except RuntimeError as error:
    print("Error:", error)


# Example 4: a slightly smarter model with a hyperparameter
class NearestNeighbourPredictor:
    """Predicts the target of the closest training example(s)."""

    def __init__(self, neighbours=1):
        self.neighbours = neighbours          # a setting chosen before training

    def fit(self, features, targets):
        self.features_ = [row[0] for row in features]   # learned from data
        self.targets_ = list(targets)
        return self

    def predict(self, features):
        predictions = []
        for row in features:
            distances = [abs(row[0] - known) for known in self.features_]
            ranked = sorted(zip(distances, self.targets_))
            nearest = [target for _, target in ranked[: self.neighbours]]
            predictions.append(sum(nearest) / len(nearest))
        return predictions


nearest = NearestNeighbourPredictor(neighbours=2).fit(sizes, prices)
print(nearest.predict([[60], [100]]))


# Example 5: a shared way to measure models - mean absolute error
def mean_absolute_error(actual, predicted):
    return sum([abs(a - p) for a, p in zip(actual, predicted)]) / len(actual)


test_sizes = [[60], [100]]
test_prices = [185, 300]
for candidate in [MeanPredictor(), NearestNeighbourPredictor(1), NearestNeighbourPredictor(2)]:
    candidate.fit(sizes, prices)
    error = mean_absolute_error(test_prices, candidate.predict(test_sizes))
    print(f"{type(candidate).__name__:<26} MAE = {error:.1f}")
