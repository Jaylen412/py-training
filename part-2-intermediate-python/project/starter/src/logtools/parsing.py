"""Turn lines of a web server log into LogRecord objects.

A line looks like:
    203.0.113.7 - - [11/Nov/2026:09:15:02 +0000] "GET /products HTTP/1.1" 200 5123 0.042
fields: client IP, timestamp, request (method, path, protocol), status code,
response size in bytes, and the time taken to respond in seconds.
"""
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime

# The format code for the timestamp, for datetime.strptime (see 08-03).
TIMESTAMP_FORMAT = "%d/%b/%Y:%H:%M:%S %z"


@dataclass(frozen=True)
class LogRecord:
    """Requirement 1. One request from the log.

    Replace `pass` with these fields, in this order:
    ip (str), timestamp (datetime), method (str), path (str), status (int),
    size (int), duration (float).
    """
    pass

    @property
    def is_error(self) -> bool:
        """True for client (4xx) and server (5xx) errors: status 400 or more."""
        raise NotImplementedError


def parse_line(line: str) -> LogRecord:
    """Requirement 2. Parse one log line into a LogRecord.

    Raise ValueError for any malformed line. Hints:
    - line.strip().split('"') gives three parts: the text before the request,
      the request itself, and the text after it.
    - The timestamp is between "[" and "]"; parse it with
      datetime.strptime(text, TIMESTAMP_FORMAT), which raises ValueError
      for a bad date.
    - The request splits into exactly 3 words; the end into exactly 3 numbers.
    """
    raise NotImplementedError


def read_records(lines: Iterable[str], skipped: list[int] | None = None) -> Iterator[LogRecord]:
    """Requirement 3. A GENERATOR: yield a LogRecord for each well-formed line.

    Skip malformed lines. If `skipped` is a list, append the 1-based line
    number of every skipped line to it.
    """
    raise NotImplementedError
