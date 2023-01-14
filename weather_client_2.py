import requests

# Importing requests library and making a GET request to the server to fetch the list of cities
response = requests.get('http://localhost:5000/cities')

# parsing the json response
cities = response.json()

# printing the list of cities and prompting the user to select a city
print("Select a city:")
for i, city in enumerate(cities):
    print(f"{i + 1}. {city}")

# Getting the index of the selected city
city_index = int(input()) - 1

# Getting the selected city name
city = cities[city_index]

# Making a GET request to the server to fetch the weather data for the selected city
response = requests.get(f'http://localhost:5000/weather/{city}')

# parsing the json response
weather_data = response.json()

# printing the weather data
for key, value in weather_data.items():
    print(f'{key}: {value}')
