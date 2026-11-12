import importlib
import math
import os
import time

import pytest

mod = importlib.import_module(
    "sol_12_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_12_02"
)


def test_linear_search_found():
    assert mod.linear_search([5, 8, 2], 8) == (1, 2)
    assert mod.linear_search([5, 8, 2], 5) == (0, 1)


def test_linear_search_missing_checks_everything():
    assert mod.linear_search([5, 8, 2], 9) == (-1, 3)
    assert mod.linear_search([], 1) == (-1, 0)


def test_binary_search_example():
    assert mod.binary_search([1, 3, 5, 7, 9], 7) == (3, 2)


@pytest.mark.parametrize("size", [1, 2, 10, 1000, 100_000])
def test_binary_search_finds_every_position_quickly(size):
    items = list(range(0, size * 2, 2))   # even numbers, sorted
    limit = math.floor(math.log2(size)) + 1
    for target_index in [0, size // 2, size - 1]:
        index, examined = mod.binary_search(items, items[target_index])
        assert index == target_index
        assert examined <= limit


def test_binary_search_missing():
    items = list(range(0, 2000, 2))
    index, examined = mod.binary_search(items, 7)
    assert index == -1
    assert examined <= math.floor(math.log2(len(items))) + 1
    assert mod.binary_search([], 3) == (-1, 0)


def test_common_elements():
    assert mod.common_elements([3, 1, 2, 2], [2, 3, 4]) == [2, 3]
    assert mod.common_elements([1], [2]) == []


def test_common_elements_is_fast_on_large_lists():
    first = list(range(200_000))
    second = list(range(100_000, 300_000))
    start = time.perf_counter()
    result = mod.common_elements(first, second)
    assert time.perf_counter() - start < 2
    assert len(result) == 100_000


def test_two_sum():
    assert mod.two_sum([2, 7, 11, 15], 9) == (0, 1)
    assert mod.two_sum([3, 2, 4], 6) == (1, 2)


def test_two_sum_repeated_value_and_missing():
    assert mod.two_sum([3, 3], 6) == (0, 1)
    assert mod.two_sum([1, 2, 3], 100) is None
    assert mod.two_sum([], 0) is None


def test_two_sum_is_fast_on_large_lists():
    numbers = list(range(200_000))
    start = time.perf_counter()
    assert mod.two_sum(numbers, 399_997) == (199_998, 199_999)
    assert time.perf_counter() - start < 2
