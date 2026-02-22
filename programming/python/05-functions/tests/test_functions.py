"""Tests for chapter 05 exercises."""

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


def test_functions_runs():
    _, _, code = run("functions")
    assert code == 0


def test_functions_output():
    stdout, _, _ = run("functions")
    assert "Hello, Zed!" in stdout
    assert "double(5) = 10" in stdout
