# 11-04 Context managers and logging
import logging
import sys
import time
from contextlib import contextmanager


# Example 1: a context manager class with __enter__ and __exit__
class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        return False   # do not hide exceptions


with Timer() as timer:
    total = sum(range(100_000))
print(total, timer.elapsed < 1)


# Example 2: __exit__ runs even when the block raises
class Announce:
    def __enter__(self):
        print("  entering")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print(f"  exiting (exception: {exc_type.__name__ if exc_type else None})")
        return False


try:
    with Announce():
        raise ValueError("something went wrong")
except ValueError as error:
    print("Caught:", error)


# Example 3: the same idea with @contextmanager and a generator
@contextmanager
def temporary_setting(settings, key, value):
    old_value = settings[key]
    settings[key] = value
    try:
        yield settings
    finally:
        settings[key] = old_value


config = {"debug": False}
with temporary_setting(config, "debug", True):
    print("inside:", config)
print("after:", config)

# Example 4: logging instead of print
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("orders")

logger.debug("not shown: below the INFO level")
logger.info("processing 3 orders")
logger.warning("order 2 has no address")
logger.error("order 3 failed to save")


# Example 5: log levels let you choose how much detail to see
def process(orders):
    processed = 0
    for order_id, quantity in orders:
        if quantity <= 0:
            logger.warning("skipping order %s: bad quantity %s", order_id, quantity)
            continue
        logger.debug("order %s ok", order_id)
        processed += 1
    logger.info("processed %d of %d orders", processed, len(orders))
    return processed


process([(1, 2), (2, 0), (3, 5)])
logger.setLevel(logging.WARNING)
process([(4, -1)])
