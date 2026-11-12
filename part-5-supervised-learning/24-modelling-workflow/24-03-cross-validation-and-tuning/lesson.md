# 24-03 Cross-validation and hyperparameter tuning

## What you will learn

- Explain why one validation split gives a noisy estimate, and how k-fold cross-validation fixes it.
- Use `KFold`, `StratifiedKFold` and `cross_val_score`, with a choice of scoring metric.
- Compare models fairly with cross-validation.
- Tune hyperparameters with `GridSearchCV` and `RandomizedSearchCV`, keeping the test set untouched until the end.

## Why it matters

Every model so far has had hyperparameters chosen by looking at the test set: `max_depth`, `C`, `k`, `gamma`. That makes the test score optimistic, because you picked the setting that happened to suit those particular test rows (20-03). This lesson gives the professional workflow: tune and compare using cross-validation on the training data only, and touch the test set exactly once. It is the workflow you will follow in the Part 5 project.

## Concepts

The examples use the churn pipeline from 24-02 (`pipe`), with the 1,600-row training set and the 400-row test set. The test set is not used until the final example.

### One split is noisy

Split the training data into a smaller training part and a validation part, three times with different seeds:

```python
for seed in [0, 1, 2]:
    a_train, a_valid, b_train, b_valid = train_test_split(X_train, y_train, test_size=0.25, random_state=seed,
                                                          stratify=y_train)
    print(f"split {seed}: validation accuracy {pipe.fit(a_train, b_train).score(a_valid, b_valid):.3f}")
```

```
split 0: validation accuracy 0.812
split 1: validation accuracy 0.802
split 2: validation accuracy 0.770
```

The same model scores anywhere from 0.770 to 0.812 depending on which rows land in validation. Differences between models of a percentage point or two are smaller than this noise, so one split cannot tell them apart reliably.

### k-fold cross-validation

**k-fold cross-validation** uses every row for validation exactly once. Divide the training data into k equal **folds**. Train on k − 1 folds and validate on the remaining one; repeat k times, each fold taking a turn as validation; average the k scores.

```python
folds = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []
for train_rows, valid_rows in folds.split(X_train):
    pipe.fit(X_train.iloc[train_rows], y_train.iloc[train_rows])
    scores.append(pipe.score(X_train.iloc[valid_rows], y_train.iloc[valid_rows]))
print(np.round(scores, 3), round(np.mean(scores), 3), round(np.std(scores), 3))
```

```
[0.762 0.816 0.772 0.819 0.778] 0.789 0.023
```

`split` yields the row positions for each fold, hence `.iloc`. The mean, 0.789, is a far steadier estimate than any single split, and the standard deviation, 0.023, tells you how much it varies. 5 or 10 folds is standard. `shuffle=True` mixes the rows first, in case the file is sorted.

### cross_val_score and stratification

**`cross_val_score`** runs the whole loop in one call. For classification, **`StratifiedKFold`** keeps the class proportions the same in every fold (like `stratify=` in `train_test_split`), which matters with imbalanced classes:

```python
stratified = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipe, X_train, y_train, cv=stratified)
print(np.round(scores, 3), round(scores.mean(), 3))
roc = cross_val_score(pipe, X_train, y_train, cv=stratified, scoring="roc_auc")
print("ROC AUC:", round(roc.mean(), 3), "+/-", round(roc.std(), 3))
```

```
[0.784 0.762 0.8   0.809 0.8  ] 0.791
ROC AUC: 0.814 +/- 0.009
```

`scoring` chooses the metric: `"accuracy"` (the default for classifiers), `"roc_auc"`, `"f1"`, `"recall"`, `"precision"`, `"neg_mean_squared_error"` for regression, and many more. Scores are always "higher is better", which is why errors appear as negatives. Because the pipeline is refitted inside every fold, the preprocessing never sees the validation fold: no leakage (24-02).

### Comparing models

Compare candidate models on the **same folds** and the same metric:

```python
for name, model in [("logistic regression", LogisticRegression(max_iter=1000)),
                    ("gradient boosting", HistGradientBoostingClassifier(random_state=42))]:
    pipe.set_params(model=model)
    auc = cross_val_score(pipe, X_train, y_train, cv=stratified, scoring="roc_auc")
    print(f"{name:<20} ROC AUC {auc.mean():.3f} +/- {auc.std():.3f}")
```

```
logistic regression  ROC AUC 0.814 +/- 0.009
gradient boosting    ROC AUC 0.760 +/- 0.021
```

The gap, 0.054, is much larger than the fold-to-fold spread, so logistic regression is genuinely better here with default settings. The churn data was generated from a mostly linear formula, which suits a linear model; untuned boosting with 1,600 rows overfits.

### Grid search

**`GridSearchCV`** cross-validates every combination of the hyperparameter values you list, then refits the best combination on the whole training set. Parameters of pipeline steps use the `step__parameter` names from 24-02:

