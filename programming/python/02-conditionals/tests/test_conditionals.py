"""Tests for chapter 02 exercises."""

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


def test_if_else_runs():
    _, _, code = run("if_else")
    assert code == 0


def test_if_else_output():
    stdout, _, _ = run("if_else")
    assert "Grade" in stdout
    assert "truthy" in stdout or "falsy" in stdout
