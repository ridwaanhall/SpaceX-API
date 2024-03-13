import requests
from Bases.Base import URL_BASE

class SpaceXDataFetcher:
    def __init__(self, url):
        self.url = URL_BASE + url
        self.last_status_code = None

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            self.last_status_code = response.status_code
            if response.status_code == 200:
                data = response.json()
                return data
            else:
                print(f"Error: Received status code {response.status_code}")
                data = response.json()
                return data
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None