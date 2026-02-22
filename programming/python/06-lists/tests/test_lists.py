"""Tests for chapter 06 exercises."""

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


def test_list_basics_runs():
    _, _, code = run("list_basics")
    assert code == 0


def test_list_basics_output():
    stdout, _, _ = run("list_basics")
    assert "numbers:" in stdout
    assert "Squares:" in stdout
