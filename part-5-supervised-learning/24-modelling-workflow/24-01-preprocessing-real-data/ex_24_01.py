"""Exercises for 24-01 Preprocessing real data."""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder, StandardScaler


def missing_report(df):
    """Return a Series of missing-value counts, keeping only columns that
    have at least one gap, sorted from most to fewest missing.

    Example: for the churn data, the first entry is satisfaction with 115.
    """
    raise NotImplementedError


def split_churn(df, test_size=0.2):
    """Drop the "customer_id" column, use "churned" as the target and the
    remaining columns as features. Return X_train, X_test, y_train, y_test
    from train_test_split with random_state=42 and stratify=y."""
    raise NotImplementedError


def column_groups(X):
    """Return (numeric, text): two lists of column names, in the original
    column order. Numeric columns are those whose dtype is a number (use
    pd.api.types.is_numeric_dtype); every other column is text."""
    raise NotImplementedError


def build_preprocessor(numeric, nominal, ordered, order):
    """Return an UNFITTED ColumnTransformer with three parts:
    - "numeric": median imputation then StandardScaler, for `numeric`;
    - "nominal": most-frequent imputation then
      OneHotEncoder(handle_unknown="ignore", sparse_output=False), for `nominal`;
    - "ordered": most-frequent imputation then
      OrdinalEncoder(categories=[order]), for `ordered`.
    Chain each part's two steps with a Pipeline.
    """
    raise NotImplementedError
