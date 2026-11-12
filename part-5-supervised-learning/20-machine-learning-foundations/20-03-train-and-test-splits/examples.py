# 20-03 Train and test splits
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

data = load_breast_cancer()
X, y = data.data, data.target

# Example 1: scoring a model on its own training data is misleading
tree = DecisionTreeClassifier(random_state=42).fit(X, y)
print("accuracy on training data:", tree.score(X, y))

# Example 2: hold out a test set the model never sees during training
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
print(X_train.shape, X_test.shape)
tree = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
print("train:", round(tree.score(X_train, y_train), 3), "test:", round(tree.score(X_test, y_test), 3))

# Example 3: random_state makes the split repeatable
again = train_test_split(X, y, test_size=0.25, random_state=42)
print(np.array_equal(X_test, again[1]))
for seed in [0, 1, 2]:
    parts = train_test_split(X, y, test_size=0.25, random_state=seed)
    model = DecisionTreeClassifier(random_state=42).fit(parts[0], parts[2])
    print(f"split seed {seed}: test accuracy {model.score(parts[1], parts[3]):.3f}")

# Example 4: stratify keeps the class balance the same in both parts
print("whole dataset:", round(y.mean(), 3))
_, _, plain_train, plain_test = train_test_split(X, y, test_size=0.1, random_state=3)
print("plain split:  ", round(plain_train.mean(), 3), round(plain_test.mean(), 3))
_, _, strat_train, strat_test = train_test_split(X, y, test_size=0.1, random_state=3, stratify=y)
print("stratified:   ", round(strat_train.mean(), 3), round(strat_test.mean(), 3))

# Example 5: data leakage - scaling with statistics from the whole dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)
leaky_scaler = StandardScaler().fit(X)                  # wrong: has seen the test rows
proper_scaler = StandardScaler().fit(X_train)           # right: training rows only
print(np.round(leaky_scaler.mean_[:3], 3))
print(np.round(proper_scaler.mean_[:3], 3))
knn = KNeighborsClassifier().fit(proper_scaler.transform(X_train), y_train)
print("test accuracy:", round(knn.score(proper_scaler.transform(X_test), y_test), 3))

# Example 6: a blatant leak - a feature that is really the answer
leaky_X = np.column_stack([X, y])
leaky_train, leaky_test, ly_train, ly_test = train_test_split(leaky_X, y, test_size=0.25, random_state=42)
leaky_model = DecisionTreeClassifier(random_state=42).fit(leaky_train, ly_train)
print("with a leaked feature:", leaky_model.score(leaky_test, ly_test))
