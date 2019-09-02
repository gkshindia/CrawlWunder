import os


class BaseConfig:
    """Base configuratin"""
    TESTING = False
    SECRET_KEY = "c83cfc83bb93424592f531605766b6c1"


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = "ec9dc6924d6643468b39de78e707ea3d"
