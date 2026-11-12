# 19-04 Covariance, correlation and sampling error
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
diabetes = load_diabetes(as_frame=True, scaled=False).frame
bmi = diabetes["bmi"].to_numpy()
progression = diabetes["target"].to_numpy()

# Example 1: covariance - do two variables move together?
products = (bmi - bmi.mean()) * (progression - progression.mean())
print(round(products.mean(), 2))
print(round(np.cov(bmi, progression, ddof=0)[0, 1], 2))

# Example 2: covariance depends on units; correlation does not
print(round(np.cov(bmi * 10, progression, ddof=0)[0, 1], 2))
correlation = products.mean() / (bmi.std() * progression.std())
print(round(correlation, 3), round(np.corrcoef(bmi, progression)[0, 1], 3))
print(round(np.corrcoef(bmi * 10, progression)[0, 1], 3))

# Example 3: a correlation matrix for several features
print(diabetes[["bmi", "bp", "s5", "target"]].corr().round(2))

# Example 4: population versus sample - every sample gives a different answer
rng = np.random.default_rng(42)
for _ in range(3):
    rows = rng.choice(len(bmi), size=40, replace=False)
    print(round(np.corrcoef(bmi[rows], progression[rows])[0, 1], 3))

# Example 5: the bootstrap - resample the one sample you have
rng = np.random.default_rng(42)
sample_rows = rng.choice(len(bmi), size=60, replace=False)
sample_bmi = bmi[sample_rows]
print(round(sample_bmi.mean(), 3))
boot_means = np.array([rng.choice(sample_bmi, size=len(sample_bmi), replace=True).mean() for _ in range(5_000)])
print(round(boot_means.std(), 3), round(sample_bmi.std(ddof=1) / np.sqrt(len(sample_bmi)), 3))
low, high = np.percentile(boot_means, [2.5, 97.5])
print(round(low, 3), round(high, 3), round(bmi.mean(), 3))

fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(boot_means, bins=40, edgecolor="white")
ax.axvline(low, color="tab:red", linestyle="--", label="95% interval")
ax.axvline(high, color="tab:red", linestyle="--")
ax.axvline(bmi.mean(), color="black", label="mean of all 442 patients")
ax.set_xlabel("Mean BMI of a resample")
ax.set_title("Bootstrap distribution of the mean BMI (sample of 60)")
ax.legend()
fig.savefig(FIGURES / "bootstrap.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 6: bootstrapping a correlation
sample_progression = progression[sample_rows]
boot_corrs = []
for _ in range(5_000):
    rows = rng.choice(len(sample_bmi), size=len(sample_bmi), replace=True)
    boot_corrs.append(np.corrcoef(sample_bmi[rows], sample_progression[rows])[0, 1])
print(round(np.corrcoef(sample_bmi, sample_progression)[0, 1], 3))
print(np.round(np.percentile(boot_corrs, [2.5, 97.5]), 3))
