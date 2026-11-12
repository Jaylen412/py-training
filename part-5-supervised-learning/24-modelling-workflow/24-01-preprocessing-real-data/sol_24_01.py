"""Solutions for 24-01 Preprocessing real data."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


def missing_report(df):
    """Missing-value counts for columns with gaps, largest first."""
    counts = df.isna().sum()
    return counts[counts > 0].sort_values(ascending=False)


def split_churn(df, test_size=0.2):
    """Separate features and target, then make a stratified split."""
    X = df.drop(columns=["customer_id", "churned"])
    y = df["churned"]
    return train_test_split(X, y, test_size=test_size, random_state=42, stratify=y)


def column_groups(X):
    """Return (numeric column names, text column names)."""
    numeric = [column for column in X.columns if pd.api.types.is_numeric_dtype(X[column])]
    text = [column for column in X.columns if column not in numeric]
    return numeric, text


def build_preprocessor(numeric, nominal, ordered, order):
    """Return the churn ColumnTransformer."""
    return ColumnTransformer([
        ("numeric", Pipeline([("impute", SimpleImputer(strategy="median")),
                              ("scale", StandardScaler())]), numeric),
        ("nominal", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                              ("encode", OneHotEncoder(handle_unknown="ignore", sparse_output=False))]), nominal),
        ("ordered", Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                              ("encode", OrdinalEncoder(categories=[order]))]), ordered),
    ])
