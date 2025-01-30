'''
flask --app app run --debug
'''

from flask import Flask, jsonify, abort
from Controller.SpaceX import SpaceX

app = Flask(__name__)

@app.route("/")
def hello_world():
    return jsonify({
        "available_endpoints": [
            "/api/homepage-tiles",
            "/api/launches-page-tiles",
            "/api/launches-page-stats"
        ]
    })

@app.route("/api/homepage-tiles")
def HomepageTiles():
    spacex = SpaceX("homepage-tiles")
    data = spacex.homepage_tiles()
    if data and spacex.data_fetcher.last_status_code == 200:
        return jsonify(data)
    else:
        return jsonify(data), spacex.data_fetcher.last_status_code

@app.route("/api/launches-page-tiles")
def LaunchesPageTiles():
    spacex = SpaceX("launches-page-tiles")
    data = spacex.launches_page_tiles()
    if data and spacex.data_fetcher.last_status_code == 200:
        return jsonify(data)
    else:
        return jsonify(data), spacex.data_fetcher.last_status_code
    
@app.route("/api/launches-page-stats")
def LaunchesPageStats():
    spacex = SpaceX("launches-page-stats")
    data = spacex.launches_page_stats()
    if data and spacex.data_fetcher.last_status_code == 200:
        return jsonify(data)
    else:
        return jsonify(data), spacex.data_fetcher.last_status_code
    
