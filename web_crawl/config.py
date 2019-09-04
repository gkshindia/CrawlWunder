import logging


class BaseConfig:
    WEATHER_URL = "https://weather.com/en-IN/weather"
    logging.basicConfig(level=logging.DEBUG)
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.53'}
    TIMEOUT = 5
    API_KEY = "d522aa97197fd864d36b418f39ebb323"
    FORMAT = "json"
    LANGUAGE = "en-IN"
    LOCATION_TYPE = "locale"
    QUERY_URL = "https://api.weather.com/v3/location/search"
    FORECAST_URL = "https://api.weather.com/v2/turbo/vt1dailyForecast"
