# 04-02 Arguments in depth


# Example 1: positional arguments are matched by position
def describe_pet(animal, name):
    return f"{name} is a {animal}"


print(describe_pet("dog", "Rex"))
print(describe_pet("Rex", "dog"))


# Example 2: keyword arguments are matched by name
print(describe_pet(name="Rex", animal="dog"))
print(describe_pet("cat", name="Tom"))


# Example 3: default values make an argument optional
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Ada"))
print(greet("Ada", "Good morning"))
print(greet("Ada", greeting="Hi"))


# Example 4: several defaults; keywords let you skip some
def format_number(value, decimals=2, prefix="", suffix=""):
    return f"{prefix}{value:.{decimals}f}{suffix}"


print(format_number(3.14159))
print(format_number(3.14159, 4))
print(format_number(19.5, prefix="$"))
print(format_number(0.25, decimals=0, suffix=" kg"))


# Example 5: print itself uses keyword arguments with defaults
print("a", "b", "c", sep="|", end="!\n")


# Example 6: the mutable default trap
# A list (Module 05) is a collection you can change; [] is an empty list
# and .append(x) adds x to the end of it.
def add_item_broken(item, basket=[]):
    basket.append(item)
    return basket


print(add_item_broken("apple"))
print(add_item_broken("bread"))


# Example 7: the fix - use None as the default and create the list inside
def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket


print(add_item("apple"))
print(add_item("bread"))
