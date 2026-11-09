#!/usr/bin/python3
import csv
import json
import sqlite3
from pathlib import Path
from flask import Flask, render_template, request

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent


def read_json():
    with open(BASE_DIR / 'products.json') as file:
        return json.load(file)


def read_csv():
    with open(BASE_DIR / 'products.csv', newline='') as file:
        return list(csv.DictReader(file))


def read_sql():
    with sqlite3.connect(BASE_DIR / 'products.db') as conn:
        conn.row_factory = sqlite3.Row
        return [dict(row) for row in conn.execute('SELECT * FROM Products')]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        try:
            data = read_sql()
        except sqlite3.Error:
            return render_template('product_display.html',
                                   error='Database error')
    else:
        return render_template('product_display.html', error='Wrong source')

    if product_id is not None:
        data = [product for product in data
                if str(product['id']) == product_id]

        if not data:
            return render_template('product_display.html',
                                   error='Product not found')

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
