import yaml
import os
from pathlib import Path

_CONFIG_PATH = Path(__file__).parent / "config.yaml"


def load_config(env: str = None) -> dict:
    """Load and return the config for the active environment.

    Environment is determined by:
    1. The `env` argument (if passed directly)
    2. The TEST_ENV environment variable
    3. Defaults to 'staging'
    """
    env = env or os.getenv("TEST_ENV", "staging")

    if not _CONFIG_PATH.exists():
        raise FileNotFoundError(f"Config file not found: {_CONFIG_PATH}")

    with _CONFIG_PATH.open("r") as f:
        data = yaml.safe_load(f)

    if env not in data:
        raise ValueError(
            f"Unknown environment '{env}'. Available environments: {list(data.keys())}"
        )

    return data[env]