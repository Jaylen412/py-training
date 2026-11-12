# 17-03 Matrices

## What you will learn

- Treat a dataset as a matrix with one row per sample and one column per feature.
- Multiply a matrix by a vector, and a matrix by a matrix, and predict the result's shape.
- Use the transpose and the identity matrix.
- Explain why the order of matrix multiplication matters.

## Why it matters

Every scikit-learn model expects its input as a matrix called `X`, with shape (number of samples, number of features). Training and prediction are built from matrix multiplications, which is why NumPy's `@` operator is at the heart of numerical machine learning. Knowing which shapes fit together lets you read model code, and fix the shape errors that are the most common bug in it.

## Concepts

### A dataset is a matrix

A **matrix** is a rectangular grid of numbers: a 2-D array. Its shape is (rows, columns), often written n × k. By convention in machine learning, each **row** is one **sample** (an example) and each **column** is one **feature**. The matrix is written with a capital letter, **X**.

```python
iris = load_iris()
X = iris.data
print(type(X).__name__, X.shape)
print(iris.feature_names)
print(X[:3])
```

```
ndarray (150, 4)
['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
[[5.1 3.5 1.4 0.2]
 [4.9 3.  1.4 0.2]
 [4.7 3.2 1.3 0.2]]
```

150 flowers, 4 measurements each. A row is a vector describing one flower (17-01); a column is one feature across all flowers:

```python
print(X[0], X[:, 2][:5])
```

```
[5.1 3.5 1.4 0.2] [1.4 1.4 1.3 1.5 1.4]
```

### Matrix times vector

Multiplying a matrix by a vector, `X @ w`, takes the dot product (17-02) of **each row** with the vector. The result has one number per row:

```python
weights = np.array([0.5, -0.2, 1.0, 0.3])
scores = X @ weights
print(scores.shape, np.round(scores[:3], 2))
print(round(X[0] @ weights, 2))
```

```
(150,) [3.31 3.31 3.07]
3.31
```

The first score is exactly the first row dotted with the weights. This one line computes a weighted score for all 150 flowers at once: it is how a linear model makes all its predictions (17-04).

### Matrix times matrix

When the second operand is a matrix, `X @ W`, each **column** of **W** is a separate set of weights, and the result has one column per set: entry (i, j) is row i of **X** dotted with column j of **W**.

```python
W = np.array([
    [0.5, 0.0],
    [-0.2, 0.0],
    [1.0, 0.5],
    [0.3, 0.5],
])
outputs = X @ W
print(W.shape, outputs.shape)
print(np.round(outputs[:3], 2))
```

```
(4, 2) (150, 2)
[[3.31 0.8 ]
 [3.31 0.8 ]
 [3.07 0.75]]
```

The first output column is the same score as before; the second is the average of the two petal measurements. One multiplication computed two different combinations of features for every flower. A layer of a neural network is exactly this: `X @ W`, one column of weights per output.

### Shapes that fit

For `A @ B` to work, the number of **columns of A** must equal the number of **rows of B**. The result has the rows of A and the columns of B:

**(n × k) @ (k × m) gives (n × m)**

In words: the inner numbers must match, and the outer numbers give the result.

```python
for left, right in [((150, 4), (4, 2)), ((150, 4), (2, 4)), ((3, 2), (2, 3))]:
    fits = left[1] == right[0]
    result = (left[0], right[1]) if fits else "no"
    print(left, "@", right, "->", result)
```

```
(150, 4) @ (4, 2) -> (150, 2)
(150, 4) @ (2, 4) -> no
(3, 2) @ (2, 3) -> (3, 3)
```

When you get a shape error, write the two shapes side by side and check the inner pair.

### Transpose

The **transpose** of a matrix, written **X**ᵀ and `X.T` in NumPy, swaps rows and columns: row i becomes column i, and an n × k matrix becomes k × n.

```python
small = np.array([[1, 2, 3], [4, 5, 6]])
print(small.T)
print(small.shape, small.T.shape)
```

```
[[1 4]
 [2 5]
 [3 6]]
(2, 3) (3, 2)
```

A very common combination is **X**ᵀ**X**. Its shape is (k × n) @ (n × k) = k × k: one row and column per feature, where entry (i, j) is the dot product of feature column i with feature column j.

```python
gram = X.T @ X
print(gram.shape)
print(np.round(gram, 1))
```

```
(4, 4)
[[5223.8 2673.4 3483.8 1128.1]
 [2673.4 1430.4 1674.3  531.9]
 [3483.8 1674.3 2582.7  869.1]
 [1128.1  531.9  869.1  302.3]]
```

It is **symmetric** (equal to its own transpose), because column i dotted with column j is the same as column j dotted with column i. It appears in the formula for linear regression's best weights, and, after centring the columns, it is closely related to the covariance matrix used by PCA (Modules 19 and 26).

### Order matters

For ordinary numbers 2 × 3 = 3 × 2. For matrices, **A**@**B** and **B**@**A** are usually different, even when both exist:

```python
A = np.array([[1, 2], [0, 1]])
B = np.array([[0, 1], [1, 0]])
print(A @ B)
print(B @ A)
```

```
[[2 1]
 [1 0]]
[[0 1]
 [1 2]]
```

### The identity matrix

The **identity matrix**, **I**, has 1s on the diagonal (top-left to bottom-right) and 0s elsewhere. It is the matrix version of the number 1: multiplying by it changes nothing.

```python
identity = np.eye(3)
v = np.array([7.0, -1.0, 2.0])
print(identity)
print(identity @ v)
```

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[ 7. -1.  2.]
```

The identity matters for the matrix **inverse** in 17-04.

## Common mistakes

- **Features in rows instead of columns.** If your data has shape (4, 150), scikit-learn will think you have 4 samples with 150 features. Transpose it.
- **Mismatched inner dimensions.** `(150, 4) @ (2, 4)` fails. Check the shapes; often a transpose fixes it: `(150, 4) @ (2, 4).T`.
- **Assuming `A @ B == B @ A`.** Matrix multiplication is not commutative; the order is part of the meaning.
- **Using `*` for matrix multiplication.** `X * W` multiplies element by element and broadcasts, which may silently give a wrong result of a different shape.

## Try it

Make a 4 × 3 matrix **W** whose three columns average the sepal measurements, average the petal measurements, and compute petal length minus sepal length. Compute `X @ W` and check the first row by hand.

## Exercises

Open `ex_17_03.py`:

1. `result_shape`: the shape of `A @ B`, or `None` if it is not defined.
2. `weighted_scores`: one weighted score per row.
3. `column_means_by_matmul`: the mean of each column, computed with a matrix product.
4. `gram_matrix`: **X**ᵀ**X**.
5. `is_symmetric`: whether a matrix equals its transpose.

Run the tests:

```
python -m pytest part-4-maths-for-ml/17-linear-algebra/17-03-matrices
```

## Summary

- A dataset is a matrix **X** of shape (samples, features): rows are samples, columns are features.
- `X @ w` gives one dot product per row; `X @ W` gives one column per column of **W**.
- (n × k) @ (k × m) gives (n × m): inner sizes must match.
- `X.T` swaps rows and columns; **X**ᵀ**X** is a symmetric k × k matrix of column dot products.
- Matrix multiplication is not commutative; the identity matrix `np.eye(n)` leaves vectors unchanged.
