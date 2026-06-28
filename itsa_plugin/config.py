"""Configuration helpers."""

import os
from pathlib import Path

from .exceptions import ConfigurationError


def get_excel_path() -> Path:
    raw_path = os.getenv("ITSA_EXCEL_PATH", "").strip()
    if not raw_path:
        raise ConfigurationError("ITSA_EXCEL_PATH is not set.")
    return Path(raw_path)
