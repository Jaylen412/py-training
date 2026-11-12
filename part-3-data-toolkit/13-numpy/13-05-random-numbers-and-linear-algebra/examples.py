# 13-05 Random numbers and linear algebra basics
import numpy as np

# Example 1: a seeded random generator
rng = np.random.default_rng(42)
print(rng.random(3))
print(rng.integers(1, 7, size=5))
print(np.round(rng.normal(loc=170, scale=10, size=4), 1))

# Example 2: the same seed gives the same numbers
print(np.random.default_rng(42).random(3))

# Example 3: choice, permutation and shuffling rows together
rng = np.random.default_rng(42)
print(rng.choice(["red", "green", "blue"], size=4))
print(rng.permutation(5))
features = np.array([[1, 10], [2, 20], [3, 30], [4, 40]])
labels = np.array(["a", "b", "c", "d"])
order = rng.permutation(len(labels))
print(features[order].tolist(), labels[order].tolist())

# Example 4: sampling - the average of many dice rolls approaches 3.5
rng = np.random.default_rng(42)
for count in [10, 1_000, 100_000]:
    rolls = rng.integers(1, 7, size=count)
    print(count, round(rolls.mean(), 3))

# Example 5: the dot product
weights = np.array([0.5, 2.0, -1.0])
house = np.array([120.0, 3.0, 10.0])
print(np.dot(weights, house))
print(weights @ house)
print((weights * house).sum())

# Example 6: matrix @ vector - one dot product per row
houses = np.array([
    [120.0, 3.0, 10.0],
    [80.0, 2.0, 30.0],
    [200.0, 5.0, 2.0],
])
print(houses.shape, weights.shape)
print(houses @ weights)

# Example 7: transpose swaps rows and columns
print(houses.T)
print(houses.shape, houses.T.shape)

# Example 8: matrix @ matrix - shapes must line up
first = np.array([[1, 2], [3, 4], [5, 6]])     # shape (3, 2)
second = np.array([[1, 0, 2], [0, 1, 3]])      # shape (2, 3)
print((first @ second).shape)
print(first @ second)
try:
    first @ first
except ValueError as error:
    print("ValueError:", str(error)[:60])
