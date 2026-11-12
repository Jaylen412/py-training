# 10-03 *args, **kwargs and unpacking


# Example 1: *args collects extra positional arguments into a tuple
def total(*numbers):
    print("  numbers is", numbers)
    return sum(numbers)


print(total(1, 2, 3))
print(total())


# Example 2: regular parameters first, then *args
def greet(greeting, *names):
    return [f"{greeting}, {name}!" for name in names]


print(greet("Hello", "Ada", "Alan"))


# Example 3: **kwargs collects extra keyword arguments into a dictionary
def make_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile


print(make_profile("Ada", born=1815, field="mathematics"))


# Example 4: all kinds together, in the required order
def describe(first, *rest, sep=", ", **options):
    return f"first={first} rest={rest} sep={sep!r} options={options}"


print(describe(1, 2, 3, sep="; ", colour="red"))

# Example 5: * and ** in a CALL unpack a list or a dictionary into arguments
point = [3, 4]
settings = {"sep": "-", "end": "!\n"}
print(*point)
print("a", "b", **settings)


def area(width, height):
    return width * height


print(area(*point))
print(area(**{"width": 2, "height": 5}))


# Example 6: keyword-only arguments come after a bare *
def connect(host, *, port=80, timeout=10):
    return f"{host}:{port} (timeout {timeout}s)"


print(connect("example.com", port=8080))
try:
    connect("example.com", 8080)
except TypeError as error:
    print("TypeError:", error)

# Example 7: unpacking also builds new lists and dictionaries
first_half = [1, 2]
second_half = [3, 4]
print([*first_half, *second_half, 5])
defaults = {"colour": "blue", "size": "M"}
choices = {"size": "L"}
print({**defaults, **choices})


# Example 8: passing arguments through to another function
def logged(function, *args, **kwargs):
    print(f"  calling {function.__name__} with {args} {kwargs}")
    return function(*args, **kwargs)


print(logged(area, 3, height=7))
