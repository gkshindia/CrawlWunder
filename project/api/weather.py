from flask import Blueprint, request
from flask_restful import Resource, Api
from project.api.utils import params_not_none, is_params_valid, GetWeather
from web_crawl.utils import todays_date


weather_blueprint = Blueprint("crawlwunder", __name__, url_prefix='/weather')
api = Api(weather_blueprint)


class WeatherResource(Resource):

    def get(self):
        location = request.args.get("location")
        forecast_type = request.args.get("forecast")
        date = request.args.get("date")
        response_object = {
            "status": "fail",
            "message": "Ooops you are wandering into the unknown area to me, where Satellites can't get you"
        }
        try:
            if location is None:
                response_object['reason'] = "No temperature for Nowhere"
                return response_object, 404
            if params_not_none(forecast_type, date):
                if is_params_valid(forecast_type, date):
                    _weather = GetWeather()
                    crawl_result = _weather.crawl(location=location, forecast_type=forecast_type, date=date)
                    return crawl_result, 200
                return response_object, 404
            if forecast_type is None:
                forecast_type = "today"
            if date is None:
                date = todays_date()
            if is_params_valid(forecast_type, date):
                _weather = GetWeather()
                crawl_result = _weather.crawl(location=location, forecast_type=forecast_type, date=date)
                return crawl_result, 200
        except Exception as e:
            return response_object, 404


class WeatherPing(Resource):

    def get(self, location, forecast_type, date):
        return{
            "location": location,
            "forecast_type": forecast_type,
            "date": date
        }


api.add_resource(WeatherResource, '')
api.add_resource(WeatherPing, '/ping/<forecast_type>/<location>/<date>')
