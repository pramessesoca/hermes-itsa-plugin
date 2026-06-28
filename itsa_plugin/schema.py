"""Column definitions and schema constants."""


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


REQUIRED_HEADERS = (
    Columns.START_DATE,
    Columns.END_DATE,
    Columns.ASSET_NAME,
    Columns.DOMAIN,
    Columns.ASSET_TYPE,
    Columns.VULNERABILITY,
    Columns.SEVERITY,
    Columns.CATEGORY,
    Columns.REMEDIATION,
    Columns.VERIFICATION,
    Columns.VERIFICATION_REPORT,
)
