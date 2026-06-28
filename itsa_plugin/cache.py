"""In-memory cache for the loaded DataFrame."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

import pandas as pd


@dataclass
class DataFrameCache:
    dataframe: Optional[pd.DataFrame] = field(default=None, init=False)
    source: Optional[str] = field(default=None, init=False)

    def set(self, dataframe: pd.DataFrame, source: str | None = None) -> None:
        self.dataframe = dataframe
        self.source = source

    def get(self) -> pd.DataFrame:
        if self.dataframe is None:
            raise RuntimeError("DataFrame cache is empty.")
        return self.dataframe

    def is_loaded(self) -> bool:
        return self.dataframe is not None

    def clear(self) -> None:
        self.dataframe = None
        self.source = None


dataframe_cache = DataFrameCache()
