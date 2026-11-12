# 21-04 Feature scaling

## What you will learn

- Explain which models need scaled features, and why.
- Standardise features with `StandardScaler` and squeeze them into a range with `MinMaxScaler`.
- Fit scalers on training data only, and apply them to test data.
- Interpret coefficients of a model trained on standardised features.

## Why it matters

Features come in wildly different units: wine proline runs into the thousands while alcohol content varies by a few percent. Models that measure distances (k-nearest neighbours, k-means, SVMs) or penalise coefficient sizes (Ridge, Lasso) treat a difference of 1 the same whatever the feature, so the biggest-numbered feature silently dominates. Scaling fixes this. It is the most common preprocessing step in machine learning, and doing it correctly, without leakage, matters.

## Concepts

### Features on different scales

```python
wine = load_wine(as_frame=True)
print(wine.data[["alcohol", "malic_acid", "magnesium", "proline"]].describe().loc[["mean", "std", "min", "max"]].round(2))
```

```
      alcohol  malic_acid  magnesium  proline
mean    13.00        2.34      99.74   746.89
std      0.81        1.12      14.28   314.91
min     11.03        0.74      70.00   278.00
max     14.83        5.80     162.00  1680.00
```

Proline's spread (standard deviation 315) is nearly 400 times alcohol's (0.81). To a distance calculation, a tiny difference in proline outweighs a huge difference in alcohol.

### StandardScaler

**`StandardScaler`** standardises each feature: subtract the mean, divide by the standard deviation (13-03), giving every feature mean 0 and standard deviation 1. It learns the means and standard deviations in `fit`, and applies them in `transform`:

```python
X_train, X_test, y_train, y_test = train_test_split(
    wine.data, wine.target, test_size=0.25, random_state=42, stratify=wine.target
)
scaler = StandardScaler().fit(X_train)
print(np.round(scaler.mean_[:3], 3), np.round(scaler.scale_[:3], 3))
X_train_std = scaler.transform(X_train)
print(np.round(X_train_std.mean(axis=0)[:3], 6), np.round(X_train_std.std(axis=0)[:3], 6))
```

```
[12.968  2.333  2.368] [0.799 1.086 0.266]
[0. 0. 0.] [1. 1. 1.]
```

The learned statistics are stored in `mean_` and `scale_` (the standard deviations), with the trailing underscore of learned attributes (20-02).

### MinMaxScaler

**`MinMaxScaler`** squeezes each feature into the range 0 to 1: subtract the minimum, divide by the range (as in your `RangeScaler` from 09-05):

```python
minmax = MinMaxScaler().fit(X_train)
X_train_mm = minmax.transform(X_train)
print(X_train_mm.min(axis=0)[:3], X_train_mm.max(axis=0)[:3])
```

```
[0. 0. 0.] [1. 1. 1.]
```

Choose **StandardScaler** by default, especially for models that assume features are centred, such as regularised regression. Choose **MinMaxScaler** when you need a fixed range (for example, pixel intensities or inputs to some neural networks). MinMaxScaler is sensitive to outliers: one extreme value squashes everything else into a tiny part of the range.

### Fit on training data, transform both

The scaler must learn its statistics from the **training data only**, then transform the test data with those same statistics (20-03). So test values can fall outside the training range:

```python
X_test_mm = minmax.transform(X_test)
print(np.round(X_test_mm.min(axis=0)[:3], 3), np.round(X_test_mm.max(axis=0)[:3], 3))
```

```
[0.139 0.03  0.183] [0.882 0.97  1.005]
```

A test value of 1.005 means one test wine is slightly beyond the largest training value for that feature. That is correct: the test set represents new data, which can be outside what the model has seen. Fitting the scaler on the test data as well would leak information.

### Scaling and distance-based models

k-nearest neighbours (Module 22) classifies by distance, so it is very sensitive to scale:

