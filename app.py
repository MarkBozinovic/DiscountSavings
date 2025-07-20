# app.py
from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Mock database of items and current prices
PRODUCTS = {
    "milk": {"store": "Woolworths", "price": 2.50, "discount": 0.50},
    "bread": {"store": "Coles", "price": 2.00, "discount": 0.30},
    "petrol": {"store": "BP", "price": 1.80, "discount": 0.15},
    "toilet paper": {"store": "Aldi", "price": 5.00, "discount": 1.00}
}

# Forecast savings for a weekly shop based on frequency
def forecast_savings(frequency):
    total_savings = 0
    for item in frequency:
        if item in PRODUCTS:
            savings = PRODUCTS[item]["discount"] * frequency[item]
            total_savings += savings
    return total_savings

@app.route("/")
def index():
    return render_template("index.html", products=PRODUCTS)

@app.route("/forecast", methods=["POST"])
def forecast():
    data = request.json
    frequency = data.get("frequency", {})
    savings = forecast_savings(frequency)
    return jsonify({"forecasted_savings": round(savings, 2)})

if __name__ == "__main__":
    app.run(debug=True)
