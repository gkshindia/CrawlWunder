import os
from flask import Flask
from flask_restful import Resource, Api


def create_app(script_info=None):

    app = Flask(__name__)
    app.config.from_object('project.config.DevelopmentConfig')

    from project.api.weather import weather_blueprint
    app.register_blueprint(weather_blueprint)

    @app.shell_context_processor
    def ctx():
        return {"app": app}

    return app
