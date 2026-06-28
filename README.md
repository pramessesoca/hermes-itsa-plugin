# ITSA Plugin for Hermes

Python package for answering questions about ITSA results from Excel data.

## Setup

1. Install dependencies from `requirements.txt`.
2. Set `ITSA_EXCEL_PATH` to the Excel file path.
3. Register the tools from `plugin.yaml` in Hermes.

## Hermes tools

- `search_itsa(keyword)`
- `get_statistics()`
- `get_summary()`
- `filter_data(instansi, severity, kategori, tanggal_mulai, tanggal_selesai, status_verifikasi, nama_aset, jenis_aset)`
- `reload_excel()`

## Core behavior

- Excel is loaded once into RAM and reused through a cache.
- Header validation runs at load time and raises a clear error when a required column is missing.
- Tool functions return clear error payloads instead of crashing Hermes.
- The data layer is abstracted so the Excel backend can later be replaced with PostgreSQL without changing tool signatures.
