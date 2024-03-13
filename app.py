'''
flask --app app run --debug
'''

from flask import Flask, jsonify, abort
from Controller.SpaceX import SpaceX

app = Flask(__name__)

@app.route("/")
def hello_world():
    abort(404)

@app.route("/api/<path:endpoint>")
def spacex_data(endpoint):
    spacex = SpaceX(endpoint)
    data = spacex.get_data()
    if data and spacex.data_fetcher.last_status_code == 200:
        return jsonify(data)
    else:
        return jsonify(data), spacex.data_fetcher.last_status_code