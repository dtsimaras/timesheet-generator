import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from timesheet.config import load_config


class LoadConfigTests(unittest.TestCase):
    def test_loads_a_valid_config(self) -> None:
        config = self.load({"month": 9, "week": None})
        self.assertEqual(config.month, 9)
        self.assertIsNone(config.week)

    def test_rejects_an_invalid_week(self) -> None:
        with self.assertRaisesRegex(ValueError, "week"):
            self.load({"month": 9, "week": 6})

    def test_rejects_an_invalid_month(self) -> None:
        with self.assertRaisesRegex(ValueError, "month"):
            self.load({"month": 13})

    def test_rejects_negative_default_hours(self) -> None:
        with self.assertRaisesRegex(ValueError, "default_hours"):
            self.load({"default_hours": -1})

    def test_rejects_non_finite_default_hours(self) -> None:
        with self.assertRaisesRegex(ValueError, "default_hours"):
            self.load({"default_hours": float("nan")})

    def test_rejects_a_missing_employee_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "employee_name"):
            self.load({"employee_name": ""})

    def test_rejects_an_unknown_holiday_country(self) -> None:
        with self.assertRaisesRegex(ValueError, "holiday_country"):
            self.load({"holiday_country": "NOT_A_COUNTRY"})

    def test_rejects_an_output_folder_outside_the_app(self) -> None:
        with self.assertRaisesRegex(ValueError, "output_directory"):
            self.load({"output_directory": "../outside"})

    def test_rejects_boolean_values_for_number_settings(self) -> None:
        with self.assertRaisesRegex(ValueError, "month"):
            self.load({"month": True})
        with self.assertRaisesRegex(ValueError, "default_hours"):
            self.load({"default_hours": False})

    def load(self, overrides: dict[str, object]):
        values = {
            "employee_name": "Example Developer", "year": 2026, "month": 1,
            "week": None, "default_hours": 8, "company_name": "Example Company",
            "holiday_country": "GR", "output_directory": "output",
        }
        values.update(overrides)
        with TemporaryDirectory() as directory:
            path = Path(directory) / "config.json"
            path.write_text(json.dumps(values), encoding="utf-8")
            return load_config(path)


if __name__ == "__main__":
    unittest.main()
