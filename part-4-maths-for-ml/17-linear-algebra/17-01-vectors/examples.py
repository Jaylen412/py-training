# 17-01 Vectors
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Example 1: a vector is an ordered list of numbers
house = np.array([120.0, 3.0, 15.0])   # floor area, bedrooms, age
point = np.array([3.0, 4.0])
print(house, house.shape, point.shape)

# Example 2: addition - add matching components
move = np.array([1.0, -2.0])
print(point + move)

# Example 3: scaling - multiply every component
print(2 * point, -0.5 * point)

# Example 4: drawing vectors as arrows from the origin
fig, ax = plt.subplots(figsize=(5, 5))
for vector, colour, label in [(point, "tab:blue", "a = (3, 4)"),
                              (move, "tab:orange", "b = (1, -2)"),
                              (point + move, "tab:green", "a + b = (4, 2)")]:
    ax.quiver(0, 0, vector[0], vector[1], angles="xy", scale_units="xy", scale=1, color=colour, label=label)
ax.quiver(point[0], point[1], move[0], move[1], angles="xy", scale_units="xy", scale=1,
          color="tab:orange", alpha=0.4)
ax.set_xlim(-1, 5)
ax.set_ylim(-3, 5)
ax.set_aspect("equal")
ax.axhline(0, color="grey", linewidth=0.5)
ax.axvline(0, color="grey", linewidth=0.5)
ax.legend(loc="upper left")
ax.set_title("Adding vectors: put them head to tail")
fig.savefig(FIGURES / "vector_addition.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: length (the norm) - Pythagoras in any number of dimensions
print(np.sqrt((point ** 2).sum()))
print(np.linalg.norm(point))
print(round(np.linalg.norm(house), 2))

# Example 6: a unit vector has length 1 and keeps the direction
unit = point / np.linalg.norm(point)
print(unit, np.linalg.norm(unit))

# Example 7: distance between two points is the length of their difference
a = np.array([1.0, 2.0])
b = np.array([4.0, 6.0])
print(np.linalg.norm(b - a))

# Example 8: distances between houses - why scale matters
houses = np.array([
    [120.0, 3.0, 15.0],
    [118.0, 1.0, 80.0],
    [160.0, 3.0, 14.0],
])
print(np.round(np.linalg.norm(houses - houses[0], axis=1), 2))
