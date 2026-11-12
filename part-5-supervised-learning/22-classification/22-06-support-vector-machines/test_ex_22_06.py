import importlib
import os

import numpy as np
import pytest
from sklearn.datasets import make_blobs, make_moons
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

mod = importlib.import_module(
    "sol_22_06" if os.environ.get("COURSE_SOLUTIONS") else "ex_22_06"
)

X_MOONS, Y_MOONS = make_moons(n_samples=300, noise=0.2, random_state=42)
PARTS = train_test_split(X_MOONS, Y_MOONS, test_size=0.3, random_state=42, stratify=Y_MOONS)


def test_svm_test_accuracy_kernels():
    assert mod.svm_test_accuracy(*PARTS, kernel="linear") == 0.833
    assert mod.svm_test_accuracy(*PARTS) == 0.922


def test_svm_test_accuracy_large_gamma_overfits():
    assert mod.svm_test_accuracy(*PARTS, gamma=1000) == 0.689


def test_support_vector_count():
    X, y = make_blobs(n_samples=60, centers=2, cluster_std=1.2, random_state=6)
    assert mod.support_vector_count(SVC(kernel="linear", C=1.0).fit(X, y)) == 3
    assert mod.support_vector_count(SVC(kernel="linear", C=0.01).fit(X, y)) == 22


def test_support_vector_count_type():
    X, y = make_blobs(n_samples=20, centers=2, random_state=0)
    assert type(mod.support_vector_count(SVC().fit(X, y))) is int


def test_best_gamma():
    assert mod.best_gamma(*PARTS, [0.1, 1, 1000]) == 1


def test_best_gamma_single():
    assert mod.best_gamma(*PARTS, [5]) == 5


def test_add_squared_distance():
    np.testing.assert_allclose(mod.add_squared_distance(np.array([[3.0, 4.0]])), [[3, 4, 25]])


def test_add_squared_distance_helps_linear_svm():
    X_train, X_test, y_train, y_test = PARTS
    lifted = mod.svm_test_accuracy(
        mod.add_squared_distance(X_train), mod.add_squared_distance(X_test), y_train, y_test, kernel="linear"
    )
    assert lifted == pytest.approx(0.844, abs=1e-3)
    assert mod.add_squared_distance(X_train).shape == (210, 3)