```python
for name, train, test in [
    ("unscaled", X_train, X_test),
    ("standardised", X_train_std, scaler.transform(X_test)),
    ("min-max", X_train_mm, X_test_mm),
]:
    knn = KNeighborsClassifier().fit(train, y_train)
    print(f"{name:<13} k-NN test accuracy {knn.score(test, y_test):.3f}")
```

```
unscaled      k-NN test accuracy 0.778
standardised  k-NN test accuracy 0.933
min-max       k-NN test accuracy 0.978
```

Scaling took accuracy from 0.778 to over 0.93. Without it, the distances are dominated by the features with the largest ranges:

```python
gap = (X_train.max() - X_train.min()).sort_values(ascending=False)
print(gap.head(3).round(1))
```

```
proline              1237.0
magnesium              92.0
alcalinity_of_ash      19.4
dtype: float64
```

Unscaled, the model was essentially classifying wines by proline alone.

### Which models need scaling?

| Need scaling | Do not need scaling |
|--------------|---------------------|
| k-nearest neighbours, k-means, SVMs (distances) | Decision trees, random forests, gradient boosting (Module 23) |
| Ridge, Lasso, logistic regression with regularisation (penalties) | Plain linear regression (predictions are unaffected, though coefficients change) |
| PCA (Module 26) and gradient descent (Module 18) | Naive Bayes (each feature is treated separately) |

Trees split one feature at a time on a threshold, and a threshold works the same in any units. When in doubt, scaling rarely hurts.

### Scaling and coefficients

For regularised regression, scaling changes the coefficients, and makes them comparable:

```python
raw = Ridge(alpha=1.0).fit(Xd_train, yd_train)
scaled = StandardScaler().fit(Xd_train)
std = Ridge(alpha=1.0).fit(scaled.transform(Xd_train), yd_train)
print(pd.DataFrame({"raw": raw.coef_, "standardised": std.coef_}, index=diabetes.data.columns).round(2).head(4))
```

```
       raw  standardised
age   0.18          2.27
sex -22.80        -11.44
bmi   5.79         25.21
bp    1.31         18.13
```

A standardised coefficient is the change in prediction for a **one standard deviation** change in the feature. On the raw scale, sex (coded 1 or 2) looks four times as important as BMI; standardised, BMI has more than twice the effect. Use standardised coefficients to compare features.

### Going back to original units

`inverse_transform` undoes the scaling:

```python
print(np.round(scaler.inverse_transform(X_train_std[:1])[0][:3], 2), X_train.iloc[0, :3].tolist())
```

```
[14.83  1.64  2.17] [14.83, 1.64, 2.17]
```

## Common mistakes

- **Fitting the scaler on all the data.** This leaks test information. Fit on training data; transform both sets.
- **Calling `fit_transform` on the test set.** That refits the scaler on the test data. Use `transform` only.
- **Forgetting to scale new data at prediction time.** A model trained on scaled features must receive scaled features. Pipelines (24-02) handle this automatically.
- **Scaling the target by accident.** Scalers are for features. (Some problems benefit from transforming the target, such as a log transform, but that is a separate, deliberate choice.)

## Try it

Train `KNeighborsClassifier` on the breast cancer data with and without `StandardScaler`. How large is the difference in test accuracy? Which features have the largest ranges?

## Exercises

Open `ex_21_04.py`:

1. `standardise`: scale training and test sets with a `StandardScaler` fitted on the training data.
2. `min_max_scale`: the same with `MinMaxScaler`.
3. `knn_accuracy`: k-NN test accuracy, optionally after scaling.
4. `widest_feature`: the name of the feature with the largest range.

Run the tests:

```
python -m pytest part-5-supervised-learning/21-regression/21-04-feature-scaling
```

## Summary

- Distance-based and regularised models need features on comparable scales; tree-based models do not.
- `StandardScaler` gives mean 0 and standard deviation 1; `MinMaxScaler` gives the range 0 to 1.
- Fit scalers on the training data only, then `transform` the training and test data.
- Scaling can transform the accuracy of a distance-based model.
- Standardised coefficients show the effect of a one-SD change, so they can be compared.
