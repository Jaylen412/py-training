# 14-01 Series and DataFrames
from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parents[3] / "data"
pd.set_option("display.width", 100)

# Example 1: a Series is a labelled 1-D array
temperatures = pd.Series([12.5, 15.0, 9.5], index=["Mon", "Tue", "Wed"], name="temp_c")
print(temperatures)
print(temperatures["Tue"], temperatures.mean())

# Example 2: a DataFrame is a table of columns that share an index
people = pd.DataFrame({
    "name": ["Ada", "Alan", "Grace"],
    "age": [36, 41, 85],
    "city": ["London", "Manchester", "New York"],
})
print(people)
print(people.shape)
print(people.columns.tolist())
print(people.index.tolist())

# Example 3: each column is a Series
print(type(people["age"]).__name__)
print(people["age"].max())

# Example 4: reading a CSV file
sales = pd.read_csv(DATA / "store_sales.csv")
print(sales.shape)
print(sales.head())

# Example 5: info - columns, non-missing counts and dtypes
sales.info()

# Example 6: describe - summary statistics of the numeric columns
print(sales.describe().round(2))

# Example 7: dtypes, and the last few rows
print(sales.dtypes)
print(sales.tail(3))
