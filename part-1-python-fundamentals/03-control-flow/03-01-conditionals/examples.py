# 03-01 Conditionals

# Example 1: a simple if
temperature = 31
if temperature > 30:
    print("It's hot today.")
    print("Drink plenty of water.")
print("Have a nice day.")

# Example 2: if and else
balance = 40
price = 55
if balance >= price:
    print("Purchase approved")
else:
    print("Not enough money")

# Example 3: elif for several choices, checked in order
score = 72
if score >= 90:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 50:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)

# Example 4: order matters - the first true branch wins
score = 95
if score >= 50:
    print("Passed")
elif score >= 90:
    print("Passed with distinction")  # never reached

# Example 5: nested conditionals
age = 16
has_ticket = True
if has_ticket:
    if age >= 18:
        print("Enjoy the film.")
    else:
        print("Enjoy the film. No alcohol, please.")
else:
    print("Please buy a ticket.")

# Example 6: truthiness in a condition
name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("Hello, stranger!")

# Example 7: conditional expression
items_in_basket = 1
label = "item" if items_in_basket == 1 else "items"
print(f"You have {items_in_basket} {label}.")
