# Timesheet Generator

Create an Excel timesheet for a month. It fills normal working days with your name and default hours, while keeping weekends and public holidays empty.

## Download and run

Use these steps after a release is available on GitHub. You do **not** need to install Python.

1. Open the project's GitHub page.
2. Click **Releases** on the right side of the page.
3. Open the newest release.
4. Under **Assets**, download the ZIP for your computer:
   - Windows: `timesheet-generator-windows-x64.zip`
   - Mac with an Apple chip (M1, M2, M3, or M4): `timesheet-generator-macos-arm64.zip`
   - Mac with an Intel chip: `timesheet-generator-macos-intel.zip`
   - Linux: `timesheet-generator-linux-x64.zip`
5. Double-click the downloaded ZIP to unzip it.
6. Open the unzipped folder.

## Set your details

1. Open `config.json` with a text editor. On Mac, TextEdit is fine. On Windows, Notepad is fine.
2. Change the values inside the quotation marks or the numbers after `:`.
3. Save the file.

Example:

```json
{
  "employee_name": "Your Name",
  "year": 2026,
  "month": 10,
  "week": 1,
  "default_hours": 8,
  "company_name": "Your Company",
  "holiday_country": "GR"
}
```

Only change the value on the right of each `:`. Keep the commas, quotation marks, and brackets exactly as they are.

| Setting | What it means | Example |
|---|---|---|
| `employee_name` | Name printed on the timesheet | `"Jane Smith"` |
| `year` | Reporting year | `2026` |
| `month` | Reporting month | `10` for October |
| `week` | Week to pre-fill, or the whole month | `1` to `5`, or `null` |
| `default_hours` | Hours added to each selected working day | `8` |
| `company_name` | Name shown at the top of the workbook | `"Your Company"` |
| `holiday_country` | Country whose public holidays are shaded | `"GR"` for Greece |

Use `"week": null` to fill every normal workday in the month. Use `"week": 1` to `"week": 5` to fill only one calendar week, while keeping all month dates visible.

## Create the Excel file

In the unzipped folder, run one file:

- **Windows:** double-click `run_windows.bat`.
- **Mac:** double-click `run_macos.command`. If Mac blocks it, right-click it, choose **Open**, then choose **Open** again. Finder will select the created Excel file.
- **Linux:** open a terminal in that folder and run `./run_linux.sh`.

The Excel file is created here:

```text
output/year/month/week/
```

For example:

```text
output/2026/10/week-1/Project_Timesheet_Your_Name.xlsx
```

You can edit the generated Excel file normally after creating it.

## If something goes wrong

- Check that `config.json` still has all commas and quotation marks.
- Confirm that `month` is a number from `1` to `12`.
- Confirm that `week` is `null` or a number from `1` to `5`.
- Run the launcher again after saving the corrected file.

## For contributors

This section is only for people working on the source code.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
cp config.example.json config.json
.venv/bin/python -m unittest discover -s tests
.venv/bin/python main.py
```

`config.json` and generated Excel files are ignored by Git, so personal settings do not get committed.
