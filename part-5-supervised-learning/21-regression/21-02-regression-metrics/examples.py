# 21-02 Regression metrics
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, root_mean_squared_error
from sklearn.model_selection import train_test_split

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=42)
model = LinearRegression().fit(X_train, y_train)
predictions = model.predict(X_test)

# Example 1: the four standard metrics
print(round(mean_absolute_error(y_test, predictions), 2))
print(round(mean_squared_error(y_test, predictions), 2))
print(round(root_mean_squared_error(y_test, predictions), 2))
print(round(r2_score(y_test, predictions), 3))

# Example 2: R squared by hand
ss_residual = np.sum((y_test - predictions) ** 2)
ss_total = np.sum((y_test - y_test.mean()) ** 2)
print(round(1 - ss_residual / ss_total, 3), round(model.score(X_test, y_test), 3))

# Example 3: the same metrics for a baseline
baseline = DummyRegressor().fit(X_train, y_train).predict(X_test)
for name, metric in [("MAE", mean_absolute_error), ("RMSE", root_mean_squared_error), ("R2", r2_score)]:
    print(f"{name:<5} model {metric(y_test, predictions):8.3f}   baseline {metric(y_test, baseline):8.3f}")

# Example 4: MAE versus RMSE when there is one large error
truth = np.array([100.0, 100.0, 100.0, 100.0])
even = np.array([110.0, 90.0, 110.0, 90.0])
one_big = np.array([100.0, 100.0, 100.0, 140.0])
for name, guess in [("even errors", even), ("one big error", one_big)]:
    print(f"{name:<14} MAE {mean_absolute_error(truth, guess):5.1f}  RMSE {root_mean_squared_error(truth, guess):5.1f}")

# Example 5: residual plots
residuals = y_test - predictions
fig, axes = plt.subplots(1, 2, figsize=(11, 4))
axes[0].scatter(predictions, y_test, s=15, alpha=0.6)
low, high = min(predictions.min(), y_test.min()), max(predictions.max(), y_test.max())
axes[0].plot([low, high], [low, high], "--", color="grey")
axes[0].set_xlabel("Predicted")
axes[0].set_ylabel("Actual")
axes[0].set_title("Predicted against actual")
axes[1].scatter(predictions, residuals, s=15, alpha=0.6)
axes[1].axhline(0, color="grey", linestyle="--")
axes[1].set_xlabel("Predicted")
axes[1].set_ylabel("Residual (actual - predicted)")
axes[1].set_title("Residuals against predictions")
fig.tight_layout()
fig.savefig(FIGURES / "residuals.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 6: a residual plot that shows a problem - a curved relationship
rng = np.random.default_rng(42)
x = rng.uniform(0, 10, 200).reshape(-1, 1)
y = 0.5 * x[:, 0] ** 2 + rng.normal(0, 2, 200)
curved = LinearRegression().fit(x, y)
curved_residuals = y - curved.predict(x)
print(round(r2_score(y, curved.predict(x)), 3))
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(curved.predict(x), curved_residuals, s=12, alpha=0.6)
ax.axhline(0, color="grey", linestyle="--")
ax.set_xlabel("Predicted")
ax.set_ylabel("Residual")
ax.set_title("A U-shaped pattern: a straight line is the wrong model")
fig.savefig(FIGURES / "residuals_curved.png", dpi=100, bbox_inches="tight")
plt.close(fig)
