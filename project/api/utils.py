from datetime import datetime
from flask import jsonify

FORECAST_TYPES = ["hourly", "today", "fifteenday"]


class GetWeather:

    def crawl(self, location, forecast_type, date):
        try:
            if forecast_type == "today":
                weather = TodaysWeather(location)
                response = weather.parse()
                response["date"] = date
            elif forecast_type == "hourly":
                weather = HourlyWeather(location, date)
                response = weather.parse()
            elif forecast_type == "fifteenday":
                weather = FifteenDaysWeather(location, date)
                response_list = weather.parse()
                response = prettify_fifteen_day_output(response_list)
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


def prettify_fifteen_day_output(data):
    dict_data = {}
    listify_dict_data = []
    for date, day, Max, Min in data:
        dict_data["date"] = date
        dict_data["day"] = day
        dict_data["Max Temperature"] = Max
        dict_data["Min Temperature"] = Min
        listify_dict_data.append(dict_data)
    return {"fifteen_day_temperature": listify_dict_data}
