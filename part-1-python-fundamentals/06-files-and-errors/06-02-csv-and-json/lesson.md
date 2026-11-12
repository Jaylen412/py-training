# 06-02 CSV and JSON

## What you will learn

- Read and write CSV files with the `csv` module, including `DictReader` and `DictWriter`.
- Convert the strings read from a CSV into the right types.
- Save Python lists and dictionaries as JSON and load them back.
- Choose between CSV and JSON for a given job.

## Why it matters

CSV is the most common format for tabular data: almost every dataset you download, and every spreadsheet you export, can be a CSV. JSON is the most common format for structured data on the web and in configuration files. Your expense tracker project stores its data as JSON, and pandas' `read_csv` in Module 14 is a turbo-charged version of what you learn here.

## Concepts

### CSV files

**CSV** (comma-separated values) is a plain-text table: one row per line, values separated by commas, usually with a **header** row of column names first. You could split each line on commas yourself, but that breaks as soon as a value contains a comma (`"London, UK"`). The standard library's `csv` module handles all the edge cases.

### Writing with csv.writer

```python
import csv
import json
from pathlib import Path

lesson_folder = Path(__file__).parent
csv_path = lesson_folder / "scores.csv"

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
```

```
name,subject,score
Ada,maths,95
Alan,maths,88
Grace,physics,91

```

Always open CSV files with `newline=""`. The `csv` module manages line endings itself, and without this you get blank lines between rows on Windows.

### Reading with csv.reader

`csv.reader` gives each row as a list of strings. `next(reader)` takes the first row off, which is the header:

```python
with open(csv_path, newline="") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)
```

```
Header: ['name', 'subject', 'score']
['Ada', 'maths', '95']
['Alan', 'maths', '88']
['Grace', 'physics', '91']
```

Notice `'95'` in quotes: **CSV has no types**, so every value is read as a string.

### DictReader

`csv.DictReader` uses the header row as keys and gives each row as a dictionary, so you can refer to columns by name instead of position. Wrapping it in `list()` reads all the rows:

```python
with open(csv_path, newline="") as file:
    records = list(csv.DictReader(file))
print(records[0])
```

```
{'name': 'Ada', 'subject': 'maths', 'score': '95'}
```

### Converting types

Convert numeric columns yourself before doing maths:

```python
for record in records:
    record["score"] = int(record["score"])
scores = [record["score"] for record in records]
print(f"Average score: {sum(scores) / len(scores):.1f}")
```

```
Average score: 91.3
```

### DictWriter

`csv.DictWriter` writes dictionaries as rows. You tell it the column order with `fieldnames`, and `writeheader()` writes the header row:

```python
results = [{"name": "Ada", "passed": True}, {"name": "Linus", "passed": False}]
results_path = lesson_folder / "results.csv"
with open(results_path, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "passed"])
    writer.writeheader()
    writer.writerows(results)
print(results_path.read_text())
```

```
name,passed
Ada,True
Linus,False

```

`True` was written as the text `True`; reading it back gives the string `"True"`, not a boolean.

### JSON

**JSON** (JavaScript Object Notation) is a text format for nested data. It looks almost exactly like Python literals: objects `{}` map to dictionaries, arrays `[]` to lists, and it has strings, numbers, `true`/`false` and `null`. Unlike CSV, JSON **keeps types**: numbers stay numbers and nesting is preserved.

`json.dump(data, file)` writes Python data to a file; `indent=2` makes it readable:

```python
json_path = lesson_folder / "scores.json"
data = {"class": "7B", "students": records, "teacher": None}
with open(json_path, "w") as file:
    json.dump(data, file, indent=2)
print(json_path.read_text()[:120])
```

```
{
  "class": "7B",
  "students": [
    {
      "name": "Ada",
      "subject": "maths",
      "score": 95
    },
    {
 
```

(Only the first 120 characters are printed.) `None` became `null` in the file. `json.load(file)` reads it back:

```python
with open(json_path) as file:
    loaded = json.load(file)
print(loaded["students"][2]["score"] + 1)
print(loaded["teacher"])
```

```
92
None
```

The score is still an `int`, so `+ 1` works. The versions ending in **s**, `json.dumps` and `json.loads`, convert to and from a **s**tring instead of a file:

```python
text = json.dumps({"a": [1, 2], "b": True})
print(text)
print(json.loads(text)["a"])
```

```
{"a": [1, 2], "b": true}
[1, 2]
```

### CSV or JSON?

- **CSV** for flat tables where every row has the same columns, especially if people will open them in a spreadsheet.
- **JSON** for nested data, data with mixed types, or a program's saved state.

## Common mistakes

- **Forgetting that CSV values are strings.** `record["score"] + 1` gives `TypeError: can only concatenate str (not "int") to str`. Convert with `int()` or `float()` when you read.
- **Blank lines between rows on Windows.** Caused by opening the file without `newline=""`. Always pass it for CSV files.
- **Saving something JSON cannot represent.** `json.dumps({1, 2})` gives `TypeError: Object of type set is not JSON serializable`. Convert sets to lists first. Tuples are saved as lists and come back as lists.
- **A broken JSON file.** A trailing comma such as `{"a": 1,}` is fine in Python but not in JSON. Python 3.13 reports `JSONDecodeError: Illegal trailing comma before end of object: line 1 column 8 (char 7)`; older versions word it differently. Lesson 06-03 shows how to handle this.

## Try it

Add a fourth student to `rows` in `examples.py` whose subject is `"maths, applied"`. Look at how `csv.writer` writes that value in the file, and check that `DictReader` reads it back correctly.

## Exercises

Open `ex_06_02.py`:

1. `read_scores`: read a CSV into a list of dictionaries with integer scores.
2. `column_average`: the average of one numeric column of a CSV.
3. `write_records`: write a list of dictionaries to a CSV with a header.
4. `save_json` and `load_json`: save data as JSON and load it back.
5. `csv_to_json`: convert a CSV file into a JSON list of records.

Run the tests:

```
python -m pytest part-1-python-fundamentals/06-files-and-errors/06-02-csv-and-json
```

## Summary

- Use the `csv` module, and open CSV files with `newline=""`.
- `csv.DictReader` gives one dictionary per row; `csv.DictWriter` writes them, with `writeheader()`.
- Every CSV value is a string; convert numbers yourself.
- `json.dump` / `json.load` save and load nested Python data, keeping numbers, booleans and `None`.
- Use CSV for flat tables and JSON for nested data or saved program state.
