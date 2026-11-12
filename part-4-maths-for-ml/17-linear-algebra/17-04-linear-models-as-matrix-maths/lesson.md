# 17-04 Linear models as matrix maths

## What you will learn

- Write a linear model's predictions for a whole dataset as **X** @ **w** + b.
- Fold the bias into the weights by adding a column of ones.
- Explain the identity and the inverse of a matrix, and when an inverse does not exist.
- Solve a system of equations with `np.linalg.solve`, and fit noisy data with least squares.

## Why it matters

Linear regression (Module 21) is the foundation of supervised learning, and it is pure matrix maths: predictions are a matrix-vector product, and the best weights come from solving a system of equations. In the Part 4 project you will find those weights in two ways, by gradient descent and by the least-squares solution introduced here, and check that they agree.

## Concepts

### A linear model

A **linear model** predicts a number as a weighted sum of the features plus a constant. For a house with features (floor area, bedrooms, age), a model might say: price = 2 × area + 10 × bedrooms − 0.5 × age + 50 (in thousands). The numbers 2, 10 and −0.5 are the **weights**, one per feature; 50 is the **bias** (or **intercept**), the starting value before any feature is counted.

For one house, the weighted sum is a dot product:

```python
weights = np.array([2.0, 10.0, -0.5])   # per m², per bedroom, per year of age
bias = 50.0                             # starting price
house = np.array([120.0, 3.0, 15.0])
print(house @ weights + bias)
```

```
312.5
```

That is 240 + 30 − 7.5 + 50 = 312.5.

### Predictions for a whole dataset

Stack the houses as rows of a matrix **X**, and the same expression predicts every house at once (17-03): **ŷ** = **X** @ **w** + b. In words: each row dotted with the weights, plus the bias. (**ŷ**, "y-hat", is the usual name for predictions; **y** is the true values.)

```python
X = np.array([
    [120.0, 3.0, 15.0],
    [80.0, 2.0, 40.0],
    [200.0, 5.0, 2.0],
    [95.0, 2.0, 10.0],
])
predictions = X @ weights + bias
print(predictions)
```

```
[312.5 210.  499.  255. ]
```

The bias is broadcast (13-03) to every row.

### The column of ones

A neat trick removes the separate bias: add a column of 1s to the front of **X**, and put the bias at the front of the weights. The first column times the bias is just the bias, so the result is the same:

```python
X_with_ones = np.column_stack([np.ones(len(X)), X])
weights_with_bias = np.concatenate([[bias], weights])
print(X_with_ones[:2])
print(X_with_ones @ weights_with_bias)
```

```
[[  1. 120.   3.  15.]
 [  1.  80.   2.  40.]]
[312.5 210.  499.  255. ]
```

`np.column_stack` joins 1-D arrays as columns; `np.concatenate` joins arrays end to end. Now the whole model is one matrix-vector product, **X** @ **w**, which makes the maths that follows simpler.

### The inverse

For a number, the **inverse** of 2 is ½, because 2 × ½ = 1. For a square matrix **A**, the inverse **A**⁻¹ is the matrix that gives the identity: **A** @ **A**⁻¹ = **I** (17-03). `np.linalg.inv` computes it:

```python
A = np.array([[2.0, 1.0], [1.0, 3.0]])
A_inverse = np.linalg.inv(A)
print(np.round(A_inverse, 3))
print(np.round(A @ A_inverse, 10) + 0.0)  # + 0.0 turns -0.0 into 0.0
```

```
[[ 0.6 -0.2]
 [-0.2  0.4]]
[[1. 0.]
 [0. 1.]]
```

(Rounding hides tiny float errors such as 1e-17; adding 0.0 tidies a −0.0 that rounding can leave.)

### Solving a system of equations

A **system of linear equations** is several equations that must all be true at once:

- 2x + 1y = 5
- 1x + 3y = 10

Written with matrices, this is **A** @ **v** = **b**, where **A** holds the coefficients, **v** = (x, y) the unknowns, and **b** the right-hand sides. In principle **v** = **A**⁻¹ @ **b**. In practice, use **`np.linalg.solve`**, which finds the solution directly and more accurately than computing the inverse:

```python
b = np.array([5.0, 10.0])
solution = np.linalg.solve(A, b)
print(solution)
print(A @ solution)
```

```
[1. 3.]
[ 5. 10.]
```

