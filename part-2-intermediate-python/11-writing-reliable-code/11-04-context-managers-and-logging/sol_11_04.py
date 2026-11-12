"""Solutions for 11-04 Context managers and logging."""
import logging
import time
from contextlib import contextmanager


class Timer:
    """Context manager that measures how long its block takes."""

    def __enter__(self):
        self.elapsed = None
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False


@contextmanager
def temporary_attribute(target, name, value):
    """Set an attribute for the duration of the block, then restore it."""
    old_value = getattr(target, name)
    setattr(target, name, value)
    try:
        yield target
    finally:
        setattr(target, name, old_value)


@contextmanager
def ignore_errors(*exception_types):
    """Swallow the given exception types raised in the block."""
    try:
        yield
    except exception_types:  # a tuple of types catches any of them
        pass


def process_orders(orders, logger):
    """Return valid order ids, logging warnings and a summary."""
    valid_ids = []
    for order_id, quantity in orders:
        if not isinstance(quantity, int) or quantity < 1:
            logger.warning("order %s has invalid quantity %r", order_id, quantity)
            continue
        valid_ids.append(order_id)
    logger.info("processed %d of %d orders", len(valid_ids), len(orders))
    return valid_ids
