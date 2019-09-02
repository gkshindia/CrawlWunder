import json
import unittest
from flask_testing import TestCase
from project import create_app
from flask import current_app
from project.tests.base import BaseTestCase

app = create_app()


class TestAPIService(BaseTestCase):

    def test_weather_ping(self):
        response = self.client.get('/weather/ping/hourly/bangalore/2012-12-12')
        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn("bangalore", data['location'])
        self.assertIn("hourly", data['forecast_type'])
        self.assertIn("2012-12-12", data['date'])

    def test_no_location(self):
        response = self.client.get()
