import requests
import json
from datetime import datetime
from web_crawl.config import BaseConfig
from web_crawl.utils import todays_date, SearchCity
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING)


class WeatherDetails:

    def __init__(self, location, date=todays_date()):
        self.location = location.lower()
        self.date = date

    def dict_creator(self, data, idx):
        iso_date = data['vt1dailyForecast']['validDate'][idx]
        day_temp = data['vt1dailyForecast']['day']['temperature'][idx]
        night_temp = data['vt1dailyForecast']['night']['temperature'][idx]
        date_format = '%Y-%m-%dT%H:%M:%S%z'
        parsed_date = datetime.strptime(iso_date, date_format)
        temperature = dict()
        temperature['date'] = parsed_date.day
        temperature['month'] = parsed_date.strftime("%b")
        temperature['year'] = parsed_date.year
        temperature['temp_hi'] = day_temp
        temperature['temp_lo'] = night_temp
        return temperature

    def parse(self):
        location_param = SearchCity(self.location).query()

        query_params = dict()
        query_params['apiKey'] = BaseConfig.API_KEY
        query_params['language'] = "en-IN"
        query_params['units'] = "m"
        query_params['format'] = "json"
        query_params['geocode'] = f"{location_param['latitude']},{location_param['longitude']}"

        weather_url = f"{BaseConfig.FORECAST_URL}"
        logging.info(f"Requesting weather details for {location_param['address']}")
        try:
            page = requests.get(url=weather_url, headers=BaseConfig.HEADERS,
                                timeout=BaseConfig.TIMEOUT, params=query_params)
            if page.status_code != 200:
                logging.error("Failed to retrieve the url Oops try again and check the url")
                return False
            r = page.content.decode('utf-8')
            response = json.loads(r)
            return response
        except Exception as e:
            logging.error(e)

    def today_temp(self):
        data = self.parse()
        return self.dict_creator(data, 0)

    def five_day_temp(self):
        data = self.parse()
        five_day_forecast = []
        for idx in range(5):
            five_day_forecast.append(self.dict_creator(data, idx=idx))
        return five_day_forecast

    def ten_day_temp(self):
        data = self.parse()
        ten_day_forecast = []
        for idx in range(10):
            ten_day_forecast.append(self.dict_creator(data, idx=idx))
        return ten_day_forecast

    def monthly_temp(self):
        data = self.parse()
        day_range = len(data['vt1dailyForecast']['validDate'])
        monthly_forecast = []
        for idx in range(day_range):
            monthly_forecast.append(self.dict_creator(data, idx=idx))
        return monthly_forecast
