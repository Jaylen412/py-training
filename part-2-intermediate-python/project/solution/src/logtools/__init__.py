"""logtools: summarise web server access logs."""
from .parsing import LogRecord, parse_line, read_records
from .reports import busiest_hours, error_rate, slowest_requests, status_counts, top_paths

__version__ = "1.0.0"

__all__ = [
    "LogRecord",
    "parse_line",
    "read_records",
    "status_counts",
    "busiest_hours",
    "top_paths",
    "slowest_requests",
    "error_rate",
]
