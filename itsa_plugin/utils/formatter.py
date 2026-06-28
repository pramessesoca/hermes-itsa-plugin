"""Formatting helpers for tool output."""

from __future__ import annotations

import pandas as pd


def dataframe_to_records(dataframe: pd.DataFrame) -> list[dict]:
    clean_dataframe = dataframe.where(pd.notna(dataframe), None)
    return clean_dataframe.to_dict(orient="records")


def normalize_mapping(mapping: dict) -> dict:
    return {key: value for key, value in mapping.items() if value not in (None, "")}
