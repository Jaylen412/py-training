# 22-05 Naive Bayes

## What you will learn

- Apply Bayes' rule to classification: combine a prior with the likelihood of the features.
- Work a Gaussian Naive Bayes prediction by hand for one feature.
- Use `GaussianNB`, and explain the "naive" independence assumption.
- Judge when Naive Bayes is a good choice and when it is not.

## Why it matters

**Naive Bayes** is Bayes' rule (19-02) turned into a classifier. It trains in a single pass over the data, needs very little of it, and works with any number of classes. It is a classic for text classification (spam filters) and a strong, fast baseline. Understanding it also makes the idea of a probabilistic model concrete: the model stores a simple description of each class and asks which class is most likely to have produced a new sample.

## Concepts

### Bayes' rule for classes

For a sample with features **x**, Bayes' rule (19-02) gives the probability of each class:

P(class | **x**) = P(**x** | class) × P(class) / P(**x**)

In words: how likely the class is after seeing the features equals:

- how likely these features are **for that class** (the **likelihood**), times
- how common the class is to begin with (the **prior**),
- divided by a number that is the same for every class (so we can ignore it and just rescale the results to add up to 1).

The classifier predicts the class with the largest result. Training means estimating the priors and the likelihoods from the training data.

### Gaussian likelihoods

For numeric features, **Gaussian Naive Bayes** assumes that within each class, each feature follows a normal distribution (19-03). Training just computes each class's mean and standard deviation for each feature. The likelihood of a value is then the height of that class's bell curve at that value.

### A worked example: one feature

Classify an iris with petal length 4.9 cm, using only petal length:

```python
petal_length = iris.data[:, 2]
classes = iris.target
priors = np.bincount(classes) / len(classes)
means = np.array([petal_length[classes == c].mean() for c in range(3)])
stds = np.array([petal_length[classes == c].std() for c in range(3)])
print(np.round(priors, 3), np.round(means, 3), np.round(stds, 3))
```

```
[0.333 0.333 0.333] [1.462 4.26  5.552] [0.172 0.465 0.546]
```

Each species is a third of the data. Setosa petals are around 1.46 cm, versicolor 4.26 cm, virginica 5.55 cm. Now the normal density, the formula for the height of a bell curve, and the posterior:

```python
def normal_density(x, mean, std):
    return np.exp(-0.5 * ((x - mean) / std) ** 2) / (std * np.sqrt(2 * np.pi))


new_length = 4.9
likelihoods = normal_density(new_length, means, stds)
unnormalised = likelihoods * priors
posteriors = unnormalised / unnormalised.sum()
print(np.round(likelihoods, 4))
print(np.round(posteriors, 3), iris.target_names[posteriors.argmax()])
```

```
[0.     0.3329 0.3583]
[0.    0.482 0.518] virginica
```

A 4.9 cm petal is impossibly long for setosa (likelihood 0), and almost equally likely for versicolor and virginica, with virginica slightly ahead: 51.8% against 48.2%. A genuinely borderline case, and the probabilities say so.

### The scikit-learn version

**`GaussianNB`** does exactly this:

```python
one_feature = GaussianNB().fit(petal_length.reshape(-1, 1), classes)
print(np.round(one_feature.predict_proba([[new_length]]), 3))
print(np.round(one_feature.theta_.ravel(), 3))
```

```
[[0.    0.482 0.518]]
[1.462 4.26  5.552]
```

The same probabilities. The learned class means are stored in `theta_` (and the variances in `var_`, the class priors in `class_prior_`).

### The naive assumption

With several features, the likelihood of a whole sample would require knowing how all the features vary **together** within each class, which needs a lot of data. Naive Bayes makes a simplifying assumption: **within each class, the features are independent**. Then the likelihood of the sample is just the **product** of the likelihoods of each feature separately (19-02: independent probabilities multiply).

```python
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42, stratify=iris.target
)
model = GaussianNB().fit(X_train, y_train)
print("test accuracy:", round(model.score(X_test, y_test), 3))
print(np.round(model.predict_proba(X_test[:3]), 3))
```

```
test accuracy: 0.911
[[0.    0.    1.   ]
 [0.    0.996 0.004]
 [0.    0.847 0.153]]
```

The assumption is called **naive** because it is usually false. Petal length and petal width are almost perfectly correlated:

```python
print(np.round(np.corrcoef(iris.data[:, 2], iris.data[:, 3])[0, 1], 3))
```

```
0.963
```

Naive Bayes treats them as two independent pieces of evidence, effectively counting the same information twice.

### Why it works anyway

Even with a false assumption, Naive Bayes often classifies well, because it only needs the **right class** to come out on top, not accurate probabilities:

```python
print("wine test accuracy:", round(GaussianNB().fit(Xw_train, yw_train).score(Xw_test, yw_test), 3))
```

```
wine test accuracy: 1.0
```

A perfect score on the wine test set, from a model that took milliseconds to train. But the double counting does make its probabilities **overconfident**:

```python
probabilities = GaussianNB().fit(Xw_train, yw_train).predict_proba(Xw_test)
print("share of predictions with probability above 0.99:", round(np.mean(probabilities.max(axis=1) > 0.99), 3))
```

```
share of predictions with probability above 0.99: 0.889
```

89% of its predictions claim more than 99% certainty. Use Naive Bayes for its predictions, but be wary of reading its probabilities literally, for example when choosing a threshold (22-03).

### When it works well, and when it fails

**Works well:** small datasets; very many features (each feature is handled separately, so there is no curse of dimensionality in training); text classification with word counts (using `MultinomialNB`, the version for counts); when you need something very fast; as a baseline.

**Fails:** when strongly correlated features distort the evidence; when features are far from normally distributed within each class (for example very skewed, or with several peaks); and whenever you need well-calibrated probabilities.

## Common mistakes

- **Trusting the probabilities.** They are usually far too extreme. Use the predictions, or calibrate the probabilities first.
- **Using GaussianNB on count data.** Word counts are not bell-shaped; use `MultinomialNB` for counts and `BernoulliNB` for yes/no features.
- **Expecting scaling to matter.** Each feature is modelled separately with its own mean and spread, so scaling makes no difference.
- **Feeding it many copies of the same information.** Duplicated or near-duplicated features are counted repeatedly, making the model overconfident.

## Try it

Train `GaussianNB` on the breast cancer data. Compare its test accuracy with logistic regression's (22-01). Then look at its `predict_proba` on the test set: what fraction of predictions are above 0.99 or below 0.01? Are the confident ones always right?

## Exercises

Open `ex_22_05.py`:

1. `class_priors`: the fraction of samples in each class.
2. `gaussian_likelihood`: the height of a normal curve at a value.
3. `one_feature_posteriors`: Naive Bayes class probabilities for one feature, by hand.
4. `naive_bayes_accuracy`: the test accuracy of `GaussianNB`.

Run the tests:

```
python -m pytest part-5-supervised-learning/22-classification/22-05-naive-bayes
```

## Summary

- Naive Bayes applies Bayes' rule: P(class | x) is proportional to P(x | class) × P(class).
- Gaussian Naive Bayes models each feature within each class as a normal distribution with its own mean and standard deviation.
- The naive assumption treats features as independent within a class, so their likelihoods multiply.
- It is fast and often accurate, even when the assumption is false, but its probabilities are overconfident.
- Use `MultinomialNB` for counts such as word frequencies; scaling makes no difference.
