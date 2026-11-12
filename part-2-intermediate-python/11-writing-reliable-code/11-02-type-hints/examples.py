# 11-02 Type hints
from collections.abc import Callable, Iterable
from typing import Optional, get_type_hints


# Example 1: hints on parameters and the return value
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


print(average([1.0, 2.0, 6.0]))
print(average.__annotations__)


# Example 2: collection types say what is inside
def count_words(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def min_max(numbers: list[int]) -> tuple[int, int]:
    return min(numbers), max(numbers)


print(count_words("a b a"))
print(min_max([4, 1, 9]))


# Example 3: Optional - a value that might be None
def find_index(items: list[str], target: str) -> Optional[int]:
    for index, item in enumerate(items):
        if item == target:
            return index
    return None


def find_index_new_style(items: list[str], target: str) -> int | None:
    return items.index(target) if target in items else None


print(find_index(["a", "b"], "b"), find_index(["a", "b"], "z"))
print(find_index_new_style(["a", "b"], "z"))


# Example 4: Callable for functions, Iterable for "anything you can loop over"
def apply_to_all(function: Callable[[int], int], values: Iterable[int]) -> list[int]:
    return [function(value) for value in values]


print(apply_to_all(abs, (-1, 2, -3)))

# Example 5: hints are not checked when the code runs
print(average([1, 2]))
try:
    count_words(["not", "a", "string"])
except AttributeError as error:
    print("AttributeError:", error)

# Example 6: tools can read the hints
print(get_type_hints(find_index))
