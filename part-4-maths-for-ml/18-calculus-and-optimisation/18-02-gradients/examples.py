# 18-02 Gradients
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)


# Example 1: a function of two inputs
def bowl(point):
    x, y = point
    return x ** 2 + 3 * y ** 2


print(bowl(np.array([1.0, 1.0])), bowl(np.array([0.0, 0.0])), bowl(np.array([2.0, -1.0])))


# Example 2: partial derivatives - change one input, hold the others still
def partial_derivative(function, point, index, step=1e-5):
    forward = point.astype(float).copy()
    backward = point.astype(float).copy()
    forward[index] += step
    backward[index] -= step
    return (function(forward) - function(backward)) / (2 * step)


point = np.array([1.0, 1.0])
print(round(partial_derivative(bowl, point, 0), 6), round(partial_derivative(bowl, point, 1), 6))


# Example 3: the gradient collects all the partial derivatives into a vector
def gradient(function, point):
    return np.array([partial_derivative(function, point, i) for i in range(len(point))])


print(np.round(gradient(bowl, point), 6))
print(np.round(gradient(bowl, np.array([2.0, -1.0])), 6))
print(np.round(gradient(bowl, np.array([0.0, 0.0])), 6))

# Example 4: the exact gradient of the bowl: (2x, 6y)
exact = lambda p: np.array([2 * p[0], 6 * p[1]])
print(exact(point), exact(np.array([2.0, -1.0])))

# Example 5: the gradient points uphill; its negative points downhill
step = 0.1
uphill = point + step * gradient(bowl, point)
downhill = point - step * gradient(bowl, point)
print(round(bowl(point), 3), round(bowl(uphill), 3), round(bowl(downhill), 3))

# Example 6: drawing the gradient field on a contour plot
xs, ys = np.meshgrid(np.linspace(-3, 3, 200), np.linspace(-2, 2, 200))
heights = xs ** 2 + 3 * ys ** 2
fig, ax = plt.subplots(figsize=(7, 5))
contours = ax.contour(xs, ys, heights, levels=12, cmap="viridis")
ax.clabel(contours, fontsize=7)
arrow_x, arrow_y = np.meshgrid(np.linspace(-2.5, 2.5, 7), np.linspace(-1.5, 1.5, 5))
ax.quiver(arrow_x, arrow_y, -2 * arrow_x, -6 * arrow_y, color="tab:red", alpha=0.7)
ax.set_aspect("equal")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Contours of x² + 3y², with arrows pointing downhill (−gradient)")
fig.savefig(FIGURES / "gradient_field.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 7: gradient size tells you how steep it is
for p in [np.array([0.1, 0.1]), np.array([1.0, 1.0]), np.array([3.0, 2.0])]:
    print(p, round(float(np.linalg.norm(exact(p))), 3))
