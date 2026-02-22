"""Tests for chapter 07 exercises."""

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


def test_dictionaries_runs():
    _, _, code = run("dictionaries")
    assert code == 0


def test_dictionaries_output():
    stdout, _, _ = run("dictionaries")
    assert "person:" in stdout
    assert "squares:" in stdout
