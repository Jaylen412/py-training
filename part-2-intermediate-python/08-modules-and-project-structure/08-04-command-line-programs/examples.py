# 08-04 Command-line programs
# The examples below pass argument lists to the functions directly, so this
# file runs without any command-line arguments. greet.py, next to this file,
# is a complete program you can run from the terminal.
import argparse
import sys

# Example 1: sys.argv holds the words typed after `python`
print(sys.argv[0].endswith("examples.py"), len(sys.argv))


# Example 2: reading arguments by hand from a list like sys.argv[1:]
def add_numbers(arguments):
    return sum([float(argument) for argument in arguments])


print(add_numbers(["3", "4.5"]))


# Example 3: argparse describes the arguments and does the parsing
def build_parser():
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument("name", help="who to greet")
    parser.add_argument("--times", type=int, default=1, help="how many greetings")
    parser.add_argument("--shout", action="store_true", help="use capitals")
    return parser


parser = build_parser()
args = parser.parse_args(["Ada", "--times", "2", "--shout"])
print(args)
print(args.name, args.times, args.shout)
print(parser.parse_args(["Grace"]))

# Example 4: argparse writes the help text for you
parser.print_help()


# Example 5: a main function that returns an exit code
def main(argv):
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


print("exit code:", main(["Linus", "--times", "2"]))
print("exit code:", main(["Linus", "--times", "0"]))

# Example 6: bad arguments make argparse exit with code 2
try:
    build_parser().parse_args(["Ada", "--times", "lots"])
except SystemExit as error:
    print("argparse exited with code", error.code)
