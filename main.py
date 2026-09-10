"""Create a timesheet workbook from config.json."""

import sys
from pathlib import Path

from timesheet.config import load_config
from timesheet.generator import generate_timesheet


def main() -> None:
    """Load the editable settings and create the Excel file."""
    project_root = application_directory()
    config = load_config(project_root / "config.json")
    output_path = generate_timesheet(config, project_root)
    print(f"Created: {output_path}")


def application_directory() -> Path:
    """Find the folder containing config.json in source and bundled builds."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).parent


if __name__ == "__main__":
    main()
