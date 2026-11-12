# 20-02 The scikit-learn interface
import numpy as np
from sklearn.datasets import load_diabetes, load_iris
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier

# Example 1: a first model in ten lines
iris = load_iris()
X, y = iris.data, iris.target
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, y)
new_flowers = np.array([[5.0, 3.4, 1.5, 0.2], [6.7, 3.0, 5.2, 2.3]])
print(model.predict(new_flowers))
print(iris.target_names[model.predict(new_flowers)])

# Example 2: X is 2-D (samples, features); y is 1-D (one target per sample)
print(X.shape, y.shape, X.ndim, y.ndim)

# Example 3: one sample still needs to be a 2-D table
one_flower = np.array([5.0, 3.4, 1.5, 0.2])
print(model.predict(one_flower.reshape(1, -1)))

# Example 4: hyperparameters go in the constructor; get_params shows them
print(model.get_params()["n_neighbors"])
print(KNeighborsClassifier(n_neighbors=1).get_params()["n_neighbors"])

# Example 5: learned attributes end with an underscore
diabetes = load_diabetes()
regressor = LinearRegression().fit(diabetes.data, diabetes.target)
print(np.round(regressor.coef_, 1))
print(round(regressor.intercept_, 2))

# Example 6: score - accuracy for classifiers, R squared for regressors
print(round(model.score(X, y), 3))
print(round(regressor.score(diabetes.data, diabetes.target), 3))

# Example 7: predict_proba gives class probabilities
print(model.predict_proba(new_flowers))

# Example 8: every estimator works the same way
from sklearn.tree import DecisionTreeClassifier

for estimator in [KNeighborsClassifier(), DecisionTreeClassifier(random_state=42)]:
    estimator.fit(X, y)
    print(type(estimator).__name__, round(estimator.score(X, y), 3))
