"""Tests for chapter 11 exercises."""

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


def test_inheritance_runs():
    _, _, code = run("inheritance")
    assert code == 0


def test_inheritance_output():
    stdout, _, _ = run("inheritance")
    assert "Circle" in stdout
    assert "Rectangle" in stdout
    assert "MRO" in stdout
