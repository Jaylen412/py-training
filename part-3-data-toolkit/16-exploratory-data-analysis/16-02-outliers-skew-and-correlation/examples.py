# 16-02 Outliers, skew and correlation
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 120)

sales = pd.read_csv(DATA / "store_sales.csv").drop_duplicates().dropna()
sales["category"] = sales["category"].str.strip().str.title()
units = sales["units"]

# Example 1: outliers by the IQR rule
q1, q3 = units.quantile([0.25, 0.75])
iqr = q3 - q1
low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
outliers = units[(units < low) | (units > high)]
print(f"Q1={q1}, Q3={q3}, IQR={iqr}, bounds=({low}, {high})")
print(len(outliers), "outliers; smallest is", outliers.min())

# Example 2: are they errors or real? Look at which rows they are.
print(sales.loc[outliers.index, "category"].value_counts())

# Example 3: the same rule within each category tells a different story
within = sales.groupby("category")["units"].transform(
    lambda values: (values > values.quantile(0.75) + 1.5 * (values.quantile(0.75) - values.quantile(0.25)))
)
print(int(within.sum()), "outliers when judged within their own category")

# Example 4: z-scores - how many standard deviations from the mean
z_scores = (units - units.mean()) / units.std()
print(int((z_scores.abs() > 3).sum()), "rows with |z| > 3")

# Example 5: skew - a long tail on one side
print(round(units.skew(), 2), round(units.mean(), 2), units.median())
log_units = np.log1p(units)
print(round(log_units.skew(), 2))
fig, axes = plt.subplots(1, 2, figsize=(10, 3.5))
axes[0].hist(units, bins=25, edgecolor="white")
axes[0].set_title(f"Units (skew {units.skew():.2f})")
axes[1].hist(log_units, bins=25, edgecolor="white")
axes[1].set_title(f"log(1 + units) (skew {log_units.skew():.2f})")
fig.tight_layout()
fig.savefig(FIGURES / "skew.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 6: correlation is not causation - a third variable drives both
print(round(sales["unit_price"].corr(sales["units"]), 3))
for category, rows in sales.groupby("category"):
    print(f"{category:<12}{rows['unit_price'].corr(rows['units']):7.3f}")

# Example 7: a correlation of zero does not mean "no relationship"
x = np.linspace(-3, 3, 61)
print(round(np.corrcoef(x, x ** 2)[0, 1], 3))

# Example 8: Simpson's paradox - a trend that reverses inside every group
treatments = pd.DataFrame({
    "treatment": ["A"] * 2 + ["B"] * 2,
    "stone_size": ["small", "large", "small", "large"],
    "patients": [87, 263, 270, 80],
    "recovered": [81, 192, 234, 55],
})
treatments["rate"] = (treatments["recovered"] / treatments["patients"]).round(3)
print(treatments)
overall = treatments.groupby("treatment")[["patients", "recovered"]].sum()
overall["rate"] = (overall["recovered"] / overall["patients"]).round(3)
print(overall)
