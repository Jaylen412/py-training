# 06-01 Reading and writing text files
from pathlib import Path

# Example 1: build paths with pathlib
# __file__ is the path of this script, so this folder works wherever you run from.
lesson_folder = Path(__file__).parent
notes_path = lesson_folder / "notes.txt"
print(notes_path.name, notes_path.suffix, notes_path.stem)

# Example 2: write a file ("w" creates it, or empties it if it exists)
with open(notes_path, "w") as file:
    file.write("first line\n")
    file.write("second line\n")
print(notes_path.exists())

# Example 3: read the whole file as one string
with open(notes_path) as file:
    content = file.read()
print(repr(content))

# Example 4: append to the end ("a")
with open(notes_path, "a") as file:
    file.write("third line\n")

# Example 5: loop over the lines, stripping the newline from each
with open(notes_path) as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, line.rstrip("\n"))

# Example 6: read all lines into a list
with open(notes_path) as file:
    lines = file.read().splitlines()
print(lines)

# Example 7: writing several lines at once
shopping = ["eggs", "flour", "milk"]
shopping_path = lesson_folder / "shopping.txt"
with open(shopping_path, "w") as file:
    file.write("\n".join(shopping) + "\n")
print(shopping_path.read_text())

# Example 8: Path shortcuts for small files
summary_path = lesson_folder / "summary.txt"
summary_path.write_text("3 items\n")
print(summary_path.read_text().strip())

# Example 9: listing files in a folder
for path in sorted(lesson_folder.glob("*.txt")):
    print("Found:", path.name)

# Tidy up so the lesson folder stays clean
for path in [notes_path, shopping_path, summary_path]:
    path.unlink()
print(notes_path.exists())
