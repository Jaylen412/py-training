# 03-05 Loop patterns

sentence = "the cat sat on the mat"

# Example 1: counting
t_count = 0
for letter in sentence:
    if letter == "t":
        t_count += 1
print("Number of t's:", t_count)

# Example 2: summing digits found in text
order_code = "A7B3C9"
digit_sum = 0
for character in order_code:
    if character.isdigit():
        digit_sum += int(character)
print("Sum of digits:", digit_sum)

# Example 3: searching - stop at the first match with break
found_at = -1
for index in range(len(sentence)):
    if sentence[index] == "s":
        found_at = index
        break
print("First 's' at index:", found_at)

# Example 4: enumerate gives the index and the item together
for index, letter in enumerate("abc"):
    print(index, letter)

# Example 5: the same search, written with enumerate
found_at = -1
for index, letter in enumerate(sentence):
    if letter == "o":
        found_at = index
        break
print("First 'o' at index:", found_at)

# Example 6: maximum and minimum by hand
digits = "4719362"
largest = int(digits[0])
smallest = int(digits[0])
for character in digits:
    value = int(character)
    if value > largest:
        largest = value
    if value < smallest:
        smallest = value
print("Largest:", largest, "Smallest:", smallest)

# Example 7: else on a loop runs only if the loop did not break
number = 29
for divisor in range(2, number):
    if number % divisor == 0:
        print(number, "is divisible by", divisor)
        break
else:
    print(number, "is prime")

# Example 8: "all" and "any" checks with a flag
password = "secret42"
has_digit = False
for character in password:
    if character.isdigit():
        has_digit = True
        break
print("Password has a digit:", has_digit)
