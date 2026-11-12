# 02-03 Strings

# Example 1: single or double quotes
greeting = "Hello"
name = 'Ada'
print(greeting, name)

# Example 2: quotes inside strings
print("It's raining")
print('She said "hi"')
print('It\'s raining')

# Example 3: escape sequences
print("Line one\nLine two")
print("Name:\tAda")
print("A backslash: \\")

# Example 4: triple quotes for several lines
poem = """Roses are red,
Violets are blue."""
print(poem)

# Example 5: joining and repeating
first_name = "Ada"
last_name = "Lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("-" * 20)

# Example 6: length
print(len(full_name))
print(len(""))

# Example 7: indexing
word = "Python"
print(word[0])
print(word[1])
print(word[5])
print(word[-1])
print(word[-2])

# Example 8: slicing
print(word[0:2])
print(word[2:5])
print(word[:3])
print(word[3:])
print(word[::2])
print(word[::-1])

# Example 9: strings are immutable, so build a new one instead
fixed = "J" + word[1:]
print(fixed)
print(word)
