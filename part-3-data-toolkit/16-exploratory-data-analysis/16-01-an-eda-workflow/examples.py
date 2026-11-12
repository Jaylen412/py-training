# 16-01 An EDA workflow
# A repeatable checklist, applied to the breast cancer dataset from scikit-learn.
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", 8)
sns.set_theme(style="whitegrid")

dataset = load_breast_cancer(as_frame=True)
tumours = dataset.frame
tumours["diagnosis"] = tumours["target"].map({0: "malignant", 1: "benign"})

# Step 1: shape and a first look
print(tumours.shape)
print(tumours.iloc[:3, :5])

# Step 2: types
print(tumours.dtypes.value_counts())

# Step 3: missing values and duplicates
print("missing values:", int(tumours.isna().sum().sum()))
print("duplicate rows:", int(tumours.duplicated().sum()))

# Step 4: the target - how balanced are the classes?
print(tumours["diagnosis"].value_counts())
print(tumours["diagnosis"].value_counts(normalize=True).round(3))

# Step 5: distributions of individual features
features = ["mean radius", "mean texture", "mean concavity", "worst area"]
print(tumours[features].describe().round(2))
fig, axes = plt.subplots(1, 4, figsize=(14, 3))
for ax, feature in zip(axes, features):
    sns.histplot(data=tumours, x=feature, hue="diagnosis", ax=ax, bins=25, legend=(feature == features[-1]))
fig.tight_layout()
fig.savefig(FIGURES / "distributions.png", dpi=90, bbox_inches="tight")
plt.close(fig)

# Step 6: relationships - with the target, and between features
by_class = tumours.groupby("diagnosis")[features].median().round(2)
print(by_class)
correlation_with_target = (
    tumours.drop(columns=["diagnosis"]).corr()["target"].drop("target").sort_values()
)
print(correlation_with_target.head(3).round(3))
print(correlation_with_target.tail(3).round(3))
fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=tumours, x="mean radius", y="mean concavity", hue="diagnosis", alpha=0.7, ax=ax)
ax.set_title("Malignant tumours are larger and more concave")
fig.savefig(FIGURES / "relationship.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Step 7: write findings down, each backed by a number
radius_medians = by_class["mean radius"]
findings = [
    "569 tumours, 30 numeric features, no missing values or duplicates.",
    f"{(tumours['diagnosis'] == 'benign').mean():.1%} are benign: the classes are moderately imbalanced.",
    f"Median radius is {radius_medians['malignant']} for malignant vs {radius_medians['benign']} for benign.",
    f"The feature most correlated with the target is '{correlation_with_target.index[0]}' "
    f"({correlation_with_target.iloc[0]:.2f}).",
]
for number, finding in enumerate(findings, start=1):
    print(f"{number}. {finding}")
