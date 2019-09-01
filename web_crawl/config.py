import logging


class BaseConfig:
    TODAYS_URL = "https://www.wunderground.com/weather/in/"
    logging.basicConfig(level=logging.DEBUG)
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/76.0.3809.100 Safari/537.36 OPR/63.0.3368.53'}
    TIMEOUT = 5
    HOURLY_URL = "https://www.wunderground.com/hourly/in/"
    TEN_DAY_URL = "https://www.wunderground.com/forecast/in/"
    MONTHLY_URL = "https://www.wunderground.com/calendar/in/"
    FIFTEEN_DAY_API_BASE_URL = "https://api.weather.com/v3/wx/forecast/daily/15day"
