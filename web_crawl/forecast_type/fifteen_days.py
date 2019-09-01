import requests
from bs4 import BeautifulSoup
from web_crawl.config import BaseConfig
from web_crawl.utils import todays_date, extract_query_parameters, utc_to_date
import json
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


class FifteenDaysWeather:

    def __init__(self, location, date=todays_date()):
        self.location = location.lower()
        self.date = date

    def parse(self):
        weather_url = f"{BaseConfig.TEN_DAY_URL}{self.location}"
        logging.debug(f"Requesting weather for {self.location}")
        try:
            page = requests.get(url=weather_url, headers=BaseConfig.HEADERS, timeout=BaseConfig.TIMEOUT)
            if page.status_code != 200:
                logging.error("Failed to retrieve the url Oops try again and check the url")
                return Exception
            soup = BeautifulSoup(page.text, 'html.parser')
            script_id = soup.find(id="app-root-state")
            try:
                script = script_id.contents[0]
                if not script:
                    return Exception
                parameters = extract_query_parameters(script)
                page = requests.get(BaseConfig.FIFTEEN_DAY_API_BASE_URL, headers=BaseConfig.HEADERS,
                                    params=parameters, timeout=BaseConfig.TIMEOUT)
                r = page.content.decode('utf-8')
                response = json.loads(r)
                concat_values = []
                for idx in range(15):
                    date = utc_to_date(int(response['validTimeUtc'][idx]))

                    day = response['dayOfWeek'][idx]
                    temp_max = response['temperatureMax'][idx]
                    temp_min = response['temperatureMin'][idx]
                    concat_values.append([date, day, temp_max, temp_min])
                return concat_values
            except Exception as e:
                logging.error(e)
                return e
        except Exception as e:
            logging.error(e)
