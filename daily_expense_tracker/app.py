from flask import Flask, render_template, request, redirect
from database import get_db, get_expenses, get_total

app = Flask(__name__)

@app.route("/")
def home():
    expenses = get_expenses()
    total = get_total()
    total = f"{total:,.0f}"
    return render_template("index.html", expenses=expenses, total=total)
@app.route("/add-expense", methods=["POST"])
def add_expense():
    description = request.form["description"]
    amount = request.form["amount"]
    category = request.form["category"]
     
    if not description.strip():
        return "Description is required"
    
    db = get_db()

    db.execute(
        "INSERT INTO expenses (description, amount, category) VALUES (?, ?, ?)",
        (description, amount, category)
    )

    db.commit()
    db.close()

    return redirect("/")
if __name__ == "__main__":
    app.run(debug=True)