# 21-01 Linear regression
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
pd.set_option("display.width", 120)

diabetes = load_diabetes(as_frame=True, scaled=False).frame
X_train, X_test, y_train, y_test = train_test_split(
    diabetes.drop(columns="target"), diabetes["target"], test_size=0.25, random_state=42
)

# Example 1: a line - one feature
line = LinearRegression().fit(X_train[["bmi"]], y_train)
print(round(line.coef_[0], 3), round(line.intercept_, 3))
print(np.round(line.predict(pd.DataFrame({"bmi": [20.0, 30.0]})), 1))

grid = pd.DataFrame({"bmi": np.linspace(18, 43, 100)})
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(X_train["bmi"], y_train, s=12, alpha=0.5, label="training data")
ax.plot(grid["bmi"], line.predict(grid), color="tab:red", label="fitted line")
ax.set_xlabel("BMI")
ax.set_ylabel("Disease progression after one year")
ax.set_title("Each extra point of BMI adds about 10 to progression")
ax.legend()
fig.savefig(FIGURES / "fitted_line.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: a plane - two features
plane = LinearRegression().fit(X_train[["bmi", "bp"]], y_train)
print(np.round(plane.coef_, 3), round(plane.intercept_, 3))

# Example 3: all ten features
model = LinearRegression().fit(X_train, y_train)
coefficients = pd.Series(model.coef_, index=X_train.columns).round(3)
print(coefficients)
print(round(model.intercept_, 2))

# Example 4: interpreting one coefficient
print(round(model.coef_[list(X_train.columns).index("bmi")], 3))

# Example 5: test-set scores for the three models
for name, fitted, columns in [("bmi only", line, ["bmi"]), ("bmi + bp", plane, ["bmi", "bp"]),
                              ("all ten", model, list(X_train.columns))]:
    print(f"{name:<9} R squared {fitted.score(X_test[columns], y_test):.3f}")

# Example 6: residuals - what the model got wrong
predictions = model.predict(X_test)
residuals = y_test - predictions
print(np.round(residuals[:5].to_numpy(), 1))
print(round(residuals.mean(), 2), round(residuals.std(), 2))
