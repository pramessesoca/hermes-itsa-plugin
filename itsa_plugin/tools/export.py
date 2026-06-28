"""Export helper for ITSA data."""

from __future__ import annotations

from ..data_provider import DataProvider, default_provider
from ..utils.formatter import dataframe_to_records


def export_itsa(provider: DataProvider | None = None, format: str = "records") -> list[dict] | dict:
    dataframe = (provider or default_provider).get_dataframe()

    if format == "records":
        return dataframe_to_records(dataframe)

    if format == "dict":
        return {"rows": dataframe_to_records(dataframe), "count": int(len(dataframe))}

    raise ValueError(f"Unsupported export format: {format}")
