# 02-04 String methods and f-strings

# Example 1: changing case
title = "Machine Learning"
print(title.lower())
print(title.upper())
print("ada lovelace".title())

# Example 2: methods return a new string; the original is unchanged
print(title)

# Example 3: removing whitespace
raw_input = "   hello world  \n"
print("[" + raw_input.strip() + "]")
print("[" + raw_input.lstrip() + "]")
print("[" + raw_input.rstrip() + "]")

# Example 4: replace
sentence = "I like cats. Cats are great."
print(sentence.replace("cats", "dogs"))
print(sentence.replace("Cats", "Dogs").replace("cats", "dogs"))

# Example 5: split and join
csv_line = "Ada,36,London"
parts = csv_line.split(",")
print(parts)
print("one two  three".split())
print(" - ".join(parts))

# Example 6: find and in
email = "ada@example.com"
print(email.find("@"))
print(email.find("#"))
print("@" in email)
print("example" in email)
print(email.count("a"))

# Example 7: chaining methods
messy = "  PyThOn  "
print(messy.strip().lower())

# Example 8: f-strings
name = "Ada"
age = 36
print(f"{name} is {age} years old")
print(f"Next year {name} will be {age + 1}")

# Example 9: formatting numbers in f-strings
price = 1234.5
print(f"{price:.2f}")
print(f"{price:,.2f}")
print(f"{0.4567:.1%}")
print(f"{7:03d}")
print(f"[{name:>6}]")
print(f"[{name:<6}]")
