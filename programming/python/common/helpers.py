"""Helpers — Python equivalent of debug.h for learning exercises."""

import sys
import time
import functools

_DEBUG = "--debug" in sys.argv


def debug(*args):
    """Print to stderr, only when --debug flag is passed."""
    if _DEBUG:
        print("[DEBUG]", *args, file=sys.stderr)


def check(condition, msg="Assertion failed"):
    """Assert with a clear error message."""
    if not condition:
        print(f"FAIL: {msg}", file=sys.stderr)
        sys.exit(1)
    debug(f"PASS: {msg}")


def check_equal(actual, expected, label=""):
    """Equality assertion with formatted diff."""
    if actual != expected:
        prefix = f"{label}: " if label else ""
        print(f"FAIL: {prefix}expected {expected!r}, got {actual!r}", file=sys.stderr)
        sys.exit(1)
    debug(f"PASS: {label or 'check_equal'}")


def section(title):
    """Print a section separator for exercise output."""
    print(f"\n{'='*3} {title} {'='*3}")


def timed(func):
    """Decorator that prints execution time."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] {elapsed:.4f}s")
        return result
    return wrapper
