import os
import unittest
from project import create_app
from flask_testing import TestCase
from flask import current_app

app = create_app()


class TestDevelopmentConfig(TestCase):

    def create_app(self):
        app.config.from_object('project.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'c83cfc83bb93424592f531605766b6c1')
        self.assertFalse(current_app is None)


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'c83cfc83bb93424592f531605766b6c1')
        self.assertTrue(app.config['TESTING'])


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('project.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['SECRET_KEY'] == 'ec9dc6924d6643468b39de78e707ea3d')
        self.assertFalse(app.config['TESTING'])
