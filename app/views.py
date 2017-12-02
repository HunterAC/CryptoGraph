import os.path
from app import app
from flask import request, json, jsonify
from app.scripts import script


@app.route('/')
@app.route('/index')
def index():
    return "Hello, world!"

@app.route('/bitcoin')
def bitcoin():
    filepath = os.path.join("data/percentages.json")
    data = json.load(open(filepath))
    return jsonify(data)
