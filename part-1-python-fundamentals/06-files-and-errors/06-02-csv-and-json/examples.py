# 06-02 CSV and JSON
import csv
import json
from pathlib import Path

lesson_folder = Path(__file__).parent
csv_path = lesson_folder / "scores.csv"
json_path = lesson_folder / "scores.json"

# Example 1: write a CSV file with csv.writer
rows = [
    ["name", "subject", "score"],
    ["Ada", "maths", "95"],
    ["Alan", "maths", "88"],
    ["Grace", "physics", "91"],
]
with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)
print(csv_path.read_text())

# Example 2: read it back with csv.reader - every value is a string
with open(csv_path, newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Example 3: DictReader gives one dictionary per row
with open(csv_path, newline="") as file:
    records = list(csv.DictReader(file))
print(records[0])

# Example 4: convert types as you read
for record in records:
    record["score"] = int(record["score"])
scores = [record["score"] for record in records]
print(f"Average score: {sum(scores) / len(scores):.1f}")

# Example 5: DictWriter writes dictionaries as rows
results = [{"name": "Ada", "passed": True}, {"name": "Linus", "passed": False}]
results_path = lesson_folder / "results.csv"
with open(results_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "passed"])
    writer.writeheader()
    writer.writerows(results)
print(results_path.read_text())

# Example 6: save Python data as JSON
data = {"class": "7B", "students": records, "teacher": None}
with open(json_path, "w") as file:
    json.dump(data, file, indent=2)
print(json_path.read_text()[:120])

# Example 7: load it back - the types survive
with open(json_path) as file:
    loaded = json.load(file)
print(loaded["students"][2]["score"] + 1)
print(loaded["teacher"])

# Example 8: json.dumps and json.loads work with strings
text = json.dumps({"a": [1, 2], "b": True})
print(text)
print(json.loads(text)["a"])

for path in [csv_path, json_path, results_path]:
    path.unlink()
