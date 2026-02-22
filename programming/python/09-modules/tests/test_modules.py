"""Tests for chapter 09 exercises."""

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


def test_imports_runs():
    _, _, code = run("imports")
    assert code == 0


def test_imports_output():
    stdout, _, _ = run("imports")
    assert "math.sqrt(16) = 4.0" in stdout
    assert "__name__" in stdout
