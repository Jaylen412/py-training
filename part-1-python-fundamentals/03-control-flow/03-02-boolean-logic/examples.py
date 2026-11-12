# 03-02 Boolean logic

# Example 1: and, or, not
print(True and True, True and False)
print(True or False, False or False)
print(not True, not False)

# Example 2: combining comparisons with and
age = 25
has_licence = True
can_rent_car = age >= 21 and has_licence
print("Can rent a car:", can_rent_car)

# Example 3: or for "any of these"
day = "Sunday"
is_weekend = day == "Saturday" or day == "Sunday"
print("Weekend:", is_weekend)

# Example 4: not flips a boolean
is_member = False
if not is_member:
    print("Join today and save 10%!")

# Example 5: precedence - not, then and, then or
print(True or False and False)
print((True or False) and False)

# Example 6: chained comparisons
temperature = 22
print(18 <= temperature <= 25)
print(0 < 5 < 3)

# Example 7: short-circuiting skips the right-hand side when it can
count = 0
total = 10
if count != 0 and total / count > 2:
    print("High average")
else:
    print("No data, or a low average")

# Example 8: leap years combine and, or and not
year = 2000
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(year, "is a leap year:", is_leap)
year = 1900
is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print(year, "is a leap year:", is_leap)
