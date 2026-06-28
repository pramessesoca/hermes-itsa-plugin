"""Reload helper for ITSA data."""

from __future__ import annotations

from ..data_provider import DataProvider, default_provider


def reload_excel() -> dict:
    """Reload the configured ITSA Excel file without restarting Hermes."""
    return _reload(default_provider)


def reload_itsa() -> dict:
    """Backward-compatible alias for older callers."""
    return reload_excel()


def _reload(provider: DataProvider) -> dict:
    try:
        dataframe = provider.reload()
        return {
            "reloaded": True,
            "rows": int(len(dataframe)),
        }
    except Exception as exc:
        return {
            "reloaded": False,
            "error": str(exc),
        }
