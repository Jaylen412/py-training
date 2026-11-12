# 20-01 What machine learning is
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris(as_frame=True)
X = iris.data
y = iris.target


# Example 1: a hand-written rule
def rule_based(row):
    if row["petal length (cm)"] < 2.5:
        return 0          # setosa
    if row["petal width (cm)"] < 1.75:
        return 1          # versicolor
    return 2              # virginica


rule_predictions = X.apply(rule_based, axis=1)
print("hand-written rule accuracy:", round((rule_predictions == y).mean(), 3))

# Example 2: a model that learns its own rules from examples
model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X, y)
print("learned rule accuracy:", round(model.score(X, y), 3))

# Example 3: features, targets and samples
print(X.shape, y.shape)
print(X.columns.tolist())
print(iris.target_names.tolist())
print(X.iloc[0].tolist(), "->", int(y.iloc[0]))

# Example 4: regression (a number) versus classification (a category)
print(np.unique(y))
from sklearn.datasets import load_diabetes

diabetes = load_diabetes()
print(diabetes.target[:5])
