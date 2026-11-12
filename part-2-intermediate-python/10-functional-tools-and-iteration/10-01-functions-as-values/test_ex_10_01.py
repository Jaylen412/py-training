import importlib
import os

mod = importlib.import_module(
    "sol_10_01" if os.environ.get("COURSE_SOLUTIONS") else "ex_10_01"
)


def test_apply_twice():
    assert mod.apply_twice(lambda n: n + 3, 10) == 16
    assert mod.apply_twice(str.upper, "hi") == "HI"


def test_apply_twice_order_matters():
    assert mod.apply_twice(lambda text: text + "!", "go") == "go!!"


def test_sort_by_length():
    assert mod.sort_by_length(["pear", "fig", "kiwi", "apple"]) == ["fig", "kiwi", "pear", "apple"]


def test_sort_by_length_empty_and_does_not_change_input():
    words = ["bb", "a"]
    assert mod.sort_by_length(words) == ["a", "bb"]
    assert words == ["bb", "a"]
    assert mod.sort_by_length([]) == []


def test_sort_people():
    people = [
        {"name": "Ada", "age": 36},
        {"name": "Alan", "age": 41},
        {"name": "Grace", "age": 36},
    ]
    assert [person["name"] for person in mod.sort_people(people)] == ["Alan", "Ada", "Grace"]


def test_sort_people_same_age_alphabetical():
    people = [{"name": "Zed", "age": 20}, {"name": "Amy", "age": 20}]
    assert [person["name"] for person in mod.sort_people(people)] == ["Amy", "Zed"]


def test_longest_by():
    assert mod.longest_by(["a", "abc", "ab"], len) == "abc"
    assert mod.longest_by([3, -7, 5], abs) == -7


def test_longest_by_tie_and_empty():
    assert mod.longest_by(["ab", "cd"], len) == "ab"
    assert mod.longest_by([], len) is None


def test_count_matching():
    assert mod.count_matching([1, 2, 3, 4], lambda n: n % 2 == 0) == 2


def test_count_matching_none_and_empty():
    assert mod.count_matching(["a", "b"], str.isdigit) == 0
    assert mod.count_matching([], bool) == 0
