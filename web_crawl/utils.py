from datetime import date
import json
from web_crawl.config import BaseConfig
import requests


def todays_date():
    today = date.today()
    today = today.strftime("%Y-%m-%d")
    return today


def extract_place_id(response):
    location = {}
    response_decoded = response.content.decode("utf-8")
    resp = json.loads(response_decoded)
    location['address'] = resp['location']['address'][0]
    location['placeId'] = resp['location']['placeId'][0]
    location['latitude'] = resp['location']['latitude'][0]
    location['longitude'] = resp['location']['longitude'][0]
    return location


class SearchCity:

    def __init__(self, location):
        if location:
            self.location = location
        else:
            return -1

    def query(self):
        query_parameters = {
            "apiKey": BaseConfig.API_KEY,
            "format": BaseConfig.FORMAT,
            "language": BaseConfig.LANGUAGE,
            "locationType": BaseConfig.LOCATION_TYPE,
            "query": self.location,
        }
        try:
            query_response = requests.get(BaseConfig.QUERY_URL, headers=BaseConfig.HEADERS,
                                          params=query_parameters, timeout=BaseConfig.TIMEOUT)
            if query_response.status_code != 200:
                return False
            _details = extract_place_id(query_response)
            return _details
        except Exception as e:
            return e, False
