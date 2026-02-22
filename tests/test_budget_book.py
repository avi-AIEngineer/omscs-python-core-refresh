import unittest
import tempfile
from pathlib import Path

from mini_apps.budget_book.budget_book import (
    Expense,
    append_expense,
    read_expenses,
    filter_by_month,
    summarize,
)


class TestBudgetBook(unittest.TestCase):

    def test_append_and_read_roundtrip(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "ledger.csv"

            e1 = Expense("2026-02-12", "groceries", 45.20, "milk eggs")
            e2 = Expense("2026-02-13", "fuel", 30.00, "")

            append_expense(path, e1)
            append_expense(path, e2)

            loaded = read_expenses(path)
            self.assertEqual(loaded, [e1, e2])

    def test_filter_by_month(self):
        rows = [
            Expense("2026-02-01", "a", 10.0, ""),
            Expense("2026-03-01", "b", 20.0, ""),
            Expense("2026-02-15", "c", 5.0, ""),
        ]
        feb = filter_by_month(rows, "2026-02")
        self.assertEqual(feb, [rows[0], rows[2]])

    def test_summarize(self):
        rows = [
            Expense("2026-02-01", "groceries", 10.0, ""),
            Expense("2026-02-02", "fuel", 20.0, ""),
            Expense("2026-02-03", "groceries", 5.5, ""),
        ]
        total, by_category = summarize(rows)

        self.assertAlmostEqual(total, 35.5, places=2)
        self.assertEqual(by_category["groceries"], 15.5)
        self.assertEqual(by_category["fuel"], 20.0)


if __name__ == "__main__":
    unittest.main()