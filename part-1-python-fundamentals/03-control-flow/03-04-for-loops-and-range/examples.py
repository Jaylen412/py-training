# 03-04 for loops and range

# Example 1: looping over the characters of a string
for letter in "cat":
    print(letter)

# Example 2: range gives a sequence of whole numbers
for number in range(4):
    print(number, end=" ")
print()
for number in range(2, 6):
    print(number, end=" ")
print()
for number in range(0, 20, 5):
    print(number, end=" ")
print()
for number in range(5, 0, -1):
    print(number, end=" ")
print()

# Example 3: repeating something a fixed number of times
for _ in range(3):
    print("Hip hip hooray!")

# Example 4: the accumulator pattern - a running total
total = 0
for number in range(1, 101):
    total += number
print("1 + 2 + ... + 100 =", total)

# Example 5: accumulating a string
shout = ""
for letter in "hello":
    shout += letter.upper() + "!"
print(shout)

# Example 6: counting with a condition inside the loop
vowel_count = 0
for letter in "machine learning":
    if letter in "aeiou":
        vowel_count += 1
print("Vowels:", vowel_count)

# Example 7: nested loops - a small multiplication table
for row in range(1, 4):
    line = ""
    for column in range(1, 6):
        line += f"{row * column:4}"
    print(line)

# Example 8: nested loops - a triangle of stars
for size in range(1, 5):
    print("*" * size)
