"""Statistics tool for ITSA data."""

from __future__ import annotations

import pandas as pd

from ..data_provider import DataProvider, default_provider
from ..schema import Columns
from ..utils.helper import unique_non_empty_values


def get_statistics() -> dict:
    try:
        return _get_statistics(default_provider)
    except Exception as exc:
        return {"error": str(exc)}


def _get_statistics(provider: DataProvider) -> dict:
    dataframe = provider.get_dataframe()

    severity_counts = _value_counts(dataframe, Columns.SEVERITY)
    status_counts = _value_counts(dataframe, Columns.VERIFICATION)

    return {
        "total_data": int(len(dataframe)),
        "total_instansi": unique_non_empty_values(dataframe[Columns.DOMAIN]),
        "severity": severity_counts,
        "status": status_counts,
    }


def _value_counts(dataframe: pd.DataFrame, column_name: str) -> dict[str, int]:
    if column_name not in dataframe.columns:
        return {}

    counts = dataframe[column_name].fillna("").astype(str).str.strip()
    counts = counts[counts != ""]
    return {key: int(value) for key, value in counts.value_counts().to_dict().items()}
