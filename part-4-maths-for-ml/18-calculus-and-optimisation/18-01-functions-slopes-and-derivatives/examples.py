# 18-01 Functions, slopes and derivatives
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)


# Example 1: the slope of a straight line - rise over run
def slope(point_a, point_b):
    (x1, y1), (x2, y2) = point_a, point_b
    return (y2 - y1) / (x2 - x1)


print(slope((1, 3), (4, 9)))
print(slope((0, 5), (2, 1)))


# Example 2: a curve has a different slope at every point
def f(x):
    return x ** 2


for x1, x2 in [(1, 3), (1, 2), (1, 1.1), (1, 1.001)]:
    print(f"slope between x={x1} and x={x2}: {slope((x1, f(x1)), (x2, f(x2))):.4f}")


# Example 3: a numerical derivative with a small step
def derivative(function, x, step=1e-5):
    return (function(x + step) - function(x - step)) / (2 * step)


for x in [-2, 0, 1, 3]:
    print(x, round(derivative(f, x), 6))

# Example 4: the tangent line touches the curve and has the derivative's slope
x0 = 1.0
tangent_slope = derivative(f, x0)
xs = np.linspace(-1, 3, 100)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(xs, f(xs), label="f(x) = x²")
ax.plot(xs, f(x0) + tangent_slope * (xs - x0), "--", label=f"tangent at x = 1 (slope {tangent_slope:.0f})")
ax.scatter([x0], [f(x0)], color="black", zorder=3)
ax.set_ylim(-2, 9)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.set_title("The derivative is the slope of the tangent line")
fig.savefig(FIGURES / "tangent.png", dpi=100, bbox_inches="tight")
plt.close(fig)


# Example 5: the sign of the derivative says which way is downhill
def g(x):
    return (x - 3) ** 2 + 1


for x in [0, 2, 3, 5]:
    d = derivative(g, x)
    direction = "decreasing" if d < 0 else "increasing" if d > 0 else "flat (minimum)"
    print(f"x={x}: derivative {d:+.3f}, function is {direction}")

# Example 6: rules you will see - the power rule
cube = lambda x: x ** 3
print(round(derivative(cube, 2.0), 4), 3 * 2.0 ** 2)
