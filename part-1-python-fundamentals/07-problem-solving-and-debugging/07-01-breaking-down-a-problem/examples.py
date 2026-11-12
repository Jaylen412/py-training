# 07-01 Breaking down a problem
# Problem: "Given a string, find the longest run of the same character
# repeated in a row, and report the character and the length of the run."


# Step 1: work some examples by hand, written as data
examples = [
    ("aaabbc", ("a", 3)),
    ("abbbbc", ("b", 4)),
    ("abc", ("a", 1)),
    ("", (None, 0)),
]


# Step 2: solve a simpler version first - just the length, no character
def longest_run_length(text):
    longest = 0
    current = 0
    previous = None
    for character in text:
        if character == previous:
            current += 1
        else:
            current = 1
        previous = character
        if current > longest:
            longest = current
    return longest


print(longest_run_length("aaabbc"), longest_run_length("abbbbc"), longest_run_length(""))


# Step 3: extend the simpler version to the full problem
def longest_run(text):
    """Return (character, length) of the longest run in `text`."""
    best_character = None
    longest = 0
    current = 0
    previous = None
    for character in text:
        if character == previous:
            current += 1
        else:
            current = 1
        previous = character
        if current > longest:
            longest = current
            best_character = character
    return best_character, longest


# Step 4: check every worked example
for text, expected in examples:
    result = longest_run(text)
    status = "ok" if result == expected else "WRONG"
    print(f"{text!r:10} -> {result}  expected {expected}  {status}")
