This is a Sample project for getting weather of a particular location,

It prompts 3 factors, location, date(YYYY-MM-DD), forecast_type

* location is mandatory
* date is optional , if not entered todays local date will be taken
* forecast_type is optional and it contains 3 options - todays, hourly, fifteendays. Default is todays

It is pip installable package, command line tool. But not uploaded as pypi project, so you would have to clone or download the project, 
inorder to run the package.

You need to cd into the project root folder and run the below snippet

<code>python crawl_weather</code>

### API

The project folder contains the REST API, which could be run from the below comman
by cd'ing into the root directory

<code> python manage.py run </code>

The base example url is 

```{url}/weather?location=bangalore&forecast=hourly&date=2019-09-03```

[Note]
* location is mandatory
* forecast and date are optional, 
  * default forecast=today
  * default date = Local Todays' date



