# 20-02 The scikit-learn interface

## What you will learn

- Train a model and make predictions with `fit` and `predict`.
- Give scikit-learn data in the shapes it expects: a 2-D **X** and a 1-D **y**.
- Set hyperparameters in the constructor, and read learned attributes ending in `_`.
- Evaluate a model with `score`, and get class probabilities with `predict_proba`.

## Why it matters

**scikit-learn** (imported as `sklearn`) is the standard machine learning library for tabular data in Python. Its great strength is consistency: every model, from linear regression to random forests, is used in exactly the same way. You already know the pattern from 09-05 and the Part 4 project. Learn it once here and you can use any of the dozens of models in the rest of Part 5.

## Concepts

### A first model in ten lines

An **estimator** is scikit-learn's name for any object that learns from data. Using one always follows three steps: **create** it (choosing hyperparameters), **fit** it to training data, then **predict**.

```python
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X, y = iris.data, iris.target
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)
new_flowers = np.array([[5.0, 3.4, 1.5, 0.2], [6.7, 3.0, 5.2, 2.3]])
print(model.predict(new_flowers))
print(iris.target_names[model.predict(new_flowers)])
```

```
[0 2]
['setosa' 'virginica']
```

A **k-nearest neighbours** classifier predicts each new flower's species from the 5 most similar training flowers, like the nearest-neighbour model you built in 09-05 (Module 22 covers it fully). The first new flower has small petals, so it is classed as setosa; the second as virginica. Using `target_names` with the predictions as indexes turns class numbers into names.

### The shapes of X and y

scikit-learn expects:

- **X**: a **2-D** array or DataFrame, shape (number of samples, number of features).
- **y**: a **1-D** array or Series, shape (number of samples,).

```python
print(X.shape, y.shape, X.ndim, y.ndim)
```

```
(150, 4) (150,) 2 1
```

Even a **single** sample must be a 2-D table with one row. Reshape it with `reshape(1, -1)`: one row, as many columns as needed (13-04):

```python
one_flower = np.array([5.0, 3.4, 1.5, 0.2])
print(model.predict(one_flower.reshape(1, -1)))
```

```
[0]
```

### Hyperparameters and learned attributes

As in 09-05, **hyperparameters** are passed to the constructor and stored as they are; `get_params()` lists them all:

```python
print(model.get_params()["n_neighbors"])
print(KNeighborsClassifier(n_neighbors=1).get_params()["n_neighbors"])
```

```
5
1
```

Everything **learned** during `fit` is stored in attributes whose names **end with an underscore**. A linear regression model learns one coefficient (weight) per feature and an intercept (bias):

```python
from sklearn.linear_model import LinearRegression

diabetes = load_diabetes()
regressor = LinearRegression().fit(diabetes.data, diabetes.target)
print(np.round(regressor.coef_, 1))
print(round(regressor.intercept_, 2))
```

```
[ -10.  -239.8  519.8  324.4 -792.2  476.7  101.   177.1  751.3   67.6]
152.13
```

These are the same kind of numbers your Part 4 model learned (different values, because these features are scaled differently). `fit` returns the estimator itself, so you can create, fit and keep it in one line.

### score

Every estimator has a `score(X, y)` method that predicts **X** and compares the predictions with **y**:

- for **classifiers**, it returns **accuracy**: the fraction of correct predictions;
- for **regressors**, it returns **R squared** (R²): 1 minus the model's mean squared error divided by the variance of y, the fraction of the target's variation the model explains (Module 21).

```python
print(round(model.score(X, y), 3))
print(round(regressor.score(diabetes.data, diabetes.target), 3))
```

```
0.967
0.518
```

These scores are measured on the same data the models were trained on, which flatters them. Lesson 20-03 explains why, and how to score honestly.

### predict_proba

Most classifiers can also say **how confident** they are. `predict_proba` returns one row per sample and one column per class, giving the estimated probability of each class:

```python
print(model.predict_proba(new_flowers))
```

```
[[1. 0. 0.]
 [0. 0. 1.]]
```

All 5 neighbours of each new flower belonged to the same species, so the probabilities are certain. Each row adds up to 1, and `predict` simply picks the class with the highest probability (the `argmax` of each row, 13-04). Module 22 uses these probabilities to tune classifiers.

### One interface for every model

Because all estimators share `fit`, `predict` and `score`, swapping models is a one-word change:

```python
from sklearn.tree import DecisionTreeClassifier

for estimator in [KNeighborsClassifier(), DecisionTreeClassifier(random_state=42)]:
    estimator.fit(X, y)
    print(type(estimator).__name__, round(estimator.score(X, y), 3))
```

```
KNeighborsClassifier 0.967
DecisionTreeClassifier 1.0
```

Many models involve randomness; pass `random_state=42` to make their results repeatable, as throughout this course.

## Common mistakes

- **Passing a 1-D array as X.** `model.predict(one_flower)` raises `ValueError: Expected 2D array, got 1D array instead`, and the message suggests `reshape(1, -1)` (one sample) or `reshape(-1, 1)` (one feature).
- **Predicting before fitting.** This raises `NotFittedError: This KNeighborsClassifier instance is not fitted yet. Call 'fit' with appropriate arguments before using this estimator.`.
- **The wrong number of features.** A model fitted on 4 features cannot predict from 3; scikit-learn raises a `ValueError` saying how many it expected.
- **Trusting a training score.** The decision tree's 1.0 above does not mean it is perfect; it means it memorised its training data. Always score on held-out data.

## Try it

Fit `KNeighborsClassifier` with `n_neighbors` set to 1, 15 and 50 on the iris data, and print each one's training score and its `predict_proba` for the flower `[6.0, 2.8, 4.9, 1.7]`. How do the probabilities change as k grows?

## Exercises

Open `ex_20_02.py`:

1. `fit_and_predict`: fit any estimator and predict new samples.
2. `as_one_sample`: turn a 1-D feature vector into a one-row 2-D array.
3. `learned_attributes`: the names of a fitted model's learned attributes.
4. `training_scores`: the training score of several models, by class name.

Run the tests:

```
python -m pytest part-5-supervised-learning/20-machine-learning-foundations/20-02-the-scikit-learn-interface
```

## Summary

- Every estimator is used the same way: create with hyperparameters, `fit(X, y)`, then `predict(X)`.
- **X** is 2-D (samples, features), **y** is 1-D; reshape a single sample with `reshape(1, -1)`.
- Hyperparameters live in the constructor (`get_params()`); learned attributes end in `_` (such as `coef_`).
- `score` gives accuracy for classifiers and R² for regressors; `predict_proba` gives class probabilities.
- Pass `random_state` to models that involve randomness.
