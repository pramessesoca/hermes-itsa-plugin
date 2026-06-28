"""Excel loader that validates and caches the ITSA dataset."""

from __future__ import annotations

import logging
from pathlib import Path

import pandas as pd

from .cache import dataframe_cache
from .config import get_excel_path
from .exceptions import DataNotLoadedError, DataValidationError
from .utils.validator import normalize_dataframe_columns, validate_headers

logger = logging.getLogger(__name__)


class ExcelLoader:
    def __init__(self, excel_path: Path | None = None) -> None:
        self.excel_path = Path(excel_path) if excel_path is not None else None

    def _resolve_excel_path(self) -> Path:
        if self.excel_path is not None:
            return self.excel_path
        return get_excel_path()

    def load(self) -> pd.DataFrame:
        if dataframe_cache.is_loaded():
            logger.info("Loading ITSA data from cache.")
            return dataframe_cache.get()
        return self.reload()

    def reload(self) -> pd.DataFrame:
        excel_path = self._resolve_excel_path()
        logger.info("Loading ITSA Excel data from %s.", excel_path)

        if not excel_path.exists():
            raise FileNotFoundError(f"Excel file not found: {excel_path}")

        try:
            dataframe = pd.read_excel(excel_path)
        except ValueError as exc:
            raise DataValidationError(f"Unable to read Excel sheet: {exc}") from exc
        except Exception as exc:
            raise DataValidationError(f"Unable to read Excel file: {exc}") from exc

        if dataframe.empty:
            raise DataValidationError("Excel file is empty.")

        logger.info("Validating ITSA Excel headers.")
        dataframe = normalize_dataframe_columns(dataframe)
        validate_headers(dataframe)
        dataframe_cache.set(dataframe, source=str(excel_path))
        logger.info("ITSA data loaded. Rows: %s.", len(dataframe))
        return dataframe

    def is_loaded(self) -> bool:
        return dataframe_cache.is_loaded()


def get_loaded_dataframe() -> pd.DataFrame:
    if not dataframe_cache.is_loaded():
        raise DataNotLoadedError("ITSA data is not loaded yet.")
    return dataframe_cache.get()
