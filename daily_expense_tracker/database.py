import sqlite3
from datetime import date

def get_db():
    return sqlite3.connect("expense.db")
def create_table():
    db = get_db()
    db.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description  TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
         )
    """)
    db.commit()
    db.close()
def get_expenses():
    db = get_db()

    expenses = db.execute(
        "SELECT  * FROM expenses  ORDER BY id DESC"
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
create_table()
add_date_column()