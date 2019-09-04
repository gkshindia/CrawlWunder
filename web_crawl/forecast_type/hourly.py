import requests
from bs4 import BeautifulSoup
from web_crawl.config import BaseConfig
from web_crawl.utils import todays_date, SearchCity
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


class HourlyWeather:

    def __init__(self, location, date=todays_date()):
        self.location = location.lower()
        self.date = date

    def parse(self):
        location_param = SearchCity(self.location).query()
        query_id = location_param['placeId']

        weather_url = f"{BaseConfig.WEATHER_URL}/hourbyhour/l/{query_id}"
        logging.info(f"Requesting weather details for {location_param['address']}")
        try:
            page = requests.get(url=weather_url, headers=BaseConfig.HEADERS, timeout=BaseConfig.TIMEOUT)
            if page.status_code != 200:
                logging.error("Failed to retrieve the url Oops try again and check the url")
                return False
            soup = BeautifulSoup(page.text, 'html.parser')
            table = soup.find("table", {"class":"twc-table"})
            rows = table.find_all('tr')
            temp_by_hour = {}
            for row in rows[1:]:
                hour = row.find("span", {"class": "dsx-date"}).get_text()
                temp = row.find(class_="temp").get_text()
                temp_by_hour[hour] = f"{temp} C"
            return temp_by_hour
        except Exception as e:
            logging.error(e)
