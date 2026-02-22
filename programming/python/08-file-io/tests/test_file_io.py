"""Tests for chapter 08 exercises."""

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


def test_read_file_runs():
    _, _, code = run("read_file")
    assert code == 0


def test_read_file_output():
    stdout, _, _ = run("read_file")
    assert "Alice" in stdout
    assert "Hello" in stdout
