# 17-03 Matrices
import numpy as np
from sklearn.datasets import load_iris

# Example 1: a dataset is a matrix - rows are samples, columns are features
iris = load_iris()
X = iris.data
print(type(X).__name__, X.shape)
print(iris.feature_names)
print(X[:3])

# Example 2: one row is one sample (a vector of features); one column is one feature
print(X[0], X[:, 2][:5])

# Example 3: matrix @ vector - one dot product per row
weights = np.array([0.5, -0.2, 1.0, 0.3])
scores = X @ weights
print(scores.shape, np.round(scores[:3], 2))
print(round(X[0] @ weights, 2))

# Example 4: matrix @ matrix - each column of the second matrix gives one output column
W = np.array([
    [0.5, 0.0],
    [-0.2, 0.0],
    [1.0, 0.5],
    [0.3, 0.5],
])
outputs = X @ W
print(W.shape, outputs.shape)
print(np.round(outputs[:3], 2))

# Example 5: shapes that fit - (n, k) @ (k, m) gives (n, m)
for left, right in [((150, 4), (4, 2)), ((150, 4), (2, 4)), ((3, 2), (2, 3))]:
    fits = left[1] == right[0]
    result = (left[0], right[1]) if fits else "no"
    print(left, "@", right, "->", result)

# Example 6: transpose swaps rows and columns
small = np.array([[1, 2, 3], [4, 5, 6]])
print(small.T)
print(small.shape, small.T.shape)

# Example 7: X.T @ X - every column dotted with every column
gram = X.T @ X
print(gram.shape)
print(np.round(gram, 1))

# Example 8: matrix multiplication is not commutative
A = np.array([[1, 2], [0, 1]])
B = np.array([[0, 1], [1, 0]])
print(A @ B)
print(B @ A)

# Example 9: the identity matrix leaves vectors unchanged
identity = np.eye(3)
v = np.array([7.0, -1.0, 2.0])
print(identity)
print(identity @ v)
