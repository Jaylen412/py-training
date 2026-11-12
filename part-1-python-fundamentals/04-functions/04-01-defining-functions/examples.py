# 04-01 Defining and calling functions


# Example 1: defining and calling a function
def say_hello():
    print("Hello!")


say_hello()
say_hello()


# Example 2: a parameter receives the argument's value
def greet(name):
    print(f"Hello, {name}!")


greet("Ada")
greet("Grace")


# Example 3: return hands a value back to the caller
def square(number):
    return number * number


result = square(7)
print(result)
print(square(3) + square(4))


# Example 4: return versus print
def add_and_print(first, second):
    print(first + second)


def add_and_return(first, second):
    return first + second


printed = add_and_print(2, 3)
returned = add_and_return(2, 3)
print("printed is", printed)
print("returned is", returned)


# Example 5: return ends the function straight away
def describe_age(age):
    if age < 13:
        return "child"
    if age < 18:
        return "teenager"
    return "adult"


print(describe_age(8), describe_age(15), describe_age(40))


# Example 6: a docstring explains what the function does
def area_of_circle(radius):
    """Return the area of a circle with the given radius."""
    return 3.14159 * radius ** 2


print(round(area_of_circle(2), 2))
print(area_of_circle.__doc__)


# Example 7: functions can call other functions
def hypotenuse(side_a, side_b):
    """Return the longest side of a right-angled triangle."""
    return (square(side_a) + square(side_b)) ** 0.5


print(hypotenuse(3, 4))
