"""Tests for chapter 10 exercises."""

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


def test_first_class_runs():
    _, _, code = run("first_class")
    assert code == 0


def test_first_class_output():
    stdout, _, _ = run("first_class")
    assert "Rex" in stdout
    assert "Woof" in stdout
