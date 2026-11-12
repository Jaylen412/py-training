"""Exercises for 11-04 Context managers and logging."""
import logging
import time
from contextlib import contextmanager


class Timer:
    """Context manager that measures how long its block takes.

    Example:
        with Timer() as timer:
            do_something()
        print(timer.elapsed)
    """

    def __enter__(self):
        """Record the start time (time.perf_counter()) and return self.
        Also set self.elapsed = None until the block finishes."""
        raise NotImplementedError

    def __exit__(self, exc_type, exc_value, traceback):
        """Store the elapsed seconds in self.elapsed and return False, so
        exceptions are not hidden."""
        raise NotImplementedError


@contextmanager
def temporary_attribute(target, name, value):
    """Set target.<name> to `value` for the duration of the block, then put
    the old value back, even if the block raises. Yield `target`.
    Hint: getattr(target, name) reads an attribute by name and
    setattr(target, name, value) sets one.
    """
    raise NotImplementedError
    yield  # keeps this a generator function; remove it when you write yours


@contextmanager
def ignore_errors(*exception_types):
    """Run the block; if it raises one of `exception_types`, swallow the
    exception. Any other exception must still be raised.

    Example:
        with ignore_errors(KeyError):
            {}["missing"]       # no error escapes
    """
    raise NotImplementedError
    yield  # keeps this a generator function; remove it when you write yours


def process_orders(orders, logger):
    """`orders` is a list of (order_id, quantity) tuples.
    For each order whose quantity is not a positive whole number, call
    logger.warning with a message containing the order id. Then call
    logger.info once with a message containing "processed <n> of <total>".
    Return the list of valid order ids.

    Example: process_orders([(1, 2), (2, 0)], logger) returns [1] and logs a
    warning about order 2 and the info message "processed 1 of 2 orders"
    """
    raise NotImplementedError
