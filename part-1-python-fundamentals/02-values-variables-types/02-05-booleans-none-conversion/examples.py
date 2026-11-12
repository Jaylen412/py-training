# 02-05 Booleans, None and type conversion

# Example 1: the two boolean values
is_raining = True
has_umbrella = False
print(is_raining, has_umbrella)
print(type(is_raining))

# Example 2: comparisons produce booleans
age = 20
print(age > 18)
print(age < 18)
print(age >= 20)
print(age == 21)
print(age != 21)

# Example 3: comparing strings
print("apple" == "apple")
print("apple" == "Apple")
print("apple" < "banana")

# Example 4: None means "no value"
middle_name = None
print(middle_name)
print(type(middle_name))
print(middle_name is None)

# Example 5: converting between types
print(int("42") + 1)
print(float("3.5") * 2)
print(str(42) + "!")
print(int(3.99))
print(float(7))

# Example 6: truthiness with bool()
print(bool(0), bool(1), bool(-5))
print(bool(""), bool("hello"), bool(" "))
print(bool(None))

# Example 7: True and False behave like 1 and 0 in arithmetic
print(True + True + False)

# Example 8: checking types
print(type("42"), type(42), type(42.0))

# Example 9: input() always gives back a string.
# In your own programs you would write:
#     typed_age = input("How old are you? ")
# examples.py must run without waiting for you to type, so here we use a
# fixed string to stand in for what the user typed.
typed_age = "20"
print(type(typed_age))
age_next_year = int(typed_age) + 1
print(f"Next year you will be {age_next_year}")
