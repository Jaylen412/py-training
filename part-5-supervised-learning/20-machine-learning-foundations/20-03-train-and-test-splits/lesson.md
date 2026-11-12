# 20-03 Train and test splits

## What you will learn

- Explain why a model must be evaluated on data it was not trained on.
- Split data into training and test sets with `train_test_split`.
- Keep class proportions equal in both parts with stratification.
- Recognise data leakage and avoid it.

## Why it matters

The purpose of a model is to make good predictions on **new** data: tomorrow's customers, next month's patients. A model that has memorised its training data can score perfectly on it and still be useless. The test set is your stand-in for the future. Getting this right is the difference between an honest result and a misleading one, and it is the most important habit in all of machine learning.

## Concepts

The examples use the breast cancer data (16-01): 569 tumours, 30 features, and a target of malignant (0) or benign (1).

### Scoring on training data misleads

```python
tree = DecisionTreeClassifier(random_state=42).fit(X, y)
print("accuracy on training data:", tree.score(X, y))
```

```
accuracy on training data: 1.0
```

A perfect score. But this tree has simply memorised all 569 tumours. Asking it about tumours it has already seen tells you nothing about how it will do on a new one, just as a student who has seen the exam answers would score perfectly without understanding anything.

### The train/test split

The solution is to set aside part of the data before training. The model learns from the **training set** only, and is scored on the **test set**, which it has never seen. **`train_test_split`** shuffles the rows and cuts them into the two parts:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print(X_train.shape, X_test.shape)
tree = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
print("train:", round(tree.score(X_train, y_train), 3), "test:", round(tree.score(X_test, y_test), 3))
```

```
(426, 30) (143, 30)
train: 1.0 test: 0.951
```

- It returns **four** arrays, always in the order X_train, X_test, y_train, y_test. Unpack them in one line (05-02).
- `test_size=0.25` puts a quarter of the rows in the test set. 20% to 30% is typical.
- Rows are shuffled first, so the test set is a random sample, not just the last rows of the file.

The test accuracy of 0.951 is the honest estimate. The gap between 1.0 on training data and 0.951 on test data is a sign of **overfitting** (20-04).

### random_state and split-to-split variation

`random_state` fixes the shuffle, so the split is the same every time you run the code. Different seeds give different splits, and different scores:

```python
again = train_test_split(X, y, test_size=0.25, random_state=42)
print(np.array_equal(X_test, again[1]))
for seed in [0, 1, 2]:
    parts = train_test_split(X, y, test_size=0.25, random_state=seed)
    model = DecisionTreeClassifier(random_state=42).fit(parts[0], parts[2])
    print(f"split seed {seed}: test accuracy {model.score(parts[1], parts[3]):.3f}")
```

```
True
split seed 0: test accuracy 0.916
split seed 1: test accuracy 0.965
split seed 2: test accuracy 0.916
```

The same model scores anywhere from 0.916 to 0.965 depending on which tumours happened to land in the test set. A single test score is an estimate with sampling error (19-04). Cross-validation (24-03) averages over several splits to give a more reliable figure.

### Stratification

With a small test set, random chance can leave the classes unbalanced. The whole dataset is 62.7% benign; a plain 10% test set here came out at 71.9%:

```python
print("whole dataset:", round(y.mean(), 3))
_, _, plain_train, plain_test = train_test_split(X, y, test_size=0.1, random_state=3)
print("plain split:  ", round(plain_train.mean(), 3), round(plain_test.mean(), 3))
_, _, strat_train, strat_test = train_test_split(X, y, test_size=0.1, random_state=3, stratify=y)
print("stratified:   ", round(strat_train.mean(), 3), round(strat_test.mean(), 3))
```

```
whole dataset: 0.627
plain split:   0.617 0.719
stratified:    0.627 0.632
```

(The mean of a 0/1 target is the fraction of 1s.) **`stratify=y`** splits each class separately, so both parts keep the original class proportions. Always stratify for classification, especially with imbalanced classes or small datasets.

### Data leakage

**Data leakage** means information from the test set (or from the future, or from the answer itself) sneaks into training. It makes test scores look better than the model will really do. Two common forms:

**1. Preprocessing on the whole dataset.** Many models need features standardised (13-03). Computing the means and standard deviations from **all** the data lets the test set influence the training data:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
leaky_scaler = StandardScaler().fit(X)                  # wrong: has seen the test rows
proper_scaler = StandardScaler().fit(X_train)           # right: training rows only
print(np.round(leaky_scaler.mean_[:3], 3))
print(np.round(proper_scaler.mean_[:3], 3))
knn = KNeighborsClassifier().fit(proper_scaler.transform(X_train), y_train)
print("test accuracy:", round(knn.score(proper_scaler.transform(X_test), y_test), 3))
```

```
[14.127 19.29  91.969]
[14.075 19.295 91.593]
test accuracy: 0.979
```

`StandardScaler` (Module 21) learns column means and standard deviations in `fit`, and applies them with `transform`. The rule: **fit every preprocessing step on the training data only**, then apply the same fitted transformation to the test data. The difference here is small, but with some steps (such as choosing features using the target) it can be dramatic. Pipelines (24-02) make the right way automatic.

**2. A feature that contains the answer.** Here the target itself is accidentally included as a column:

```python
leaky_X = np.column_stack([X, y])
leaky_train, leaky_test, ly_train, ly_test = train_test_split(leaky_X, y, test_size=0.25, random_state=42)
leaky_model = DecisionTreeClassifier(random_state=42).fit(leaky_train, ly_train)
print("with a leaked feature:", leaky_model.score(leaky_test, ly_test))
```

```
with a leaked feature: 1.0
```

Real leaks are subtler: a "treatment given" column when predicting the diagnosis that decided the treatment, or a "last login" date recorded after the customer had already cancelled. **Be suspicious of results that look too good**, and ask of every feature: would I actually know this at the moment of prediction?

### The golden rule

The test set is for a **final**, honest check. If you use it to choose between models or settings, you are tuning to the test set, and its score stops being honest. Module 24 introduces validation sets and cross-validation for making choices, keeping the test set untouched until the end.

## Common mistakes

- **Unpacking in the wrong order.** `X_train, y_train, X_test, y_test = train_test_split(...)` silently mixes features and targets. The order is X_train, X_test, y_train, y_test.
- **Fitting the scaler (or any preprocessing) on all the data.** Fit on the training set, then transform both.
- **Forgetting `stratify=y`.** Small or imbalanced test sets can end up unrepresentative.
- **Peeking at the test set repeatedly.** Every decision made by looking at test scores makes them more optimistic.

## Try it

Run the decision tree with 20 different split seeds and collect the test accuracies. What are the minimum, maximum and mean? Repeat with `test_size=0.1` and `test_size=0.4`. Which test size gives the most stable scores, and why?

## Exercises

Open `ex_20_03.py`:

1. `split_data`: a stratified, repeatable train/test split.
2. `train_and_test_scores`: fit a model and return its training and test scores.
3. `scale_without_leakage`: standardise training and test features using training statistics only.
4. `score_range_over_splits`: the lowest and highest test score over several split seeds.

Run the tests:

```
python -m pytest part-5-supervised-learning/20-machine-learning-foundations/20-03-train-and-test-splits
```

## Summary

- Training scores are optimistic; evaluate on a test set the model never saw.
- `train_test_split(X, y, test_size=..., random_state=..., stratify=y)` returns X_train, X_test, y_train, y_test.
- Test scores vary from split to split; one score is an estimate.
- Stratify classification splits to keep the class proportions.
- Avoid leakage: fit preprocessing on the training data only, and never use features you would not have at prediction time.
