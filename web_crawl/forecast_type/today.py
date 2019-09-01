import requests
from bs4 import BeautifulSoup
from web_crawl.config import BaseConfig
from web_crawl.utils import fahrenheit_to_celsius, todays_date
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


class TodaysWeather:

    def __init__(self, location, date=todays_date()):
        self.location = location.lower()
        self.date = date

    def parse(self):

        weather_url = f"{BaseConfig.TODAYS_URL}/{self.location}/date/{self.date}"
        logging.info(f"Requesting weather for {self.location}")
        try:
            page = requests.get(url=weather_url, headers=BaseConfig.HEADERS, timeout=BaseConfig.TIMEOUT)
            if page.status_code != 200:
                logging.error("Failed to retrieve the url Oops try again and check the url")
                return False
            soup = BeautifulSoup(page.text, 'html.parser')
            temp = soup.find(class_='temp').get_text()
            if temp:
                temp = fahrenheit_to_celsius(temp)
                return {"Temperature": temp, "location": self.location}
            else:
                logging.error("Unable to find the temp")
        except Exception as e:
            logging.error(e)
