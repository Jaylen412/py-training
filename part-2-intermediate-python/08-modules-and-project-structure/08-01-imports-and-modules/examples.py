# 08-01 Imports and modules

# Example 1: import a whole module and use its contents with a dot
import math

print(math.pi)
print(math.sqrt(16))
print(math.floor(3.7), math.ceil(3.2))

# Example 2: import specific names
from math import pi, sqrt

print(round(pi * 2 ** 2, 2))
print(sqrt(81))

# Example 3: aliases with `as`
import statistics as stats

print(stats.mean([2, 4, 9]))
print(stats.median([5, 1, 3]))

# Example 4: importing your own module - temperatures.py sits next to this file.
# Its top-level code runs once, the first time it is imported.
import temperatures

print(temperatures.c_to_f(25))
print(temperatures.FREEZING_C)

# Example 5: importing again does not run the module again
import temperatures

print("Imported twice, but the message above appeared once")

# Example 6: what's inside a module?
print([name for name in dir(temperatures) if not name.startswith("_")])

# Example 7: __name__ is "__main__" in the file you run directly
print("In examples.py, __name__ is", repr(__name__))

# Example 8: where Python looks for modules - the script's folder comes first
import sys

print(sys.path[0].endswith("08-01-imports-and-modules"))
print(math.__name__, type(math))
