# 24-02 Pipelines
import tempfile
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

DATA = Path(__file__).resolve().parents[3] / "data"

# Example 1: a pipeline chains steps into one model
from sklearn.datasets import load_breast_cancer  # noqa: E402

cancer = load_breast_cancer()
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
pipe = Pipeline([("scale", StandardScaler()), ("model", LogisticRegression(max_iter=1000))])
pipe.fit(Xc_train, yc_train)
print(round(pipe.score(Xc_test, yc_test), 3))
print(list(pipe.named_steps))
print(pipe.named_steps["scale"].mean_[:2].round(2))

# Example 2: make_pipeline names the steps for you
quick = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000))
print(list(quick.named_steps))

# Example 3: leakage - selecting features on ALL the data before cross-validation
rng = np.random.default_rng(42)
noise = rng.normal(size=(100, 5000))
labels = rng.integers(0, 2, size=100)
leaky_features = SelectKBest(f_classif, k=20).fit_transform(noise, labels)
leaky = cross_val_score(LogisticRegression(), leaky_features, labels, cv=5).mean()
honest = cross_val_score(make_pipeline(SelectKBest(f_classif, k=20), LogisticRegression()), noise, labels, cv=5).mean()
print(f"leaky: {leaky:.3f}  honest: {honest:.3f}")

# Example 4: the full churn pipeline - preprocessing and model together
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
churn_model = Pipeline([("preprocess", preprocess), ("model", LogisticRegression(max_iter=1000))])
churn_model.fit(X_train, y_train)
print("logistic regression test accuracy:", round(churn_model.score(X_test, y_test), 3))
print(churn_model.predict_proba(X_test.head(3)).round(3))

# Example 5: swapping the model is one line
churn_model.set_params(model=HistGradientBoostingClassifier(random_state=42))
churn_model.fit(X_train, y_train)
print("gradient boosting test accuracy:", round(churn_model.score(X_test, y_test), 3))
churn_model.set_params(model=LogisticRegression(max_iter=1000)).fit(X_train, y_train)

# Example 6: saving and loading the whole pipeline with joblib
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
