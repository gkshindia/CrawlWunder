from project import create_app
from flask_testing import TestCase

app = create_app()


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('project.config.TestingConfig')
        return app