x = 1 and y = 3; multiplying back gives the right-hand sides, which confirms it.

### When there is no inverse

Some matrices have no inverse. Here the second row is exactly twice the first, so the two equations say the same thing and cannot pin down two unknowns. Such a matrix is called **singular**, and its **determinant** (a number computed from a square matrix that is zero exactly when it has no inverse) is 0:

```python
singular = np.array([[1.0, 2.0], [2.0, 4.0]])
print(np.linalg.det(singular))
try:
    np.linalg.inv(singular)
except np.linalg.LinAlgError as error:
    print("LinAlgError:", error)
```

```
0.0
LinAlgError: Singular matrix
```

In data, this happens when one feature is an exact combination of others, for example floor area recorded in both m² and ft². The model then cannot decide how to share the weight between them.

### Finding weights from data

Here is the key idea. If we know the prices of four houses, then **X** @ **w** = **y** is a system of four equations with four unknown weights (bias, area, bedrooms, age), and we can solve it:

```python
true_weights = np.array([30.0, 2.0, 10.0, -0.5])  # bias, area, bedrooms, age
four_houses = np.column_stack([np.ones(4), X])
prices = four_houses @ true_weights
print(prices)
print(np.linalg.solve(four_houses, prices))
```

```
[292.5 190.  479.  235. ]
[30.   2.  10.  -0.5]
```

We recovered the weights exactly from the data.

### Least squares

Real data has two complications: there are many more samples than weights, and prices are **noisy** (no weights fit every house exactly). The system has no exact solution. Instead, we look for the weights that make the predictions as close as possible to the true values, by making the sum of squared errors as small as it can be. This is called **least squares**, and `np.linalg.lstsq` solves it:

```python
rng = np.random.default_rng(42)
areas = rng.uniform(50, 200, size=100)
bedrooms = rng.integers(1, 6, size=100)
ages = rng.uniform(0, 80, size=100)
features = np.column_stack([np.ones(100), areas, bedrooms, ages])
noisy_prices = features @ true_weights + rng.normal(0, 15, size=100)
fitted, *_ = np.linalg.lstsq(features, noisy_prices, rcond=None)
print(np.round(fitted, 2))
```

```
[34.94  1.96 11.35 -0.56]
```

From 100 noisy houses, least squares estimated weights close to the true (30, 2, 10, −0.5), without ever seeing them. That is linear regression. `lstsq` returns several things; `fitted, *_ =` keeps the first (the weights) and ignores the rest. `rcond=None` just selects the modern default behaviour.

In Module 18 you will find the same weights in a completely different way, by gradient descent, and in Module 21 you will let scikit-learn do it.

## Common mistakes

- **Forgetting the column of ones.** Without it, the model is forced through zero (no bias), and the other weights twist to compensate.
- **Computing the inverse to solve a system.** `np.linalg.inv(A) @ b` works but is slower and less accurate than `np.linalg.solve(A, b)`.
- **Solving with a singular matrix.** Duplicate or perfectly related features give `LinAlgError: Singular matrix`. Remove the redundant feature, or use `lstsq`, which copes.
- **Calling `solve` with more rows than columns.** `np.linalg.solve` needs a square matrix; with more samples than unknowns use `np.linalg.lstsq`.

## Try it

Rerun Example 8 with 10 houses instead of 100, then with 1,000. How do the fitted weights change? Then increase the noise from 15 to 100. More data and less noise both give better estimates.

## Exercises

Open `ex_17_04.py`:

1. `predict`: predictions **X** @ **w** + b.
2. `add_bias_column`: put a column of ones in front of **X**.
3. `solve_system`: solve a square system of equations.
4. `fit_least_squares`: the bias and weights that best fit noisy data.

Run the tests:

```
python -m pytest part-4-maths-for-ml/17-linear-algebra/17-04-linear-models-as-matrix-maths
```

## Summary

- A linear model predicts **ŷ** = **X** @ **w** + b: one weight per feature plus a bias.
- A column of ones in **X** absorbs the bias into the weights.
- **A** @ **A**⁻¹ = **I**; singular matrices (determinant 0) have no inverse.
- `np.linalg.solve(A, b)` solves square systems; `np.linalg.lstsq(X, y)` finds the least-squares weights when there are more samples than unknowns.
- Least squares on noisy data recovers weights close to the true ones: that is linear regression.
