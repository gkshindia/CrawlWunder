import requests
from bs4 import BeautifulSoup
from web_crawl.config import BaseConfig
from web_crawl.utils import todays_date, SearchCity
import logging
from datetime import date
from calendar import monthrange
logging.getLogger("urllib3").setLevel(logging.WARNING)


class Monthly:

    def __init__(self, location):
        self.location = location

    def parse(self):
        location_param = SearchCity(self.location).query()
        query_id = location_param['placeId']

        weather_url = f"{BaseConfig.WEATHER_URL}/monthly/l/{query_id}"
        logging.info(f"Requesting weather details for {location_param['address']}")
        try:
            page = requests.get(url=weather_url, headers=BaseConfig.HEADERS, timeout=BaseConfig.TIMEOUT)
            if page.status_code != 200:
                logging.error("Failed to retrieve the url Oops try again and check the url")
                return False
            soup = BeautifulSoup(page.text, 'html.parser')
            forecast_calendar = soup.find("span", {"class": "forecast-monthly__calendar"})
            day_cell = forecast_calendar.findChildren("div", recursive=False)
            this_year = date.today().year
            this_month = date.today().month
            this_month_name = date.today().strftime("%b")
            this_month_range = monthrange(this_year, this_month)[1]
            month_temperature = []
            for divs in day_cell[:this_month_range + 1]:
                if divs.find(class_="date") is None:
                    continue
                _date = divs.find(class_="date").get_text()
                if divs.find(class_="temp hi") is None:
                    max_temp = "--"
                else:
                    max_temp = divs.find(class_="temp hi").get_text()
                if divs.find(class_="temp low") is None:
                    min_temp = "--"
                else:
                    min_temp = divs.find(class_="temp low").get_text()
                month_temperature.append([this_year, this_month_name, _date, max_temp, min_temp])
            return month_temperature
        except Exception as e:
            logging.error(e)
