"""Prepare a self-contained release folder after PyInstaller has built the app."""

import argparse
import shutil
from pathlib import Path


def main() -> None:
    """Copy the editable config and the appropriate launcher into a ZIP file."""
    arguments = parse_arguments()
    project_root = Path(__file__).resolve().parent.parent
    bundle_dir = project_root / "dist" / "timesheet-generator"
    release_dir = project_root / "release"

    if not bundle_dir.is_dir():
        raise FileNotFoundError("Run PyInstaller before packaging a release.")

    shutil.copy2(project_root / "config.example.json", bundle_dir / "config.json")
    launcher_name = f"run_{arguments.platform}{launcher_extension(arguments.platform)}"
    launcher = project_root / "scripts" / launcher_name
    launcher_destination = bundle_dir / launcher.name
    shutil.copy2(launcher, launcher_destination)
    if arguments.platform != "windows":
        launcher_destination.chmod(0o755)

    release_dir.mkdir(exist_ok=True)
    archive_name = release_dir / f"timesheet-generator-{arguments.platform}"
    shutil.make_archive(
        str(archive_name), "zip", project_root / "dist", "timesheet-generator"
    )


def parse_arguments() -> argparse.Namespace:
    """Read the release platform selected by the GitHub Actions matrix."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--platform", choices=("macos", "windows", "linux"), required=True
    )
    return parser.parse_args()


def launcher_extension(platform: str) -> str:
    """Return the file extension used by each platform's starter script."""
    extensions = {"windows": ".bat", "macos": ".command", "linux": ".sh"}
    return extensions[platform]


if __name__ == "__main__":
    main()
