# 10-01 Functions as values

## What you will learn

- Store functions in variables and data structures, and pass them to other functions.
- Write small unnamed functions with `lambda`.
- Sort, and find the maximum or minimum, by a computed value with `key=`.
- Use `map` and `filter`, and decide when a comprehension is clearer.

## Why it matters

In Python a function is a value, just like a number or a list. That lets you write code that is told **what to do** as well as **what to do it to**. You will use this constantly: sorting records by a field, passing a scoring function to a model-evaluation routine, and, in pandas, calling `.apply(some_function)` on a whole column.

## Concepts

### Functions are values

Writing a function's name **without brackets** refers to the function itself, without calling it. You can assign it to another name:

```python
def shout(text):
    return text.upper() + "!"


speak = shout
print(speak("hello"))
print(type(shout).__name__, shout.__name__)
```

```
HELLO!
function shout
```

`speak` and `shout` are two names for the same function.

### Passing functions to functions

A function that takes another function as an argument is called a **higher-order function**. Here `apply_to_all` does not care what the function does; it just calls it on every item:

```python
def apply_to_all(function, items):
    return [function(item) for item in items]


print(apply_to_all(shout, ["hi", "bye"]))
print(apply_to_all(len, ["hi", "bye"]))
```

```
['HI!', 'BYE!']
[2, 3]
```

Built-in functions such as `len` are values too.

### lambda

A **lambda** is a small function written as a single expression, without `def` or a name: `lambda parameters: expression`. The expression's value is returned automatically.

```python
add = lambda first, second: first + second
print(add(2, 3))
```

```
5
```

Assigning a lambda to a name like this is legal but pointless; use `def` for named functions. Lambdas shine as short, throwaway arguments. Here they are stored in a dictionary so that behaviour can be chosen by name:

```python
operations = {
    "double": lambda number: number * 2,
    "square": lambda number: number ** 2,
    "negate": lambda number: -number,
}
for name, operation in operations.items():
    print(name, operation(5))
```

```
double 10
square 25
negate -5
```

### Sorting with key

`sorted`, `list.sort`, `max` and `min` accept a **`key`** argument: a function applied to each item to get the value to compare. The items themselves are not changed.

```python
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, key=lambda word: word[-1]))
```

```
['apple', 'banana', 'fig', 'kiwi']
['fig', 'kiwi', 'apple', 'banana']
['banana', 'apple', 'fig', 'kiwi']
```

The second line sorts by length; the third by last letter.

Sorting records by a field is the most common use:

```python
people = [
    {"name": "Ada", "age": 36},
    {"name": "Alan", "age": 41},
    {"name": "Grace", "age": 36},
]
print([person["name"] for person in sorted(people, key=lambda person: person["age"])])
by_age_then_name = sorted(people, key=lambda person: (-person["age"], person["name"]))
print([person["name"] for person in by_age_then_name])
```

```
['Ada', 'Grace', 'Alan']
['Alan', 'Ada', 'Grace']
```

Ada and Grace are both 36. Python's sort is **stable**: items with equal keys keep their original order, so Ada stays ahead of Grace in the first result.

To sort by **several** things, return a tuple: tuples compare item by item, so ties on the first item are broken by the second. Negating a number (`-person["age"]`) sorts it from largest to smallest while the name still sorts A to Z.

`max` and `min` work the same way:

```python
print(max(words, key=len))
print(min(people, key=lambda person: person["age"])["name"])
```

```
banana
Ada
```

`min` returns the whole record, so you can read any field from the winner.

### map and filter

**`map(function, items)`** applies a function to every item; **`filter(function, items)`** keeps the items for which the function returns something truthy. Both produce their results lazily (one at a time, see 10-02), so wrap them in `list()` to see them. Each has a comprehension equivalent:

```python
numbers = [1, 2, 3, 4, 5, 6]
print(list(map(lambda number: number * 10, numbers)))
print([number * 10 for number in numbers])
print(list(filter(lambda number: number % 2 == 0, numbers)))
print([number for number in numbers if number % 2 == 0])
print(list(map(str.upper, ["a", "b"])))
```

```
[10, 20, 30, 40, 50, 60]
[10, 20, 30, 40, 50, 60]
[2, 4, 6]
[2, 4, 6]
['A', 'B']
```

Most Python programmers prefer comprehensions, which read more naturally. `map` is neat when you already have a named function, as in `map(str.upper, ...)`, where `str.upper` is the string method used as a plain function.

## Common mistakes

- **Calling the function instead of passing it.** `sorted(words, key=len())` gives `TypeError: len() takes exactly one argument (0 given)`. Pass `len`, not `len()`.
- **Putting statements in a lambda.** `lambda x: return x` is a `SyntaxError`. A lambda is a single expression and returns it automatically. Use `def` for anything longer.
- **Using a `map` or `filter` result twice.** The second `list(...)` is empty, because the results were already used up. Convert to a list once and reuse the list.
- **Sorting mixed types.** A key that returns a number for some items and `None` for others gives `TypeError: '<' not supported between instances of 'NoneType' and 'int'`. Make the key return comparable values for every item.

## Try it

Sort `["Banana", "apple", "Cherry"]` with plain `sorted`, then with `key=str.lower`. Why do the results differ? (Hint: 02-05 says capital letters come before lower-case ones.)

## Exercises

Open `ex_10_01.py`:

1. `apply_twice`: call a function on a value, then again on the result.
2. `sort_by_length`: sort words by length, alphabetically within each length.
3. `sort_people`: sort records oldest first, then by name.
4. `longest_by`: the item with the largest key value.
5. `count_matching`: how many items a test function accepts.

Run the tests:

```
python -m pytest part-2-intermediate-python/10-functional-tools-and-iteration/10-01-functions-as-values
```

## Summary

- Functions are values: assign them, store them in collections, pass them as arguments.
- `lambda parameters: expression` makes a small unnamed function, best used as an argument.
- `sorted`, `max` and `min` take `key=function`; return a tuple from the key to sort by several things.
- `map` and `filter` apply and select lazily; comprehensions usually read better.
