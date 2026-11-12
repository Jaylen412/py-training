# 18-04 Gradient descent
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

FIGURES = Path(__file__).parent / "figures"
FIGURES.mkdir(exist_ok=True)


# Example 1: one variable - minimise f(x) = (x - 3)² + 1
def f(x):
    return (x - 3) ** 2 + 1


def f_derivative(x):
    return 2 * (x - 3)


x = 0.0
learning_rate = 0.1
for step in range(1, 26):
    x = x - learning_rate * f_derivative(x)
    if step in (1, 2, 3, 10, 25):
        print(f"step {step:>2}: x = {x:.4f}, f(x) = {f(x):.4f}")


# Example 2: the learning rate matters
def run(learning_rate, steps=20, start=0.0):
    xs = [start]
    for _ in range(steps):
        xs.append(xs[-1] - learning_rate * f_derivative(xs[-1]))
    return np.array(xs)


for rate in [0.01, 0.1, 0.9, 1.1]:
    path = run(rate)
    print(f"learning rate {rate}: x after 20 steps = {path[-1]:.4f}")

fig, ax = plt.subplots(figsize=(7, 4))
grid = np.linspace(-1.5, 7.5, 200)
ax.plot(grid, f(grid), color="lightgrey")
for rate, colour in [(0.01, "tab:blue"), (0.1, "tab:green"), (0.9, "tab:orange")]:
    path = run(rate, steps=12)
    ax.plot(path, f(path), "o-", color=colour, markersize=4, label=f"learning rate {rate}")
ax.set_ylim(0, 12)
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.legend()
ax.set_title("Too small crawls, well chosen converges, too large zig-zags")
fig.savefig(FIGURES / "learning_rates.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 3: two parameters - fit a line y = w x + b by gradient descent
hours = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
scores = np.array([52.0, 55.0, 61.0, 64.0, 70.0, 72.0])


def mse(w, b):
    return np.mean((scores - (w * hours + b)) ** 2)


def mse_gradient(w, b):
    errors = (w * hours + b) - scores
    return 2 * np.mean(errors * hours), 2 * np.mean(errors)


w, b = 0.0, 0.0
learning_rate = 0.02
history = []
for epoch in range(5001):
    dw, db = mse_gradient(w, b)
    w -= learning_rate * dw
    b -= learning_rate * db
    history.append(mse(w, b))
    if epoch in (0, 10, 100, 1000, 5000):
        print(f"epoch {epoch:>4}: w = {w:.3f}, b = {b:.3f}, loss = {history[-1]:.3f}")

# Example 4: check against the exact least-squares answer (17-04)
X = np.column_stack([np.ones_like(hours), hours])
exact, *_ = np.linalg.lstsq(X, scores, rcond=None)
print("least squares: b = %.3f, w = %.3f" % (exact[0], exact[1]))

fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(history)
ax.set_yscale("log")
ax.set_xlabel("Epoch")
ax.set_ylabel("Mean squared error (log scale)")
ax.set_title("The loss falls quickly, then levels off")
fig.savefig(FIGURES / "loss_history.png", dpi=100, bbox_inches="tight")
plt.close(fig)

# Example 5: a learning rate that is too large makes the loss explode
w, b = 0.0, 0.0
for epoch in range(6):
    dw, db = mse_gradient(w, b)
    w -= 0.1 * dw
    b -= 0.1 * db
    print(f"epoch {epoch}: loss = {mse(w, b):.3e}")
