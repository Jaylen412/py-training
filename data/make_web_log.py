"""Generate data/web_server.log, the sample log for the Part 2 project.

Run from the repository root:
    python data/make_web_log.py

Each line has the form:
    203.0.113.7 - - [11/Nov/2026:09:15:02 +0000] "GET /products HTTP/1.1" 200 5123 0.042
that is: client IP, timestamp, request (method, path, protocol), status code,
response size in bytes, and the time taken to respond in seconds.
A few malformed lines are included on purpose.
"""
import random
from datetime import datetime, timedelta
from pathlib import Path

SEED = 42
LINE_COUNT = 800
OUTPUT = Path(__file__).parent / "web_server.log"

PATHS = {
    "/": 30, "/products": 20, "/products/42": 8, "/products/7": 6, "/cart": 10,
    "/checkout": 5, "/login": 8, "/api/search": 9, "/about": 3, "/static/app.js": 12,
}
METHODS = {"GET": 85, "POST": 15}
# Busier in the afternoon and evening, quiet at night.
HOUR_WEIGHTS = [1, 1, 1, 1, 1, 2, 3, 5, 7, 8, 8, 9, 10, 9, 9, 10, 11, 12, 14, 13, 10, 7, 4, 2]


def pick(rng, weighted):
    return rng.choices(list(weighted), weights=list(weighted.values()))[0]


def make_line(rng, day_start):
    hour = rng.choices(range(24), weights=HOUR_WEIGHTS)[0]
    moment = day_start + timedelta(hours=hour, minutes=rng.randrange(60), seconds=rng.randrange(60))
    path = pick(rng, PATHS)
    method = "POST" if path in ("/checkout", "/login") and rng.random() < 0.6 else pick(rng, METHODS)
    roll = rng.random()
    if roll < 0.03:
        status = 500
    elif roll < 0.09:
        status = 404
    elif roll < 0.12:
        status = 301
    else:
        status = 200
    size = 0 if status in (301, 500) else rng.randint(200, 20_000)
    duration = round(rng.lognormvariate(-3, 0.8) * (6 if path == "/api/search" else 1), 3)
    ip = f"203.0.113.{rng.randint(1, 60)}"
    stamp = moment.strftime("%d/%b/%Y:%H:%M:%S +0000")
    return f'{ip} - - [{stamp}] "{method} {path} HTTP/1.1" {status} {size} {duration}'


def main():
    rng = random.Random(SEED)
    day_start = datetime(2026, 11, 11)
    lines = sorted((make_line(rng, day_start) for _ in range(LINE_COUNT)),
                   key=lambda line: line.split("[")[1][:20])
    malformed = [
        "this line is not a log entry",
        '203.0.113.9 - - [11/Nov/2026:10:00:00 +0000] "GET /" 200',
        '203.0.113.9 - - [not a date] "GET / HTTP/1.1" 200 512 0.010',
        "",
        '203.0.113.9 - - [11/Nov/2026:10:00:00 +0000] "GET / HTTP/1.1" OK 512 0.010',
    ]
    for offset, bad_line in enumerate(malformed):
        lines.insert(100 + offset * 150, bad_line)
    OUTPUT.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(lines)} lines to {OUTPUT}")


if __name__ == "__main__":
    main()
