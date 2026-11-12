# 17-02 Dot product and similarity
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)

# Example 1: the dot product - multiply matching components and add
a = np.array([3.0, 4.0])
b = np.array([2.0, 1.0])
print(a[0] * b[0] + a[1] * b[1], a @ b, np.dot(a, b))

# Example 2: the dot product of a vector with itself is its length squared
print(a @ a, np.linalg.norm(a) ** 2)

# Example 3: the sign tells you the rough direction
right = np.array([1.0, 0.0])
for other in [np.array([2.0, 1.0]), np.array([0.0, 3.0]), np.array([-2.0, 1.0])]:
    print(other, right @ other)


# Example 4: the angle between two vectors
def angle_degrees(first, second):
    cosine = first @ second / (np.linalg.norm(first) * np.linalg.norm(second))
    return np.degrees(np.arccos(np.clip(cosine, -1, 1)))


print(round(angle_degrees(a, b), 1))
print(angle_degrees(right, np.array([0.0, 3.0])))


# Example 5: cosine similarity - direction, ignoring length
def cosine_similarity(first, second):
    return first @ second / (np.linalg.norm(first) * np.linalg.norm(second))


print(round(cosine_similarity(a, 10 * a), 3))
print(round(cosine_similarity(a, -a), 3))

# Example 6: comparing documents by word counts
words = ["goal", "match", "team", "vote", "election"]
football = np.array([3, 2, 4, 0, 0])
match_report = np.array([6, 5, 7, 0, 1])
politics = np.array([0, 0, 1, 4, 5])
print(round(cosine_similarity(football, match_report), 3))
print(round(cosine_similarity(football, politics), 3))
print(round(np.linalg.norm(football - match_report), 2), round(np.linalg.norm(football - politics), 2))

# Example 7: projection - the shadow of one vector on another
direction = np.array([1.0, 0.0])
shadow_length = a @ direction / np.linalg.norm(direction)
projection = shadow_length * direction / np.linalg.norm(direction)
print(shadow_length, projection)

fig, ax = plt.subplots(figsize=(5, 4))
ax.quiver(0, 0, *a, angles="xy", scale_units="xy", scale=1, color="tab:blue", label="a = (3, 4)")
ax.quiver(0, 0, *(4 * direction), angles="xy", scale_units="xy", scale=1, color="grey", alpha=0.5, label="direction")
ax.quiver(0, 0, *projection, angles="xy", scale_units="xy", scale=1, color="tab:orange", label="projection of a")
ax.plot([a[0], projection[0]], [a[1], projection[1]], "k:", linewidth=1)
ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.5, 4.5)
ax.set_aspect("equal")
ax.legend(loc="upper left")
ax.set_title("Projecting a onto the x direction")
fig.savefig(FIGURES / "projection.png", dpi=100, bbox_inches="tight")
plt.close(fig)
