# Libraries
import os
import datetime as dt
import requests
from tabulate import tabulate

# CONSTANTS

# API KEY STORED IN ENVIRONMENT VARIABLE --> WEATHERAPI
API_KEY = os.environ.get("WEATHERAPI")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITIES = ["DUBAI", "NEW YORK", "LONDON", "TOKYO", "BEIJING"]


def get_weather_data(city):
    # Creating the API request URL
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city

    # Making the API request and storing the response
    response = requests.get(url).json()

    # Extracting the relevant data from the response
    weather_data = {
        'Temperature': response['main']['temp'],
        'Pressure': response['main']['pressure'],
        'Humidity': response['main']['humidity'],
        'Min Temperature': response['main']['temp_min'],
        'Max Temperature': response['main']['temp_max'],
        'Wind Speed': response['wind']['speed'],
        'Weather Description': response['weather'][0]['description'],
    }
    return weather_data


def print_weather_data(city):
    weather_data = get_weather_data(city)
    print(tabulate(weather_data.items(), headers=['Weather Parameter', 'Value'], tablefmt='fancy_grid'))


def show_city_menu():
    print("Select a city:")
    for i, city in enumerate(CITIES):
        print(f"{i + 1}. {city}")
    city_index = int(input()) - 1
    city = CITIES[city_index]
    print_weather_data(city)


if __name__ == '__main__':
    show_city_menu()
