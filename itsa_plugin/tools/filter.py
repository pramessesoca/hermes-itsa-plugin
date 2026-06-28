"""Filter tool for ITSA data."""

from __future__ import annotations

from ..data_provider import DataProvider, default_provider
from ..schema import Columns
from ..utils.formatter import dataframe_to_records
from ..utils.helper import normalize_text, to_str_series


def filter_data(
    instansi: str | None = None,
    severity: str | None = None,
    kategori: str | None = None,
    tanggal_mulai: str | None = None,
    tanggal_selesai: str | None = None,
    status_verifikasi: str | None = None,
    nama_aset: str | None = None,
    jenis_aset: str | None = None,
) -> list[dict]:
    """Filter ITSA rows with explicit Hermes-friendly parameters."""
    try:
        return _filter_dataframe(
            default_provider,
            {
                Columns.DOMAIN: instansi,
                Columns.SEVERITY: severity,
                Columns.CATEGORY: kategori,
                Columns.START_DATE: tanggal_mulai,
                Columns.END_DATE: tanggal_selesai,
                Columns.VERIFICATION: status_verifikasi,
                Columns.ASSET_NAME: nama_aset,
                Columns.ASSET_TYPE: jenis_aset,
            },
        )
    except Exception as exc:
        return [{"error": str(exc)}]


def filter_itsa(**criteria: str) -> list[dict]:
    """Backward-compatible alias for older callers."""
    try:
        return _filter_dataframe(default_provider, criteria)
    except Exception as exc:
        return [{"error": str(exc)}]


def _filter_dataframe(provider: DataProvider, criteria: dict[str, str | None]) -> list[dict]:
    dataframe = provider.get_dataframe()
    filtered = dataframe.copy()
    for column_name, expected_value in criteria.items():
        if expected_value in (None, ""):
            continue
        if column_name not in filtered.columns:
            continue
        normalized_expected = normalize_text(expected_value)
        column_values = to_str_series(filtered[column_name])
        matches = column_values.str.contains(
            normalized_expected,
            case=False,
            na=False,
            regex=False,
        )
        filtered = filtered[matches]

    return dataframe_to_records(filtered)
