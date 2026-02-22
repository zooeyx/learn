"""Shared pytest configuration for all chapters."""

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.fixture
def chapter_dir(request):
    """Return the chapter directory containing the test file."""
    return Path(request.fspath).parent.parent


def run_exercise(name, chapter_path=None):
    """Run an exercise file and return (stdout, stderr, returncode)."""
    if chapter_path:
        script = Path(chapter_path) / f"{name}.py"
    else:
        script = Path(f"{name}.py")
    result = subprocess.run(
        [sys.executable, str(script)],
        capture_output=True, text=True, timeout=5,
    )
    return result.stdout, result.stderr, result.returncode
