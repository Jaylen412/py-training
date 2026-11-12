# 24-02 Pipelines

## What you will learn

- Chain preprocessing and a model into one object with `Pipeline` and `make_pipeline`.
- Explain how pipelines prevent data leakage, and see how badly leakage can mislead.
- Build a complete churn model that takes raw data in and gives predictions out.
- Save a fitted pipeline with `joblib` and load it again.

## Why it matters

In 24-01 you had to remember to `fit_transform` the training data, `transform` the test data, then fit the model, in the right order, every time. A **pipeline** packages all of that into one object with `fit` and `predict`. It makes code shorter, makes leakage hard to commit by accident (especially inside cross-validation, 24-03), and gives you a single thing to save and deploy.

## Concepts

### A pipeline is a chain of steps

A **`Pipeline`** is a list of named steps. Every step except the last is a **transformer** (it has `fit` and `transform`); the last is usually a model:

```python
pipe = Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(max_iter=1000))])
pipe.fit(Xc_train, yc_train)
print(round(pipe.score(Xc_test, yc_test), 3))
print(list(pipe.named_steps))
print(pipe.named_steps["scale"].mean_[:2].round(2))
```

```
0.986
['scale', 'model']
[14.08 19.3 ]
```

(This is the breast cancer data from Module 22.) Calling `pipe.fit(X, y)` runs `fit_transform` on each transformer in turn and then fits the model on the result. Calling `pipe.predict(X)` or `pipe.score(X, y)` runs only `transform` on each transformer, using what was learned during `fit`, then the model. You can no longer accidentally refit the scaler on test data. `named_steps` gives access to each fitted step.

**`make_pipeline`** is a shortcut that names the steps after their classes:

```python
quick = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print(list(quick.named_steps))
```

```
['standardscaler', 'logisticregression']
```

### How bad can leakage be?

Leakage is easiest to see in an extreme case. Make 100 rows of **pure noise**, 5,000 random features, and random labels. No model can genuinely predict these labels: the true accuracy is 50%. Now pick the 20 features most related to the labels and cross-validate (24-03 explains cross-validation; for now, it is an average of five train/validation splits):

```python
noise = rng.normal(size=(100, 5000))
labels = rng.integers(0, 2, size=100)
leaky_features = SelectKBest(f_classif, k=20).fit_transform(noise, labels)
leaky = cross_val_score(LogisticRegression(), leaky_features, labels, cv=5).mean()
honest = cross_val_score(make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression()), noise, labels, cv=5).mean()
print(f"leaky: {leaky:.3f}  honest: {honest:.3f}")
```

```
leaky: 0.890  honest: 0.520
```

`SelectKBest` keeps the k features with the strongest statistical link to the target. In the leaky version, the features were chosen using **all** the labels, including those later used for validation. Out of 5,000 noise columns, some match the labels by chance, and the selection found them: 89% "accuracy" on random data. In the honest version, the selection is inside the pipeline, so it is redone inside each training split and never sees the validation labels: 52%, the truth.

The same thing happens, more subtly, with scaling, imputation and encoding. The rule: **every step that learns from data belongs inside the pipeline.**

### The full churn pipeline

Combine the `ColumnTransformer` from 24-01 with a model, and the whole process from raw DataFrame to prediction becomes one object:

```python
preprocess = ColumnTransformer([
    ("numeric", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), numeric),
    ("nominal", make_pipeline(SimpleImputer(strategy="most_frequent"),
                              OneHotEncoder(handle_unknown="ignore")), nominal),
    ("ordered", make_pipeline(SimpleImputer(strategy="most_frequent"),
                              OrdinalEncoder(categories=[["low", "medium", "high"]])), ordered),
])
churn_model = Pipeline([("preprocess", preprocess), ("model", LogisticRegression(max_iter=1000))])
churn_model.fit(X_train, y_train)
print("logistic regression test accuracy:", round(churn_model.score(X_test, y_test), 3))
print(churn_model.predict_proba(X_test.head(3)).round(3))
```

