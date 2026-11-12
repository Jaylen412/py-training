"""Summaries of a list of LogRecord objects."""
from collections import Counter

from .parsing import LogRecord


def status_counts(records: list[LogRecord]) -> dict[int, int]:
    """Return the number of requests for each status code, smallest code first."""
    counts = Counter(record.status for record in records)
    return dict(sorted(counts.items()))


def busiest_hours(records: list[LogRecord], top: int = 3) -> list[tuple[int, int]]:
    """Return the `top` (hour, request count) pairs, busiest first.

    Ties are broken by the earlier hour.
    """
    counts = Counter(record.timestamp.hour for record in records)
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:top]


def top_paths(records: list[LogRecord], top: int = 5) -> list[tuple[str, int]]:
    """Return the `top` (path, request count) pairs, most requested first.

    Ties are broken alphabetically by path.
    """
    counts = Counter(record.path for record in records)
    ranked = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))
    return ranked[:top]


def slowest_requests(records: list[LogRecord], top: int = 5) -> list[LogRecord]:
    """Return the `top` records with the longest duration, slowest first."""
    return sorted(records, key=lambda record: record.duration, reverse=True)[:top]


def error_rate(records: list[LogRecord]) -> float:
    """Return the fraction of requests with a 4xx or 5xx status (0.0 if none)."""
    if not records:
        return 0.0
    return sum(record.is_error for record in records) / len(records)
