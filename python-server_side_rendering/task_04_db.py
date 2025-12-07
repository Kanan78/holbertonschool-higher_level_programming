#!/usr/bin/python3

from flask import Flask, render_template, request
import csv
import json
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except:
        return []


def read_csv():
    data = []
    try:
        with open("products.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                        })
        return data
    except Exception:
        return []


def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()



@app.route("/products")
def products_route():
    source = request.args.get("source")
    product_id = request.args.get("id")
    error = None
    products = []


    if source == "sql":
        try:
            conn = sqlite3.connect("products.db")
            cursor = conn.cursor()

            cursor.execute("SELECT name FROM Products;")

            rows = cursor.fetchall()
            data = [row[0] for row in rows]
            conn.close()

        except Exception as e:
            data = [f"Database Error: {str(e)}"]

    if source not in ["json", "csv","sql"]:
        return render_template("product_display.html", error="Wrong source", products=None)

    products = read_json() if source == "json" else read_csv()


    if product_id:
        try:
            pid = int(product_id)
            filtered = [p for p in products if p["id"] == pid]

            if not filtered:
                return render_template("product_display.html", error="Product not found", products=None)

            products = filtered

        except ValueError:
            return render_template("product_display.html", error="Invalid ID", products=None)

    return render_template("product_display.html", error=None, products=products)



if __name__ == "__main__":
    app.run()
    create_database()
