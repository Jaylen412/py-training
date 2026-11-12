"""Command-line interface: `logtools path/to/access.log [--top N] [--report NAME]`."""
import argparse
import sys
from pathlib import Path

from .parsing import read_records
from .reports import busiest_hours, error_rate, slowest_requests, status_counts, top_paths

REPORTS = ["all", "status", "hours", "paths", "slow"]


def build_parser() -> argparse.ArgumentParser:
    """Requirement 8. Return a parser with:
    - a positional argument "logfile" (type=Path),
    - "--top" (int, default 5),
    - "--report" (choices=REPORTS, default "all").
    """
    raise NotImplementedError


def main(argv: list[str] | None = None) -> int:
    """Requirement 8. Run the tool and return an exit code.

    - If --top is below 1, print an error to sys.stderr and return 2.
    - If the log file does not exist, print an error containing
      "no such file" to sys.stderr and return 1.
    - Read the records with read_records, collecting skipped line numbers.
    - Print "<file name>: <n> requests". If any lines were skipped, print a
      warning containing "skipped <count>" to sys.stderr.
    - Print each requested report section under these headings:
      "Requests by status" (including the error rate), "Busiest hours",
      "Top paths", "Slowest requests". --report all prints all four.
    - Return 0.
    """
    raise NotImplementedError


if __name__ == "__main__":
    sys.exit(main())
