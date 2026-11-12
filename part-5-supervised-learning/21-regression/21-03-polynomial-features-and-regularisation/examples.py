# 21-03 Polynomial features and regularisation
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)
pd.set_option("display.width", 120)

# Example 1: PolynomialFeatures adds powers (and products) of the features
x = np.array([[2.0], [3.0]])
print(PolynomialFeatures(degree=3, include_bias=False).fit_transform(x))
two = np.array([[2.0, 5.0]])
poly = PolynomialFeatures(degree=2, include_bias=False).fit(two)
print(poly.get_feature_names_out(["a", "b"]))
print(poly.transform(two))

# Example 2: a linear model on polynomial features fits a curve
rng = np.random.default_rng(42)
x = rng.uniform(0, 10, 200).reshape(-1, 1)
y = 0.5 * x[:, 0] ** 2 - 2 * x[:, 0] + rng.normal(0, 2, 200)
x_squared = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)
curve = LinearRegression().fit(x_squared, y)
print(np.round(curve.coef_, 3), round(curve.intercept_, 3), round(curve.score(x_squared, y), 3))

# Example 3: many polynomial features overfit
diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=42)
scaler = StandardScaler().fit(X_train)
X_train_s, X_test_s = scaler.transform(X_train), scaler.transform(X_test)
poly3 = PolynomialFeatures(degree=3, include_bias=False).fit(X_train_s)
P_train, P_test = poly3.transform(X_train_s), poly3.transform(X_test_s)
print(P_train.shape)
plain = LinearRegression().fit(P_train, y_train)
print("degree 3, no regularisation:", round(plain.score(P_train, y_train), 3), round(plain.score(P_test, y_test), 3))

# Example 4: Ridge shrinks the coefficients and rescues the model
for alpha in [0.1, 10, 100, 1000]:
    ridge = Ridge(alpha=alpha).fit(P_train, y_train)
    print(f"Ridge alpha {alpha:>6}: train {ridge.score(P_train, y_train):.3f}, test {ridge.score(P_test, y_test):.3f}, "
          f"largest coefficient {np.abs(ridge.coef_).max():8.1f}")

# Example 5: the effect of alpha on the coefficients of the original ten features
alphas = np.logspace(-2, 4, 40)
paths = np.array([Ridge(alpha=a).fit(X_train_s, y_train).coef_ for a in alphas])
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(alphas, paths)
ax.set_xscale("log")
ax.set_xlabel("alpha (regularisation strength)")
ax.set_ylabel("Coefficient")
ax.set_title("Ridge: larger alpha shrinks every coefficient towards zero")
fig.savefig(FIGURES / "ridge_paths.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 6: Lasso sets some coefficients exactly to zero
lasso = Lasso(alpha=1.0).fit(X_train_s, y_train)
print(pd.Series(lasso.coef_, index=diabetes.feature_names).round(2))
print("features kept:", int(np.sum(lasso.coef_ != 0)), "of", len(lasso.coef_))
print("test R squared:", round(lasso.score(X_test_s, y_test), 3))
for alpha in [0.1, 1, 5, 20]:
    kept = int(np.sum(Lasso(alpha=alpha).fit(X_train_s, y_train).coef_ != 0))
    print(f"Lasso alpha {alpha:>4}: {kept} features kept")
