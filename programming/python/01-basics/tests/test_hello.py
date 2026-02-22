"""Tests for chapter 01 exercises."""

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


def test_hello_runs():
    _, _, code = run("hello")
    assert code == 0


def test_hello_output():
    stdout, _, _ = run("hello")
    assert "Hello, World!" in stdout


def test_types_runs():
    _, _, code = run("types")
    assert code == 0


def test_types_shows_types():
    stdout, _, _ = run("types")
    assert "int" in stdout
    assert "float" in stdout
    assert "str" in stdout
