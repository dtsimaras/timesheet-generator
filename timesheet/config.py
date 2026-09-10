"""Read and validate the small JSON configuration file."""

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TimesheetConfig:
    """The settings a user can safely change in config.json."""

    employee_name: str
    year: int
    month: int
    week: int | None
    default_hours: float
    company_name: str
    holiday_country: str
    output_directory: str


def load_config(path: Path) -> TimesheetConfig:
    """Load config.json and return validated settings.

    `week` is optional. Use null for a whole month, or 1 to 5 for a
    Monday-to-Sunday calendar week that overlaps the selected month.
    """
    with path.open(encoding="utf-8") as file:
        values = json.load(file)

    config = TimesheetConfig(
        employee_name=required_text(values, "employee_name"),
        year=required_int(values, "year"),
        month=required_int(values, "month"),
        week=optional_int(values, "week"),
        default_hours=required_number(values, "default_hours"),
        company_name=required_text(values, "company_name"),
        holiday_country=required_text(values, "holiday_country"),
        output_directory=required_text(values, "output_directory"),
    )
    validate_config(config)
    return config


def required_text(values: dict[str, object], key: str) -> str:
    """Return a non-empty text setting, or explain what needs fixing."""
    value = values.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"config.json: '{key}' must be non-empty text.")
    return value.strip()


def required_int(values: dict[str, object], key: str) -> int:
    """Return an integer setting without accepting true/false by mistake."""
    value = values.get(key)
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"config.json: '{key}' must be an integer.")
    return value


def optional_int(values: dict[str, object], key: str) -> int | None:
    """Return null or an integer setting."""
    value = values.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"config.json: '{key}' must be an integer or null.")
    return value


def required_number(values: dict[str, object], key: str) -> float:
    """Return a numeric setting without accepting true/false by mistake."""
    value = values.get(key)
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"config.json: '{key}' must be a number.")
    return float(value)


def validate_config(config: TimesheetConfig) -> None:
    """Keep invalid reporting periods and hours out of the workbook."""
    if not 1 <= config.month <= 12:
        raise ValueError("config.json: 'month' must be between 1 and 12.")
    if config.week is not None and not 1 <= config.week <= 5:
        raise ValueError("config.json: 'week' must be null or between 1 and 5.")
    if config.default_hours < 0:
        raise ValueError("config.json: 'default_hours' cannot be negative.")
