import requests
from bs4 import BeautifulSoup
from web_crawl.config import BaseConfig
from web_crawl.utils import fahrenheit_to_celsius, todays_date
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


class HourlyWeather:

    def __init__(self, location, date=todays_date()):
        self.location = location.lower()
        self.date = date

    def parse(self):
        weather_url = f"{BaseConfig.HOURLY_URL}{self.location}/date/{self.date}"
        logging.debug(f"Requesting weather for {self.location}")
        try:
            page = requests.get(url=weather_url, headers=BaseConfig.HEADERS, timeout=BaseConfig.TIMEOUT)
            if page.status_code != 200:
                logging.error("Failed to retrieve the url Oops try again and check the url")
                return False
            soup = BeautifulSoup(page.text, 'html.parser')
            table = soup.find('table', {'id': 'hourly-forecast-table'})
            rows = table.find_all('tr')
            temp_by_hour = {}
            for row in rows[1:]:
                table_data = row.find_all('td')
                temp = table_data[2].get_text()
                temp = fahrenheit_to_celsius(temp)
                hour = table_data[0].get_text()
                hour = hour.strip('\n')
                temp_by_hour[hour] = temp
            return temp_by_hour
        except Exception as e:
            logging.error(e)
