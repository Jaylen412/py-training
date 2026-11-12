# 05-05 Nested data and references

## What you will learn

- Represent records as lists of dictionaries, and groups as dictionaries of lists.
- Read values from nested structures by chaining indexes and keys.
- Explain why assigning a list to a new name does not copy it.
- Choose between a shallow copy and a deep copy.

## Why it matters

Real data is nested: a list of customers, each with a list of orders. JSON files from web services look exactly like this, and a list of dictionaries is the most common way to hand data to pandas. Understanding references prevents one of the most confusing bugs in Python: changing a list "over here" and finding it has also changed "over there".

## Concepts

### Lists of dictionaries

A **list of dictionaries** is the standard way to hold a table of records in plain Python. Each dictionary is one row; its keys are the column names.

```python
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
```

```
Notebook
Stock value: 35.0
```

Read `products[1]["name"]` from left to right: item 1 of the list (the notebook dictionary), then its `"name"` value.

### Dictionaries of lists

A **dictionary of lists** groups items under a key. To build one, create an empty list the first time you see a key, then append to it:

```python
people = [("Ada", "London"), ("Alan", "Manchester"), ("Grace", "London")]
by_city = {}
for name, city in people:
    if city not in by_city:
        by_city[city] = []
    by_city[city].append(name)
print(by_city)
print(by_city["London"][1])
```

```
{'London': ['Ada', 'Grace'], 'Manchester': ['Alan']}
Grace
```

This is the grouping pattern. pandas does the same thing with `groupby` in Module 14.

### Lists of lists

A **list of lists** represents a grid or table of numbers. `grid[row][column]` picks out one value:

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
print(grid[1][2])
for row in grid:
    print(sum(row))
```

```
6
6
15
```

This is how a dataset looks before NumPy: rows are samples, columns are features.

### Names are references

Here is the key idea of this lesson. A variable does not hold a value inside it; it **refers to** a value stored elsewhere. Assignment `alias = original` does **not** copy the list. It makes a second name refer to the **same** list. Changing the list through one name is visible through the other:

```python
original = [1, 2, 3]
alias = original
alias.append(4)
print(original)
print(alias is original)
```

```
[1, 2, 3, 4]
True
```

Two names that refer to the same object are called **aliases**. The `is` operator checks whether two names refer to the very same object.

This never surprised you with numbers or strings because they are immutable: there is no way to change them in place, only to make a name refer to a new value. With mutable objects such as lists and dictionaries, aliasing matters.

### Functions get references too

Passing a list to a function passes a reference. If the function changes the list in place, the caller sees the change:

```python
def add_bonus(scores):
    scores.append(100)


my_scores = [70, 80]
add_bonus(my_scores)
print(my_scores)
```

```
[70, 80, 100]
```

Sometimes that is what you want, but it is easy to do by accident. Unless a function's job is clearly to modify its argument, build and return a new list instead.

### Shallow copies

To get an independent list, make a **copy**. `my_list.copy()` and the slice `my_list[:]` both create a new outer list:

```python
numbers = [1, 2, 3]
copied = numbers.copy()
copied.append(4)
print(numbers, copied)
print(numbers[:] == numbers, numbers[:] is numbers)
```

```
[1, 2, 3] [1, 2, 3, 4]
True False
```

`==` compares **values** (same items), while `is` checks **identity** (same object). A copy is equal but not identical.

This is called a **shallow copy**: only the outer list is new. If the items are themselves lists or dictionaries, the copy still shares them:

```python
grid_copy = grid.copy()
grid_copy[0][0] = 99
print(grid)
```

```
[[99, 2, 3], [4, 5, 6]]
```

`grid_copy` is a new list, but its two items are the same inner lists as `grid`'s, so changing `grid_copy[0][0]` changed `grid` too.

### Deep copies

A **deep copy** copies everything, all the way down. Python's built-in `copy` module provides `deepcopy`. Load it with `import copy` at the top of the file (Module 08 explains imports).

```python
import copy

grid = [[1, 2, 3], [4, 5, 6]]
deep = copy.deepcopy(grid)
deep[0][0] = 99
print(grid)
print(deep)
```

```
[[1, 2, 3], [4, 5, 6]]
[[99, 2, 3], [4, 5, 6]]
```

Use a deep copy when you need to change a nested structure without touching the original.

```python
first = [1, 2]
second = [1, 2]
print(first == second, first is second)
```

```
True False
```

## Common mistakes

- **Thinking `b = a` copies a list.** Changes through `b` show up in `a`. Use `a.copy()` or `a[:]`.
- **Shallow-copying nested data.** `grid.copy()` shares the inner lists. Use `copy.deepcopy(grid)`.
- **Mutating an argument by accident.** A function that calls `.append` or `.sort()` on its parameter changes the caller's list. Work on a copy or build a new list.
- **A missing key deep inside.** `by_city["Paris"][0]` raises `KeyError: 'Paris'` if there is no such group. Use `by_city.get("Paris", [])` when a group might be absent.

## Try it

Create `row = [0, 0, 0]` and `board = [row, row, row]`. Set `board[0][0] = "X"` and print `board`. Explain what you see, then fix it by building the board with a loop that appends a fresh `[0, 0, 0]` each time.

## Exercises

Open `ex_05_05.py`:

1. `total_value`: the total stock value of a list of product dictionaries.
2. `cheapest_product`: the name of the cheapest product.
3. `names_by_city`: group names by city into a dictionary of lists.
4. `doubled`: a new list with every number doubled, leaving the original alone.
5. `copy_grid`: an independent copy of a list of lists, without using `copy`.

Run the tests:

```
python -m pytest part-1-python-fundamentals/05-collections/05-05-nested-data-and-references
```

## Summary

- A list of dictionaries holds records; a dictionary of lists holds groups; a list of lists holds a grid.
- Chain indexes and keys left to right: `products[1]["name"]`, `grid[row][column]`.
- Assignment and argument passing create references, not copies.
- `copy()` and `[:]` make shallow copies; `copy.deepcopy` copies nested data completely.
- `==` compares values; `is` checks whether two names refer to the same object.
