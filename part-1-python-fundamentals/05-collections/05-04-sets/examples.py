# 05-04 Sets

# Example 1: a set keeps only one copy of each value
colours = {"red", "green", "blue", "red"}
print(len(colours))
print(sorted(colours))

# Example 2: removing duplicates from a list
visits = ["home", "about", "home", "blog", "home"]
unique_pages = set(visits)
print(len(visits), len(unique_pages))
print(sorted(unique_pages))

# Example 3: an empty set needs set(), because {} is an empty dict
empty_set = set()
empty_dict = {}
print(type(empty_set), type(empty_dict))

# Example 4: adding and removing
tags = {"python"}
tags.add("data")
tags.add("python")
print(sorted(tags))
tags.discard("data")
tags.discard("missing")
print(sorted(tags))

# Example 5: fast membership tests
allowed = {"admin", "editor", "viewer"}
print("editor" in allowed, "guest" in allowed)

# Example 6: set operations
python_fans = {"Ada", "Alan", "Grace", "Linus"}
java_fans = {"Grace", "James", "Linus"}
print(sorted(python_fans | java_fans))
print(sorted(python_fans & java_fans))
print(sorted(python_fans - java_fans))
print(sorted(python_fans ^ java_fans))

# Example 7: the same operations as methods
print(sorted(python_fans.union(java_fans)))
print(sorted(python_fans.intersection(java_fans)))
print(sorted(python_fans.difference(java_fans)))

# Example 8: subset checks
required = {"name", "email"}
provided = {"name", "email", "phone"}
print(required <= provided)
print(required.issubset(provided))

# Example 9: sets have no order and no indexes
letters = set("hello")
print(len(letters), "l" in letters)
