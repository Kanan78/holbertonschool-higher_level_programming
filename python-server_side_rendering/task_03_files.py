#!/usr/bin/python3

from flask import Flask, render_template, requests
import csv
import json

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

@app.route("/products")
def products_route():
    source = requests.args.get("source")
    product_id = requests.args.get("id")
    error = None
    products = []

    if source not in ["json", "csv"]:
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
