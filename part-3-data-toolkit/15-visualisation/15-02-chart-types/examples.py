# 15-02 Chart types and when to use them
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
DATA = Path(__file__).resolve().parents[3] / "data"

sales = pd.read_csv(DATA / "store_sales.csv").drop_duplicates().dropna()
sales["category"] = sales["category"].str.strip().str.title()
sales["revenue"] = sales["units"] * sales["unit_price"]

# Example 1: bar chart - compare a number across categories
revenue = sales.groupby("category")["revenue"].sum().sort_values(ascending=False)
print(revenue.round(0))
fig, ax = plt.subplots(figsize=(6, 4))
ax.bar(revenue.index, revenue.values)
ax.set_title("Total revenue by category, Q1 2026")
ax.set_ylabel("Revenue (£)")
fig.savefig(FIGURES / "bar.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: horizontal bars for long labels or many categories
store_revenue = sales.groupby("store")["revenue"].sum().sort_values()
fig, ax = plt.subplots(figsize=(6, 4))
ax.barh(store_revenue.index, store_revenue.values)
ax.set_title("Total revenue by store")
ax.set_xlabel("Revenue (£)")
fig.savefig(FIGURES / "barh.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 3: histogram - the distribution of one numeric variable
fig, ax = plt.subplots(figsize=(6, 4))
counts, edges, _ = ax.hist(sales["units"], bins=15, edgecolor="white")
ax.set_title("Units sold per row")
ax.set_xlabel("Units")
ax.set_ylabel("Number of rows")
fig.savefig(FIGURES / "histogram.png", dpi=100, bbox_inches="tight")
plt.close(fig)
print(counts[:5], np.round(edges[:3], 2))

# Example 4: box plot - compare distributions between groups
groups = [sales.loc[sales["category"] == name, "unit_price"] for name in revenue.index]
fig, ax = plt.subplots(figsize=(6, 4))
ax.boxplot(groups, tick_labels=revenue.index)
ax.set_title("Unit price by category")
ax.set_ylabel("Unit price (£)")
ax.set_yscale("log")
fig.savefig(FIGURES / "boxplot.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: scatter - the relationship between two numeric variables
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(sales["unit_price"], sales["units"], alpha=0.5, s=15)
ax.set_title("Units sold against unit price")
ax.set_xlabel("Unit price (£)")
ax.set_ylabel("Units sold")
fig.savefig(FIGURES / "scatter.png", dpi=100, bbox_inches="tight")
plt.close(fig)
print(round(sales["unit_price"].corr(sales["units"]), 3))

# Example 6: line chart - change over time
daily = sales.assign(date=pd.to_datetime(sales["date"])).groupby("date")["revenue"].sum()
weekly = daily.resample("W").sum()
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(weekly.index, weekly.values, marker="o")
ax.set_title("Weekly revenue")
ax.set_ylabel("Revenue (£)")
fig.autofmt_xdate()
fig.savefig(FIGURES / "line_over_time.png", dpi=100, bbox_inches="tight")
plt.close(fig)
print(len(weekly), weekly.index[0].date(), weekly.index[-1].date())
