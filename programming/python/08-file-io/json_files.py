"""JSON Files — reading and writing JSON with the json module.

Exercises:
  1. Read config.json and access nested values
  2. Modify the config and write it back
  3. Convert Python objects to/from JSON strings
  4. Handle JSON with custom types
"""

import json
import tempfile
from pathlib import Path

DATA = Path(__file__).parent / "data"


def main():
    # TODO: Read config.json
    # Hint: with open(DATA / "config.json") as f:
    #           config = json.load(f)

    # TODO: Access nested values
    # Hint: print(f"App: {config['app']['name']}")
    # Hint: print(f"Features: {config['features']}")

    # TODO: Modify config and write to temp file
    # Hint: config["app"]["version"] = "2.0.0"
    # Hint: json.dump(config, f, indent=2)

    # TODO: json.dumps (to string) and json.loads (from string)
    # Hint: s = json.dumps({"key": "value"})
    # Hint: obj = json.loads(s)

    pass  # Remove when done


if __name__ == "__main__":
    main()
