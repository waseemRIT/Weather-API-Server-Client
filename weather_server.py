from socketserver import ThreadingMixIn
from flask import Flask, jsonify
import os
import requests

# Creating a custom Flask class that inherits from the ThreadingMixIn class and the Flask class
# This allows the server to handle multiple clients simultaneously by creating a new thread for each incoming request
class ThreadedFlaskServer(ThreadingMixIn, Flask):
    pass

# Creating an instance of the ThreadedFlaskServer class and assigning it to the app variable
app = ThreadedFlaskServer(__name__)

# Retrieving the API key from an environment variable
API_KEY = os.environ.get("WEATHERAPI")

# Base URL for the OpenWeatherMap API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# List of cities for which the weather data is provided
CITIES = ["DUBAI", "NEW YORK", "LONDON", "TOKYO", "BEIJING"]


# Function to fetch and parse the weather data for a given city
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


# Route for fetching the weather data for a given city
@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    weather_data = get_weather_data(city)
    return jsonify(weather_data)


# Route for fetching the list of cities
@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(CITIES)


# Starting the server
if __name__ == '__main__':
    app.run(debug=True)
