# 13-03 Vectorised operations and broadcasting
import timeit

import numpy as np

# Example 1: element-wise arithmetic between arrays of the same shape
first = np.array([1, 2, 3, 4])
second = np.array([10, 20, 30, 40])
print(first + second)
print(second - first)
print(first * second)
print(second / first)
print(first ** 2)

# Example 2: comparisons are element-wise too
print(first > 2)
print(first == second / 10)

# Example 3: universal functions (ufuncs)
values = np.array([1.0, 4.0, 9.0, 16.0])
print(np.sqrt(values))
print(np.log(values))
print(np.round(np.exp([0, 1, 2]), 3))
print(np.abs(np.array([-3, 0, 2])))
print(np.maximum(np.array([1, 5, 2]), np.array([3, 3, 3])))

# Example 4: broadcasting a single number
celsius = np.array([0, 15, 30, 100])
print(celsius * 9 / 5 + 32)

# Example 5: broadcasting a row across every row of a table
prices = np.array([
    [10.0, 20.0, 30.0],
    [12.0, 18.0, 33.0],
])
tax_rates = np.array([0.2, 0.05, 0.0])     # one rate per column
print(prices.shape, tax_rates.shape)
print(prices * (1 + tax_rates))

# Example 6: broadcasting a column needs shape (rows, 1)
discounts = np.array([[0.1], [0.5]])       # one discount per row
print(discounts.shape)
print(prices * (1 - discounts))

# Example 7: incompatible shapes raise an error
try:
    prices + np.array([1, 2])
except ValueError as error:
    print("ValueError:", error)

# Example 8: replacing a loop - standardise every column at once
data = np.array([
    [150.0, 50.0],
    [160.0, 60.0],
    [170.0, 65.0],
    [180.0, 85.0],
])
column_means = data.mean(axis=0)
column_stds = data.std(axis=0)
standardised = (data - column_means) / column_stds
print(np.round(standardised, 3))

# Example 9: how much faster than a Python loop?
rng = np.random.default_rng(42)
big = rng.random(1_000_000)
as_list = big.tolist()
loop_time = timeit.timeit(lambda: [value * 2 + 1 for value in as_list], number=5) / 5
numpy_time = timeit.timeit(lambda: big * 2 + 1, number=5) / 5
print(f"list comprehension: {loop_time * 1000:.1f} ms, NumPy: {numpy_time * 1000:.2f} ms")
print(f"NumPy was about {loop_time / numpy_time:.0f}x faster")
