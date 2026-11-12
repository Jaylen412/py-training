# 22-01 Logistic regression
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer, load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)


# Example 1: the sigmoid squeezes any number into 0 to 1
def sigmoid(z):
    return 1 / (1 + np.exp(-z))


print(np.round(sigmoid(np.array([-5, -1, 0, 1, 5])), 3))
z = np.linspace(-8, 8, 200)
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot(z, sigmoid(z))
ax.axhline(0.5, color="grey", linestyle=":")
ax.axvline(0, color="grey", linestyle=":")
ax.set_xlabel("linear score z = X @ w + b")
ax.set_ylabel("probability")
ax.set_title("The sigmoid turns a score into a probability")
fig.savefig(FIGURES / "sigmoid.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 2: logistic regression on one feature
cancer = load_breast_cancer()
radius = cancer.data[:, [0]]       # mean radius
is_malignant = (cancer.target == 0).astype(int)
one_feature = LogisticRegression().fit(radius, is_malignant)
print(np.round(one_feature.coef_, 3), np.round(one_feature.intercept_, 3))
for r in [10, 15, 20]:
    print(r, np.round(one_feature.predict_proba([[r]])[0], 3), one_feature.predict([[r]])[0])

# Example 3: the decision boundary is where the probability is 0.5
boundary = -one_feature.intercept_[0] / one_feature.coef_[0, 0]
print("boundary radius:", round(boundary, 2))
grid = np.linspace(5, 30, 300).reshape(-1, 1)
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.scatter(radius, is_malignant + np.random.default_rng(42).normal(0, 0.03, len(radius)), s=8, alpha=0.4)
ax.plot(grid, one_feature.predict_proba(grid)[:, 1], color="tab:red", label="P(malignant)")
ax.axvline(boundary, color="grey", linestyle="--", label=f"boundary at {boundary:.1f}")
ax.set_xlabel("mean radius")
ax.set_ylabel("malignant (1) or benign (0)")
ax.legend()
ax.set_title("Logistic regression on one feature")
fig.savefig(FIGURES / "one_feature.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 4: all 30 features, scaled
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
scaler = StandardScaler().fit(X_train)
model = LogisticRegression(max_iter=1000).fit(scaler.transform(X_train), y_train)
print("test accuracy:", round(model.score(scaler.transform(X_test), y_test), 3))
print(np.round(model.predict_proba(scaler.transform(X_test[:3])), 3))
print(model.predict(scaler.transform(X_test[:3])), y_test[:3])

# Example 5: the regularisation strength C
for C in [0.001, 0.1, 1, 100]:
    fitted = LogisticRegression(C=C, max_iter=5000).fit(scaler.transform(X_train), y_train)
    print(f"C {C:>6}: test accuracy {fitted.score(scaler.transform(X_test), y_test):.3f}, "
          f"largest coefficient {np.abs(fitted.coef_).max():6.2f}")

# Example 6: more than two classes
iris = load_iris()
multi = LogisticRegression(max_iter=1000).fit(iris.data, iris.target)
print(multi.coef_.shape)
print(np.round(multi.predict_proba(iris.data[[0, 75, 149]]), 3))
print(multi.predict(iris.data[[0, 75, 149]]))
