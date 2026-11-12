"""Part 3 project: exploratory data analysis of the wine and store sales data.

Run from the repository root to rebuild the figures and print the numbers
used in REPORT.md:
    python part-3-data-toolkit/project/solution/eda.py
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
    """Return the wine data with a "cultivar" name column."""
    wine = load_wine(as_frame=True)
    frame = wine.frame.copy()
    frame["cultivar"] = frame["target"].map(dict(enumerate(wine.target_names)))
    return frame


def wine_summary(wines):
    """Return the median of the key wine features for each cultivar."""
    return wines.groupby("cultivar")[WINE_FEATURES].median()


def strongest_wine_correlations(wines, count=3):
    """Return the features most correlated (by absolute value) with the target."""
    correlations = wines.select_dtypes(include="number").corr()["target"].drop("target")
    order = correlations.abs().sort_values(ascending=False).index
    return correlations[order][:count]


# ---------- Requirement 2: sales cleaning ----------

def clean_sales(raw):
    """Return cleaned sales data.

    Removes duplicates, tidies categories, parses dates, drops rows with no
    units, and fills missing prices with the median price of the category.
    """
    sales = raw.drop_duplicates().copy()
    sales["category"] = sales["category"].str.strip().str.title()
    sales["date"] = pd.to_datetime(sales["date"])
    sales = sales.dropna(subset=["units"])
    category_median = sales.groupby("category")["unit_price"].transform("median")
    sales["unit_price"] = sales["unit_price"].fillna(category_median)
    sales["units"] = sales["units"].astype(int)
    return sales.reset_index(drop=True)


# ---------- Requirement 3: sales features ----------

def add_features(sales):
    """Return sales with revenue, month, weekday and is_weekend columns."""
    return sales.assign(
        revenue=sales["units"] * sales["unit_price"],
        month=sales["date"].dt.month,
        weekday=sales["date"].dt.day_name(),
        is_weekend=sales["date"].dt.day_of_week >= 5,
    )


# ---------- Requirement 4: sales summary ----------

def sales_summary(sales, stores):
    """Return the headline numbers for the report as a dictionary."""
    with_regions = sales.merge(stores, on="store", how="left", validate="many_to_one")
    weekend = sales.loc[sales["is_weekend"], "units"].mean()
    weekday = sales.loc[~sales["is_weekend"], "units"].mean()
    return {
        "total_revenue": round(float(sales["revenue"].sum()), 2),
        "revenue_by_category": sales.groupby("category")["revenue"].sum().round(2).sort_values(ascending=False).to_dict(),
        "revenue_by_store": sales.groupby("store")["revenue"].sum().round(2).sort_values(ascending=False).to_dict(),
        "unmatched_stores": sorted(set(sales["store"]) - set(stores["store"])),
        "revenue_without_region": round(float(with_regions.loc[with_regions["region"].isna(), "revenue"].sum()), 2),
        "weekend_uplift": round(float(weekend / weekday - 1), 3),
        "monthly_revenue": sales.groupby("month")["revenue"].sum().round(2).to_dict(),
    }


# ---------- Requirement 5: figures ----------

def _save(fig, folder, name):
    path = folder / name
    fig.savefig(path, dpi=100, bbox_inches="tight")
    plt.close(fig)
    return path


def make_figures(wines, sales, folder):
    """Create the report's figures in `folder` and return their paths."""
    folder.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    paths = []

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=wines, x="cultivar", y="proline", ax=ax)
    ax.set_title("Class 0 wines have far more proline")
    paths.append(_save(fig, folder, "wine_proline.png"))

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.scatterplot(data=wines, x="color_intensity", y="flavanoids", hue="cultivar", ax=ax)
    ax.set_title("Colour intensity and flavanoids separate the cultivars")
    paths.append(_save(fig, folder, "wine_scatter.png"))

    fig, ax = plt.subplots(figsize=(7, 5))
    correlations = wines[WINE_FEATURES + ["hue", "malic_acid", "target"]].corr()
    sns.heatmap(correlations, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
    ax.set_title("Correlations between wine features and the target")
    paths.append(_save(fig, folder, "wine_correlations.png"))

    revenue = sales.groupby("category")["revenue"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(revenue.index, revenue.values, color="tab:blue")
    ax.set_title("Clothing and Electronics earn the most")
    ax.set_xlabel("Revenue, Q1 2026 (£)")
    paths.append(_save(fig, folder, "sales_by_category.png"))

    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=sales, x="is_weekend", y="units", ax=ax)
    ax.set_yscale("log")
    ax.set_xticks([0, 1], ["Weekday", "Weekend"])
    ax.set_xlabel("")
    ax.set_title("More units are sold per row at weekends")
    paths.append(_save(fig, folder, "sales_weekend.png"))

    weekly = sales.groupby(pd.Grouper(key="date", freq="W"))["revenue"].sum().iloc[:-1]
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(weekly.index, weekly.values, marker="o")
    ax.set_title("Weekly revenue drifts down over the quarter")
    ax.set_ylabel("Revenue (£)")
    fig.autofmt_xdate()
    paths.append(_save(fig, folder, "sales_weekly.png"))

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.hist(np.log1p(sales["units"]), bins=25, edgecolor="white")
    ax.set_title("Units sold, after a log transform")
    ax.set_xlabel("log(1 + units)")
    paths.append(_save(fig, folder, "sales_units_log.png"))

    return paths


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
