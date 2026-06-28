"""Search tool for ITSA data."""

from __future__ import annotations

import re

import pandas as pd

from ..data_provider import DataProvider, default_provider
from ..utils.formatter import dataframe_to_records
from ..utils.helper import normalize_text, to_str_series


def search_itsa(keyword: str) -> list[dict]:
    try:
        return _search(keyword, default_provider)
    except Exception as exc:
        return [{"error": str(exc)}]


def _search(keyword: str, provider: DataProvider) -> list[dict]:
    normalized_keyword = normalize_text(keyword)
    if normalized_keyword == "":
        return []

    dataframe = provider.get_dataframe()
    keyword_pattern = re.escape(normalized_keyword)

    match_mask = pd.Series(False, index=dataframe.index)
    for column in dataframe.columns:
        column_mask = to_str_series(dataframe[column]).str.contains(
            keyword_pattern,
            case=False,
            regex=True,
            na=False,
        )
        match_mask = match_mask | column_mask

    return dataframe_to_records(dataframe.loc[match_mask].copy())
