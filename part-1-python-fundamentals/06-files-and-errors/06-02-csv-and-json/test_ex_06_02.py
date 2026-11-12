import importlib
import json
import os

import pytest

mod = importlib.import_module(
    "sol_06_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_06_02"
)


def test_read_scores(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("name,score\nAda,95\nAlan,88\n")
    assert mod.read_scores(path) == [
        {"name": "Ada", "score": 95},
        {"name": "Alan", "score": 88},
    ]


def test_read_scores_header_only(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text("name,score\n")
    assert mod.read_scores(path) == []


def test_read_scores_comma_inside_quotes(tmp_path):
    path = tmp_path / "scores.csv"
    path.write_text('name,score\n"Lovelace, Ada",95\n')
    assert mod.read_scores(path) == [{"name": "Lovelace, Ada", "score": 95}]


def test_column_average(tmp_path):
    path = tmp_path / "prices.csv"
    path.write_text("item,price\npen,1.5\npad,2.5\n")
    assert mod.column_average(path, "price") == pytest.approx(2.0)


def test_column_average_no_rows(tmp_path):
    path = tmp_path / "prices.csv"
    path.write_text("item,price\n")
    assert mod.column_average(path, "price") == 0.0


def test_write_records(tmp_path):
    path = tmp_path / "out.csv"
    mod.write_records(path, [{"a": 1, "b": 2}], ["a", "b"])
    assert path.read_text().splitlines() == ["a,b", "1,2"]


def test_write_records_column_order_and_empty(tmp_path):
    path = tmp_path / "out.csv"
    mod.write_records(path, [{"a": 1, "b": 2}], ["b", "a"])
    assert path.read_text().splitlines() == ["b,a", "2,1"]
    empty = tmp_path / "empty.csv"
    mod.write_records(empty, [], ["x"])
    assert empty.read_text().splitlines() == ["x"]


def test_save_json_writes_valid_json(tmp_path):
    path = tmp_path / "data.json"
    mod.save_json(path, {"a": [1, 2], "b": None})
    assert json.loads(path.read_text()) == {"a": [1, 2], "b": None}


def test_load_json_round_trip(tmp_path):
    path = tmp_path / "data.json"
    data = {"name": "Ada", "scores": [95, 88], "active": True}
    mod.save_json(path, data)
    assert mod.load_json(path) == data


def test_load_json_list(tmp_path):
    path = tmp_path / "list.json"
    path.write_text("[1, 2, 3]")
    assert mod.load_json(path) == [1, 2, 3]


def test_csv_to_json(tmp_path):
    csv_path = tmp_path / "in.csv"
    csv_path.write_text("name,age\nAda,36\nAlan,41\nGrace,85\n")
    json_path = tmp_path / "out.json"
    assert mod.csv_to_json(csv_path, json_path) == 3
    assert json.loads(json_path.read_text())[1] == {"name": "Alan", "age": "41"}


def test_csv_to_json_no_rows(tmp_path):
    csv_path = tmp_path / "in.csv"
    csv_path.write_text("name,age\n")
    json_path = tmp_path / "out.json"
    assert mod.csv_to_json(csv_path, json_path) == 0
    assert json.loads(json_path.read_text()) == []
