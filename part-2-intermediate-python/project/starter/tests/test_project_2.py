"""Tests for the Part 2 project. Run from the repository root with:

    python -m pytest part-2-intermediate-python/project/starter

Set COURSE_SOLUTIONS=1 to run the same tests against the reference solution.
"""
import dataclasses
import inspect
import os
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

PROJECT = Path(__file__).resolve().parent.parent.parent
SOURCE = PROJECT / ("solution" if os.environ.get("COURSE_SOLUTIONS") else "starter") / "src"
sys.path.insert(0, str(SOURCE))

from logtools import cli, parsing, reports  # noqa: E402
from logtools.parsing import LogRecord  # noqa: E402

SAMPLE_LOG = Path(__file__).resolve().parents[4] / "data" / "web_server.log"
GOOD_LINE = '203.0.113.7 - - [11/Nov/2026:09:15:02 +0000] "GET /products HTTP/1.1" 200 5123 0.042'


def make_record(path="/", status=200, hour=9, duration=0.1, method="GET"):
    stamp = datetime(2026, 11, 11, hour, 0, tzinfo=timezone.utc)
    return LogRecord("203.0.113.1", stamp, method, path, status, 100, duration)


@pytest.fixture
def records():
    return [
        make_record("/", 200, hour=9, duration=0.05),
        make_record("/", 200, hour=9, duration=0.10),
        make_record("/cart", 404, hour=10, duration=0.02),
        make_record("/api/search", 500, hour=18, duration=1.50),
        make_record("/api/search", 200, hour=18, duration=0.90),
        make_record("/", 301, hour=18, duration=0.01),
    ]


# Requirement 1: LogRecord

def test_log_record_fields_and_is_error():
    record = make_record(status=404)
    assert (record.method, record.path, record.status) == ("GET", "/", 404)
    assert record.is_error is True
    assert make_record(status=301).is_error is False


def test_log_record_is_immutable():
    record = make_record()
    with pytest.raises(dataclasses.FrozenInstanceError):
        record.status = 500


# Requirement 2: parse_line

def test_parse_line():
    record = parsing.parse_line(GOOD_LINE)
    assert record == LogRecord(
        ip="203.0.113.7",
        timestamp=datetime(2026, 11, 11, 9, 15, 2, tzinfo=timezone(timedelta(0))),
        method="GET",
        path="/products",
        status=200,
        size=5123,
        duration=0.042,
    )


def test_parse_line_ignores_trailing_newline():
    assert parsing.parse_line(GOOD_LINE + "\n").status == 200


@pytest.mark.parametrize(
    "bad_line",
    [
        "",
        "this line is not a log entry",
        '203.0.113.9 - - [11/Nov/2026:10:00:00 +0000] "GET /" 200',
        '203.0.113.9 - - [not a date] "GET / HTTP/1.1" 200 512 0.010',
        '203.0.113.9 - - [11/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" OK 512 0.010',
    ],
)
def test_parse_line_rejects_malformed_lines(bad_line):
    with pytest.raises(ValueError):
        parsing.parse_line(bad_line)


# Requirement 3: read_records

def test_read_records_is_a_generator_that_skips_bad_lines():
    assert inspect.isgeneratorfunction(parsing.read_records)
    skipped = []
    result = list(parsing.read_records([GOOD_LINE, "junk", GOOD_LINE], skipped))
    assert len(result) == 2
    assert skipped == [2]


def test_read_records_without_skipped_list():
    assert len(list(parsing.read_records(["junk", GOOD_LINE]))) == 1


def test_read_records_on_sample_log():
    skipped = []
    with open(SAMPLE_LOG) as file:
        result = list(parsing.read_records(file, skipped))
    assert len(result) == 800
    assert len(skipped) == 5


# Requirement 4: status_counts and error_rate

def test_status_counts(records):
    assert reports.status_counts(records) == {200: 3, 301: 1, 404: 1, 500: 1}
    assert list(reports.status_counts(records)) == [200, 301, 404, 500]


def test_error_rate(records):
    assert reports.error_rate(records) == pytest.approx(2 / 6)
    assert reports.error_rate([]) == 0.0


# Requirement 5: busiest_hours

def test_busiest_hours(records):
    assert reports.busiest_hours(records, top=2) == [(18, 3), (9, 2)]


def test_busiest_hours_tie_goes_to_earlier_hour():
    tied = [make_record(hour=14), make_record(hour=8)]
    assert reports.busiest_hours(tied, top=3) == [(8, 1), (14, 1)]


# Requirement 6: top_paths

def test_top_paths(records):
    assert reports.top_paths(records, top=2) == [("/", 3), ("/api/search", 2)]


def test_top_paths_tie_goes_alphabetically():
    tied = [make_record("/b"), make_record("/a")]
    assert reports.top_paths(tied) == [("/a", 1), ("/b", 1)]


# Requirement 7: slowest_requests

def test_slowest_requests(records):
    slowest = reports.slowest_requests(records, top=2)
    assert [record.duration for record in slowest] == [1.50, 0.90]


def test_slowest_requests_more_than_available(records):
    assert len(reports.slowest_requests(records, top=50)) == 6


# Requirement 8: the command-line interface

def test_cli_full_report(capsys):
    assert cli.main([str(SAMPLE_LOG), "--top", "3"]) == 0
    captured = capsys.readouterr()
    assert "800 requests" in captured.out
    for heading in ["Requests by status", "Busiest hours", "Top paths", "Slowest requests"]:
        assert heading in captured.out
    assert "skipped 5" in captured.err


def test_cli_single_report(capsys):
    assert cli.main([str(SAMPLE_LOG), "--report", "paths", "--top", "2"]) == 0
    output = capsys.readouterr().out
    assert "Top paths" in output
    assert "Busiest hours" not in output
    assert "/products" in output


def test_cli_missing_file(tmp_path, capsys):
    assert cli.main([str(tmp_path / "missing.log")]) == 1
    assert "no such file" in capsys.readouterr().err


def test_cli_bad_top(capsys):
    assert cli.main([str(SAMPLE_LOG), "--top", "0"]) == 2


def test_cli_rejects_unknown_report():
    with pytest.raises(SystemExit):
        cli.main([str(SAMPLE_LOG), "--report", "everything"])


# Requirement 9: packaging

def test_pyproject_declares_entry_point():
    pyproject = (SOURCE.parent / "pyproject.toml").read_text()
    assert 'logtools = "logtools.cli:main"' in pyproject
