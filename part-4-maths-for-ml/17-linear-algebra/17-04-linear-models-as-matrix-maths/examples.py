# 17-04 Linear models as matrix maths
import numpy as np

# Example 1: a linear model's prediction for one house
weights = np.array([2.0, 10.0, -0.5])   # per m², per bedroom, per year of age
bias = 50.0                             # starting price
house = np.array([120.0, 3.0, 15.0])
print(house @ weights + bias)

# Example 2: predictions for a whole dataset in one line: X @ w + b
X = np.array([
    [120.0, 3.0, 15.0],
    [80.0, 2.0, 40.0],
    [200.0, 5.0, 2.0],
    [95.0, 2.0, 10.0],
])
predictions = X @ weights + bias
print(predictions)

# Example 3: folding the bias into the weights with a column of ones
X_with_ones = np.column_stack([np.ones(len(X)), X])
weights_with_bias = np.concatenate([[bias], weights])
print(X_with_ones[:2])
print(X_with_ones @ weights_with_bias)

# Example 4: the identity matrix and the inverse
A = np.array([[2.0, 1.0], [1.0, 3.0]])
A_inverse = np.linalg.inv(A)
print(np.round(A_inverse, 3))
print(np.round(A @ A_inverse, 10) + 0.0)  # + 0.0 turns -0.0 into 0.0

# Example 5: solving a system of equations
# 2x + 1y = 5
# 1x + 3y = 10
b = np.array([5.0, 10.0])
solution = np.linalg.solve(A, b)
print(solution)
print(A @ solution)

# Example 6: some matrices have no inverse
singular = np.array([[1.0, 2.0], [2.0, 4.0]])
print(np.linalg.det(singular))
try:
    np.linalg.inv(singular)
except np.linalg.LinAlgError as error:
    print("LinAlgError:", error)

# Example 7: finding weights from data - exactly as many houses as unknowns
true_weights = np.array([30.0, 2.0, 10.0, -0.5])  # bias, area, bedrooms, age
four_houses = np.column_stack([np.ones(4), X])
prices = four_houses @ true_weights
print(prices)
print(np.linalg.solve(four_houses, prices))

# Example 8: real data has noise and more rows than unknowns - least squares
rng = np.random.default_rng(42)
areas = rng.uniform(50, 200, size=100)
bedrooms = rng.integers(1, 6, size=100)
ages = rng.uniform(0, 80, size=100)
features = np.column_stack([np.ones(100), areas, bedrooms, ages])
noisy_prices = features @ true_weights + rng.normal(0, 15, size=100)
fitted, *_ = np.linalg.lstsq(features, noisy_prices, rcond=None)
print(np.round(fitted, 2))
