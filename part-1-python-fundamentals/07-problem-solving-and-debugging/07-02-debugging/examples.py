# 07-02 Debugging


# Example 1: a buggy function - it should average the numbers
def average_buggy(numbers):
    total = 0
    for index in range(1, len(numbers)):
        total += numbers[index]
    return total / len(numbers)


print(average_buggy([10, 20, 30]))   # expected 20.0


# Example 2: print debugging - show the values as the loop runs
def average_traced(numbers):
    total = 0
    for index in range(1, len(numbers)):
        total += numbers[index]
        print(f"  index={index} value={numbers[index]} total={total}")
    return total / len(numbers)


print(average_traced([10, 20, 30]))


# Example 3: the fix - loop over the items themselves
def average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


print(average([10, 20, 30]))


# Example 4: bisecting - check the intermediate results of a pipeline
def clean(text):
    return text.strip().lower()


def to_words(text):
    return text.split(" ")


def count_words(text):
    return len(to_words(clean(text)))


sentence = "  The  quick fox "
print(count_words(sentence))            # expected 3
print(repr(clean(sentence)))            # is the cleaning step right?
print(to_words(clean(sentence)))        # is the splitting step right?


def to_words_fixed(text):
    return text.split()


print(len(to_words_fixed(clean(sentence))))

# Example 5: in your own code, breakpoint() pauses here and opens the
# debugger. It is commented out so that this file runs straight through.
# breakpoint()
