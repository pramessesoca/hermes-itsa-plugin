"""Data provider abstractions."""

from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd

from .loader import ExcelLoader


class DataProvider(ABC):
    @abstractmethod
    def get_dataframe(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def reload(self) -> pd.DataFrame:
        raise NotImplementedError

    @abstractmethod
    def is_loaded(self) -> bool:
        raise NotImplementedError


class ExcelDataProvider(DataProvider):
    def __init__(self, loader: ExcelLoader | None = None) -> None:
        self.loader = loader or ExcelLoader()

    def get_dataframe(self) -> pd.DataFrame:
        return self.loader.load()

    def reload(self) -> pd.DataFrame:
        return self.loader.reload()

    def is_loaded(self) -> bool:
        return self.loader.is_loaded()


class PostgreSQLDataProvider(DataProvider):
    def __init__(self, *args, **kwargs) -> None:
        self._loaded = False

    def get_dataframe(self) -> pd.DataFrame:
        raise NotImplementedError("PostgreSQL provider is not implemented yet.")

    def reload(self) -> pd.DataFrame:
        raise NotImplementedError("PostgreSQL provider is not implemented yet.")

    def is_loaded(self) -> bool:
        return self._loaded


default_provider = ExcelDataProvider()
