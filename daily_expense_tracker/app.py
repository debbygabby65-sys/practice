from flask import Flask, render_template, request, redirect
from database import get_db, get_expenses, get_total, get_expense_count, get_today_total, get_category_totals, search_expenses, filter_by_category, get_monthly_total
from datetime import date
app = Flask(__name__)
@app.route("/")
def home():
    search = request.args.get("search", "").strip()
    category = request.args.get("category", "").strip()

    if search:
        expenses = search_expenses(search)
    elif category:
        expenses = filter_by_category(category)
    else:
        expenses = get_expenses()

    total = get_total()
    count = get_expense_count()
    today_total = get_today_total()
    monthly_total = get_monthly_total()
    category_totals = get_category_totals()
    total = f"{total:,.0f}"

    return render_template(
        "index.html",
        expenses=expenses,
        total=total,
        count=count,
        today_total=today_total,
        monthly_total=monthly_total,
        category_totals=category_totals
    )

@app.route("/add-expense", methods=["POST"])
def add_expense():
    description = request.form["description"]
    amount = request.form["amount"]
    try:
        amount = float(amount)
    except ValueError:
        return "Amount must be a number"
    if amount <= 0:
        return "Amount must be greater than 0"
    category = request.form["category"]
    allowed_categories = ["Food", "Transport", "Bills", "Shopping", "Health", "Other"]
    if category not in allowed_categories:
        return "Invalid category"
    if not description.strip():
      return "Description is required"
    
    db = get_db()
    db.execute(
    "INSERT INTO expenses (description, amount, category, date) VALUES (?, ?, ?, ?)",
    (description, amount, category, date.today().isoformat())
    )
    
    db.commit()
    db.close()

    return redirect("/")
    
@app.route("/delete-expense/<int:expense_id>", methods=["POST"])
def delete_expense(expense_id):
    db = get_db()

    db.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    db.commit()
    db.close()

    return redirect("/")
@app.route("/edit-expense/<int:expense_id>", methods=["GET", "POST"])
def edit_expense(expense_id):
    if request.method == "POST":
        description = request.form["description"]
        amount = request.form["amount"]
        try:
            amount = float(amount)
        except ValueError:
            return "Amount must be a number"
        if amount <= 0:
            return "Amount must be greater than 0"
    
        if  not description.strip():
            return "Description is required"   
        category = request.form["category"]

        allowed_categories = ["Food", "Transport", "Bills", "Shopping", "Health", "Other"]

        if category not in allowed_categories:
            return "Invalid category"

        db = get_db()

        db.execute(
            "UPDATE expenses SET description = ?, amount = ?, category = ? WHERE id = ?",
            (description, amount, category, expense_id)
        )

        db.commit()
        db.close()

        return redirect("/")
    db = get_db()
    expense = db.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    ).fetchone()
    db.close()
    return render_template("edit.html", expense=expense)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
