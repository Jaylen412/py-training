# 24-01 Preprocessing real data
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler

DATA = Path(__file__).resolve().parents[3] / "data"

# Example 1: a first look at the churn data
churn = pd.read_csv(DATA / "customer_churn.csv")
print(churn.shape)
print(churn.dtypes.value_counts().to_string())
print(churn.isna().sum()[churn.isna().sum() > 0].to_string())
print(churn["churned"].mean().round(3))

# Example 2: split BEFORE any preprocessing
X = churn.drop(columns=["customer_id", "churned"])
y = churn["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
print(X_train.shape, X_test.shape)

# Example 3: one-hot encoding a nominal category
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(X_train[["contract"]])
print(encoder.get_feature_names_out())
print(X_train["contract"].head(3).tolist())
print(encoded[:3])

# Example 4: unseen categories at prediction time
strict = OneHotEncoder(sparse_output=False).fit(pd.DataFrame({"contract": ["one-year", "two-year"]}))
try:
    strict.transform(pd.DataFrame({"contract": ["month-to-month"]}))
except ValueError as error:
    print("ValueError:", str(error).splitlines()[0])
tolerant = OneHotEncoder(sparse_output=False, handle_unknown="ignore").fit(pd.DataFrame({"contract": ["one-year", "two-year"]}))
print(tolerant.transform(pd.DataFrame({"contract": ["month-to-month"]})))

# Example 5: ordinal encoding keeps the order
ordinal = OrdinalEncoder(categories=[["low", "medium", "high"]])
print(ordinal.fit_transform(pd.DataFrame({"satisfaction": ["high", "low", "medium"]})).ravel())

# Example 6: imputing missing values
imputer = SimpleImputer(strategy="median")
filled = imputer.fit_transform(X_train[["monthly_charges", "total_charges"]])
print(imputer.statistics_.round(2))
print(np.isnan(filled).sum())
most_frequent = SimpleImputer(strategy="most_frequent").fit(X_train[["payment_method"]])
print(most_frequent.statistics_)

# Example 7: ColumnTransformer - a different recipe for each group of columns
numeric = ["tenure_months", "monthly_charges", "total_charges", "support_calls"]
nominal = ["contract", "payment_method", "internet_service", "region"]
ordered = ["satisfaction"]

numeric_steps = [("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())]
from sklearn.pipeline import Pipeline  # noqa: E402  (24-02 explains Pipeline fully)

preprocess = ColumnTransformer([
    ("numeric", Pipeline(numeric_steps), numeric),
    ("nominal", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), nominal),
    ("ordered", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                          ("encode", OrdinalEncoder(categories=[["low", "medium", "high"]]))]), ordered),
])
train_ready = preprocess.fit_transform(X_train)
test_ready = preprocess.transform(X_test)
print(train_ready.shape, test_ready.shape)
print(list(preprocess.get_feature_names_out())[:6])
print(np.isnan(train_ready).sum(), np.isnan(test_ready).sum())
