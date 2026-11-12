# 05-03 Dictionaries

# Example 1: creating a dictionary and looking up values
ages = {"Ada": 36, "Alan": 41, "Grace": 85}
print(ages)
print(ages["Alan"])
print(len(ages))

# Example 2: get returns a default instead of failing
print(ages.get("Grace"))
print(ages.get("Linus"))
print(ages.get("Linus", 0))

# Example 3: in checks the keys
print("Ada" in ages, "Linus" in ages)

# Example 4: adding, changing and deleting
ages["Linus"] = 55
ages["Ada"] = 37
print(ages)
del ages["Grace"]
print(ages)
removed = ages.pop("Linus")
print(removed, ages)

# Example 5: looping over keys, values and items
prices = {"apple": 0.5, "bread": 1.2, "milk": 0.9}
for item in prices:
    print(item, end=" ")
print()
for item in prices.keys():
    print(item, end=" ")
print()
for price in prices.values():
    print(price, end=" ")
print()
for item, price in prices.items():
    print(f"{item} costs {price:.2f}")

# Example 6: the counting pattern
words = "the cat and the hat and the bat".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print(counts)

# Example 7: finding the key with the largest value
best_word = None
best_count = 0
for word, count in counts.items():
    if count > best_count:
        best_word = word
        best_count = count
print("Most common:", best_word, best_count)

# Example 8: keys must be immutable; values can be anything
locations = {(51.5, -0.1): "London", (48.9, 2.4): "Paris"}
print(locations[(51.5, -0.1)])
inventory = {"fruit": ["apple", "pear"], "count": 2}
print(inventory["fruit"][1])

# Example 9: building a dictionary from two lists with zip
keys = ["name", "language"]
values = ["Ada", "Python"]
record = dict(zip(keys, values))
print(record)
