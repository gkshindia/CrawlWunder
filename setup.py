import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="crawl_weather_wunder",
    version='0.1',
    scripts=['weather'],
    author="Gourav Kumar Singh",
    author_email="gkshindia@gmail.com",
    description="A sample project to get weather temperature in daily, hourly, 5day, 10 day and monthly report",
    license="PIP",
)