```
logistic regression test accuracy: 0.797
[[0.816 0.184]
 [0.822 0.178]
 [0.552 0.448]]
```

`X_train` here is the raw DataFrame, text and gaps included. Pipelines can be nested: the column transformer contains small pipelines, and it is itself a step of the big one.

### Swapping steps

`set_params` replaces a step by name, so trying another model is one line:

```python
churn_model.set_params(model=HistGradientBoostingClassifier(random_state=42))
churn_model.fit(X_train, y_train)
print("gradient boosting test accuracy:", round(churn_model.score(X_test, y_test), 3))
```

```
gradient boosting test accuracy: 0.76
```

Interesting: on this data, the simple linear model wins. Default boosting is not always best; 24-03 compares them properly.

Parameters of steps inside a pipeline are addressed as `step__parameter` with a **double underscore**: `churn_model.set_params(model__C=0.1)` sets the logistic regression's C. This naming matters for tuning in 24-03.

### Saving and loading

A trained pipeline is a Python object. **`joblib`** (installed with scikit-learn) saves it to a file and loads it back, ready to predict:

```python
with tempfile.TemporaryDirectory() as folder:
    path = Path(folder) / "churn_model.joblib"
    joblib.dump(churn_model, path)
    loaded = joblib.load(path)
    new_customer = pd.DataFrame([{
        "tenure_months": 2, "monthly_charges": 95.0, "total_charges": 190.0, "support_calls": 4,
        "contract": "month-to-month", "payment_method": "electronic check",
        "internet_service": "fibre", "region": "North", "satisfaction": "low",
    }])
    print("churn probability:", loaded.predict_proba(new_customer)[0, 1].round(3))
    print(np.array_equal(loaded.predict(X_test), churn_model.predict(X_test)))
```

```
churn probability: 0.901
True
```

(`tempfile.TemporaryDirectory` creates a folder that is deleted afterwards, so the example leaves nothing behind.) Because the preprocessing is inside the pipeline, the loaded model accepts a raw customer record. A new, unhappy, month-to-month customer on fibre with four support calls is 90% likely to churn.

Two cautions: load model files only from sources you trust (loading can run arbitrary code), and load them with the same scikit-learn version that saved them.

## Common mistakes

- **Fitting a transformer outside the pipeline and then cross-validating.** That is leakage, as the noise example shows. Put every data-dependent step inside.
- **Single underscore in parameter names.** It is `model__C`, with two underscores.
- **Saving only the model.** Save the whole pipeline, or you must recreate the exact preprocessing to use it.
- **Loading untrusted joblib or pickle files.** They can execute code when loaded.

## Try it

Add `SelectKBest(f_classif, k=8)` as a step between `preprocess` and `model` in the churn pipeline. Does test accuracy change? Which 8 features did it keep? (Hint: `get_support()` on the fitted selector, combined with `get_feature_names_out()` on the fitted preprocessor.)

## Exercises

Open `ex_24_02.py`:

1. `scaled_logistic_pipeline`: a two-step pipeline with named steps.
2. `churn_pipeline`: preprocessing plus any model, for the churn columns.
3. `save_and_reload`: round-trip a fitted pipeline through a joblib file.
4. `leaky_and_honest_scores`: the leakage experiment.

Run the tests:

```
python -m pytest part-5-supervised-learning/24-modelling-workflow/24-02-pipelines
```

## Summary

- A `Pipeline` chains transformers and a final model; `fit` fits each step in order, `predict` only transforms.
- Every step that learns from data must be inside the pipeline, or validation scores are inflated by leakage.
- `make_pipeline` names steps automatically; `set_params(step=...)` swaps a step; `step__param` sets a nested parameter.
- A pipeline with a `ColumnTransformer` takes raw DataFrames, gaps and text included.
- `joblib.dump` and `joblib.load` save and restore a fitted pipeline; only load files you trust.
