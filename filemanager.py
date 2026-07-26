"""Small, dependency-free helpers shared by the legacy TiBot modules."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent


def file_dir(filename: str = "") -> str:
    """Return a path relative to the project root."""
    return str(ROOT / filename)


def readfile(filename: str) -> str:
    """Read UTF-8 text and raise a useful error instead of swallowing it."""
    return Path(filename).read_text(encoding="utf-8")


def readjson(filename: str) -> Any:
    return json.loads(readfile(filename))


def read_api_key(key: str) -> str:
    """Read a key from an environment variable or an optional local secret file.

    Environment variables make the project safe to deploy.  The old
    ``api_key.json`` file is still supported locally but is intentionally
    ignored by git.
    """
    env_name = f"TIBOT_{key.upper()}_API_KEY"
    value = os.getenv(env_name)
    if value:
        return value

    secret_file = ROOT / "api_key.json"
    if secret_file.exists():
        value = readjson(str(secret_file)).get(key)
        if value:
            return value

    raise RuntimeError(
        f"Missing {env_name}. Set it in the environment or create a local api_key.json."
    )


def prtBanner() -> None:
    print(readfile(file_dir("banner.txt")))


def read_quiz() -> Any:
    return readjson(file_dir("quiz.json"))
