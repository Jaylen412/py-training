# 01-03 Virtual environments and pip
# This file checks which Python is running it. The `import` line loads a
# built-in tool called `sys`; you will learn how imports work in Module 08.
import sys

# Example 1: where is the Python program that is running this file?
print("Python program:", sys.executable)

# Example 2: which version is it?
print("Python version:", sys.version.split()[0])

# Example 3: is a virtual environment active?
# Inside a virtual environment, sys.prefix and sys.base_prefix are different.
print("Inside a virtual environment:", sys.prefix != sys.base_prefix)
