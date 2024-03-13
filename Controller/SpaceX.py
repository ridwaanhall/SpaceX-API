from flask import jsonify
from Bases.DataBases import SpaceXDataFetcher

class SpaceX:
    def __init__(self, url):
        self.url = url
        self.data_fetcher = SpaceXDataFetcher(self.url)

    def homepage_tiles(self):
        return self.data_fetcher.fetch_data()
    
    def launches_page_tiles(self):
        return self.data_fetcher.fetch_data()
    
    def launches_page_stats(self):
        return self.data_fetcher.fetch_data()
    