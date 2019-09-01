import re
from datetime import date
import json


def fahrenheit_to_celsius(temperature):
    temperature = temperature.strip('\n')
    temperature = int(re.sub("[^0-9]", '', temperature))
    temp_celsius = round((temperature - 32) * (5/9), 1)
    return temp_celsius


def todays_date():
    today = date.today()
    today = today.strftime("%Y-%m-%d")
    return today


def extract_query_parameters(script):
    quote_the_data = script.replace("&q;", '"')
    replace_with_comma = quote_the_data.replace("%2C", ',')
    loaded = replace_with_comma.replace("&a;", "&")
    data = json.loads(loaded)
    query_params = dict()
    query_params['apiKey'] = data["process.env"]["SUN_API_KEY"]
    query_params['language'] = "en-US"
    query_params['units'] = "e"
    query_params['format'] = "json"
    first_key = next(iter(data['wu-next-state-key']))
    latitude = data['wu-next-state-key'][first_key]['value']['location']['latitude'][0]
    longitude = data['wu-next-state-key'][first_key]['value']['location']['longitude'][0]
    query_params['geocode'] = f"{latitude},{longitude}"
    return query_params


def utc_to_date(local_utc_date):
    ping = date.fromtimestamp(local_utc_date)
    string_date = f"{ping.year}-{ping.month}-{ping.day}"
    return string_date
