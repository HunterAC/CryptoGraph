import os.path
from app import app
from flask import request, json, jsonify


@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

@app.route('/bitcoin')
def bitcoin():
    filepath = os.path.join("data/bitcoin.json")
    data = json.load(open(filepath))
    return jsonify(data)
