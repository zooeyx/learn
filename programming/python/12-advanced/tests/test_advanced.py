"""Tests for chapter 12 exercises."""

import subprocess
import sys
from pathlib import Path

CHAPTER = Path(__file__).parent.parent


def run(name):
    r = subprocess.run(
        [sys.executable, str(CHAPTER / f"{name}.py")],
        capture_output=True, text=True, timeout=5,
    )
    return r.stdout, r.stderr, r.returncode


def test_comprehensions_runs():
    _, _, code = run("comprehensions")
    assert code == 0


def test_comprehensions_output():
    stdout, _, _ = run("comprehensions")
    assert "Squares:" in stdout
    assert "Flattened:" in stdout
