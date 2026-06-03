from flask import Flask, render_template, request, redirect
import json
from finance import load_data, save_data

app = Flask(__name__)

@app.route("/")
def index():
    data = load_data()

    total_income = sum(item["amount"] for item in data["income"])
    total_expenses = sum(item["amount"] for item in data["expenses"])
    balance = total_income - total_expenses

    return render_template(
        "index.html",
        income=data["income"],
        expenses=data["expenses"],
        total_income=total_income,
        total_expenses=total_expenses,
        balance=balance
    )


@app.route("/add/<type>", methods=["GET", "POST"])
def add(type):
    if request.method == "POST":
        data = load_data()

        entry = {
            "title": request.form["title"],
            "amount": float(request.form["amount"])
        }

        data[type].append(entry)
        save_data(data)

        return redirect("/")

    return render_template("add.html", type=type)


if __name__ == "__main__":
    app.run(debug=True)