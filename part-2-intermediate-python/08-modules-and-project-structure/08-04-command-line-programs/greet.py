"""A complete command-line program for lesson 08-04.

Try, from the repository root:
    python part-2-intermediate-python/08-modules-and-project-structure/08-04-command-line-programs/greet.py Ada --times 2 --shout
    python .../greet.py --help
"""
import argparse
import sys


def build_parser():
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--times", type=int, default=1, help="how many greetings")
    parser.add_argument("--shout", action="store_true", help="use capitals")
    return parser


def main(argv=None):
    """Run the program. Returns 0 on success, 1 on a usage problem."""
    args = build_parser().parse_args(argv)
    if args.times < 1:
        print("error: --times must be at least 1", file=sys.stderr)
        return 1
    greeting = f"Hello, {args.name}!"
    if args.shout:
        greeting = greeting.upper()
    for _ in range(args.times):
        print(greeting)
    return 0


if __name__ == "__main__":
    sys.exit(main())
