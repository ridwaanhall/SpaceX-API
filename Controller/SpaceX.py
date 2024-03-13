from flask import jsonify
from Bases.DataBases import SpaceXDataFetcher

class SpaceX:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.url = self.endpoint
        self.data_fetcher = SpaceXDataFetcher(self.url)

    def get_data(self):
        return self.data_fetcher.fetch_data()