# 02-02 Variables and assignment

# Example 1: assignment gives a value a name
price = 4.50
quantity = 3
total_price = price * quantity
print(total_price)

# Example 2: the right-hand side is worked out first
width = 5
height = 2
area = width * height
print("Area:", area)

# Example 3: reassignment replaces the old value
score = 10
print(score)
score = 25
print(score)

# Example 4: a variable can be used to compute its own new value
lives = 3
lives = lives - 1
print(lives)

# Example 5: assigning one variable to another copies the current value
first = 100
second = first
first = 200
print(first, second)

# Example 6: augmented assignment
balance = 100
balance += 50   # same as balance = balance + 50
print(balance)
balance -= 30   # same as balance = balance - 30
print(balance)
balance *= 2    # same as balance = balance * 2
print(balance)
balance /= 4    # same as balance = balance / 4
print(balance)

# Example 7: good names say what the value means
seconds_per_minute = 60
minutes_per_hour = 60
seconds_per_hour = seconds_per_minute * minutes_per_hour
print(seconds_per_hour)

# Example 8: constants are written in capitals by convention
VAT_RATE = 0.2
net_price = 80
print(net_price * (1 + VAT_RATE))
