# 05-05 Nested data and references
# `import copy` loads Python's built-in copy tools (imports are covered in Module 08).
import copy

# Example 1: a list of dictionaries - one dictionary per record
products = [
    {"name": "Pen", "price": 1.50, "quantity": 10},
    {"name": "Notebook", "price": 3.25, "quantity": 4},
    {"name": "Stapler", "price": 7.00, "quantity": 1},
]
print(products[1]["name"])
stock_value = 0
for product in products:
    stock_value += product["price"] * product["quantity"]
print("Stock value:", stock_value)

# Example 2: a dictionary of lists - grouping
people = [("Ada", "London"), ("Alan", "Manchester"), ("Grace", "London")]
by_city = {}
for name, city in people:
    if city not in by_city:
        by_city[city] = []
    by_city[city].append(name)
print(by_city)
print(by_city["London"][1])

# Example 3: a list of lists - a grid
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grid[1][2])
for row in grid:
    print(sum(row))

# Example 4: assignment does NOT copy - both names refer to one list
original = [1, 2, 3]
alias = original
alias.append(4)
print(original)
print(alias is original)

# Example 5: functions receive references too
def add_bonus(scores):
    scores.append(100)


my_scores = [70, 80]
add_bonus(my_scores)
print(my_scores)

# Example 6: a shallow copy is a new outer list
numbers = [1, 2, 3]
copied = numbers.copy()
copied.append(4)
print(numbers, copied)
print(numbers[:] == numbers, numbers[:] is numbers)

# Example 7: ...but a shallow copy shares the inner lists
grid_copy = grid.copy()
grid_copy[0][0] = 99
print(grid)

# Example 8: a deep copy copies everything, all the way down
grid = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(grid)
deep[0][0] = 99
print(grid)
print(deep)

# Example 9: == compares values, `is` checks for the same object
first = [1, 2]
second = [1, 2]
print(first == second, first is second)
