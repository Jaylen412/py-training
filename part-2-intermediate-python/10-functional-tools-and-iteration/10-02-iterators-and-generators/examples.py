# 10-02 Iterators and generators
import sys

# Example 1: iter() and next() - what a for loop does underneath
letters = ["a", "b", "c"]
iterator = iter(letters)
print(next(iterator))
print(next(iterator))
print(next(iterator))
try:
    next(iterator)
except StopIteration:
    print("StopIteration: no more items")

# Example 2: an iterator can only be used once
squares = map(lambda number: number ** 2, [1, 2, 3])
print(list(squares))
print(list(squares))


# Example 3: a generator function uses yield
def countdown(start):
    print("  (starting)")
    while start > 0:
        yield start
        start -= 1
    print("  (finished)")


generator = countdown(3)
print(type(generator).__name__)
for number in generator:
    print(number)


# Example 4: generators pause at each yield
generator = countdown(2)
print(next(generator))
print("doing something else")
print(next(generator))


# Example 5: a generator for a sequence that never ends
def even_numbers():
    number = 0
    while True:
        yield number
        number += 2


evens = even_numbers()
print([next(evens) for _ in range(5)])

# Example 6: generator expressions use round brackets
lazy_squares = (number ** 2 for number in range(1_000_000))
print(next(lazy_squares), next(lazy_squares), next(lazy_squares))
print(sum(number ** 2 for number in range(10)))

# Example 7: laziness saves memory
as_list = [number for number in range(1_000_000)]
as_generator = (number for number in range(1_000_000))
print(sys.getsizeof(as_list) > 1_000_000, sys.getsizeof(as_generator) < 1_000)


# Example 8: a pipeline of generators processes one item at a time
def read_lines(text):
    for line in text.splitlines():
        yield line


def non_blank(lines):
    for line in lines:
        if line.strip():
            yield line.strip()


def as_numbers(lines):
    for line in lines:
        yield float(line)


raw = "3.5\n\n 4.5\n2\n"
print(sum(as_numbers(non_blank(read_lines(raw)))))
