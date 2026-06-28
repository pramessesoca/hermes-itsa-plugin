"""Validation helpers for the input data."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from ..exceptions import DataValidationError
from ..schema import REQUIRED_HEADERS


@dataclass(frozen=True)
class HeaderValidationResult:
    missing_headers: tuple[str, ...]

    @property
    def is_valid(self) -> bool:
        return len(self.missing_headers) == 0


def normalize_dataframe_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    cleaned = dataframe.copy()
    cleaned.columns = [str(column).strip() for column in cleaned.columns]
    return cleaned


def validate_headers(dataframe: pd.DataFrame) -> HeaderValidationResult:
    missing_headers = tuple(header for header in REQUIRED_HEADERS if header not in dataframe.columns)
    if missing_headers:
        raise DataValidationError(
            "Missing required Excel headers: " + ", ".join(missing_headers)
        )
    return HeaderValidationResult(missing_headers=())
