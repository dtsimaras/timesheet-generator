# Timesheet generator

This project creates an Excel timesheet with default eight hours for each working day.

## Start here

Copy the template to a local configuration file, then edit it for your report:

```bash
cp config.example.json config.json
```

`config.json` is intentionally ignored by Git, so your name and company never get committed. It contains settings like these:

```json
{
  "employee_name": "Your Name",
  "year": 2026,
  "month": 9,
  "week": null,
  "default_hours": 8
}
```

- Set `week` to `null` to create a full-month report.
- Set `week` to `1`, `2`, `3`, `4`, or `5` to pre-fill only that Monday-to-Sunday calendar week. The workbook always contains the full selected month. Week 1 is the first calendar week that overlaps the month.
- Keep `default_hours` as `8` for a normal week. You can adjust individual values in Excel later.

## Run it

Create a virtual environment and install the two dependencies once:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Generate the workbook:

```bash
.venv/bin/python main.py
```

The generated workbook keeps its stable filename and is stored by reporting period:

```text
output/<year>/<month>/<week>/Project_Timesheet_<employee_name>.xlsx
```

For a full-month report, the week folder is `all-weeks`. It is safe to delete and regenerate generated files.

## Use a download without Python

After a release is published on GitHub, download the ZIP for your operating system and unzip it. Then edit the `config.json` sitting next to the application. It starts with generic values and is never sent back to Git.

- macOS: run `run_macos.command`.
- Windows: run `run_windows.bat`.
- Linux: run `run_linux.sh` from a terminal.

The generated Excel workbook appears in the bundle's `output/` folder.

## Project layout

```text
config.json                 The settings you edit.
main.py                     The tiny entry point you run.
timesheet/config.py         Reads and validates settings.
timesheet/generator.py      Creates and formats the workbook.
tests/test_config.py        A small example test suite.
```

Read `main.py` first. Then read `timesheet/config.py`, followed by `timesheet/generator.py`. Each function has one small job and a plain-English docstring.

## Version plan

- v0.1: Generate the correctly formatted workbook for a selected month.
- v0.2: Use `config.json` to choose the name, month, year, and optional calendar week.
- v0.3: Add a simple input format for overtime, leave, standby, comments, and client details. The existing workbook columns and the leave dropdown are already ready for this step.

## Check the code

```bash
.venv/bin/python -m unittest discover -s tests
```

## Publish a no-Python download

After the project is on GitHub, every push and pull request runs the test suite on macOS, Windows, and Linux. Creating and pushing a version tag builds a downloadable ZIP for each operating system:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Each ZIP contains a native application, a `config.json` file to edit, and a platform-specific launcher. Python is bundled into the application, so users do not need to install it. The generated Excel file remains under `output/<year>/<month>/<week>/`.

macOS users may need to right-click the launcher and choose **Open** the first time because it is an unsigned application. Windows users can run `run_windows.bat`; Linux users can run `run_linux.sh` from a terminal.

## Support the project

Once you create a Buy Me a Coffee profile, add your username to `.github/FUNDING.yml`:

```yaml
buy_me_a_coffee: your-username
```

GitHub will then display a Sponsor button on the repository page.