```python
pipe.set_params(model=LogisticRegression(max_iter=1000))
grid = GridSearchCV(pipe, {"model__C": [0.01, 0.1, 1, 10]}, cv=stratified, scoring="roc_auc")
grid.fit(X_train, y_train)
print(grid.best_params_, round(grid.best_score_, 3))
results = pd.DataFrame(grid.cv_results_)[["param_model__C", "mean_test_score", "rank_test_score"]]
print(results.round(3).to_string(index=False))
```

```
{'model__C': 0.1} 0.815
 param_model__C  mean_test_score  rank_test_score
           0.01            0.808                4
           0.10            0.815                1
           1.00            0.814                2
          10.00            0.814                3
```

`best_params_` and `best_score_` give the winner; `cv_results_` holds every combination's scores. The fitted `grid` behaves like the best model (`grid.predict`, `grid.best_estimator_`). With several parameters, the number of combinations multiplies: 4 values of C × 3 penalties × 5 folds is 60 fits.

### Randomized search

When there are many hyperparameters, a grid becomes huge. **`RandomizedSearchCV`** instead tries a fixed number of random combinations, drawing each value from a list or a distribution:

```python
pipe.set_params(model=HistGradientBoostingClassifier(random_state=42))
search = RandomizedSearchCV(
    pipe,
    {"model__learning_rate": loguniform(0.01, 0.3),
     "model__max_depth": randint(2, 8),
     "model__max_iter": randint(50, 400)},
    n_iter=20, cv=stratified, scoring="roc_auc", random_state=42,
)
search.fit(X_train, y_train)
for name, value in search.best_params_.items():
    print(f"{name}: {value:.3g}")
print("best cross-validated ROC AUC:", round(search.best_score_, 3))
```

```
model__learning_rate: 0.0106
model__max_depth: 3
model__max_iter: 389
best cross-validated ROC AUC: 0.8
```

`loguniform(0.01, 0.3)` (from `scipy.stats`, installed with scikit-learn) draws values spread evenly on a log scale, so 0.01 to 0.03 is as likely as 0.1 to 0.3: right for learning rates and C. `randint(2, 8)` draws whole numbers from 2 to 7. Tuning lifted boosting from 0.760 to 0.800, with a small learning rate and shallow trees, but it still trails logistic regression. Tuning helps, but it rarely turns the wrong model into the right one.

### The test set, once

Only now, with the model chosen and tuned using training data alone, evaluate on the test set:

```python
final = grid.best_estimator_
print("test ROC AUC:", round(roc_auc_score(y_test, final.predict_proba(X_test)[:, 1]), 3))
print("test accuracy:", round(final.score(X_test, y_test), 3))
```

```
test ROC AUC: 0.837
test accuracy: 0.785
```

This is the number to report. It is close to the cross-validated estimate (0.815), slightly higher by the luck of this particular test set. If you now went back and changed the model because of this score, the test set would stop being an honest estimate.

The full workflow:

1. Split off a test set and put it aside.
2. Explore and build a pipeline using the training set.
3. Compare models with cross-validation on the training set.
4. Tune the best one or two with grid or randomized search.
5. Evaluate the final model on the test set, once.

## Common mistakes

- **Tuning on the test set.** Any choice made by looking at test scores makes them optimistic.
- **Preprocessing outside the cross-validated pipeline.** Leakage again; keep everything inside.
- **Plain `KFold` on imbalanced or sorted classification data.** Use `StratifiedKFold` with `shuffle=True`.
- **Huge grids.** Combinations multiply. Start coarse (powers of 10), then refine around the best, or use randomized search.
- **Ignoring the spread.** A difference smaller than the standard deviation across folds may be noise.

## Try it

Run a `GridSearchCV` over both `model__C` in [0.01, 0.1, 1, 10] and `model__class_weight` in [None, "balanced"], scoring by `"recall"`. Which combination wins? Then score that model's test-set precision and recall, and explain the trade-off in one sentence (22-02).

## Exercises

Open `ex_24_03.py`:

1. `kfold_scores`: k-fold cross-validation by hand.
2. `compare_with_cv`: mean cross-validated score for several models.
3. `tune_c`: grid search over C, returning the best value and score.
4. `final_test_auc`: the one-time test-set ROC AUC.

Run the tests:

```
python -m pytest part-5-supervised-learning/24-modelling-workflow/24-03-cross-validation-and-tuning
```

## Summary

- A single validation split is noisy; k-fold cross-validation averages k train/validation rounds that use every row once.
- `cross_val_score(pipeline, X, y, cv=StratifiedKFold(...), scoring=...)` runs it in one call without leakage.
- Compare models on the same folds and metric, and look at the spread as well as the mean.
- `GridSearchCV` tries every combination; `RandomizedSearchCV` samples a fixed number; both refit the best on all training data.
- Choose and tune with training data only, then evaluate on the test set exactly once.
