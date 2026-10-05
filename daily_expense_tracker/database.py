import sqlite3
import os
import psycopg
from datetime import date


def get_db():
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        return psycopg.connect(database_url)

    return sqlite3.connect("expense.db")


def placeholder():
    if os.getenv("DATABASE_URL"):
        return "%s"

    return "?"


def create_table():
    db = get_db()

    if os.getenv("DATABASE_URL"):
        db.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id SERIAL PRIMARY KEY,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )
        """)
    else:
        db.execute("""
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )
        """)

    db.commit()
    db.close()


def get_expenses():
    db = get_db()

    expenses = db.execute(
        "SELECT * FROM expenses ORDER BY id DESC"
    ).fetchall()

    db.close()

    return expenses


def get_total():
    db = get_db()

    total = db.execute(
        "SELECT SUM(amount) FROM expenses"
    ).fetchone()[0]

    db.close()

    return total or 0


def add_date_column():
    db = get_db()

    if os.getenv("DATABASE_URL"):
        columns = db.execute("""
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = 'expenses'
        """).fetchall()

        column_names = [column[0] for column in columns]

        if "date" not in column_names:
            db.execute(
                "ALTER TABLE expenses ADD COLUMN date TEXT"
            )

            today = date.today().isoformat()

            db.execute(
                "UPDATE expenses SET date = %s WHERE date IS NULL",
                (today,)
            )

            db.commit()

    else:
        columns = db.execute(
            "PRAGMA table_info(expenses)"
        ).fetchall()

        column_names = [column[1] for column in columns]

        if "date" not in column_names:
            db.execute(
                "ALTER TABLE expenses ADD COLUMN date TEXT"
            )

            today = date.today().isoformat()

            db.execute(
                "UPDATE expenses SET date = ? WHERE date IS NULL",
                (today,)
            )

            db.commit()

    db.close()


def get_expense_count():
    db = get_db()

    count = db.execute(
        "SELECT COUNT(*) FROM expenses"
    ).fetchone()[0]

    db.close()

    return count


def get_today_total():
    db = get_db()

    total = db.execute(
        f"SELECT SUM(amount) FROM expenses WHERE date = {placeholder()}",
        (date.today().isoformat(),)
    ).fetchone()[0]

    db.close()

    return total or 0


def get_category_totals():
    db = get_db()

    totals = db.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """).fetchall()

    db.close()

    return totals


def search_expenses(search_term):
    db = get_db()

    expenses = db.execute(
        f"""
        SELECT * FROM expenses
        WHERE description LIKE {placeholder()}
        ORDER BY id DESC
        """,
        (f"%{search_term}%",)
    ).fetchall()

    db.close()

    return expenses


def filter_by_category(category):
    db = get_db()

    expenses = db.execute(
        f"""
        SELECT * FROM expenses
        WHERE category = {placeholder()}
        ORDER BY id DESC
        """,
        (category,)
    ).fetchall()

    db.close()

    return expenses


def get_monthly_total():
    db = get_db()

    current_month = date.today().strftime("%Y-%m")

    total = db.execute(
        f"""
        SELECT SUM(amount)
        FROM expenses
        WHERE date LIKE {placeholder()}
        """,
        (f"{current_month}%",)
    ).fetchone()[0]

    db.close()

    return total or 0


create_table()
add_date_column()