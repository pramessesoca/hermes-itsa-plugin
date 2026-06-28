"""Lightweight data models used by tools."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ValidationReport:
    missing_headers: tuple[str, ...] = field(default_factory=tuple)
    is_valid: bool = True


@dataclass(frozen=True)
class StatisticsResult:
    total_data: int
    total_instansi: int
    severity: dict[str, int]
    status: dict[str, int]


@dataclass(frozen=True)
class ToolResponse:
    data: Any
    metadata: dict[str, Any] = field(default_factory=dict)
