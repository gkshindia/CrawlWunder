from datetime import datetime
from web_crawl.forecast_type.weather_crawler import WeatherDetails

FORECAST_TYPES = ["hourly", "today", "fiveday", "tenday", "monthly"]


class GetWeather:

    def crawl(self, location, forecast_type, date):
        weather = WeatherDetails(location, date)
        try:
            if forecast_type == "today":
                response = weather.today_temp()
            elif forecast_type == "hourly":
                response = weather.temp_by_hour()
            elif forecast_type == "fiveday":
                response = weather.five_day_temp()
            elif forecast_type == "tenday":
                response = weather.ten_day_temp()
            elif forecast_type == "monthly":
                response = weather.monthly_temp()
            else:
                return -1
            return response
        except Exception as e:
            return e


def params_not_none(forecast_type, date):
    if forecast_type is None or date is None:
        return False
    return True


def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def is_params_valid(forecast, date):
    if forecast in FORECAST_TYPES and validate_date(date):
        return True
    return False
