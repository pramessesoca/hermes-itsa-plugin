"""Utility helpers shared across the plugin."""

from __future__ import annotations

from typing import Any

import pandas as pd


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, float) and pd.isna(value):
        return ""
    return str(value).strip()


def unique_non_empty_values(series: pd.Series) -> int:
    cleaned = series.dropna().map(normalize_text)
    cleaned = cleaned[cleaned != ""]
    return int(cleaned.nunique())


def to_str_series(series: pd.Series) -> pd.Series:
    return series.fillna("").astype(str)
