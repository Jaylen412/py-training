# 13-05 Random numbers and linear algebra basics

## What you will learn

- Generate reproducible random numbers with `np.random.default_rng` and a seed.
- Sample, choose and shuffle, keeping features and labels in step.
- Compute dot products with `@`, and multiply a matrix by a vector.
- Transpose arrays and predict when matrix shapes fit together.

## Why it matters

Randomness runs through machine learning: splitting data into training and test sets, initialising models, and simulating data. Seeding it makes every result in this course reproducible, so your numbers match the lessons. The dot product and matrix multiplication are the core arithmetic of models: a linear model's predictions for a whole dataset are one matrix-vector product. Module 17 explains the ideas properly; this lesson introduces the tools.

## Concepts

### A seeded random generator

`np.random.default_rng(seed)` creates a **random number generator** (as with `random.Random` in 08-03, the seed fixes the sequence). Call its methods to draw numbers:

```python
rng = np.random.default_rng(42)
print(rng.random(3))
print(rng.integers(1, 7, size=5))
print(np.round(rng.normal(loc=170, scale=10, size=4), 1))
```

```
[0.77395605 0.43887844 0.85859792]
[1 5 2 1 4]
[171.3 166.8 169.8 161.5]
```

- `random(size)` gives floats from 0 up to (not including) 1.
- `integers(low, high, size)` gives whole numbers from `low` up to but **not including** `high`, so `integers(1, 7)` simulates a dice roll (unlike `random.randint` in 08-03, which includes the top).
- `normal(loc, scale, size)` draws from a bell-shaped **normal distribution** centred on `loc` with spread `scale` (Module 19). Here: heights around 170 cm.

The same seed always gives the same numbers:

```python
print(np.random.default_rng(42).random(3))
```

```
[0.77395605 0.43887844 0.85859792]
```

From here on, every lesson seeds its randomness with 42 so that your output matches.

### Choosing and shuffling

```python
rng = np.random.default_rng(42)
print(rng.choice(["red", "green", "blue"], size=4))
print(rng.permutation(5))
```

```
['red' 'blue' 'green' 'green']
[3 0 1 2 4]
```

`choice` picks items at random (with repeats unless you pass `replace=False`); `permutation(n)` gives the numbers 0 to n-1 in random order.

A common need is to shuffle the rows of a dataset **and** its labels in the same order, so they stay matched. Shuffle the **positions** once, then use fancy indexing (13-02) on both:

```python
features = np.array([[1, 10], [2, 20], [3, 30], [4, 40]])
labels = np.array(["a", "b", "c", "d"])
order = rng.permutation(len(labels))
print(features[order].tolist(), labels[order].tolist())
```

```
[[3, 30], [1, 10], [2, 20], [4, 40]] ['c', 'a', 'b', 'd']
```

Row `[3, 30]` still goes with label `"c"`. This is exactly what a train/test split does before cutting the data in two (Module 20).

### Sampling

Drawing many random numbers and averaging them shows how sample averages settle down as samples grow (Module 19 explores this):

```python
rng = np.random.default_rng(42)
for count in [10, 1_000, 100_000]:
    rolls = rng.integers(1, 7, size=count)
    print(count, round(rolls.mean(), 3))
```

```
10 3.1
1000 3.503
100000 3.5
```

The true average of a fair dice is 3.5. Ten rolls can be well off; a hundred thousand rolls land almost exactly on it.

### The dot product

The **dot product** of two equal-length vectors multiplies them element by element and adds up the results. (A **vector** here just means a 1-D array of numbers.) NumPy writes it as `np.dot(a, b)` or `a @ b`:

```python
weights = np.array([0.5, 2.0, -1.0])
house = np.array([120.0, 3.0, 10.0])
print(np.dot(weights, house))
print(weights @ house)
print((weights * house).sum())
```

```
56.0
56.0
56.0
```

