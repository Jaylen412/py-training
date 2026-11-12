"""Turn lines of a web server log into LogRecord objects.

A line looks like:
    203.0.113.7 - - [11/Nov/2026:09:15:02 +0000] "GET /products HTTP/1.1" 200 5123 0.042
"""
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from datetime import datetime

TIMESTAMP_FORMAT = "%d/%b/%Y:%H:%M:%S %z"


@dataclass(frozen=True)
class LogRecord:
    """One request from the log."""

    ip: str
    timestamp: datetime
    method: str
    path: str
    status: int
    size: int
    duration: float

    @property
    def is_error(self) -> bool:
        """True for client (4xx) and server (5xx) errors."""
        return self.status >= 400


def parse_line(line: str) -> LogRecord:
    """Parse one log line, raising ValueError if it is malformed."""
    parts = line.strip().split('"')
    if len(parts) != 3:
        raise ValueError(f"expected one quoted request, got: {line!r}")
    prefix, request, suffix = parts

    if "[" not in prefix or "]" not in prefix:
        raise ValueError(f"missing timestamp: {line!r}")
    ip = prefix.split()[0]
    stamp = prefix[prefix.index("[") + 1:prefix.index("]")]
    timestamp = datetime.strptime(stamp, TIMESTAMP_FORMAT)

    request_parts = request.split()
    if len(request_parts) != 3:
        raise ValueError(f"request should be METHOD PATH PROTOCOL: {request!r}")
    method, path, _protocol = request_parts

    numbers = suffix.split()
    if len(numbers) != 3:
        raise ValueError(f"expected status, size and duration: {suffix!r}")
    status, size, duration = int(numbers[0]), int(numbers[1]), float(numbers[2])

    return LogRecord(ip, timestamp, method, path, status, size, duration)


def read_records(lines: Iterable[str], skipped: list[int] | None = None) -> Iterator[LogRecord]:
    """Yield a LogRecord for each well-formed line, one at a time.

    Malformed lines are skipped. If `skipped` is a list, the 1-based line
    number of each skipped line is appended to it.
    """
    for line_number, line in enumerate(lines, start=1):
        try:
            yield parse_line(line)
        except ValueError:
            if skipped is not None:
                skipped.append(line_number)
