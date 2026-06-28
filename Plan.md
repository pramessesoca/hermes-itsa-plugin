# AI ITSA Plugin for Hermes Agent

## Tujuan

Membangun plugin Hermes yang memungkinkan AI menjawab pertanyaan mengenai hasil ITSA menggunakan data dari file Excel.

Versi pertama menggunakan Excel sebagai sumber data.

Arsitektur harus dirancang agar nantinya dapat bermigrasi ke PostgreSQL tanpa mengubah interface tool yang digunakan Hermes.

---

# Arsitektur

```
Telegram
        │
        ▼
Hermes Agent
        │
        ▼
ITSA Plugin
        │
        ▼
Data Provider
        │
        ├── Excel Provider (Phase 1)
        └── PostgreSQL Provider (Phase 2)
```

Hermes tidak mengetahui sumber data.

Hermes hanya memanggil tool.

Tool hanya meminta data dari Data Provider.

---

# Struktur Folder

```
itsa-plugin/

├── plugin.yaml
├── requirements.txt
├── README.md
├── __init__.py

├── config.py
├── schema.py
├── models.py
├── exceptions.py

├── cache.py
├── data_provider.py
├── loader.py

├── tools/
│   ├── search.py
│   ├── statistics.py
│   ├── summary.py
│   ├── filter.py
│   ├── export.py
│   └── reload.py

└── utils/
    ├── formatter.py
    ├── validator.py
    └── helper.py
```

---

# Konfigurasi

```
ITSA_EXCEL_PATH=/data/ITSA.xlsx
```

Plugin membaca lokasi file Excel dari environment variable.

---

# Schema

Seluruh kode **tidak boleh menggunakan nama kolom secara hardcode**.

Buat file

```
schema.py
```

Contoh

```python
class Columns:

    START_DATE = "Tgl Mulai"

    END_DATE = "Tgl Selesai"

    ASSET_NAME = "Nama Aset"

    DOMAIN = "Domain"

    ASSET_TYPE = "Jenis Aset"

    VULNERABILITY = "Kerentanan"

    SEVERITY = "Severity"

    CATEGORY = "Kategori Kerentanan"

    REMEDIATION = "Perbaikan"

    VERIFICATION = "Verifikasi"

    VERIFICATION_REPORT = "Lap Verifikasi"
```

Seluruh project wajib menggunakan

```
Columns.SEVERITY
```

bukan

```
"Severity"
```

---

# Struktur Excel

Plugin mengasumsikan file Excel memiliki header berikut.

| Header |
|----------|
| Tgl Mulai |
| Tgl Selesai |
| Nama Aset |
| Domain |
| Jenis Aset |
| Kerentanan |
| Severity |
| Kategori Kerentanan |
| Perbaikan |
| Verifikasi |
| Lap Verifikasi |

Saat startup plugin harus memvalidasi seluruh header.

Jika ada header yang hilang, plugin mengembalikan error yang jelas.

---

# Data Provider

Buat interface

```
get_dataframe()

reload()

is_loaded()
```

Saat ini implementasinya membaca Excel.

Nanti implementasi dapat diganti menjadi PostgreSQL.

Tool tidak boleh mengetahui sumber data.

---

# Cache

Excel hanya boleh dibaca satu kali.

```
Excel

↓

load()

↓

DataFrame

↓

RAM
```

Semua tool menggunakan DataFrame yang berada di memori.

---

# Loader

Loader bertugas

- membaca Excel
- validasi header
- menyimpan DataFrame ke cache
- reload

---

# Tool

## search_itsa()

Parameter

```
keyword
```

Mencari seluruh kolom yang mengandung keyword.

Return

```
List[dict]
```

---

## get_statistics()

Menghasilkan statistik.

Contoh

- total data
- total instansi
- severity
- status

Return

```
dict
```

---

## get_summary()

Menghasilkan ringkasan dataset.

---

## filter_data()

Parameter

- instansi
- severity
- kategori
- tanggal mulai
- tanggal selesai
- status verifikasi

Return

```
List[dict]
```

---

## reload_excel()

Reload file Excel tanpa restart Hermes.

---

# Registrasi Tool

Hermes harus memiliki tool berikut.

```
search_itsa

get_statistics

get_summary

filter_data

reload_excel
```

---

# Requirements

```
pandas

openpyxl
```

---

# Logging

Gunakan logging.

Contoh

```
Loading Excel...

Validating headers...

Loading cache...

Rows : 1200

Finished.
```

---

# Error Handling

Plugin tidak boleh crash.

Tangani kondisi berikut.

- file tidak ditemukan

- file corrupt

- sheet tidak ditemukan

- header tidak lengkap

- DataFrame kosong

Semua error harus memiliki pesan yang jelas.

---

# Coding Standard

- Python 3.11+
- Type Hint
- Docstring
- Logging
- SOLID Principle
- Clean Architecture

---

# Migrasi ke PostgreSQL

Migrasi ke PostgreSQL hanya mengubah

```
loader.py

data_provider.py
```

Tool berikut **tidak boleh berubah**.

```
search_itsa()

get_statistics()

get_summary()

filter_data()

reload_excel()
```

Dengan demikian seluruh prompt, skill, dan konfigurasi Hermes tetap kompatibel setelah migrasi dari Excel ke PostgreSQL.