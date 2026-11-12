# Part 5 Project: End-to-End Classification

## Brief

Predict which customers of a subscription service will **churn** (cancel), using `data/customer_churn.csv` (generate it with `python data/make_customer_churn.py` if it is missing). Follow the professional workflow from Module 24 from start to finish: understand the data, split it, build a leak-free pipeline, compare model families with cross-validation, tune the best one, evaluate on the test set **once**, and write up what the model does and where it fails.

This project brings Part 5 together: metrics and thresholds (22), tree and linear models (21 to 23), and preprocessing, pipelines and cross-validation (24).

## The data

2,000 customers with nine usable columns: tenure, monthly and total charges, number of support calls, contract type, payment method, internet service, region and a satisfaction rating (low, medium, high). The target `churned` is 1 for the 27.7% who left. Four columns have missing values.

## Getting started

Work in `starter/churn_model.py` and `starter/REPORT.md`. Every function has a docstring that says exactly what to return; `load_churn`, `folds` and `main` are written for you.

```
python -m pytest part-5-supervised-learning/project/starter
python part-5-supervised-learning/project/starter/churn_model.py
```

Run on a fresh starter, the tests that use a fixture show `ERROR` rather than `FAILED`, because the fixture calls a function you have not written yet. They turn green as you implement the functions.

## Requirements

1. `churn_summary`: the facts for your EDA (rows, churn rate, missing values, churn rate by contract).
2. `split_data`: drop the ID, make a stratified 80/20 split with `random_state=42`. Nothing is fitted before this.
3. `build_pipeline`: preprocessing (impute, scale, one-hot encode, ordinal encode) inside a `Pipeline`, ending with the model you pass in.
4. `candidate_models` and `compare_models`: a baseline plus at least three model families, compared by 5-fold cross-validated ROC AUC on the training data only.
5. `tune_logistic`: grid search over `C` with cross-validation.
6. `evaluate`: accuracy, precision, recall, ROC AUC and confusion counts on the test set, with an adjustable threshold. `best_threshold` picks a threshold from the costs of each mistake, using out-of-fold predictions.
7. `top_coefficients` and `plot_evaluation`: the strongest effects, and a figure with the confusion matrix and ROC curve.
8. `REPORT.md`: fill in each section using your own numbers.

## Suggested order of work

1. Requirements 1 and 2, then look at the numbers `main` prints.
2. Requirement 3. Test it by hand: fit it on the training data and predict three test rows, including one with an invented region.
3. Requirements 4 and 5. Expect the **baseline to score an AUC of exactly 0.5**: any real model must beat that.
4. Requirement 6. Look at recall at the default threshold of 0.5, then at your chosen threshold.
5. Requirement 7, then the report.

## Things to notice

- The best model is the **simplest** one. The data has mostly linear structure, and a tuned logistic regression beats the random forest and gradient boosting. Do not assume that complex means better.
- At the default threshold the model **misses over half the churners** (recall 0.47), even though accuracy is a respectable 78.5%. Accuracy hides this: always predicting "stays" scores 72.3%.
- The threshold is a **business decision**, not a modelling one. If a retention offer costs 1 unit and losing a customer costs 5, a threshold of 0.2 finds 89% of churners at the price of many more offers.
- Choose the threshold from out-of-fold **training** predictions. If you pick it by looking at the test set, the test result is no longer honest.

## Stretch goals

1. Add `class_weight="balanced"` to the logistic regression and compare its recall and precision with the threshold approach.
2. Add a `RandomizedSearchCV` for gradient boosting (24-03). Can tuning make it beat logistic regression?
3. Plot the precision-recall curve (22-03) and mark your chosen threshold on it.
4. Save the final pipeline with `joblib` and write a function that takes one customer as a dictionary and returns the churn probability.

## Reference solution

`solution/churn_model.py` passes every test, `solution/REPORT.md` is a completed write-up, and `solution/figures/evaluation.png` is its evaluation figure. To run the tests against it:

```
COURSE_SOLUTIONS=1 python -m pytest part-5-supervised-learning/project/starter
```
