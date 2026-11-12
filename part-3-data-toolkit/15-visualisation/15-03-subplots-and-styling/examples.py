# 15-03 Subplots and styling
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
sales["date"] = pd.to_datetime(sales["date"])
sales["revenue"] = sales["units"] * sales["unit_price"]
categories = sorted(sales["category"].unique())

# Example 1: a grid of subplots
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(9, 6))
print(axes.shape)
for ax, category in zip(axes.flat, categories):
    subset = sales[sales["category"] == category]
    ax.hist(subset["units"], bins=12, edgecolor="white")
    ax.set_title(category)
fig.suptitle("Units sold per row, by category")
fig.tight_layout()
fig.savefig(FIGURES / "grid.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: shared axes make panels comparable
fig, axes = plt.subplots(1, 4, figsize=(12, 3), sharey=True)
for ax, category in zip(axes, categories):
    weekly = sales[sales["category"] == category].groupby(pd.Grouper(key="date", freq="W"))["revenue"].sum()
    ax.plot(weekly.index, weekly.values)
    ax.set_title(category)
    ax.tick_params(axis="x", labelrotation=45)
axes[0].set_ylabel("Weekly revenue (£)")
fig.tight_layout()
fig.savefig(FIGURES / "shared_y.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 3: colours, and highlighting one thing on purpose
store_revenue = sales.groupby("store")["revenue"].sum().sort_values()
colours = ["tab:orange" if store == "S1" else "lightgrey" for store in store_revenue.index]
fig, ax = plt.subplots(figsize=(6, 4))
ax.barh(store_revenue.index, store_revenue.values, color=colours)
ax.set_title("S1 earns the most revenue")
ax.set_xlabel("Revenue (£)")
ax.spines[["top", "right"]].set_visible(False)
fig.savefig(FIGURES / "highlight.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 4: annotations point the reader at what matters
daily = sales.groupby("date")["revenue"].sum()
best_day = daily.idxmax()
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(daily.index, daily.values, linewidth=1)
ax.annotate(
    f"Best day: {best_day:%d %b}",
    xy=(best_day, daily.max()),
    xytext=(best_day + pd.Timedelta(days=12), daily.max() * 0.95),
    arrowprops={"arrowstyle": "->"},
)
ax.axhline(daily.mean(), color="grey", linestyle=":", label="Daily average")
ax.set_title("Daily revenue")
ax.legend()
fig.autofmt_xdate()
fig.savefig(FIGURES / "annotated.png", dpi=100, bbox_inches="tight")
plt.close(fig)
print(best_day.date(), round(daily.max(), 2), round(daily.mean(), 2))

# Example 5: a style sheet changes the look of every plot
print(plt.style.available[:5])
with plt.style.context("ggplot"):
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(categories, sales.groupby("category")["units"].sum().reindex(categories))
    ax.set_title("Units by category (ggplot style)")
    fig.savefig(FIGURES / "styled.png", dpi=100, bbox_inches="tight")
    plt.close(fig)
