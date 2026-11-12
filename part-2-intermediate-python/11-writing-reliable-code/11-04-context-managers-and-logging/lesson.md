# 11-04 Context managers and logging

## What you will learn

- Explain what `with` does, and write a context manager class with `__enter__` and `__exit__`.
- Write a context manager more simply with `contextlib.contextmanager`.
- Use the `logging` module instead of `print` for diagnostic messages.
- Choose log levels so you can control how much detail you see.

## Why it matters

You have used `with open(...)` since Module 06 to make sure files are closed. The same pattern guarantees clean-up for anything that must be undone: restoring a setting, releasing a lock, stopping a timer. Logging replaces scattered `print` calls with messages you can switch on and off, timestamp and send to a file. Long-running jobs, such as model training, report their progress through logs.

## Concepts

### What `with` does

A **context manager** is an object that sets something up at the start of a `with` block and tears it down at the end, **even if the block raises an exception**. Python calls two special methods:

- `__enter__(self)` runs at the start; its return value is what `as name` receives.
- `__exit__(self, exc_type, exc_value, traceback)` runs at the end. If the block raised, the three arguments describe the exception; otherwise they are all `None`. Returning `False` (or nothing) lets the exception continue; returning `True` would swallow it.

A timer is a simple example:

```python
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
```

```
4999950000 True
```

### Clean-up even on errors

The guarantee is what makes context managers valuable:

```python
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
```

```
  entering
  exiting (exception: ValueError)
Caught: something went wrong
```

`__exit__` ran before the exception reached the `except`. This is how `with open(...)` closes a file even when reading it fails.

### @contextmanager

Writing a class is often more than you need. **`contextlib.contextmanager`** turns a generator function (10-02) into a context manager: code before `yield` is the set-up, the yielded value is what `as` receives, and code after `yield` is the clean-up. Put the clean-up in `finally` so it runs even after an exception:

```python
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
```

```
inside: {'debug': True}
after: {'debug': False}
```

The "change something, then put it back" pattern is very common in tests and scripts.

### Why logging instead of print

`print` is fine for a program's actual output. For **diagnostic** messages (what the program is doing, warnings, errors), the **`logging`** module is better:

- Each message has a **level** of importance, and you choose the minimum level to show. Turn on detail while debugging; turn it off in normal use, without deleting any lines.
- Messages can be formatted with timestamps and the name of the part of the program that sent them.
- They can go to the screen, a file, or both.

### Basic logging

`logging.basicConfig` sets up logging once, near the start of a program. `logging.getLogger(name)` gets a named **logger**, conventionally `logging.getLogger(__name__)` in a module, so messages show which module sent them.

```python
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
```

```
INFO:orders:processing 3 orders
WARNING:orders:order 2 has no address
ERROR:orders:order 3 failed to save
```

(By default logs go to standard error; `stream=sys.stdout` sends them to normal output here so that they appear in order with the rest of the example. Add `%(asctime)s` to the format to include a timestamp.)

### Log levels

The levels, from least to most serious:

| Level | Use for |
|-------|---------|
| `DEBUG` | detailed information for diagnosing problems |
| `INFO` | confirmation that things are working as expected |
| `WARNING` | something unexpected, but the program carries on |
| `ERROR` | a problem that stopped some part from working |
| `CRITICAL` | a serious failure; the program may not continue |

Only messages at or above the configured level are shown. Changing the level changes how much you see, without touching the code that logs:

```python
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
```

```
WARNING:orders:skipping order 2: bad quantity 0
INFO:orders:processed 2 of 3 orders
WARNING:orders:skipping order 4: bad quantity -1
```

After `setLevel(logging.WARNING)`, the INFO summary disappeared but the warning still showed. Notice the style `logger.warning("... %s ...", value)`: logging fills in the `%s` placeholders itself, and only if the message will actually be shown.

## Common mistakes

- **Forgetting `finally` in a `@contextmanager`.** If the block raises, the code after `yield` never runs, and the setting is never restored.
- **Swallowing exceptions by accident.** An `__exit__` that returns `True` hides every error raised in the block. Return `False` unless hiding errors is the whole point.
- **Calling `basicConfig` after logging has already been used.** It does nothing the second time. Call it once, at the start of the program (usually in `main`).
- **Logging in a library with `print`.** Code that other programs import should log, not print, so that the program using it decides what to show.

## Try it

Add `filename="orders.log"` to the `basicConfig` call in `examples.py` and run it. Where did the messages go? Then change the level to `DEBUG` and look for the "order 1 ok" lines.

## Exercises

Open `ex_11_04.py`:

1. `Timer`: a context manager class that records elapsed time.
2. `temporary_attribute`: a `@contextmanager` that sets an attribute on an object and restores it afterwards.
3. `ignore_errors`: a `@contextmanager` that swallows the given exception types.
4. `process_orders`: validate orders, logging a warning for each bad one and an info summary.

Run the tests:

```
python -m pytest part-2-intermediate-python/11-writing-reliable-code/11-04-context-managers-and-logging
```

## Summary

- A context manager's `__enter__` runs at the start of `with` and `__exit__` at the end, even after an exception.
- `@contextmanager` builds one from a generator: set-up, `yield`, then clean-up in `finally`.
- Use `logging` for diagnostic messages; configure it once with `basicConfig`, and get loggers with `getLogger(__name__)`.
- Levels from DEBUG to CRITICAL control which messages appear.
- Pass values as arguments: `logger.warning("bad value %s", value)`.
