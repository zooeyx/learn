"""Tests for chapter 03 exercises."""

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


def test_while_loops_runs():
    _, _, code = run("while_loops")
    assert code == 0


def test_while_loops_output():
    stdout, _, _ = run("while_loops")
    assert "Count: 0" in stdout
    assert "Found: 7" in stdout
