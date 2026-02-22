"""Todo CLI — command-line task manager.

Usage:
    python3 main.py add "Task description"
    python3 main.py list
    python3 main.py done <id>
    python3 main.py delete <id>
"""

import json
import sys
from pathlib import Path

TODO_FILE = Path(__file__).parent / "todos.json"


def load_todos():
    """Load todos from JSON file."""
    # TODO: Read TODO_FILE if it exists, return list of dicts
    # Hint: if TODO_FILE.exists(): return json.loads(TODO_FILE.read_text())
    return []


def save_todos(todos):
    """Save todos to JSON file."""
    # TODO: Write todos list to TODO_FILE as JSON
    pass


def add_todo(todos, description):
    """Add a new todo item."""
    # TODO: Create a dict with id, description, done status
    # Hint: new_id = max((t["id"] for t in todos), default=0) + 1
    pass


def list_todos(todos):
    """Display all todos."""
    # TODO: Print each todo with status indicator
    # Hint: status = "x" if todo["done"] else " "
    # Hint: print(f"[{status}] {todo['id']}: {todo['description']}")
    pass


def complete_todo(todos, todo_id):
    """Mark a todo as complete."""
    # TODO: Find todo by id and set done=True
    pass


def delete_todo(todos, todo_id):
    """Delete a todo by id."""
    # TODO: Remove todo with matching id
    pass


def main():
    todos = load_todos()

    if len(sys.argv) < 2:
        print(__doc__)
        return

    command = sys.argv[1]

    # TODO: Handle commands: add, list, done, delete
    # Hint: if command == "add": add_todo(todos, sys.argv[2])
    # Don't forget to save_todos() after modifications

    print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
