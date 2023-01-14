import requests

response = requests.get('http://localhost:5000/cities')
cities = response.json()

print("Select a city:")
for i, city in enumerate(cities):
    print(f"{i + 1}. {city}")
city_index = int(input()) - 1
city = cities[city_index]

response = requests.get(f'http://localhost:5000/weather/{city}')
weather_data = response.json()

for key, value in weather_data.items():
    print(f'{key}: {value}')
