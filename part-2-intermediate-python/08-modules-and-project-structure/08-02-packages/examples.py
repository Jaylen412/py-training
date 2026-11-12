# 08-02 Packages
# The folder shop/ next to this file is a package:
#   shop/__init__.py   runs when the package is imported
#   shop/pricing.py    a module inside the package
#   shop/cart.py       another module, which imports from pricing

# Example 1: import a module from inside a package
import shop.pricing

print(shop.pricing.with_tax(10))

# Example 2: from package.module import name
from shop.pricing import apply_discount

print(apply_discount(50, 0.1))

# Example 3: from package import module
from shop import cart

print(cart.cart_total([10, 20]))

# Example 4: names that __init__.py imports are available on the package itself
import shop

print(shop.cart_total([5]))
print(shop.VERSION)

# Example 5: a package is a module too - it has a __name__ and a file
print(shop.__name__, shop.pricing.__name__)
print(shop.__file__.endswith("__init__.py"))
