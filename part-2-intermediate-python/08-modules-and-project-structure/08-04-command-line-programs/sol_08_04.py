"""Solutions for 08-04 Command-line programs."""
import argparse
import sys

ABSOLUTE_ZERO_C = -273.15


def parse_key_values(arguments):
    """Turn "key=value" strings into a dictionary."""
    result = {}
    for argument in arguments:
        if "=" not in argument:
            raise ValueError(f"expected key=value, got {argument!r}")
        key, value = argument.split("=", 1)  # 1 = split at the first "=" only
        result[key] = value
    return result


def convert(value, to):
    """Convert Celsius to Fahrenheit (to="f") or Fahrenheit to Celsius (to="c")."""
    if to == "f":
        return value * 9 / 5 + 32
    return (value - 32) * 5 / 9


def build_parser():
    """Return the parser for the conversion tool."""
    parser = argparse.ArgumentParser(description="Convert temperatures.")
    parser.add_argument("value", type=float, help="the temperature to convert")
    parser.add_argument("--to", choices=["c", "f"], default="f", help="unit to convert to")
    parser.add_argument("--decimals", type=int, default=1, help="decimal places")
    return parser


def main(argv):
    """Run the tool and return an exit code."""
    args = build_parser().parse_args(argv)
    celsius = args.value if args.to == "f" else convert(args.value, "c")
    if celsius < ABSOLUTE_ZERO_C:
        print(f"error: {args.value} is below absolute zero", file=sys.stderr)
        return 1
    result = round(convert(args.value, args.to), args.decimals)
    if args.decimals == 0:
        result = int(result)  # show 100, not 100.0
    print(f"{result} {args.to.upper()}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
