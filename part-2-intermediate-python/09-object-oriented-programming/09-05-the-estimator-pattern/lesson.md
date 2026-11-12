# 09-05 The estimator pattern

## What you will learn

- Design a class with `fit` and `predict` methods, the interface every scikit-learn model uses.
- Separate hyperparameters (set in `__init__`) from learned attributes (set in `fit`, ending in `_`).
- Make `fit` return `self` and make `predict` fail clearly before fitting.
- Compare different models fairly because they share one interface.

## Why it matters

In Part 5 you will train dozens of models from scikit-learn: linear regression, decision trees, k-means and more. They look very different inside, but you use every one of them in exactly the same way: create it, call `fit` with training data, call `predict` with new data. This lesson builds that pattern yourself with plain Python, so that by Part 5 the interface is second nature and you know what is happening behind it.

## Concepts

### Features, targets and predictions

A few words you will use for the rest of the course:

- **Features** are the inputs a model uses: here, the size of a house. We store them as a list of rows, one row per example, each row a list of feature values: `[[50], [70], ...]`. Even with a single feature, each row is a list, because real datasets have many features.
- **Targets** are the values we want to predict: here, the price of each house.
- **Training** (or **fitting**) a model means letting it learn from features and targets whose answers we know. **Predicting** means using what it learned on new features.

### The simplest model

The simplest possible "model" ignores the features entirely and always predicts the average of the training targets. It sounds silly, but it is a genuinely useful **baseline**: any real model must beat it (Module 20 returns to this).

```python
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
```

```python
sizes = [[50], [70], [90], [110]]
prices = [150, 210, 260, 330]

model = MeanPredictor()
model.fit(sizes, prices)
print(model.mean_)
print(model.predict([[60], [100]]))
```

```
237.5
[237.5, 237.5]
```

### The rules of the pattern

These conventions come straight from scikit-learn:

1. **`fit(features, targets)` learns from data and stores what it learned as attributes.** It does not return predictions.
2. **Learned attributes end in an underscore**, such as `mean_`. The underscore says "this was learned from data during `fit`", and it only exists after fitting.
3. **`fit` returns `self`**, so calls can be chained:

   ```python
   print(MeanPredictor().fit(sizes, prices).predict([[80]]))
   ```

   ```
   [237.5]
   ```

4. **`predict(features)` returns one prediction per row.**
5. **Using a model before fitting fails clearly.** The built-in `hasattr(object, name)` returns `True` if the object has an attribute with that name, which is a neat way to check whether `fit` has run:

   ```python
   try:
       MeanPredictor().predict([[80]])
   except RuntimeError as error:
       print("Error:", error)
   ```

   ```
   Error: call fit() before predict()
   ```

### Hyperparameters

A **hyperparameter** is a setting chosen **before** training that controls how a model learns. Hyperparameters are passed to `__init__` and stored unchanged; nothing is learned in `__init__`. Here is a model that predicts the average price of the `neighbours` most similar houses:

```python
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
```

```
[180.0, 295.0]
```

For each new house, `predict` measures the distance to every training house, sorts the `(distance, price)` pairs so the closest come first (tuples sort by their first item), and averages the prices of the `neighbours` closest. A 60 m² house is between the 50 and 70 m² houses, so it gets the average of 150 and 210. You will meet the real version of this model, k-nearest neighbours, in Module 22.

### Why one interface matters

Because both models have the same `fit` and `predict`, the code that evaluates them does not care which one it gets. Here we measure each one with the **mean absolute error**: the average size of the mistakes, in thousands.

```python
def mean_absolute_error(actual, predicted):
    return sum([abs(a - p) for a, p in zip(actual, predicted)]) / len(actual)


test_sizes = [[60], [100]]
test_prices = [185, 300]
for candidate in [MeanPredictor(), NearestNeighbourPredictor(1), NearestNeighbourPredictor(2)]:
    candidate.fit(sizes, prices)
    error = mean_absolute_error(test_prices, candidate.predict(test_sizes))
    print(f"{type(candidate).__name__:<26} MAE = {error:.1f}")
```

```
MeanPredictor              MAE = 57.5
NearestNeighbourPredictor  MAE = 37.5
NearestNeighbourPredictor  MAE = 5.0
```

The models were tested on houses they had **not** seen during training, which is the only honest way to measure them (Module 20). Two neighbours beat one neighbour, which beat the baseline. Swapping models was a one-word change. This is the whole workflow of Part 5, in miniature.

## Common mistakes

- **Learning in `__init__`.** `__init__` should only store hyperparameters. Anything computed from data belongs in `fit`, otherwise refitting on new data does not work.
- **Forgetting to return `self` from `fit`.** Chaining `Model().fit(X, y).predict(X)` then fails with `AttributeError: 'NoneType' object has no attribute 'predict'`.
- **Returning one value from `predict` instead of a list.** Callers expect one prediction per row, even for a single row: `predict([[80]])` returns `[237.5]`, not `237.5`.
- **Testing on the training data.** A nearest-neighbour model with one neighbour scores perfectly on its own training houses, because each one is its own nearest neighbour. Always evaluate on data the model has not seen.

## Try it

Write a `MedianPredictor` that predicts the median of the training targets, and add it to the comparison loop. Then add an outlier, a 100 m² house that sold for 2,000, to the training data, and compare how the mean and median baselines change.

## Exercises

Open `ex_09_05.py`:

1. `MedianPredictor`: a regression baseline using the median.
2. `MajorityClassifier`: a classification baseline that predicts the most common label.
3. `RangeScaler`: a transformer with `fit`, `transform` and `fit_transform` that rescales numbers to between 0 and 1.

Run the tests:

```
python -m pytest part-2-intermediate-python/09-object-oriented-programming/09-05-the-estimator-pattern
```

## Summary

- Models share one interface: `__init__` takes hyperparameters, `fit(features, targets)` learns, `predict(features)` returns one prediction per row.
- Learned attributes end in `_` and only exist after `fit`; `fit` returns `self`.
- Raise a clear error if `predict` is called before `fit`.
- A shared interface lets you compare models with the same evaluation code.
- Always evaluate on data the model did not see during training.
