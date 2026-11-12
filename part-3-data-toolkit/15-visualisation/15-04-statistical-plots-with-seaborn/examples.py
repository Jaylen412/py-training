# 15-04 Statistical plots with seaborn
import warnings
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris, load_wine

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
pd.set_option("display.width", 120)
pd.set_option("display.max_columns", None)
# seaborn 0.13 uses a Matplotlib option that newer Matplotlib versions have
# deprecated. The warning comes from inside seaborn, not from this code.
warnings.filterwarnings("ignore", message="vert: bool was deprecated")

# Example 1: a scikit-learn dataset as a DataFrame
wine = load_wine(as_frame=True)
wines = wine.frame
wines["cultivar"] = wines["target"].map(dict(enumerate(wine.target_names)))
print(wines.shape)
print(wines[["alcohol", "color_intensity", "proline", "cultivar"]].head(3))
print(wines["cultivar"].value_counts().sort_index())

sns.set_theme(style="whitegrid")

# Example 2: histplot - a distribution, split by group with hue
fig, ax = plt.subplots(figsize=(6, 4))
sns.histplot(data=wines, x="alcohol", hue="cultivar", bins=20, ax=ax)
ax.set_title("Alcohol content by cultivar")
fig.savefig(FIGURES / "histplot.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 3: boxplot - compare groups at a glance
fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(data=wines, x="cultivar", y="proline", ax=ax)
ax.set_title("Proline by cultivar")
fig.savefig(FIGURES / "boxplot.png", dpi=100, bbox_inches="tight")
plt.close(fig)
print(wines.groupby("cultivar")["proline"].median())

# Example 4: scatterplot with hue - do the groups separate?
fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=wines, x="color_intensity", y="proline", hue="cultivar", ax=ax)
ax.set_title("Two features that separate the cultivars")
fig.savefig(FIGURES / "scatterplot.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: pairplot - every pair of features at once
iris = load_iris(as_frame=True)
flowers = iris.frame.rename(columns=lambda name: name.replace(" (cm)", "").replace(" ", "_"))
flowers["species"] = flowers["target"].map(dict(enumerate(iris.target_names)))
grid = sns.pairplot(flowers.drop(columns="target"), hue="species", height=1.8)
grid.savefig(FIGURES / "pairplot.png", dpi=80)
plt.close(grid.figure)
print(flowers.columns.tolist())

# Example 6: heatmap of a correlation matrix
features = ["alcohol", "malic_acid", "flavanoids", "color_intensity", "hue", "proline"]
correlations = wines[features].corr()
print(correlations.round(2))
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(correlations, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1, ax=ax)
ax.set_title("Correlation between wine features")
fig.savefig(FIGURES / "heatmap.png", dpi=100, bbox_inches="tight")
plt.close(fig)
