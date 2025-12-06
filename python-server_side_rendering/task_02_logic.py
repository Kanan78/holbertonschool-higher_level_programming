#!/usr/bin/python3

from flask import Flask, render_template
import json


app = Flask(__name__)

@app.route("/items")
def items():
    
    try:
        with open("items.json", "r") as f:
            data = json.load(f)

    except Exception:
        data = []

    return render_template("items.html", items=data)

if __name__ == "__main__":
    app.run()
