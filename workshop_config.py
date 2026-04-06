"""
Workshop Configuration Helper

Provides centralized save/load for workshop resource values
(S3 Bucket, S3 Vector Bucket, OpenSearch Endpoint, etc.)
so they only need to be entered once in 0_setup/setup.ipynb.
"""

import json
import os

CONFIG_FILENAME = "workshop_config.json"

# Resolve config path relative to this module (project root), not the notebook CWD
_MODULE_DIR = os.path.dirname(os.path.abspath(__file__))


def _find_config_path():
    """Return the path to workshop_config.json at the project root (next to workshop_config.py)."""
    return os.path.join(_MODULE_DIR, CONFIG_FILENAME)


def save_config(config: dict):
    """Save workshop configuration to workshop_config.json."""
    path = _find_config_path()
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
    print(f"Configuration saved to {os.path.abspath(path)}")


def load_config() -> dict:
    """Load workshop configuration from workshop_config.json.

    Raises FileNotFoundError with a helpful message if the file doesn't exist.
    """
    path = _find_config_path()
    if not os.path.exists(path):
        raise FileNotFoundError(
            "workshop_config.json not found. "
            "Please run 0_setup/setup.ipynb first to configure workshop resources."
        )
    with open(path) as f:
        return json.load(f)
