# 18-03 Loss functions
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Data: hours studied and exam score
hours = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
scores = np.array([52.0, 55.0, 61.0, 64.0, 70.0, 72.0])

# Example 1: errors (residuals) of one candidate model
predictions = 50 + 4 * hours
errors = scores - predictions
print(predictions)
print(errors)

# Example 2: summing raw errors hides mistakes - they cancel out
print(errors.sum())

# Example 3: mean squared error and mean absolute error
mse = np.mean(errors ** 2)
mae = np.mean(np.abs(errors))
print(round(mse, 3), round(mae, 3), round(np.sqrt(mse), 3))

# Example 4: comparing two models with the loss
for intercept, slope in [(50, 4), (47, 4.3)]:
    candidate = intercept + slope * hours
    print(intercept, slope, round(np.mean((scores - candidate) ** 2), 3))

# Example 5: squared error punishes big mistakes much more
small_errors = np.array([2.0, 2.0, 2.0, 2.0])
one_big_error = np.array([0.0, 0.0, 0.0, 8.0])
for errs in [small_errors, one_big_error]:
    print(np.mean(np.abs(errs)), np.mean(errs ** 2))

# Example 6: loss as a function of one parameter (intercept fixed at 47)
slopes = np.linspace(2, 7, 101)
losses = np.array([np.mean((scores - (47 + s * hours)) ** 2) for s in slopes])
best = slopes[losses.argmin()]
print(round(best, 2), round(losses.min(), 3))

fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].scatter(hours, scores, color="black", zorder=3)
for s, style in [(3.0, ":"), (best, "-"), (6.0, "--")]:
    axes[0].plot(hours, 47 + s * hours, style, label=f"slope {s:.2f}")
axes[0].set_xlabel("Hours studied")
axes[0].set_ylabel("Exam score")
axes[0].legend()
axes[0].set_title("Three candidate lines")
axes[1].plot(slopes, losses)
axes[1].scatter([best], [losses.min()], color="tab:red", zorder=3)
axes[1].set_xlabel("Slope")
axes[1].set_ylabel("Mean squared error")
axes[1].set_title("Loss against slope: the best slope is at the bottom")
fig.tight_layout()
fig.savefig(FIGURES / "loss_curve.png", dpi=100, bbox_inches="tight")
plt.close(fig)
