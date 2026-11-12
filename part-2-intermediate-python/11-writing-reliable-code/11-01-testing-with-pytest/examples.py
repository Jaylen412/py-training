# 11-01 Testing with pytest
from pathlib import Path

import pytest

from basket import Basket

# Example 1: the code under test, used directly
basket = Basket()
basket.add("pen", 1.50, quantity=2)
basket.add("pad", 4.00)
print(basket.total())
basket.apply_code("SAVE10")
print(basket.total())

# Example 2: pytest.raises works as a plain `with` block too
with pytest.raises(ValueError) as error_info:
    basket.add("pen", -1)
print("Raised:", error_info.value)

# Example 3: pytest.approx compares floats with a tolerance
print(0.1 + 0.2 == pytest.approx(0.3))

# Example 4: run the test file and print pytest's report.
# -q is quiet mode, -v would list every test, and the -p option just stops
# pytest from creating a cache folder here.
checks = Path(__file__).parent / "basket_checks.py"
exit_code = pytest.main(["-v", "-p", "no:cacheprovider", str(checks)])
print("pytest exit code:", int(exit_code))
