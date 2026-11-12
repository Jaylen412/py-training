# 12-02 Big-O intuition
# Timings depend on your computer, so your numbers will differ from the lesson.
import timeit


# Example 1: count the steps an algorithm takes as the input grows
def linear_search_steps(items, target):
    steps = 0
    for item in items:
        steps += 1
        if item == target:
            break
    return steps


def binary_search_steps(sorted_items, target):
    low, high = 0, len(sorted_items) - 1
    steps = 0
    while low <= high:
        steps += 1
        middle = (low + high) // 2
        if sorted_items[middle] == target:
            break
        if sorted_items[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return steps


def all_pairs_steps(items):
    steps = 0
    for first in items:
        for second in items:
            steps += 1
    return steps


print(f"{'n':>9} {'linear':>9} {'binary':>7} {'pairs':>14}")
for size in [10, 100, 1_000, 3_000]:
    items = list(range(size))
    target = size - 1   # worst case: the last item
    print(f"{size:>9} {linear_search_steps(items, target):>9} "
          f"{binary_search_steps(items, target):>7} {all_pairs_steps(items):>14}")

# Example 2: membership tests - list versus set versus dict
for size in [1_000, 100_000]:
    as_list = list(range(size))
    as_set = set(as_list)
    as_dict = dict.fromkeys(as_list)
    missing = -1
    list_time = timeit.timeit(lambda: missing in as_list, number=200) / 200
    set_time = timeit.timeit(lambda: missing in as_set, number=200) / 200
    dict_time = timeit.timeit(lambda: missing in as_dict, number=200) / 200
    print(f"n={size:>7}: list {list_time * 1e6:9.2f} us   set {set_time * 1e6:6.3f} us   dict {dict_time * 1e6:6.3f} us")


# Example 3: the same task in O(n^2) and O(n)
def has_duplicates_slow(items):
    for index, first in enumerate(items):
        for second in items[index + 1:]:
            if first == second:
                return True
    return False


def has_duplicates_fast(items):
    return len(set(items)) < len(items)


numbers = list(range(2_000))
slow = timeit.timeit(lambda: has_duplicates_slow(numbers), number=3) / 3
fast = timeit.timeit(lambda: has_duplicates_fast(numbers), number=3) / 3
print(f"slow: {slow * 1000:.1f} ms, fast: {fast * 1000:.3f} ms, ratio: {slow / fast:.0f}x")
