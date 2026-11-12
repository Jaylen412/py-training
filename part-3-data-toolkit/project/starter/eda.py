"""Part 3 project: exploratory data analysis of the wine and store sales data.

Fill in each function, then run this file from the repository root to build
your figures and print the numbers for REPORT.md:
    python part-3-data-toolkit/project/starter/eda.py
"""
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_wine

DATA = Path(__file__).resolve().parents[3] / "data"
FIGURES = Path(__file__).parent / "figures"
WINE_FEATURES = ["alcohol", "flavanoids", "color_intensity", "proline"]

# seaborn 0.13 triggers a Matplotlib deprecation warning internally.
warnings.filterwarnings("ignore", message="vert: bool was deprecated")


# ---------- Requirement 1: wine ----------

def load_wine_frame():
    """Return load_wine(as_frame=True).frame with an extra "cultivar" column
    holding the class name ("class_0", "class_1" or "class_2")."""
    raise NotImplementedError


def wine_summary(wines):
    """Return a DataFrame indexed by cultivar with the median of each column
    in WINE_FEATURES (in that order)."""
    raise NotImplementedError


def strongest_wine_correlations(wines, count=3):
    """Return a Series of the `count` numeric features whose correlation with
    "target" is largest in absolute value, strongest first, keeping the sign."""
    raise NotImplementedError


# ---------- Requirement 2: sales cleaning ----------

def clean_sales(raw):
    """Return a cleaned COPY of the raw sales data:
    - remove duplicate rows,
    - strip and title-case the category column,
    - convert date to datetimes,
    - drop rows with no units, and make units an int column,
    - fill missing unit_price with the median price of the same category,
    - renumber the index from 0.
    The result has 468 rows and no missing values.
    """
    raise NotImplementedError


# ---------- Requirement 3: sales features ----------

def add_features(sales):
    """Return a copy of the clean sales with four new columns: revenue
    (units * unit_price), month (1-12), weekday (such as "Monday") and
    is_weekend (True on Saturday and Sunday)."""
    raise NotImplementedError


# ---------- Requirement 4: sales summary ----------

def sales_summary(sales, stores):
    """Return a dictionary with these keys:
    - "total_revenue": total revenue rounded to 2 places,
    - "revenue_by_category": {category: revenue}, largest first,
    - "revenue_by_store": {store: revenue}, largest first,
    - "unmatched_stores": sorted list of stores in sales but not in stores,
    - "revenue_without_region": revenue of rows whose store has no region,
    - "weekend_uplift": mean weekend units / mean weekday units - 1, rounded to 3,
    - "monthly_revenue": {month number: revenue}.
    """
    raise NotImplementedError


# ---------- Requirement 5: figures ----------

def make_figures(wines, sales, folder):
    """Create at least SIX well-chosen, titled and labelled figures as PNG
    files in `folder` (create it if needed), covering both datasets.
    Return the list of their paths.
    Choose each chart to answer a question (15-02), and put the finding in
    the title where you can (15-03).
    """
    raise NotImplementedError


def main():
    wines = load_wine_frame()
    sales = add_features(clean_sales(pd.read_csv(DATA / "store_sales.csv")))
    stores = pd.read_csv(DATA / "stores.csv")
    print(wine_summary(wines).round(2))
    print(strongest_wine_correlations(wines).round(3))
    print(len(sales), "clean sales rows")
    for key, value in sales_summary(sales, stores).items():
        print(f"{key}: {value}")
    for path in make_figures(wines, sales, FIGURES):
        print("saved", path.name)


if __name__ == "__main__":
    main()
