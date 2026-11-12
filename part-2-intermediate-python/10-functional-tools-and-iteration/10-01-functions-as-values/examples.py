# 10-01 Functions as values


# Example 1: a function is a value you can store in a variable
def shout(text):
    return text.upper() + "!"


speak = shout
print(speak("hello"))
print(type(shout).__name__, shout.__name__)


# Example 2: passing a function to another function
def apply_to_all(function, items):
    return [function(item) for item in items]


print(apply_to_all(shout, ["hi", "bye"]))
print(apply_to_all(len, ["hi", "bye"]))

# Example 3: functions in a dictionary - choosing behaviour by name
operations = {
    "double": lambda number: number * 2,
    "square": lambda number: number ** 2,
    "negate": lambda number: -number,
}
for name, operation in operations.items():
    print(name, operation(5))

# Example 4: lambda makes a small unnamed function
add = lambda first, second: first + second
print(add(2, 3))

# Example 5: sorted with key - sort by a computed value
words = ["banana", "kiwi", "apple", "fig"]
print(sorted(words))
print(sorted(words, key=len))
print(sorted(words, key=lambda word: word[-1]))

# Example 6: sorting records by a field, and by two fields
people = [
    {"name": "Ada", "age": 36},
    {"name": "Alan", "age": 41},
    {"name": "Grace", "age": 36},
]
print([person["name"] for person in sorted(people, key=lambda person: person["age"])])
by_age_then_name = sorted(people, key=lambda person: (-person["age"], person["name"]))
print([person["name"] for person in by_age_then_name])

# Example 7: max and min accept key too
print(max(words, key=len))
print(min(people, key=lambda person: person["age"])["name"])

# Example 8: map and filter versus comprehensions
numbers = [1, 2, 3, 4, 5, 6]
print(list(map(lambda number: number * 10, numbers)))
print([number * 10 for number in numbers])
print(list(filter(lambda number: number % 2 == 0, numbers)))
print([number for number in numbers if number % 2 == 0])
print(list(map(str.upper, ["a", "b"])))
