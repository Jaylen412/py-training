# 03-03 while loops

# Example 1: a counter
count = 1
while count <= 3:
    print("Count is", count)
    count += 1
print("Finished; count is now", count)

# Example 2: the loop body may run zero times
fuel = 0
while fuel > 0:
    print("Driving...")
    fuel -= 1
print("Out of fuel")

# Example 3: repeat until a goal is reached
savings = 100.0
years = 0
while savings < 200:
    savings *= 1.07
    years += 1
print(f"Savings double after {years} years: {savings:.2f}")

# Example 4: break leaves the loop straight away
number = 1
while True:
    if number * number > 50:
        break
    number += 1
print("First number whose square is over 50:", number)

# Example 5: continue skips to the next check of the condition
number = 0
while number < 10:
    number += 1
    if number % 3 != 0:
        continue
    print(number, "is a multiple of 3")

# Example 6: taking a number apart digit by digit
remaining = 2026
digit_total = 0
while remaining > 0:
    digit_total += remaining % 10
    remaining //= 10
print("Sum of the digits of 2026:", digit_total)

# Example 7: keep going until the input is valid.
# In a real program, `answer` would come from input(). Here a counter
# stands in for a user who types something different on each attempt.
attempt = 0
answer = ""
while answer != "yes" and answer != "no":
    attempt += 1
    if attempt == 1:
        answer = "maybe"
    else:
        answer = "yes"
    print(f"Attempt {attempt}: got {answer}")
print("Valid answer received:", answer)
