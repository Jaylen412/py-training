# 15-01 Matplotlib fundamentals
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # draw to files only; no window needed
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Example 1: the smallest plot - a figure, one axes, one line
months = np.arange(1, 13)
temperature = np.array([5, 6, 9, 12, 15, 18, 21, 21, 18, 14, 9, 6])

fig, ax = plt.subplots()
ax.plot(months, temperature)
fig.savefig(FIGURES / "first_line.png")
plt.close(fig)
print(type(fig).__name__, type(ax).__name__)

# Example 2: labels, a title, and a saved file
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(months, temperature, marker="o")
ax.set_title("Average monthly temperature, London")
ax.set_xlabel("Month")
ax.set_ylabel("Temperature (°C)")
ax.set_xticks(months)
fig.savefig(FIGURES / "labelled_line.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 3: several lines and a legend
rainfall_london = np.array([55, 41, 42, 44, 49, 45, 45, 50, 49, 69, 59, 55])
rainfall_glasgow = np.array([110, 80, 82, 59, 59, 59, 64, 77, 92, 116, 106, 115])
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(months, rainfall_london, label="London")
ax.plot(months, rainfall_glasgow, label="Glasgow", linestyle="--")
ax.set_title("Monthly rainfall")
ax.set_xlabel("Month")
ax.set_ylabel("Rainfall (mm)")
ax.legend()
fig.savefig(FIGURES / "two_lines.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 4: a scatter plot shows the relationship between two variables
rng = np.random.default_rng(42)
floor_area = rng.uniform(40, 150, size=60)
price = 2.5 * floor_area + rng.normal(0, 30, size=60)
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(floor_area, price, alpha=0.7)
ax.set_title("House price against floor area")
ax.set_xlabel("Floor area (m²)")
ax.set_ylabel("Price (£ thousands)")
fig.savefig(FIGURES / "scatter.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: inspecting a figure in code
fig, ax = plt.subplots()
line, = ax.plot(months, temperature, label="London")
ax.set_title("Check me")
print(ax.get_title(), len(ax.get_lines()), line.get_label())
print(line.get_ydata()[:3])
plt.close(fig)

print(sorted(path.name for path in FIGURES.glob("*.png")))
