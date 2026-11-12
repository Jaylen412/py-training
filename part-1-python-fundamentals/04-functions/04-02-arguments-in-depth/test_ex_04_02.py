import importlib
import os

mod = importlib.import_module(
    "sol_04_02" if os.environ.get("COURSE_SOLUTIONS") else "ex_04_02"
)


def test_greet_default():
    assert mod.greet("Ada") == "Hello, Ada!"


def test_greet_custom():
    assert mod.greet("Ada", greeting="Hi") == "Hi, Ada!"
    assert mod.greet("Ada", "Good morning") == "Good morning, Ada!"


def test_power_default_squares():
    assert mod.power(3) == 9


def test_power_custom_exponent():
    assert mod.power(2, 10) == 1024
    assert mod.power(5, exponent=0) == 1


def test_full_name_without_middle():
    assert mod.full_name("Ada", "Lovelace") == "Ada Lovelace"


def test_full_name_with_middle():
    assert mod.full_name("Ada", "Lovelace", middle="King") == "Ada King Lovelace"


def test_repeat_text_defaults():
    assert mod.repeat_text("ha") == "ha ha"


def test_repeat_text_custom():
    assert mod.repeat_text("ha", times=3, separator="-") == "ha-ha-ha"
    assert mod.repeat_text("x", separator="", times=4) == "xxxx"


def test_repeat_text_edge_cases():
    assert mod.repeat_text("ha", times=1) == "ha"
    assert mod.repeat_text("ha", times=0) == ""


def test_add_item_to_existing_basket():
    assert mod.add_item("milk", ["bread"]) == ["bread", "milk"]


def test_add_item_new_basket_each_time():
    first = mod.add_item("apple")
    second = mod.add_item("bread")
    assert first == ["apple"]
    assert second == ["bread"]
