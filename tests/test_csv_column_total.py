import unittest
import tempfile
from pathlib import Path

from src.fundamentals.io.csv_column_total import Expense, read_expenses, append_expense


class TestCsvExpenses(unittest.TestCase):

    def test_append_and_read_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "expenses.csv"

            append_expense(p, Expense("2026-02-18", "Groceries", 45.25, "Walmart"))
            append_expense(p, Expense("2026-02-19", "Fuel", 30.0, ""))

            exps = read_expenses(p)
            self.assertEqual(len(exps), 2)
            self.assertEqual(exps[0].category, "Groceries")
            self.assertAlmostEqual(exps[0].amount, 45.25, places=2)
            self.assertEqual(exps[1].note, "")

    def test_read_missing_file_returns_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "missing.csv"
            self.assertEqual(read_expenses(p), [])


if __name__ == "__main__":
    unittest.main()
