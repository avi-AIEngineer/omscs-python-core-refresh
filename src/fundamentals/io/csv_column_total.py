from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Expense:
    date: str           #Fomat yyyy-mm-dd
    category: str
    amount: float
    note: str = ""

HEADER = ["date", "category", "amount", "note"]


def read_expenses(csv_path: str | Path) -> list[Expense]:
    path = Path(csv_path)

    if not path.exists():
        return []

    expenses: list[Expense] = []
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row:
                continue
            expenses.append(
                Expense(
                    date=(row.get("date") or "").strip(),
                    category=(row.get("category") or "").strip(),
                    amount=float((row.get("amount") or "0").strip()),
                    note=(row.get("note") or "").strip(),
                )
            )
    return expenses


def append_expense(csv_path: str | Path, exp: Expense) -> None:
    path = Path(csv_path)
    file_exists = path.exists()

    # create parent dir if needed
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)

        if not file_exists or path.stat().st_size == 0:
            writer.writeheader()

        writer.writerow(
            {
                "date": exp.date,
                "category": exp.category,
                "amount": f"{exp.amount:.2f}",
                "note": exp.note,
            }
        )