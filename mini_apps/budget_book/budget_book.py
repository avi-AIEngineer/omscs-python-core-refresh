from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class Expense:
    date: str        # YYYY-MM-DD
    category: str
    amount: float
    note: str = ""


HEADER = ["date", "category", "amount", "note"]
DEFAULT_CSV = Path("mini_apps/budget_book/sample_ledger.csv")


def append_expense(csv_path: str | Path, exp: Expense) -> None:
    path = Path(csv_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    file_exists = path.exists()

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=HEADER)

        if not file_exists or path.stat().st_size == 0:
            writer.writeheader()

        writer.writerow(
            {
                "date": exp.date.strip(),
                "category": exp.category.strip(),
                "amount": f"{exp.amount:.2f}",
                "note": exp.note.strip(),
            }
        )


def read_expenses(csv_path: str | Path) -> list[Expense]:
    path = Path(csv_path)
    if not path.exists():
        return []

    out: list[Expense] = []
    with path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row:
                continue
            out.append(
                Expense(
                    date=(row.get("date") or "").strip(),
                    category=(row.get("category") or "").strip(),
                    amount=float((row.get("amount") or "0").strip()),
                    note=(row.get("note") or "").strip(),
                )
            )
    return out


def filter_by_month(expenses: Iterable[Expense], year_month: str) -> list[Expense]:
    prefix = year_month.strip()  # YYYY-MM
    return [e for e in expenses if e.date.startswith(prefix)]


def summarize(expenses: Iterable[Expense]) -> tuple[float, dict[str, float]]:
    total = 0.0
    by_category: dict[str, float] = {}
    for e in expenses:
        total += e.amount
        by_category[e.category] = by_category.get(e.category, 0.0) + e.amount
    return total, by_category


def print_usage() -> None:
    print("Budget Book MVP")
    print("")
    print("Commands:")
    print("  add <date> <category> <amount> [note...]")
    print("    Example: add 2026-02-21 groceries 45.20 milk eggs")
    print("")
    print("  list [limit]")
    print("    Example: list 5")
    print("")
    print("  summary <YYYY-MM>")
    print("    Example: summary 2026-02")


def cmd_add(args: list[str]) -> None:
    if len(args) < 3:
        print("Usage: add <date> <category> <amount> [note...]")
        return

    date = args[0]
    category = args[1]

    try:
        amount = float(args[2])
    except ValueError:
        print("Error: amount must be a number")
        return

    note = " ".join(args[3:]) if len(args) > 3 else ""

    append_expense(DEFAULT_CSV, Expense(date, category, amount, note))
    print("Added.")


def cmd_list(args: list[str]) -> None:
    expenses = read_expenses(DEFAULT_CSV)

    limit = None
    if args:
        try:
            limit = int(args[0])
        except ValueError:
            print("Error: list limit must be an integer")
            return

    rows = list(reversed(expenses))  # newest first
    if limit is not None:
        rows = rows[:limit]

    if not rows:
        print("No expenses found.")
        return

    for e in rows:
        if e.note:
            print(f"{e.date} | {e.category:<12} | $ {e.amount:7.2f} | {e.note}")
        else:
            print(f"{e.date} | {e.category:<12} | $ {e.amount:7.2f}")


def cmd_summary(args: list[str]) -> None:
    if len(args) != 1:
        print("Usage: summary <YYYY-MM>")
        return

    year_month = args[0]
    expenses = read_expenses(DEFAULT_CSV)
    month_rows = filter_by_month(expenses, year_month)
    total, by_category = summarize(month_rows)

    print(f"Summary for {year_month}")
    print(f"TOTAL: ${total:.2f}")
    for category in sorted(by_category.keys()):
        print(f"{category:<12}: ${by_category[category]:.2f}")


def main(argv: list[str] | None = None) -> None:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        print_usage()
        return

    cmd = argv[0].lower()
    args = argv[1:]

    if cmd == "add":
        cmd_add(args)
    elif cmd == "list":
        cmd_list(args)
    elif cmd == "summary":
        cmd_summary(args)
    else:
        print(f"Unknown command: {cmd}")
        print()
        print_usage()


if __name__ == "__main__":
    main()