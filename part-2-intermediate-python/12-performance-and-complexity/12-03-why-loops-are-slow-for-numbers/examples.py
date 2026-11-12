# 12-03 Why loops are slow for numbers
# Timings depend on your computer, so your numbers will differ from the lesson.
import math
import random
import timeit

rng = random.Random(42)
values = [rng.random() for _ in range(1_000_000)]


# Example 1: summing a million numbers with a Python loop
def loop_sum(numbers):
    total = 0.0
    for number in numbers:
        total += number
    return total


# Example 2: the built-in sum, and math.fsum
loop_time = timeit.timeit(lambda: loop_sum(values), number=5) / 5
sum_time = timeit.timeit(lambda: sum(values), number=5) / 5
fsum_time = timeit.timeit(lambda: math.fsum(values), number=5) / 5
print(f"loop:      {loop_time * 1000:6.1f} ms  -> {loop_sum(values):.4f}")
print(f"sum():     {sum_time * 1000:6.1f} ms  -> {sum(values):.4f}")
print(f"math.fsum: {fsum_time * 1000:6.1f} ms  -> {math.fsum(values):.4f}")
print(f"the loop is {loop_time / sum_time:.1f}x slower than sum()")


# Example 3: element-wise maths on two lists - a typical data-science operation
def scale_and_add_loop(first, second, factor):
    result = []
    for index in range(len(first)):
        result.append(first[index] * factor + second[index])
    return result


def scale_and_add_comprehension(first, second, factor):
    return [a * factor + b for a, b in zip(first, second)]


other = [rng.random() for _ in range(1_000_000)]
loop_time = timeit.timeit(lambda: scale_and_add_loop(values, other, 2.0), number=3) / 3
comp_time = timeit.timeit(lambda: scale_and_add_comprehension(values, other, 2.0), number=3) / 3
print(f"index loop:    {loop_time * 1000:6.1f} ms")
print(f"comprehension: {comp_time * 1000:6.1f} ms")

# Example 4: why - every Python number is a full object
print(type(values[0]).__name__, values[0].__sizeof__(), "bytes for one float object")
print("a list of 1,000,000 floats points to 1,000,000 separate objects")


# Example 5: a mean and a dot product, written by hand
def mean(numbers):
    return sum(numbers) / len(numbers)


def dot_product(first, second):
    return sum(a * b for a, b in zip(first, second))


print(f"mean: {mean(values):.4f}")
print(f"dot product: {dot_product(values, other):.1f}")
dot_time = timeit.timeit(lambda: dot_product(values, other), number=3) / 3
print(f"dot product of two 1,000,000-long lists: {dot_time * 1000:.1f} ms")
