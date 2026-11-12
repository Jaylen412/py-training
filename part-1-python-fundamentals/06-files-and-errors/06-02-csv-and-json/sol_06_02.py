"""Solutions for 06-02 CSV and JSON."""
import csv
import json


def read_scores(path):
    """Read name/score rows, converting score to int."""
    with open(path, newline="") as file:
        records = list(csv.DictReader(file))
    for record in records:
        record["score"] = int(record["score"])
    return records


def column_average(path, column):
    """Return the average of a numeric column."""
    with open(path, newline="") as file:
        values = [float(row[column]) for row in csv.DictReader(file)]
    if len(values) == 0:
        return 0.0
    return sum(values) / len(values)


def write_records(path, records, fieldnames):
    """Write a list of dictionaries to a CSV with a header."""
    with open(path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def save_json(path, data):
    """Save `data` as indented JSON."""
    with open(path, "w") as file:
        json.dump(data, file, indent=2)


def load_json(path):
    """Load JSON data from the file."""
    with open(path) as file:
        return json.load(file)


def csv_to_json(csv_path, json_path):
    """Convert a CSV file into a JSON list of row dictionaries."""
    with open(csv_path, newline="") as file:
        rows = list(csv.DictReader(file))
    save_json(json_path, rows)
    return len(rows)
