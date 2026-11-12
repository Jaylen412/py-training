# 20-05 Baselines

## What you will learn

- Build trivial baseline models with `DummyClassifier` and `DummyRegressor`.
- Explain why accuracy can look impressive while meaning nothing.
- Compare a real model against its baseline, in the target's own units.

## Why it matters

"Our model is 95% accurate" sounds great, unless 95% of the cases belong to one class, in which case a model that always guesses that class is also 95% accurate. A **baseline** is the score of a deliberately simple model that uses no real learning. Every model you report should be compared with one. If it does not clearly beat the baseline, it has not learned anything useful.

## Concepts

### The majority-class baseline

For classification, the simplest baseline always predicts the most common class in the training data. scikit-learn provides it as **`DummyClassifier`**, with the usual interface:

```python
from sklearn.dummy import DummyClassifier, DummyRegressor

cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print(baseline.predict(X_test[:5]))
print("baseline accuracy:", round(baseline.score(X_test, y_test), 3))
```

```
[1 1 1 1 1]
baseline accuracy: 0.629
```

It ignores the features entirely and says "benign" every time, and is right 62.9% of the time, just because 62.9% of tumours are benign. This is the same idea as the `MajorityClassifier` you wrote in 09-05.

### Beating the baseline

```python
tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print("tree accuracy:", round(tree.score(X_test, y_test), 3))
```

```
tree accuracy: 0.944
```

A decision tree reaches 0.944. The meaningful statement is not "94.4% accurate" but "94.4% against a baseline of 62.9%": the model has learned something real.

### When accuracy lies

With **imbalanced classes**, the baseline can be very high. `make_classification` generates a synthetic classification dataset; here 95% of samples belong to class 0, like a fraud dataset where most transactions are genuine:

```python
X, y = make_classification(n_samples=2000, weights=[0.95], flip_y=0, random_state=42)
print("fraction of class 1:", y.mean())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print("majority baseline:", DummyClassifier(strategy="most_frequent").fit(X_train, y_train).score(X_test, y_test))
```

```
fraction of class 1: 0.05
majority baseline: 0.95
```

A model that never detects a single fraudulent transaction scores 95% accuracy. On a problem like this, a model with 96% accuracy may be nearly useless and one with 93% may be excellent; accuracy simply cannot tell them apart. Module 22 introduces measures that can: precision, recall and the confusion matrix.

### Other baseline strategies

`DummyClassifier` has other strategies:

```python
for strategy in ["most_frequent", "stratified", "uniform"]:
    dummy = DummyClassifier(strategy=strategy, random_state=42).fit(X_train, y_train)
    print(f"{strategy:<14}{dummy.score(X_test, y_test):.3f}")
```

```
most_frequent 0.950
stratified    0.894
uniform       0.486
```

- `"most_frequent"`: always predict the majority class.
- `"stratified"`: guess randomly, with the training class proportions (95% class 0, 5% class 1).
- `"uniform"`: guess every class with equal probability, like a coin toss.

The most-frequent strategy is the usual baseline for accuracy. The others are useful baselines for metrics that most-frequent scores badly on.

### Regression baselines

For regression, the simplest baseline predicts the **mean** of the training targets for every sample, as your `MeanPredictor` did in 09-05:

```python
diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=42)
mean_baseline = DummyRegressor(strategy="mean").fit(X_train, y_train)
print(round(mean_baseline.predict(X_test[:1])[0], 2), round(y_train.mean(), 2))
print("baseline R squared:", round(mean_baseline.score(X_test, y_test), 3))
regression = LinearRegression().fit(X_train, y_train)
print("linear regression R squared:", round(regression.score(X_test, y_test), 3))
```

```
154.34 154.34
baseline R squared: -0.014
linear regression R squared: 0.485
```

R² compares a model with predicting the mean, so the mean baseline scores about 0 by definition. (It is slightly below 0 here because it predicts the **training** mean, which differs a little from the test set's mean. R² can be negative for a model worse than the mean.) `strategy="median"` is another option.

### Comparing in real units

Scores such as R² are abstract. Comparing errors in the target's own units makes the improvement concrete:

```python
baseline_error = np.mean(np.abs(mean_baseline.predict(X_test) - y_test))
model_error = np.mean(np.abs(regression.predict(X_test) - y_test))
print(f"mean absolute error: baseline {baseline_error:.1f}, model {model_error:.1f}")
print(f"improvement: {1 - model_error / baseline_error:.1%}")
```

```
mean absolute error: baseline 65.5, model 41.5
improvement: 36.6%
```

"The model's predictions are off by 41.5 points on average, against 65.5 for simply guessing the average: a 36.6% improvement" is something anyone can understand.

### Baselines in practice

1. Before building any model, fit a baseline and record its test score.
2. Report every model's score next to the baseline's.
3. A complex model that barely beats the baseline is a warning: either the features carry little information, or something is wrong.
4. A simple, sensible rule (such as "predict last week's sales") is often a better baseline than a dummy, and much harder to beat.

## Common mistakes

- **Reporting accuracy without a baseline.** "90% accurate" means nothing until you know the majority class is, say, 88%.
- **Fitting the baseline on all the data.** Like any model, fit it on the training set only, so its prediction (the training mean or majority class) is not influenced by the test set.
- **Ignoring class imbalance.** With rare classes, accuracy is dominated by the common class. Use the metrics in Module 22.
- **Being satisfied by beating a dummy.** Beating the dummy is the minimum. Also compare against a simple, sensible rule if one exists.

## Try it

On the imbalanced `make_classification` data, train a `DecisionTreeClassifier(max_depth=3, random_state=42)`. Is its accuracy higher than the baseline's 0.95? Now count how many of the test set's class-1 samples it predicts correctly, compared with the baseline's zero.

## Exercises

Open `ex_20_05.py`:

1. `majority_baseline_accuracy`: the test accuracy of always predicting the training majority class.
2. `mean_baseline_mae`: the test MAE of always predicting the training mean.
3. `beats_baseline`: whether a model's test score beats a dummy's by a margin.
4. `improvement`: the fractional reduction in error compared with a baseline.

Run the tests:

```
python -m pytest part-5-supervised-learning/20-machine-learning-foundations/20-05-baselines
```

## Summary

- A baseline is a trivial model that every real model must clearly beat.
- `DummyClassifier(strategy="most_frequent")` predicts the majority class; `DummyRegressor(strategy="mean")` predicts the training mean.
- With imbalanced classes, the majority baseline's accuracy can be very high, so accuracy alone is misleading.
- Report model scores next to baseline scores, and compare errors in the target's own units.
- Fit baselines on the training data only, like any other model.
