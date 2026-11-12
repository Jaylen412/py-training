# 19-03 Distributions and sampling
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
rng = np.random.default_rng(42)

# Example 1: three distributions, 10,000 draws each
uniform = rng.uniform(0, 10, size=10_000)
normal = rng.normal(loc=170, scale=10, size=10_000)
binomial = rng.binomial(n=20, p=0.3, size=10_000)
for name, sample in [("uniform", uniform), ("normal", normal), ("binomial", binomial)]:
    print(f"{name:<9} mean {sample.mean():8.3f}  std {sample.std():6.3f}")

fig, axes = plt.subplots(1, 3, figsize=(13, 3.5))
axes[0].hist(uniform, bins=30, edgecolor="white")
axes[0].set_title("Uniform(0, 10)")
axes[1].hist(normal, bins=40, edgecolor="white")
axes[1].set_title("Normal(mean 170, sd 10)")
counts = np.bincount(binomial, minlength=21)
axes[2].bar(np.arange(21), counts)
axes[2].set_title("Binomial(20 trials, p = 0.3)")
fig.tight_layout()
fig.savefig(FIGURES / "distributions.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: the 68-95-99.7 rule for the normal distribution
for k in [1, 2, 3]:
    within = np.mean(np.abs(normal - 170) <= k * 10)
    print(f"within {k} sd: {within:.3f}")

# Example 3: binomial probabilities by counting
print(round(np.mean(binomial == 6), 4), round(np.mean(binomial >= 10), 4))
print(20 * 0.3, round(np.sqrt(20 * 0.3 * 0.7), 3))

# Example 4: a skewed population
population = rng.exponential(scale=10, size=100_000)
print(round(population.mean(), 3), round(np.median(population), 3))

# Example 5: sample means vary from sample to sample
for _ in range(3):
    sample = rng.choice(population, size=30)
    print(round(sample.mean(), 2))

# Example 6: the central limit theorem - means of samples look normal
sample_means = np.array([rng.choice(population, size=30).mean() for _ in range(5_000)])
print(round(sample_means.mean(), 3), round(sample_means.std(), 3))
print(round(population.std() / np.sqrt(30), 3))

fig, axes = plt.subplots(1, 2, figsize=(11, 3.5))
axes[0].hist(population, bins=60, edgecolor="white")
axes[0].set_title("Population: strongly skewed")
axes[1].hist(sample_means, bins=40, edgecolor="white")
axes[1].set_title("Means of 5,000 samples of size 30: bell-shaped")
fig.tight_layout()
fig.savefig(FIGURES / "central_limit.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 7: bigger samples give less variable means
for size in [5, 30, 200]:
    means = np.array([rng.choice(population, size=size).mean() for _ in range(2_000)])
    print(f"sample size {size:>3}: spread of means {means.std():.3f}")
