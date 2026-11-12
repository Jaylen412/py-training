# Part 4 Project: Linear Regression From Scratch

## Brief

Build a linear regression model that **learns**, using only NumPy: a `LinearRegressionGD` class with `fit`, `predict` and `score` methods that trains by gradient descent and records its loss at every epoch. Train it on two datasets, plot its loss curves, and prove it works by checking that its weights match the exact least-squares solution from `np.linalg.lstsq`.

This project brings Part 4 together: vectors and matrix products (17), gradients, loss functions and gradient descent (18), and standardising data (19). It follows the estimator pattern from 09-05, so in Part 5 you will recognise scikit-learn's `LinearRegression` as the same idea.

## The datasets

- **`make_regression`** (scikit-learn): 200 synthetic samples with 3 features, generated from known true weights plus noise. Because the true weights are known, you can see how close the model gets.
- **`load_diabetes`** (scikit-learn): 442 real patients, 10 features (age, sex, BMI, blood pressure and six blood serum measurements), and a measure of disease progression one year later.

## Getting started

Work in `starter/linear_regression_gd.py`. The class and every function have docstrings saying exactly what to do; `compare` and `main` are written for you.

```
python -m pytest part-4-maths-for-ml/project/starter
python part-4-maths-for-ml/project/starter/linear_regression_gd.py
```

## Requirements

1. `__init__` stores `learning_rate` and `epochs`, and learns nothing.
2. `fit` validates the inputs, runs gradient descent on the MSE for every weight and the bias, records `loss_history_`, and returns `self`.
3. `predict` returns `X @ weights_ + bias_`, with clear errors when called too early or with the wrong number of columns.
4. `score` returns R squared, the fraction of the target's variance the model explains.
5. `standardise` and `fit_least_squares` helpers.
6. `plot_loss` saves a log-scale loss curve.

When everything works, `main()` should print something like:

```
make_regression true weights: [72.004 22.925 72.225]
--- make_regression ---
gradient descent weights: [71.642 21.846 72.754] bias: -0.368
least squares weights:    [71.642 21.846 72.754] bias: -0.368
largest weight difference: 8.53e-14
R squared: 0.9893
```

## Suggested order of work

1. Requirements 1 and 5 first: they are short and the later tests use them.
2. Requirement 2. Start with a single feature (write the gradient for one weight as in 18-04), get the one-epoch test passing, then rewrite it with `X.T @ errors` so it handles any number of features at once. Work out the shapes on paper: `X` is (n, k), `errors` is (n,), so `X.T @ errors` is (k,), one value per weight.
3. Requirements 3 and 4.
4. Requirement 6, then run the script and look at the loss curves in `figures/`.

## Things to notice

- The diabetes features must be standardised before training. Try `fit` on `load_diabetes(scaled=False).data` without standardising: what happens to the loss?
- The gradient descent weights for `make_regression` are not the **true** weights; they are the least-squares weights. Noise means even the best possible line differs from the one that generated the data.
- The diabetes R squared is only about 0.52: half the variation in disease progression is not explained by a straight-line combination of these features.

## Stretch goals

1. Add an optional `tolerance` argument: stop early when the loss improves by less than it between epochs, and record how many epochs were used in `n_epochs_`.
2. Add **mini-batch** gradient descent: on each epoch, shuffle the rows (with a seeded generator) and update on batches of 32 rows at a time. Compare the loss curve with the full-batch version.
3. Compare your model with `sklearn.linear_model.LinearRegression` on the diabetes data: fit both, and check their `coef_` and `intercept_` against your `weights_` and `bias_`.

## Reference solution

`solution/linear_regression_gd.py` passes every test, and `solution/figures/` holds its loss curves. To run the tests against it:

```
COURSE_SOLUTIONS=1 python -m pytest part-4-maths-for-ml/project/starter
```
