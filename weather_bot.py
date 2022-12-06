
# Libraries
import os
import datetime as dt
import requests

# CONSTANTS

# API KEY STORED IN ENVIRONMENT VARIABLE --> WEATHERAPI
API_KEY = os.environ.get("WEATHERAPI")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITY = "DUBAI"


url = BASE_URL + "appid="+  API_KEY + "&q=" + CITY

response = requests.get(url).json()

print(dict(response).keys())