In words: 0.5 × 120 + 2.0 × 3 + (−1.0) × 10 = 60 + 6 − 10 = 56. Read the house as (floor area, bedrooms, age) and the weights as how much each feature adds to the price: the dot product is a simple **linear model**'s prediction. Module 17 makes this precise.

### Matrix times vector

A **matrix** is a 2-D array. `matrix @ vector` computes the dot product of **each row** with the vector, giving one result per row. That is: one prediction per house, in a single operation.

```python
houses = np.array([
    [120.0, 3.0, 10.0],
    [80.0, 2.0, 30.0],
    [200.0, 5.0, 2.0],
])
print(houses.shape, weights.shape)
print(houses @ weights)
```

```
(3, 3) (3,)
[ 56.  14. 108.]
```

The number of **columns** of the matrix must equal the length of the vector.

### Transpose

The **transpose**, `.T`, swaps rows and columns: row i becomes column i.

```python
print(houses.T)
print(houses.shape, houses.T.shape)
```

```
[[120.  80. 200.]
 [  3.   2.   5.]
 [ 10.  30.   2.]]
(3, 3) (3, 3)
```

For a non-square array, the shape flips: a `(100, 3)` array becomes `(3, 100)`.

### Matrix times matrix

`A @ B` works when the number of **columns of A** equals the number of **rows of B**. The result has A's rows and B's columns: `(3, 2) @ (2, 3)` gives `(3, 3)`. Each entry is the dot product of a row of A with a column of B.

```python
first = np.array([[1, 2], [3, 4], [5, 6]])     # shape (3, 2)
second = np.array([[1, 0, 2], [0, 1, 3]])      # shape (2, 3)
print((first @ second).shape)
print(first @ second)
try:
    first @ first
except ValueError as error:
    print("ValueError:", str(error)[:60])
```

```
(3, 3)
[[ 1  2  8]
 [ 3  4 18]
 [ 5  6 28]]
ValueError: matmul: Input operand 1 has a mismatch in its core dimension
```

`(3, 2) @ (3, 2)` fails because the inner numbers, 2 and 3, differ. A quick shape check: write the two shapes side by side; the inner pair must match, and the outer pair gives the result.

## Common mistakes

- **Using the old global functions.** Older tutorials use `np.random.seed(42)` and `np.random.rand(...)`. They still work, but the generator style, `rng = np.random.default_rng(42)`, is the modern recommendation and is what scikit-learn's examples use.
- **Confusing `*` and `@`.** `a * b` multiplies element by element; `a @ b` is the dot product or matrix product.
- **Shuffling features and labels separately.** Two separate shuffles break the link between each row and its label. Shuffle positions once and index both.
- **Mismatched inner dimensions.** `(n, 3) @ (2,)` fails. Check that the matrix has as many columns as the vector has elements.

## Try it

Simulate 10,000 rounds of rolling two dice, using `rng.integers(1, 7, size=(10_000, 2))`, then `sum(axis=1)` to get each round's total. Which total appears most often? (Hint: `np.bincount(totals).argmax()`.)

## Exercises

Open `ex_13_05.py`:

1. `dice_rolls`: reproducible dice rolls from a seed.
2. `shuffle_together`: shuffle features and labels in the same order.
3. `predict_linear`: predictions `X @ weights + bias` for a whole dataset.
4. `can_multiply`: whether two shapes fit together for `@`.
5. `gram_matrix`: `X.T @ X`, used in Module 17.

Run the tests:

```
python -m pytest part-3-data-toolkit/13-numpy/13-05-random-numbers-and-linear-algebra
```

## Summary

- `rng = np.random.default_rng(42)` makes a seeded generator; use `rng.random`, `rng.integers`, `rng.normal`, `rng.choice` and `rng.permutation`.
- Shuffle positions once and index features and labels with them to keep rows matched.
- `a @ b` (or `np.dot`) is the dot product: multiply element by element, then sum.
- `matrix @ vector` gives one dot product per row: a whole dataset's linear predictions at once.
- `.T` transposes; `(a, b) @ (b, c)` gives `(a, c)`, and the inner sizes must match.
