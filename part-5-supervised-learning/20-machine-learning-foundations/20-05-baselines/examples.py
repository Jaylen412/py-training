# 20-05 Baselines
import numpy as np
from sklearn.datasets import load_breast_cancer, load_diabetes, make_classification
from sklearn.dummy import DummyClassifier, DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Example 1: a majority-class baseline for classification
cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    cancer.data, cancer.target, test_size=0.25, random_state=42, stratify=cancer.target
)
baseline = DummyClassifier(strategy="most_frequent").fit(X_train, y_train)
print(baseline.predict(X_test[:5]))
print("baseline accuracy:", round(baseline.score(X_test, y_test), 3))

# Example 2: the real model must beat it
tree = DecisionTreeClassifier(max_depth=3, random_state=42).fit(X_train, y_train)
print("tree accuracy:", round(tree.score(X_test, y_test), 3))

# Example 3: with imbalanced classes, a useless model looks great
X, y = make_classification(n_samples=2000, weights=[0.95], flip_y=0, random_state=42)
print("fraction of class 1:", y.mean())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
print("majority baseline:", DummyClassifier(strategy="most_frequent").fit(X_train, y_train).score(X_test, y_test))

# Example 4: other classifier strategies
for strategy in ["most_frequent", "stratified", "uniform"]:
    dummy = DummyClassifier(strategy=strategy, random_state=42).fit(X_train, y_train)
    print(f"{strategy:<14}{dummy.score(X_test, y_test):.3f}")

# Example 5: a mean baseline for regression
diabetes = load_diabetes()
X_train, X_test, y_train, y_test = train_test_split(diabetes.data, diabetes.target, test_size=0.25, random_state=42)
mean_baseline = DummyRegressor(strategy="mean").fit(X_train, y_train)
print(round(mean_baseline.predict(X_test[:1])[0], 2), round(y_train.mean(), 2))
print("baseline R squared:", round(mean_baseline.score(X_test, y_test), 3))
regression = LinearRegression().fit(X_train, y_train)
print("linear regression R squared:", round(regression.score(X_test, y_test), 3))

# Example 6: baseline errors in the target's own units
baseline_error = np.mean(np.abs(mean_baseline.predict(X_test) - y_test))
model_error = np.mean(np.abs(regression.predict(X_test) - y_test))
print(f"mean absolute error: baseline {baseline_error:.1f}, model {model_error:.1f}")
print(f"improvement: {1 - model_error / baseline_error:.1%}")
