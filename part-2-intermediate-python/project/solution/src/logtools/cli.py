"""Command-line interface: `logtools path/to/access.log [--top N] [--report NAME]`."""
import argparse
import sys
from pathlib import Path

from .parsing import read_records
from .reports import busiest_hours, error_rate, slowest_requests, status_counts, top_paths

REPORTS = ["all", "status", "hours", "paths", "slow"]


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="logtools", description="Summarise a web server access log.")
    parser.add_argument("logfile", type=Path, help="path to the log file")
    parser.add_argument("--top", type=int, default=5, help="how many rows to show in ranked reports")
    parser.add_argument("--report", choices=REPORTS, default="all", help="which report to show")
    return parser


def format_report(records, report="all", top=5) -> str:
    """Return the requested report sections as text."""
    sections = []
    if report in ("all", "status"):
        lines = ["Requests by status"]
        lines += [f"  {status}  {count:>6}" for status, count in status_counts(records).items()]
        lines.append(f"  error rate: {error_rate(records):.1%}")
        sections.append("\n".join(lines))
    if report in ("all", "hours"):
        lines = ["Busiest hours"]
        lines += [f"  {hour:02d}:00  {count:>6}" for hour, count in busiest_hours(records, top)]
        sections.append("\n".join(lines))
    if report in ("all", "paths"):
        lines = ["Top paths"]
        lines += [f"  {path:<20}{count:>6}" for path, count in top_paths(records, top)]
        sections.append("\n".join(lines))
    if report in ("all", "slow"):
        lines = ["Slowest requests"]
        lines += [
            f"  {record.duration:>7.3f}s  {record.method:<5}{record.path:<20}{record.timestamp:%H:%M:%S}"
            for record in slowest_requests(records, top)
        ]
        sections.append("\n".join(lines))
    return "\n\n".join(sections)


def main(argv: list[str] | None = None) -> int:
    """Run the command line tool and return an exit code."""
    args = build_parser().parse_args(argv)
    if args.top < 1:
        print("error: --top must be at least 1", file=sys.stderr)
        return 2
    skipped: list[int] = []
    try:
        with open(args.logfile) as file:
            records = list(read_records(file, skipped))
    except FileNotFoundError:
        print(f"error: no such file: {args.logfile}", file=sys.stderr)
        return 1

    print(f"{args.logfile.name}: {len(records)} requests")
    if skipped:
        print(f"warning: skipped {len(skipped)} malformed line(s): {skipped}", file=sys.stderr)
    print()
    print(format_report(records, args.report, args.top))
    return 0


if __name__ == "__main__":
    sys.exit(main())
