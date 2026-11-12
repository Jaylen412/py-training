# 24-03 Cross-validation and hyperparameter tuning
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import loguniform, randint
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (GridSearchCV, KFold, RandomizedSearchCV, StratifiedKFold,
                                     cross_val_score, train_test_split)
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

DATA = Path(__file__).resolve().parents[3] / "data"

churn = pd.read_csv(DATA / "customer_churn.csv")
X = churn.drop(columns=["customer_id", "churned"])
y = churn["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

numeric = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
nominal = ["contract", "payment_method", "internet_service", "region"]
ordered = ["satisfaction"]
preprocess = ColumnTransformer([
    ("numeric", make_pipeline(SimpleImputer(strategy="median"), StandardScaler()), numeric),
    ("nominal", make_pipeline(SimpleImputer(strategy="most_frequent"),
                              OneHotEncoder(handle_unknown="ignore")), nominal),
    ("ordered", make_pipeline(SimpleImputer(strategy="most_frequent"),
                              OrdinalEncoder(categories=[["low", "medium", "high"]])), ordered),
])
pipe = Pipeline([("preprocess", preprocess), ("model", LogisticRegression(max_iter=1000))])

# Example 1: one split gives one noisy number
for seed in [0, 1, 2]:
    a_train, a_valid, b_train, b_valid = train_test_split(X_train, y_train, test_size=0.25, random_state=seed,
                                                          stratify=y_train)
    print(f"split {seed}: validation accuracy {pipe.fit(a_train, b_train).score(a_valid, b_valid):.3f}")

# Example 2: k-fold by hand
folds = KFold(n_splits=5, shuffle=True, random_state=42)
scores = []
for train_rows, valid_rows in folds.split(X_train):
    pipe.fit(X_train.iloc[train_rows], y_train.iloc[train_rows])
    scores.append(pipe.score(X_train.iloc[valid_rows], y_train.iloc[valid_rows]))
print(np.round(scores, 3), round(np.mean(scores), 3), round(np.std(scores), 3))

# Example 3: cross_val_score does the loop for you
stratified = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipe, X_train, y_train, cv=stratified)
print(np.round(scores, 3), round(scores.mean(), 3))
roc = cross_val_score(pipe, X_train, y_train, cv=stratified, scoring="roc_auc")
print("ROC AUC:", round(roc.mean(), 3), "+/-", round(roc.std(), 3))

# Example 4: comparing models with cross-validation
for name, model in [("logistic regression", LogisticRegression(max_iter=1000)),
                    ("gradient boosting", HistGradientBoostingClassifier(random_state=42))]:
    pipe.set_params(model=model)
    auc = cross_val_score(pipe, X_train, y_train, cv=stratified, scoring="roc_auc")
    print(f"{name:<20} ROC AUC {auc.mean():.3f} +/- {auc.std():.3f}")

# Example 5: GridSearchCV tries every combination
pipe.set_params(model=LogisticRegression(max_iter=1000))
grid = GridSearchCV(pipe, {"model__C": [0.01, 0.1, 1, 10]}, cv=stratified, scoring="roc_auc")
grid.fit(X_train, y_train)
print(grid.best_params_, round(grid.best_score_, 3))
results = pd.DataFrame(grid.cv_results_)[["param_model__C", "mean_test_score", "rank_test_score"]]
print(results.round(3).to_string(index=False))

# Example 6: RandomizedSearchCV samples combinations
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

# Example 7: the test set, used exactly once at the very end
final = grid.best_estimator_
from sklearn.metrics import roc_auc_score  # noqa: E402

print("test ROC AUC:", round(roc_auc_score(y_test, final.predict_proba(X_test)[:, 1]), 3))
print("test accuracy:", round(final.score(X_test, y_test), 3))
