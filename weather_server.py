from flask import Flask, jsonify
import os
import requests

app = Flask(__name__)

# API KEY STORED IN ENVIRONMENT VARIABLE --> WEATHERAPI
API_KEY = os.environ.get("WEATHERAPI")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
CITIES = ["DUBAI", "NEW YORK", "LONDON", "TOKYO", "BEIJING"]

def get_weather_data(city):
    # Creating the API request URL
    url = BASE_URL + "appid="+ API_KEY + "&q=" + city

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

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    weather_data = get_weather_data(city)
    return jsonify(weather_data)

@app.route('/cities', methods=['GET'])
def get_cities():
    return jsonify(CITIES)

if __name__ == '__main__':
    app.run(debug=True)
