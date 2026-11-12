"""Solutions for 17-02 Dot product and similarity."""
import numpy as np


def cosine_similarity(first, second):
    """Return the cosine similarity of two vectors."""
    lengths = np.linalg.norm(first) * np.linalg.norm(second)
    if lengths == 0:
        raise ValueError("cosine similarity is undefined for a zero vector")
    return float(first @ second / lengths)


def angle_between(first, second):
    """Return the angle between two vectors in degrees."""
    cosine = np.clip(cosine_similarity(first, second), -1.0, 1.0)
    return float(np.degrees(np.arccos(cosine)))


def most_similar(query, documents):
    """Return the index of the row most similar in direction to `query`."""
    similarities = documents @ query / (np.linalg.norm(documents, axis=1) * np.linalg.norm(query))
    return int(similarities.argmax())


def project(vector, onto):
    """Return the projection of `vector` onto `onto`."""
    onto = np.asarray(onto, dtype=float)
    return (vector @ onto) / (onto @ onto) * onto


def are_orthogonal(first, second, tolerance=1e-9):
    """Return True if the vectors are at right angles."""
    return bool(abs(first @ second) <= tolerance)
