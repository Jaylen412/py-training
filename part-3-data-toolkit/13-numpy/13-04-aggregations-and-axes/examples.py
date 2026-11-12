# 13-04 Aggregations and axes
import numpy as np

# Example 1: aggregations over the whole array
sales = np.array([
    [120, 95, 140],    # week 1: shop A, shop B, shop C
    [130, 80, 150],    # week 2
    [110, 105, 160],   # week 3
    [125, 90, 155],    # week 4
])
print(sales.sum(), sales.mean(), sales.min(), sales.max())
print(round(sales.std(), 2))

# Example 2: axis=0 collapses the rows -> one result per column
print(sales.sum(axis=0))
print(sales.mean(axis=0))

# Example 3: axis=1 collapses the columns -> one result per row
print(sales.sum(axis=1))
print(sales.max(axis=1))

# Example 4: argmax and argmin give positions, not values
print(sales.sum(axis=0).argmax())
print(sales.argmax(axis=1))
flat_position = sales.argmax()
row, column = np.unravel_index(flat_position, sales.shape)
print(flat_position, int(row), int(column))

# Example 5: keepdims keeps the axis so the result broadcasts back
row_totals = sales.sum(axis=1, keepdims=True)
print(row_totals.shape)
print(np.round(sales / row_totals, 3))

# Example 6: cumulative sums and counting with booleans
print(sales[:, 0].cumsum())
print((sales > 100).sum(axis=0))
print((sales > 100).all(axis=1))
print((sales > 150).any())

# Example 7: reshape
numbers = np.arange(12)
print(numbers.reshape(3, 4))
print(numbers.reshape(2, -1).shape)
print(sales.reshape(-1))
print(sales.ravel()[:3])

# Example 8: NaN means "not a number" - and spoils ordinary aggregations
readings = np.array([3.0, np.nan, 5.0])
print(readings.mean(), np.nanmean(readings))
