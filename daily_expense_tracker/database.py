import sqlite3

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

create_table()