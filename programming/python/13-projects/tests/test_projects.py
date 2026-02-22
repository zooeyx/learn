"""Tests for chapter 13 projects."""

import subprocess
import sys
from pathlib import Path

CHAPTER = Path(__file__).parent.parent


def run(project, script="main"):
    r = subprocess.run(
        [sys.executable, str(CHAPTER / project / f"{script}.py")],
        capture_output=True, text=True, timeout=5,
    )
    return r.stdout, r.stderr, r.returncode


def test_todo_cli_runs():
    _, _, code = run("todo-cli")
    assert code == 0


def test_text_adventure_runs():
    _, _, code = run("text-adventure")
    assert code == 0


def test_web_scraper_runs():
    _, _, code = run("web-scraper")
    assert code == 0


def test_api_client_runs():
    _, _, code = run("api-client")
    assert code == 0
