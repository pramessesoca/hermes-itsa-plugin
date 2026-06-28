"""Summary tool for ITSA data."""

from __future__ import annotations

from .statistics import get_statistics


def get_summary() -> dict:
    statistics = get_statistics()
    if "error" in statistics:
        return statistics

    return {
        "summary": {
            "total_data": statistics["total_data"],
            "total_instansi": statistics["total_instansi"],
            "severity_levels": len(statistics["severity"]),
            "status_levels": len(statistics["status"]),
        },
        "statistics": statistics,
    }
